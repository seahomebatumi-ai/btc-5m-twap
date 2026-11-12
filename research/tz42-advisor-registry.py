#!/usr/bin/env python3
# tz42-advisor-registry.py - TZ-42's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the readings
# after the unit's restart - UNIT-NEW and G-FIRST - and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's bot, which reads Binance's public market), and it
# never reads or prints the bot's token or the pinned chat, a coin, a price or a size. It writes one file of the unit's record,
# /var/lib/adv3-bot/check-done: at the kill mark the slot before the day's signal check, so that the new process replays that
# check at its start, and at the rollback mark the kill mark's value again where the new process never moved it. It re-derives
# the registry the bot keeps - its chain, the signals the journal seeds and every signal's walk on the 1- and 5-minute candles the bot
# read, in the order it read them - and every position and allocation, by its own reading, never by the bot's functions.
# Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import array, ast, bisect, calendar, contextlib, datetime as dt, hashlib, importlib.util, io, itertools, json, math, os, re, shutil, \
    subprocess, sys, time

WORK = '/root/tz42-work'
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
TZ_FILE = 'CryptoTZ/TZ-42-advisor-registry.md'
NUMBER = 'TZ-42-'
BRANCH = 'tz-42-advisor-registry'
MAP_REV = '2026-11-01-b'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3': '81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1',
     'bot_old': '9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1',
     'bot_new': 'c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11',
     'selftest': '6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
# G-RULE's table for adv3-bot.py: (changed, added, removed) definitions and assignments against origin/main's; the definitions whose
# code is the same and only their docstring changed; and those that must stay identical, docstring and all.
BOT_DEFS = ({'Telegram', 'base_record', 'candidates', 'check', 'check_record', 'compose', 'done_after', 'due', 'event_lines', 'handle',
             'hello', 'probe', 'route', 'selftest', 'serve', 'zone_lines'},
            {'Registry', 'advance', 'allocate', 'assess_view', 'base_fund', 'bat', 'by_side', 'card_lines', 'carded', 'ceil1', 'ceil5', 'chain_line',
             'day_ms', 'ended_line', 'ensure', 'event_line', 'excluded_lines', 'first_window', 'footer', 'from_iso', 'iso', 'item_record',
             'klines', 'last_check', 'legend', 'line_hash', 'live_line', 'mean_ci', 'model_plan', 'ms_at', 'new_signal', 'note_lines', 'notes_of',
             'notional_of', 'open_risk', 'params', 'params_line', 'pct0', 'position', 'ranking_view', 'reconcile', 'register',
             'registry_view', 'risk_line', 'second', 'seed', 'seed_line', 'sg', 'signal_view', 'signed_usdt', 'stats_lines', 'status_of',
             't975', 'view_plan', 'walk', 'wilson', 'zones_of'},
            {'alerted', 'alerts_of', 'alloc_fields', 'candidate_lines', 'correlation', 'follow', 'followed_lines', 'forming_candles',
             'item_lines', 'journal_scan', 'make', 'numbers', 'offers', 'plan', 'plan_parts', 'plan_strong', 'quiet_line', 'returns_of',
             'strong_shares', 'top_n', 'weak_lines', 'weakened', 'zones_left'})
DOC_ONLY = ('due', 'done_after')
BOT_SAME = ('Data', 'TooMany', 'append', 'chunks', 'find_chat', 'hhmm', 'journal_records', 'latest_slot', 'liquidity', 'live_report', 'log',
            'main', 'malloc_tune', 'next_at', 'put', 'ranked', 'read', 'slot_at', 'slot_key', 'slot_parse', 'slot_text', 'strong_all',
            'volumes')
BOT_ASG = ({'CARD_KEYS', 'HELP', 'SLOTS', 'TOPN'},
           {'(CAPITAL, RISK_TOTAL, STOP_MAX, NEW_MAX)', '(K1_MS, K5_MS, K5_PAGE)', '(LIQ_FRAC, Z_CAP, LIQ_DAYS)',
            '(MARGIN_MIN, MARGIN_MAX, MARGIN_EXC)', '(RANK_LIST, RANK_MAX)', '(REG_FILE, REG_STATE, GENESIS)', 'COMMANDS', 'DAY_MS',
            'DEFAULTS', 'HELPS', 'INTERVAL', 'KEYBOARD', 'KEYWORDS', 'LABEL', 'LEGACY_KEYS', 'LOUD', 'NUMBER', 'RANKING', 'REGISTRY', 'SHOWN', 'T975'},
           {'(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'FOOTER', 'LIST_MAX'})
# this TZ's numbers: the model's defaults, the margin's bounds in percent of the capital, the liquidity share, the strength's cap, the
# new signals a close, the rung, the pause between parts, |z| 1 for STRONG; the old schedule the running process keeps and the new one
CAPITAL, RISK, RISK_MAX, RISK_TOTAL, STOP_MAX, NEW_MAX = 200000.0, 0.5, 1.0, 10.0, 14.0, 7
MARGIN_MIN, MARGIN_MAX, MARGIN_EXC, LIQ_FRAC, Z_CAP, COST, RUNG, PACE, STRONG_Z = 0.5, 3.5, 4.0, 0.005, 3.0, 0.001, 1, 1.1, 1.0
OLD_SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(15, 7)))
K1_MS, K5_MS, DAY_MS = 60_000, 300_000, 86_400_000
MEM_FLOOR, DISK_FLOOR, COIN_DAYS_MAX = 150_369_520, 7_400_000_000, 120
ROWS, FROZEN = 60, 57
FIRST_BOUND = 900
TZ40_REPLAY = '2026-11-01 signal'   # TZ-40's replay at its restart, 18:06 UTC (map §2.7): the last check record naming this slot
# TZ-41 (L0) runs on this host from 2026-11-08 07:30 UTC and reads the advisor's unit unchanged through its run (its G-STILL): this TZ
# deploys only before 07:00 that day, or once TZ-41's report is on main, and never while TZ-41's work tree exists.
TZ41_EDGE = 1794121200
TZ41_REPORT = 'CryptoReports/TZ-41-l0-our-quote-report.md'
TZ41_WORK = '/root/tz41-work'
RENDER_CASES = ('сигнал', 'сигнал 50000 риск 1 лимит 2 топ 3', 'реестр', 'рейтинг', 'оценка', 'помощь', 'привет')
RENDER_KINDS = ['request', 'request', 'registry', 'ranking', 'assess', 'check', 'check']
TRUST_KEYS = {'system', 'strong_justified', 'served', 'cards', 'quality', 'fresh', 'complete', 'expectancy_established'}
DAY = dt.timedelta(days=1)
GENESIS = '0' * 64


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


def strip_docs(src):
    """{name: ast.dump} of a module's functions with each docstring - its first statement where that is a string - removed."""
    out_ = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef):
            body = n.body[1:] if n.body and isinstance(n.body[0], ast.Expr) and isinstance(getattr(n.body[0], 'value', None), ast.Constant) \
                and isinstance(n.body[0].value.value, str) else n.body
            out_[n.name] = ast.dump(ast.Module(body=body, type_ignores=[]))
    return out_


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


def ms_of(text):
    return int(dt.datetime.fromisoformat(text).timestamp() * 1000)


def iso_of(ms):
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).isoformat(timespec='seconds')


def midnight(day):
    return calendar.timegm(day.timetuple()) * 1000


def journal_lines(text):
    """A journal text's lines as the bot's journal_records reads them - a text file's universal newlines, '\\n', '\\r\\n' and '\\r' -
    without their ends, a last line without an end kept."""
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    return lines[:-1] if lines and lines[-1] == '' else lines


def journal_objects(text):
    """Every line of a journal text that parses as a JSON object, in order: the records the bot's seed counts and reads."""
    out_ = []
    for line in journal_lines(text):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if isinstance(r, dict):
            out_.append(r)
    return out_


def records_since(text, t0):
    """The journal's objects from the first stamped at or after t0 less 1 s, and whether the text ends in a newline with every line
    from that record on parsing as an object."""
    recs, ok, on = [], text.endswith('\n') or text == '', False
    for line in journal_lines(text):
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


def count_kind(text, kind):
    """How many records of a kind a journal.jsonl text holds; a broken line left out."""
    return sum(r.get('kind') == kind for r in journal_objects(text))


def prefix_before_check(raw, t0):
    """The journal's bytes before its first check record stamped at or after t0 less 1 s - the journal as the new process's seed read
    it, its first record being that check - or the whole where there is none: (the bytes, whether such a record was found)."""
    pos = 0
    for line in raw.split(b'\n'):
        try:
            r = json.loads(line.decode('utf-8'))
            found = r.get('kind') == 'check' and dt.datetime.fromisoformat(r['utc']).timestamp() >= t0 - 1
        except (ValueError, KeyError, TypeError, AttributeError, UnicodeDecodeError):
            found = False
        if found:
            return raw[:pos], True
        pos += len(line) + 1
    return raw, False


def own_chunks(text, limit=4000):
    """The parts a message of the bot is sent in, by TZ-40's rule read here: split at line ends, never inside a line, each part at most
    limit characters but a line longer than it; a line that would begin a part and is empty is left out."""
    parts, cur = [], ''
    for line in text.split('\n'):
        if cur and len(cur) + 1 + len(line) > limit:
            parts.append(cur)
            cur = line
        else:
            cur = cur + '\n' + line if cur else line
    if cur:
        parts.append(cur)
    return parts


def own_chain(text):
    """The registry's chain by this checker's own reading: (events, the position of the first line whose prev is not the SHA-256 of
    the line before it - the genesis for the first - or whose n is not its position, or that does not parse, else None, the SHA-256 of
    the last line, whether the text ends in a newline)."""
    events, broken, prev = [], None, GENESIS
    lines = text.split('\n')
    whole = text.endswith('\n') or text == ''
    for k, raw in enumerate(lines[:-1] if whole else lines, 1):
        try:
            ev = json.loads(raw)
        except ValueError:
            ev = None
        if not isinstance(ev, dict) or ev.get('prev') != prev or ev.get('n') != k:
            broken = broken or k
        if isinstance(ev, dict):
            events.append(ev)
        prev = hashlib.sha256(raw.encode('utf-8')).hexdigest()
    return events, broken, prev, whole


def head_at(text, n):
    """The chain's head after its first n lines: the SHA-256 of line n, the genesis for n = 0."""
    if n == 0:
        return GENESIS
    lines = text.split('\n')
    return hashlib.sha256(lines[n - 1].encode('utf-8')).hexdigest() if 0 < n <= len(lines) else None


def own_signals(events):
    """{id: the signal} from the events by this checker's own reading: the open's fields, then 'fill', 'hit' (the highest target), 'end'
    ('stop', 'exit' or 'expire') and the end's R and pnl."""
    out_ = {}
    for e in events:
        t = e.get('type')
        if t == 'open':
            out_[e['id']] = dict(e, fill=None, hit=0, end=None, R=None, pnl=None)
        elif e.get('id') in out_:
            s = out_[e['id']]
            if t == 'fill':
                s['fill'] = e['price']
            elif t == 'target':
                s['hit'] = max(s['hit'], e['k'])
            elif t in ('stop', 'exit', 'expire'):
                s['end'], s['R'], s['pnl'] = t, e.get('R'), e.get('pnl')
    return out_


def start_of(o):
    """A signal's place at its issue by this checker's own reading: its first minute the one opening at or after the issue; filled at
    its entry and its instant where it enters at market."""
    issued = ms_of(o['utc'])
    market = o['mode'] == 'market'
    return {'filled': market, 'fp': o['entry'] if market else None, 'fill_ms': issued if market else None, 'hit': 0,
            't': -(-issued // K1_MS) * K1_MS, 'b': issued, 'end': None}


def own_walk(o, k5, daily, fund, until=None, start=None, k1=()):
    """One signal's events on its candles by this checker's own reading of TZ-42's rule. o: its open event's fields; start: its place
    ({'filled', 'fp', 'fill_ms', 'hit', 't', 'b', 'end'}), start_of(o) where None; k1 its first minutes' 1-minute candles, then k5 the
    5-minute ones, each [(open ms, o, h, l, c, closed)] in time order; daily: [(day, (o, h, l, c))] in day order; fund: day -> the
    funding sum. From the first candle at or after the place: a
    daily close - 00:00 UTC of the day after - at or before a candle's open ends a filled signal whose sum of four signs (sign_sum) has
    left its side, at that close; a candle opening at or after the validity's end ends a waiting limit; a waiting limit's candle that
    reaches the limit fills it - at the open where the open is past it - and ends it where it also reaches the stop; a filled signal's
    candle opening past targets credits them, then a stop reached in it ends the signal - at the open where the open is beyond the
    stop - else it credits each target reached. Closed candles advance the place, the last one open is read; with until, no candle
    closing after it is read. Returns (events [(type, k, utc ms, price, R, the result per unit)], the place at the end)."""
    side, E, S, T = o['side'], o['entry'], o['stop'], o['targets']
    valid = ms_of(o['valid'])
    D = dt.date.fromisoformat(o['close_of'])
    st = dict(start) if start else start_of(o)
    days = [d for d, _c in daily]
    closes = [c[3] for _d, c in daily]
    out_ = []

    def end(kind, at, X):
        held = sum(side * fund(days[i]) * closes[i] for i in range(len(days)) if st['fill_ms'] < midnight(days[i] + DAY) <= at)
        unit = side * (X - st['fp']) - COST * (st['fp'] + X) - held
        out_.append((kind, None, at, X, unit / abs(E - S), unit))
        st['end'] = kind

    bounds = [(midnight(d + DAY), i) for i, d in enumerate(days) if d > D and midnight(d + DAY) > st['b']]
    at = [0]

    def closes_upto(limit):
        while at[0] < len(bounds) and bounds[at[0]][0] <= limit:
            B, i = bounds[at[0]]
            at[0] += 1
            st['b'] = B
            if st['filled']:
                sgn = sign_sum(days, closes, i)
                rule = 1 if sgn is not None and sgn >= 2 else -1 if sgn is not None and sgn <= -2 else 0
                if rule != side:
                    end('exit', B, closes[i])
                    return True
        return False

    if st['end']:
        return out_, st
    for width, (t0, op, hi, lo, cl, closed) in itertools.chain(((K1_MS, x) for x in k1), ((K5_MS, x) for x in k5)):
        if t0 < st['t']:
            continue
        if until is not None and t0 + width > until:
            break
        if closes_upto(t0):
            return out_, st
        if not st['filled']:
            if t0 >= valid:
                out_.append(('expire', None, valid, None, None, None))
                st['end'] = 'expire'
                return out_, st
            if (lo <= E) if side > 0 else (hi >= E):
                fp = min(op, E) if side > 0 else max(op, E)
                st.update(filled=True, fp=fp, fill_ms=t0)
                out_.append(('fill', None, t0, fp, None, None))
                if (lo <= S) if side > 0 else (hi >= S):
                    end('stop', t0, op if ((op <= S) if side > 0 else (op >= S)) else S)
                    return out_, st
        else:
            for k in (1, 2, 3):
                if st['hit'] < k and ((op >= T[k - 1]) if side > 0 else (op <= T[k - 1])):
                    st['hit'] = k
                    out_.append(('target', k, t0, T[k - 1], None, None))
            beyond = (op <= S) if side > 0 else (op >= S)
            if beyond or ((lo <= S) if side > 0 else (hi >= S)):
                end('stop', t0, op if beyond else S)
                return out_, st
            for k in (1, 2, 3):
                if st['hit'] < k and ((hi >= T[k - 1]) if side > 0 else (lo <= T[k - 1])):
                    st['hit'] = k
                    out_.append(('target', k, t0, T[k - 1], None, None))
        if closed:
            st['t'] = t0 + width
    limit = st['t'] if until is None else min(st['t'], until)
    if not closes_upto(limit) and not st['filled'] and st['t'] >= valid and (until is None or valid <= until):
        out_.append(('expire', None, valid, None, None, None))
        st['end'] = 'expire'
    return out_, st


def own_coins():
    """The Boss's 42, in RULE-ADV-3's order, read here."""
    return ('BTC BCH SKY XLM XMR MORPHO LIT NEAR HBAR GRAM ENA UNI ARB ZEC HYPE SUI ADA RENDER TAO FET YFI XRP SOL ONDO LINK ALGO TRX BNB '
            'AAVE AVAX ETH INJ LTC XAU DASH PYTH WLD BTW QNT PUMP VVV EGLD').split()


def journal_cards(records):
    """The STRONG cards with an entry the journal's records published, by this checker's own reading of TZ-42's seed: of the daily,
    request, allocation and check records - of an allocation only the coins it placed - each card marked strong, at market or as a
    limit, with a coin of the 42, a side, an entry, a stop on the right side of it, three targets, a close and a unit, each positive;
    with its record's instant, to the second, and kind. In the records' order, then by instant: [(ms, coin, side, close_of, card,
    kind)]."""
    coins = set(own_coins())
    out_ = []
    for rec in records:
        kind = rec.get('kind')
        if kind not in ('daily', 'request', 'alloc', 'check'):
            continue
        try:
            t = ms_of(rec['utc'])
            close_of = str(dt.date.fromisoformat(rec['close_of']))
        except (KeyError, TypeError, ValueError):
            continue
        t -= t % 1000
        placed = None
        if kind == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {x.get('coin') for x in (rec['alloc'].get('items') or []) + (rec['alloc'].get('more') or []) if isinstance(x, dict)}
        for cd in rec.get('cards') or []:
            try:
                if not (cd.get('strong') and cd.get('mode') in ('market', 'limit') and cd.get('entry') is not None
                        and (placed is None or cd['coin'] in placed)):
                    continue
                side, E, S = int(cd['side']), float(cd['entry']), float(cd['stop'])
                T = [float(x) for x in cd['targets']]
                ok_ = (cd['coin'] in coins and side in (1, -1) and len(T) == 3 and min(E, S, float(cd['close']), float(cd['U'])) > 0
                       and side * (E - S) > 0)
            except (AttributeError, KeyError, TypeError, ValueError):
                continue
            if ok_:
                out_.append((t, cd['coin'], side, close_of, cd, kind))
    return sorted(out_, key=lambda x: x[0])


def coin_days(records, t_ms):
    """How much history the seed will read, by journal_cards: for each coin the days from its first STRONG card with an entry to t_ms,
    summed - 288 5-minute candles a coin-day - and the coins: (coin-days, coins)."""
    first = {}
    for t, c, _s, _d, _cd, _k in journal_cards(records):
        first.setdefault(c, t)
    return sum((t_ms - t) / DAY_MS for t in first.values()), len(first)


def own_seed(records, k5, k1, daily, fund):
    """The signals TZ-42's seed opens from the journal's records, by this checker's own reading: each card of journal_cards, in time
    order, opens a signal issued at its record's instant unless one of its coin, side and close was opened already, or
    a signal of its coin is still open then - walked by own_walk to that instant on the coin's 5-minute candles k5 and, where its place
    is inside its first minutes, the 1-minute ones k1 holds for that place, unread without them - or the rule's leverage at its stop is
    under 1x. k1: {(coin, place): candles}; fund: coin -> (day -> the funding sum). [(coin, side, close_of, issued ms, mode, entry, stop,
    kind)] in the order of the ids, and for each its open's fields, its place and its events after the seed's walks: [(o, place,
    events)]."""
    opened, states, live = [], [], {}
    for t, coin, side, close_of, cd, kind in journal_cards(records):
        if any(x[0] == coin and x[1] == side and x[2] == close_of for x in opened):
            continue
        j = live.get(coin)
        if j is not None and k5.get(coin) is not None:
            o, st, evs = states[j]
            first = st['t'] % K5_MS != 0
            if not first or (coin, st['t']) in k1:
                got, st = own_walk(o, k5[coin], daily.get(coin) or [], fund(coin), until=t, start=st,
                                   k1=k1.get((coin, st['t']), []) if first else [])
                states[j] = (o, st, evs + got)
                if st['end']:
                    live.pop(coin)
                    j = None
        if j is not None:
            continue
        d_ = abs(float(cd['entry']) - float(cd['stop'])) / float(cd['entry'])
        if math.floor(1 / (1.5 * d_ + 0.01)) < 1:
            continue
        o = {'side': side, 'entry': float(cd['entry']), 'stop': float(cd['stop']), 'targets': [float(x) for x in cd['targets']],
             'utc': iso_of(t), 'valid': iso_of(midnight(dt.date.fromisoformat(close_of) + 2 * DAY)), 'close_of': close_of,
             'mode': cd['mode']}
        evs = [('fill', None, t, o['entry'], None, None)] if cd['mode'] == 'market' else []
        live[coin] = len(states)
        states.append((o, start_of(o), evs))
        opened.append((coin, side, close_of, t, cd['mode'], o['entry'], o['stop'], kind))
    return opened, states


class Candles:
    """A request's candles kept compact - the render holds every one the bot read - and read back as the bot's tuples, (open ms, o,
    h, l, c, closed): the same integers and floats."""
    __slots__ = ('t', 'o', 'h', 'l', 'c', 'x')

    def __init__(self, rows):
        rows = list(rows)
        self.t = array.array('q', (r[0] for r in rows))
        self.o, self.h, self.l, self.c = (array.array('d', (r[k] for r in rows)) for k in (1, 2, 3, 4))
        self.x = bytes(1 if r[5] else 0 for r in rows)

    def __iter__(self):
        return zip(self.t, self.o, self.h, self.l, self.c, (b == 1 for b in self.x))

    def __len__(self):
        return len(self.t)


def union_k5(calls):
    """Every 5-minute candle the calls read of each coin: a coin read once its candles as read, else the last version of each."""
    by = {}
    for c in calls:
        by.setdefault(c['coin'], []).append(c['rows'])
    out_ = {}
    for coin, reads in by.items():
        if len(reads) == 1:
            out_[coin] = reads[0]
            continue
        d = {}
        for rows in reads:
            for r in rows:
                d[r[0]] = r
        out_[coin] = [d[k] for k in sorted(d)]
    return out_


def replay(events, records, calls, daily, fund):
    """Every signal's events by this checker's own reading, replayed on the candles the bot read, in the order it read them: the
    legacy signals the seed opens from the journal's records on the seed's candles (own_seed), then, at each of the reconcile's reads
    of a coin's 5-minute candles, every signal of that coin whose open the registry held before the read and that has not ended, walked
    on that read's candles from its place (own_walk) - with the 1-minute candles read next for that place where it is inside its first
    minutes, and not walked without them. calls: [{'caller' - 'seed' or 'reconcile', 'coin', 'start', 'step', 'rows', 'n_before'}], in
    time order; daily: coin -> [(day, candle)]; fund: coin -> (day -> the funding sum). Returns (the legacy signals own_seed opens, {id:
    events}, {id: place}), the legacy signals numbered 1, 2, ... in their order and the model's by their open events."""
    seed5 = union_k5([c for c in calls if c['caller'] == 'seed' and c['step'] == K5_MS])
    seed1 = {(c['coin'], c['start']): c['rows'] for c in calls if c['caller'] == 'seed' and c['step'] == K1_MS}
    opened, states = own_seed(records, seed5, seed1, daily, fund)
    exp, place, op = {}, {}, {}
    for i, (o, st, evs) in enumerate(states, 1):
        exp[i], place[i], op[i] = list(evs), st, o
    n_open = {}
    for e in events:
        if e.get('type') == 'open':
            n_open[e['id']] = e['n']
            if not e.get('legacy'):
                o = {k: e[k] for k in ('side', 'entry', 'stop', 'targets', 'utc', 'valid', 'close_of', 'mode')}
                op[e['id']], place[e['id']] = o, start_of(o)
                exp[e['id']] = [('fill', None, ms_of(o['utc']), o['entry'], None, None)] if o['mode'] == 'market' else []
    coin_of = {e['id']: e['coin'] for e in events if e.get('type') == 'open'}
    rec = [c for c in calls if c['caller'] == 'reconcile']
    k = 0
    while k < len(rec):
        c = rec[k]
        k += 1
        if c['step'] != K5_MS:
            continue
        ones = {}
        while k < len(rec) and rec[k]['step'] == K1_MS and rec[k]['coin'] == c['coin']:
            ones[rec[k]['start']] = rec[k]['rows']
            k += 1
        for i in sorted(n_open):
            if coin_of[i] != c['coin'] or n_open[i] > c['n_before'] or i not in place or place[i]['end']:
                continue
            first = place[i]['t'] % K5_MS != 0
            if first and place[i]['t'] not in ones:
                continue
            got, place[i] = own_walk(op[i], c['rows'], daily.get(c['coin']) or [], fund(c['coin']), start=place[i],
                                     k1=ones[place[i]['t']] if first else [])
            exp[i] += got
    return opened, exp, place


def same_events(mine, theirs, qty):
    """Whether one signal's events as the bot wrote them, [(type, k, utc ms, price, R, pnl)], are this checker's, [(type, k, utc ms,
    price, R, the result per unit)], the pnl the unit's result times the signal's quantity."""
    close = lambda a, b, rel: (a is None and b is None) or (a is not None and b is not None and abs(a - b) <= rel * max(1.0, abs(a)))
    return len(mine) == len(theirs) and all(
        a[:3] == b[:3] and close(a[3], b[3], 1e-12) and close(a[4], b[4], 1e-9)
        and close(None if a[5] is None else a[5] * qty, b[5], 1e-9) for a, b in zip(mine, theirs))


def registry_checks(text, records, calls, daily, fund, state=None):
    """The registry a bot built, read against this checker's own chain, seed and walks: the chain whole from the genesis; a seed first
    and alone; ids 1, 2, ... in the order of their opens; the legacy signals those own_seed opens from the same journal on the same
    candles, issued at their cards' instants; at most one signal of a coin open at once; every signal's fill, targets and end, with R
    and USDT, those the replay finds on every candle the bot read, in the order it read them; and, given the bot's registry-state.json,
    every signal open there at the replay's place. (checks, the counts printed)."""
    events, broken, _head, whole = own_chain(text)
    sigs = own_signals(events)
    opened, exp, place = replay(events, records, calls, daily, fund)
    legacy = [s for _i, s in sorted(sigs.items()) if s.get('legacy')]
    got = [(s['coin'], s['side'], s['close_of'], ms_of(s['utc']), s['mode'], s['entry'], s['stop'], s['source'].split(':', 1)[-1])
           for s in legacy]
    mism = []
    for i, s in sorted(sigs.items()):
        theirs = [(e['type'], e.get('k'), ms_of(e['utc']), e.get('price'), e.get('R'), e.get('pnl')) for e in events
                  if e.get('id') == i and e.get('type') in ('fill', 'target', 'stop', 'exit', 'expire')]
        if not same_events(exp.get(i, []), theirs, s['qty']):
            mism.append(i)
    opens = [e for e in events if e.get('type') == 'open']
    live_ok, by_coin = True, {}
    for e in opens:
        if any(not _ended_before(events, j, ms_of(e['utc'])) for j in by_coin.get(e['coin'], [])):
            live_ok = False
        by_coin.setdefault(e['coin'], []).append(e['id'])
    checks = {
        'the registry\'s chain is whole from the genesis, every line numbered by its place, the file ending in a newline':
            broken is None and whole and bool(events),
        'its first event is the seed, the only one': bool(events) and events[0].get('type') == 'seed'
            and sum(e.get('type') == 'seed' for e in events) == 1,
        'the signals are numbered 1, 2, ... in the order of their opens': [e['id'] for e in opens] == list(range(1, len(opens) + 1)),
        'the legacy signals are those this checker\'s seed opens from the same journal on the same candles, first and in that order':
            got == opened and all(s['id'] == k for k, s in enumerate(legacy, 1)),
        'no coin holds two signals open at once': live_ok,
        'every signal\'s fill, targets and end, with R and USDT, are those this checker\'s replay finds on the candles the bot read':
            not mism,
    }
    if state is not None:
        cur = state.get('cursor') or {}
        checks['every signal open keeps the replay\'s place: its first candle not walked and its last close passed'] = all(
            str(i) in cur and (cur[str(i)].get('t'), cur[str(i)].get('b')) == (place[i]['t'], place[i]['b'])
            for i, s in sigs.items() if s['end'] is None and i in place)
    return checks, {'events': len(events), 'signals': len(sigs), 'legacy': len(legacy), 'walked': sum(len(v) for v in exp.values()),
                    'mismatches': mism}


def _ended_before(events, i, t):
    """Whether signal i ended at or before the instant t - its stop, exit or expiry stamped then - by the events."""
    return any(e.get('id') == i and e.get('type') in ('stop', 'exit', 'expire') and ms_of(e['utc']) <= t for e in events)


def own_entry(row):
    """The entry and the stop a card offers, by RULE-ADV-3's display rules read here: the stop C - k*U; LONG above the zone a limit at
    its top, else at market while more than 0.25*U above the stop, else no entry; SHORT mirrored; the mark, or the close without one.
    (entry, stop), the entry None where no entry is offered."""
    k, C, U = row['signal'], row['close'], row['U']
    S, P = C - k * U, row.get('mark') or C
    if k > 0:
        entry = C + 0.25 * U if P > C + 0.25 * U else P if P > S + 0.25 * U else None
    else:
        entry = C - 0.25 * U if P < C - 0.25 * U else P if P < S - 0.25 * U else None
    return entry, S


def own_stop_pct(row):
    """The stop's distance in percent of the entry a card offers (own_entry), None where it offers no entry."""
    entry, S = own_entry(row)
    return None if entry is None else 100 * abs(entry - S) / entry


def own_lev(entry, stop):
    """The rule's leverage at a stop, RULE-ADV-3's: at most 20, and so that liquidation lies beyond the stop."""
    d = abs(entry - stop) / entry
    return min(20, math.floor(1 / (1.5 * d + 0.01)))


def pos_ok(p, entry, stop, cap, lev_max, volume=None):
    """One position against this checker's own arithmetic (TZ-42): whole USDT; its loss the notional times its stop's distance and
    both sides' costs; its margin whole, within 0.5 and 4 % of the capital and covering the notional; its leverage 1 to the rule's; its
    quantity the notional over the entry; its risk the loss over the capital; within 0.5 % of the coin's volume where known."""
    rate = abs(entry - stop) / entry + 2 * COST
    return (float(p['notional']).is_integer() and float(p['margin']).is_integer() and abs(p['loss'] - p['notional'] * rate) <= 1e-9 * max(1.0, p['loss'])
            and MARGIN_MIN / 100 * cap - 1e-9 <= p['margin'] <= MARGIN_EXC / 100 * cap and p['margin'] * p['leverage'] >= p['notional']
            and p['margin'] == math.ceil(p['notional'] / p['leverage']) and 1 <= p['leverage'] <= lev_max
            and (not volume or p['notional'] <= LIQ_FRAC * volume + 1e-9) and abs(p['risk_pct'] - 100 * p['loss'] / cap) <= 1e-12 * max(1.0, p['risk_pct'])
            and ('qty' not in p or abs(p['qty'] - p['notional'] / entry) <= 1e-12 * max(1.0, p['qty'])))


def alloc_checks(calls):
    """Every allocation a bot made, read against this checker's own arithmetic (TZ-42): calls [{'prm', 'room', 'liq', 'live' - the
    coins it shared risk among, 'items' - after it, 'rows' - the report's}]. Each wanted risk k times prm's risk times min(|z|, 3) over
    the sum, at most 1 %, never rising along the order; the risk taken within the room - none where the room is spent or below
    nothing - each at most 1 %; each position by pos_ok at the
    card's entry and stop - which are this checker's own (own_entry), within prm's stop limit - the rule's leverage at them its ceiling;
    each item without a position the room's reason or the margin's."""
    wants_ok = room_ok = sized_ok = why_ok = stop_ok = True
    for c in calls:
        prm, items, live = c['prm'], c['items'], c['live']
        q = {it['coin']: min(abs(it['card']['z']), Z_CAP) for it in items if it['coin'] in live}
        w = {coin: min(RISK_MAX, len(live) * prm['risk'] * q[coin] / sum(q.values())) for coin in live}
        seq = [w[coin] for coin in live]
        wants_ok &= all(a >= b - 1e-12 for a, b in zip(seq, seq[1:]))
        sized = [it for it in items if it['coin'] in live and it.get('pos')]
        wants_ok &= all(abs(it['pos']['want'] - w[it['coin']]) < 1e-12 for it in sized)
        room_ok &= (sum(it['pos']['risk_pct'] for it in sized) <= max(0.0, c['room']) + 1e-9 and all(it['pos']['risk_pct'] <= RISK_MAX + 1e-9 for it in sized)
                    and all(it['pos']['risk_pct'] <= w[it['coin']] + 1e-9 for it in sized))
        for it in sized:
            entry, S = own_entry(c['rows'][it['coin']])
            cd = it['card']
            mine = entry is not None and abs(entry - cd['entry']) <= 1e-12 * entry and abs(S - cd['stop']) <= 1e-12 * abs(S)
            stop_ok &= mine and 100 * abs(entry - S) / entry <= prm['stop'] + 1e-9
            sized_ok &= mine and pos_ok(it['pos'], cd['entry'], cd['stop'], prm['capital'], own_lev(cd['entry'], cd['stop']), c['liq'].get(it['coin']))
        why_ok &= all(it.get('code') in ('room', 'margin') and it.get('why') for it in items if it['coin'] in live and not it.get('pos'))
    return {'allocate: each wanted risk k x the risk x min(|z|, 3) over their sum, at most 1 %, never rising along the order': wants_ok,
            'allocate: the risk taken within the room and within what each wanted, each at most 1 %': room_ok,
            'allocate: every position whole, its loss the notional times its stop and both sides\' costs, its margin within 0.5 and 4 % of '
            'the capital and covering it, its leverage 1 to the rule\'s, within 0.5 % of the volume': sized_ok,
            'allocate: an item left without a position has the room\'s reason or the margin\'s': why_ok,
            'allocate: each entry and stop this checker\'s own, the stop within the limit': stop_ok}


def opens_checks(events):
    """Every signal the registry opened, read against this checker's own arithmetic (TZ-42): at the default capital, its position by
    pos_ok at its entry and stop, its leverage at most the rule's there; a legacy signal at most the default risk, a model one at most 1 %;
    its validity the close after its card's, 00:00 UTC two days after the close it is of; a market entry filled at its entry and its
    issue, a limit not filled at its issue."""
    ok_pos = ok_valid = ok_fill = True
    fills = {}
    for e in events:
        if e.get('type') == 'fill' and e['id'] not in fills:
            fills[e['id']] = e
    for e in events:
        if e.get('type') != 'open':
            continue
        p = {k: e[k] for k in ('notional', 'leverage', 'margin', 'loss', 'risk_pct', 'qty')}
        ok_pos &= (e['capital'] == CAPITAL and pos_ok(p, e['entry'], e['stop'], CAPITAL, own_lev(e['entry'], e['stop']))
                   and e['risk_pct'] <= (RISK if e.get('legacy') else RISK_MAX) + 1e-9)
        ok_valid &= ms_of(e['valid']) == midnight(dt.date.fromisoformat(e['close_of']) + 2 * DAY)
        f = fills.get(e['id'])
        ok_fill &= ((f is not None and f['utc'] == e['utc'] and f['price'] == e['entry']) if e['mode'] == 'market'
                    else (f is None or ms_of(f['utc']) > ms_of(e['utc'])))
    return {'every signal opened at the default capital, its position whole by this checker\'s arithmetic at its entry and stop, a legacy '
            'one at most the default 0.5 %, a model one at most 1 %': ok_pos,
            'every signal valid to 00:00 UTC two days after the close it is of': ok_valid,
            'a market entry filled at its entry at its issue, a limit never at its issue': ok_fill}


def model_checks(events, sigs):
    """The registry's model limits (TZ-42), read from the events: at each signal the model opened - not a legacy one - the risk of the
    signals open then, its own included, within 10 %; the model's signals of a close at most 7, less the legacy ones of that close."""
    ok_risk = True
    for e in events:
        if e.get('type') == 'open' and not e.get('legacy'):
            t = ms_of(e['utc'])
            live = [s for i, s in sigs.items() if ms_of(s['utc']) <= t and not _ended_before(events, i, t)]
            ok_risk &= sum(s['risk_pct'] for s in live) <= RISK_TOTAL + 1e-9
    per = {}
    for s in sigs.values():
        per.setdefault(s['close_of'], [0, 0])[1 if s.get('legacy') else 0] += 1
    return {'the model opens a signal only within 10 % of risk, the signals open then counted': ok_risk,
            'the model\'s signals of a close at most 7, less the legacy ones of that close': all(m <= max(0, NEW_MAX - lg) for m, lg in per.values())}


def flags_checks(run, kind):
    """One check's flags against its own content (TZ-42): loud exactly when it announced an end - a stop, an exit, an expiry - or
    opened a signal; one line only where it announced no event and opened none and, at the signal check, held no note and the coins
    not taken for the reasons of the check before, at the fact check no zone left, and no seed; every part of its message with the
    record's flag; a line of one part beginning «✓ » where it is one line."""
    rec, sent, events = run['rec'], run['sent'], run['events']
    announced = [events[n - 1] for n in rec['events'] if 0 < n <= len(events)]
    loud = bool(rec['opened']) or any(e['type'] in ('stop', 'exit', 'expire') for e in announced)
    nothing = not announced and not rec['opened'] and (
        (kind == 'signal' and not rec['notes'] and run['prev_codes'] == rec['excluded_codes']) or (kind == 'fact' and not rec['zones']))
    return (len(announced) == len(rec['events']) and rec['quiet'] == (not loud) and bool(sent) and all(q == rec['quiet'] for _t, q, _k in sent)
            and rec['one_line'] == (nothing and rec['registry']['seeded'] is None)
            and (not rec['one_line'] or (len(sent) == 1 and '\n' not in sent[0][0] and sent[0][0].startswith('✓ '))))


def unit_checks(which, pre, now):
    """UNIT-NEW's and UNIT-OLD's nine readings after a restart: now is what the modes read; pre the snapshot of the kill mark, which
    names the check-done the new process must read at its start."""
    want = (H['adv3'], H['bot_new']) if which == 'new' else (H['adv3'], H['bot_old'])
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy\'s adv3.py is main\'s and adv3-bot.py the %s one, and the process started after the copy' % which:
            (now['sha_adv3'], now['sha_bot']) == want and now['start'] > now['copy_t'],
        'the unit file is unchanged': now['sha_unit'] == H['unit'],
        'the log shows the new process serving from check-done %s' % pre['read_done']: now['serving'] and now['read'] == pre['read_done'],
        'no traceback in the log since the mark': not now['traceback'],
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def first_checks(pre, recs, done_text, log, pid, tail_ok, reg_text, reg_state, seen):
    """G-FIRST's ten readings: the new process's first check - the day's signal check, replayed at its start because the kill mark set
    check-done to the slot before it - from the journal's records stamped since the kill mark, the check-done file and service.log's
    lines since the mark; and the registry it seeded at that check, against seen - the journal as its seed read it, its bytes before
    that check's record: {'sha', 'records', 'cards' - the set of (coin, side, close, ms) of journal_cards over it}."""
    t0 = dt.datetime.fromtimestamp(pre['t'], dt.timezone.utc)
    day = t0.date()
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    want_done = '%s %s' % (day, 'fact' if t0.time() >= SLOTS[1][1] else 'signal')
    events, broken, _head, whole = own_chain(reg_text or '')
    sigs = own_signals(events)
    legacy = [s for s in sigs.values() if s.get('legacy')]
    seed = events[0] if events else {}
    reg = r.get('registry') or {}
    ends = ('stop', 'exit', 'expire')
    return {
        'exactly one check record since the mark': len(checks_) == 1,
        'it is the day\'s signal check, of the close of the day before, under rule ee206e7c': (
            r.get('slot') == '%s signal' % day and r.get('close_of') == str(day - DAY) and r.get('rule') == H['rule']),
        'it was sent: its Telegram message ids': bool(r.get('message_ids')) and all(isinstance(x, int) for x in r.get('message_ids') or ['x']),
        'it holds the 42 coins\' state, the six ratings, STRONG at every rank, its cards numbered as it opened them with their positions, '
        'the coins not taken and their codes, the registry\'s head at its events and the seed it made; loud exactly with a new signal or '
        'an end': (
            len(r.get('state') or {}) == 42 and TRUST_KEYS <= set(r.get('trust') or {}) and isinstance(r.get('strong_all'), list)
            and [c.get('id') for c in r.get('cards') or []] == (r.get('opened') or []) and all(c.get('position') for c in r.get('cards') or [])
            and isinstance(r.get('excluded_codes'), list) and isinstance(reg.get('events'), int)
            and reg.get('head') == head_at(reg_text or '', reg['events']) and isinstance(reg.get('seeded'), int)
            and r.get('quiet') == (not r.get('opened') and not any(
                events[n - 1].get('type') in ends for n in r.get('events') or [] if 0 < n <= len(events)))),
        'check-done names the slot it covers: %s' % want_done: done_text == want_done,
        'the log since the mark: the new process serving from check-done %s, the check sent, no check failed and no traceback' % pre['read_done']: (
            ('serving the pinned chat: pid %d ' % pid in log and 'check-done %s' % pre['read_done'] in log) and 'check sent: %s signal' % day in log
            and 'check failed' not in log and 'Traceback' not in log),
        'the journal ends in a newline and every line since the mark parses': tail_ok,
        'the registry is whole from the genesis and ends in a newline; its seed first, naming by SHA-256 and its records the journal as the '
        'seed read it - its lines before that check\'s record': (
            broken is None and whole and seed.get('type') == 'seed' and seed.get('journal_sha') == seen['sha']
            and seed.get('records') == seen['records']),
        'every legacy signal is a STRONG card of that journal with an entry, issued at its record\'s instant': all(
            (s['coin'], s['side'], s['close_of'], ms_of(s['utc'])) in seen['cards'] for s in legacy),
        'the registry\'s state counts every event announced and keeps a place for every signal open': (
            isinstance(reg_state, dict) and reg_state.get('announced') == len(events)
            and all(str(i) in (reg_state.get('cursor') or {}) for i, s in sigs.items() if s['end'] is None)),
    }


def slot_instant(text, slots=SLOTS):
    """The instant of a slot 'YYYY-MM-DD signal|fact' as epoch seconds under slots, or None."""
    try:
        day, kind = text.split()
        at = dict(slots)[kind]
        return calendar.timegm(dt.datetime.combine(dt.date.fromisoformat(day), at).timetuple())
    except (ValueError, KeyError, AttributeError):
        return None


def slot_order(text):
    day, kind = text.split()
    return day, [k for k, _ in SLOTS].index(kind)


def latest_slot_text(t, slots=OLD_SLOTS):
    """The last slot whose instant is at or before the epoch second t, under slots: the running process's, 00:10 and 12:10 UTC, unless
    named."""
    d = dt.datetime.fromtimestamp(t, dt.timezone.utc)
    for kind, at in reversed(slots):
        if d.time() >= at:
            return '%s %s' % (d.date(), kind)
    return '%s %s' % (d.date() - DAY, slots[-1][0])


def replay_text(t):
    """The slot the kill mark writes to check-done: the one before the UTC day's signal check, the day before's fact - so that
    the new process's schedule owes, and runs at its start, the day's signal check."""
    return '%s %s' % (dt.datetime.fromtimestamp(t, dt.timezone.utc).date() - DAY, SLOTS[-1][0])


def clock_checks(recs, done_text):
    """H7, that the clock fires (map §2.7): the journal's check records from the last one naming 2026-11-01 signal - TZ-40's replay at
    its restart; TZ-39's first named that slot too - name strictly later slots, each once; every one after it - at least one - stamped
    at or after its slot's instant under the running code's schedule, 00:10 and 12:10 UTC; and check-done names the last one's slot,
    or that day's fact where the last is a signal check stamped at or after 12:10 UTC. (checks, the delays in seconds)."""
    every = [r for r in recs if r.get('kind') == 'check']
    starts = [k for k, r in enumerate(every) if r.get('slot') == TZ40_REPLAY]
    checks_ = every[starts[-1]:] if starts else []
    slots = [r.get('slot') for r in checks_]
    delays = []
    for r in checks_[1:]:
        at = slot_instant(r.get('slot') or '', OLD_SLOTS)
        try:
            delays.append(dt.datetime.fromisoformat(r['utc']).timestamp() - at)
        except (KeyError, TypeError, ValueError):
            delays.append(None)
    last = checks_[-1] if checks_ else {}
    covered = None
    if (last.get('slot') or '').endswith(' signal'):
        day = last['slot'].split()[0]
        try:
            covered = '%s fact' % day if dt.datetime.fromisoformat(last['utc']).timestamp() >= slot_instant('%s fact' % day, OLD_SLOTS) else None
        except (KeyError, TypeError, ValueError):
            covered = None
    ok_slots = all(slot_instant(x or '', OLD_SLOTS) is not None for x in slots)
    return {
        'H7 the check records from TZ-40\'s replay, the last naming %s, name strictly later slots, each once' % TZ40_REPLAY: (
            bool(slots) and ok_slots and all(slot_order(a) < slot_order(b) for a, b in zip(slots, slots[1:]))),
        'H7 every check after TZ-40\'s replay - at least one - stamped at or after its slot\'s instant': (
            len(checks_) > 1 and all(x is not None and x >= 0 for x in delays)),
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


def memory_gate(first, second):
    """The memory gate: MemAvailable at the first read, and at the second, 60 s later, taken only where the first fell
    below MEM_FLOOR; the second decides. Returns (passes, the read that decided)."""
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


def window_reading(t, tz41_report, tz41_work):
    """TZ-41's window: this TZ deploys only before 2026-11-08 07:00:00 UTC, half an hour before TZ-41's band opens, or once TZ-41's
    report is on main; and never while TZ-41's work tree exists."""
    return {'before 2026-11-08 07:00 UTC, or TZ-41\'s report on main': t < TZ41_EDGE or tz41_report,
            'TZ-41\'s work tree absent': not tz41_work}


def tz41_reported():
    rc, so, _ = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', TZ41_REPORT])
    return rc == 0 and so.strip() == TZ41_REPORT


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
    checks['H5 adv3.py and adv3-bot.py are TZ-40\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    jtext = read(BOTDIR + '/journal.jsonl')
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    checks['H6 the record holds a journal of whole lines and a check-done naming a slot'] = (
        jtext.endswith('\n') and done_text is not None and slot_instant(done_text, OLD_SLOTS) is not None)
    recs, _ok = records_since(jtext, 0)
    clock, delays = clock_checks(recs, done_text)
    checks.update(clock)
    checks['H8 no registry yet: neither registry.jsonl nor registry-state.json in the record'] = not any(
        os.path.exists(BOTDIR + '/' + f) for f in ('registry.jsonl', 'registry-state.json'))
    for k, v in window_reading(time.time(), tz41_reported(), os.path.exists(TZ41_WORK)).items():
        checks['H8 ' + k] = v
    slots = [r['slot'] for r in recs if r.get('kind') == 'check' and isinstance(r.get('slot'), str)]
    out('check records: %d; slots %s; delays after their instants, seconds: %s; check-done %s' % (
        len(slots), ' '.join(x.replace(' signal', ' s').replace(' fact', ' f') for x in slots),
        ' '.join('-' if x is None else '%.0f' % x for x in delays), done_text or '-'))
    objs = journal_objects(jtext)
    cdays, ncoins = coin_days(objs, time.time() * 1000)
    checks['H9 the journal\'s STRONG cards span at most %d coin-days, the span G-RENDER\'s memory floor was measured at' % COIN_DAYS_MAX] = (
        cdays <= COIN_DAYS_MAX)
    out('journal: %d bytes, %d records, %d STRONG cards with an entry the seed would read, of %d coins over %.1f coin-days' % (
        len(jtext.encode('utf-8')), len(objs), len(journal_cards(objs)), ncoins, cdays))
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
    old_bot, new_bot = git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py')
    od, nd = strip_docs(old_bot), strip_docs(new_bot)
    checks = {
        'RULE-ADV-3.txt is main\'s, byte for byte, hashes to the RULE constant, and is adv3.py\'s':
            rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
            and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'),
        'the unit file is main\'s, byte for byte, and hashes to TZ-35\'s': unit == git_show('deploy/systemd/adv3-bot.service').encode()
            and sha256_bytes(unit) == H['unit'],
        'adv3.py and selftest-adv3.py are main\'s, byte for byte - the rule, the report, the card and the ratings untouched': (
            read(WT + '/advisor/adv3.py', 'rb') == git_show('advisor/adv3.py').encode() and sha256_file(WT + '/advisor/adv3.py') == H['adv3']
            and read(WT + '/advisor/selftest-adv3.py', 'rb') == git_show('advisor/selftest-adv3.py').encode()
            and sha256_file(WT + '/advisor/selftest-adv3.py') == H['selftest']),
    }
    checks.update(tree_checks('adv3-bot.py', old_bot, new_bot, BOT_DEFS, BOT_ASG, BOT_SAME))
    checks['adv3-bot.py: %s the same code, their docstrings alone changed' % ' and '.join(DOC_ONLY)] = all(od[k] == nd[k] for k in DOC_ONLY)
    checks['the branch\'s adv3-bot.py is Appendix A\'s'] = sha256_file(WT + '/advisor/adv3-bot.py') == H['bot_new']
    verdict('RULE', checks)


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the journal's check records, lines and SHA-256, whether a
    registry exists, and check-done."""
    raw = read(BOTDIR + '/journal.jsonl', 'rb')
    text = raw.decode('utf-8')
    return {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
            'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
            'checks': count_kind(text, 'check'), 'lines': len(journal_lines(text)), 'journal_sha': sha256_bytes(raw),
            'records': len(journal_objects(text)),
            'registry': [f for f in ('registry.jsonl', 'registry-state.json') if os.path.exists(BOTDIR + '/' + f)],
            'check_done': read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None}


def put_done(text):
    """check-done replaced in one rename, as the bot's own put writes it."""
    tmp = BOTDIR + '/check-done.tz42'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, BOTDIR + '/check-done')


def mode_mark(name):
    """A mark: the snapshot, kept in state.json. deploy and kill refuse outside TZ-41's window (window_reading), and where a registry
    exists in the record. kill refuses unless check-done names the latest slot of the running code's schedule - the process owes no
    check - and then writes check-done to the slot before the UTC day's signal check, so that the new process replays that check at its
    start (G-FIRST); the old process holds its slot in memory and never reads the file again. rollback writes the kill mark's
    check-done back where the new process never moved it from the replay slot. kill2 writes nothing and records the check-done the old
    code will read at its start."""
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name in ('deploy', 'kill'):
        w = window_reading(snap['t'], tz41_reported(), os.path.exists(TZ41_WORK))
        assert all(w.values()), 'outside TZ-41\'s window: %s' % [k for k, v in w.items() if not v]
        assert not snap['registry'], 'a registry exists already: %s' % snap['registry']
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
    out('mark %s at %s: bot pid %s NRestarts %s, %d check records, journal %d lines %s…, registry %s, check-done %s%s' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'], snap['checks'],
        snap['lines'], snap['journal_sha'][:12], ','.join(snap['registry']) or 'none', snap['check_done'] or '-',
        (' -> %s, replayed by the new process at its start' % snap['read_done']) if name == 'kill'
        else (' -> restored to %s' % st['marks']['kill']['check_done']) if snap.get('restored') else ''))


def mode_copy():
    rc, head, _ = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is main\'s, unchanged': sha256_file(SVC + '/adv3.py') == H['adv3'],
        'adv3-bot.py is Appendix A\'s': sha256_file(SVC + '/adv3-bot.py') == H['bot_new'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s two files equal the service copy\'s': all(read(WT + '/advisor/' + f, 'rb') == read(SVC + '/' + f, 'rb')
                                                               for f in ('adv3.py', 'adv3-bot.py')),
    })


def own_files():
    return tuple(maybe_sha(BOTDIR + '/' + f) for f in ('journal.jsonl', 'offset', 'daily-sent', 'check-done', 'registry.jsonl',
                                                        'registry-state.json'))


def line_count(path):
    """The lines of a file, read one at a time: a year's journal is never held whole."""
    with open(path, encoding='utf-8') as fh:
        return sum(1 for _line in fh)


def lines_after(path, k):
    """The records of a journal's lines after its first k, each parsed, read one at a time."""
    with open(path, encoding='utf-8') as fh:
        return [json.loads(line) for n, line in enumerate(fh) if n >= k]


def render_run(mod, data):
    """G-RENDER's pipeline on a loaded bot and a Data, its STATE a directory holding a copy of a journal and no registry: the commands
    answered through the bot's handle - the first seeding the registry from the copy - then the signal check and the fact check through
    its check, each at the moment it runs, each record appended to the journal; Telegram a stand-in; every candle request the bot made -
    which function made it and the registry's events before it - every allocation with what it shared risk among and the report it rests
    on, every «сигнал» view and every report captured. Returns what render_checks reads."""
    jpath, rpath = mod.STATE + '/journal.jsonl', mod.STATE + '/' + mod.REG_FILE
    raw = read(jpath, 'rb')
    base_lines = line_count(jpath)
    records0 = journal_objects(raw.decode('utf-8'))

    class Cap(mod.Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.sent = []

        def call(self, method, http_timeout=30, **params):
            if method == 'sendMessage':
                self.sent.append((params['text'], params.get('disable_notification', False), 'reply_markup' in params))
                return {'message_id': len(self.sent)}
            return True

    cap, texts, runs = Cap(), {}, {}
    calls, allocs, views, reps = [], [], [], []
    real = {k: getattr(mod, k) for k in ('klines', 'allocate', 'signal_view', 'live_report')}

    def k_spy(coin, start_ms, now_ms, step=mod.K5_MS, count=None):
        caller = sys._getframe(1).f_code.co_name
        via = sys._getframe(2).f_code.co_name if caller == 'first_window' else caller
        n_before = line_count(rpath) if os.path.exists(rpath) else 0
        rows = real['klines'](coin, start_ms, now_ms, step, count)
        calls.append({'caller': via, 'coin': coin, 'start': start_ms, 'now': now_ms, 'step': step, 'count': count, 'rows': Candles(rows),
                      'n_before': n_before})
        return rows

    def alloc_spy(items, prm, room, liq):
        live = [it['coin'] for it in items if not it.get('why')]
        real['allocate'](items, prm, room, liq)
        allocs.append({'prm': dict(prm), 'room': room, 'liq': dict(liq), 'live': live, 'items': [dict(it) for it in items],
                       'rows': reps[-1]['rows'] if reps else {}})

    def view_spy(rep, reg, view, prm, now_, new_ids, seeded=None):
        text = real['signal_view'](rep, reg, view, prm, now_, new_ids, seeded)
        views.append((rep, view, dict(prm), dict(new_ids), text))
        return text

    def report_spy(d, deposit, risk):
        r = real['live_report'](d, deposit, risk)
        reps.append(r)
        return r

    mod.klines, mod.allocate, mod.signal_view, mod.live_report = k_spy, alloc_spy, view_spy, report_spy
    buf = io.StringIO()
    case_reps = {}
    try:
        with contextlib.redirect_stdout(buf):
            reg = mod.Registry(mod.STATE)
            for case in RENDER_CASES:
                n0, m0 = len(cap.sent), len(reps)
                mod.handle(cap, data, reg, case)
                texts[case] = cap.sent[n0:]
                case_reps[case] = reps[m0:]
            for kind in ('signal', 'fact'):
                prev = mod.last_check()
                n0, m0 = len(cap.sent), len(reps)
                now = dt.datetime.now(dt.timezone.utc)
                rec = mod.check(cap, data, reg, (now.date(), kind), now)
                mod.append(rec)
                runs[kind] = {'rec': rec, 'sent': cap.sent[n0:], 'rep': reps[m0], 'prev_codes': (prev or {}).get('excluded_codes')}
    finally:
        mod.klines, mod.allocate, mod.signal_view, mod.live_report = real['klines'], real['allocate'], real['signal_view'], real['live_report']
    records = lines_after(jpath, base_lines)
    reg_text = read(rpath) if os.path.exists(rpath) else ''
    sp = mod.STATE + '/' + mod.REG_STATE
    reg_state = json.loads(read(sp)) if os.path.exists(sp) else None
    events = own_chain(reg_text)[0]
    for x in runs.values():
        x['events'] = events
    m, a = mod, mod.adv3
    expect = {'help': m.HELP,
              'consts': (m.CAPITAL, a.RISK, a.RISK_MAX, m.RISK_TOTAL, m.STOP_MAX, m.NEW_MAX, m.MARGIN_MIN, m.MARGIN_MAX, m.MARGIN_EXC,
                         m.LIQ_FRAC, m.Z_CAP, a.COST, m.SLOTS, a.RELIABILITY, m.PACE, a.STRONG_Z, m.K1_MS, m.K5_MS),
              'defaults': dict(m.DEFAULTS), 'usdt': a.usdt}
    daily = {c: sorted(v.items()) for c, v in data.cs.items() if v}
    funds = data.funds or {}
    return {'texts': texts, 'runs': runs, 'records': records, 'log': buf.getvalue(), 'expect': expect, 'calls': calls, 'allocs': allocs,
            'views': views, 'case_reps': case_reps, 'records0': records0, 'jsha': sha256_bytes(raw), 'reg_text': reg_text,
            'reg_state': reg_state, 'daily': daily, 'fund': lambda coin: funds.get(coin) or (lambda d: 3 * a.BASE_F)}


def render_print(r):
    """What G-RENDER prints: sizes, counts and labels, never a coin, a price or a size."""
    events = own_chain(r['reg_text'])[0]
    sigs = own_signals(events)
    one = [c for c in r['calls'] if c['step'] == K1_MS]
    out('replies: %s; the bot\'s log: %d lines; candle requests %d - %d of 1-minute candles - and candles %d; allocations %d; views %d' % (
        ', '.join('%d chars in %d parts' % (sum(len(t) for t, _q, _k in r['texts'][k]), len(r['texts'][k])) for k in RENDER_CASES),
        r['log'].count('\n'), len(r['calls']), len(one), sum(len(c['rows']) for c in r['calls']), len(r['allocs']), len(r['views'])))
    kinds = {}
    for e in events:
        kinds[e.get('type')] = kinds.get(e.get('type'), 0) + 1
    out('registry: %d events %s; %d signals - %d legacy, %d open, %d ended by a stop, %d by an exit, %d expired; the seed of %d records '
        'and %d cards' % (len(events), json.dumps(kinds, sort_keys=True), len(sigs), sum(bool(s.get('legacy')) for s in sigs.values()),
                          sum(s['end'] is None for s in sigs.values()), sum(s['end'] == 'stop' for s in sigs.values()),
                          sum(s['end'] == 'exit' for s in sigs.values()), sum(s['end'] == 'expire' for s in sigs.values()),
                          (events[0] if events else {}).get('records', -1), (events[0] if events else {}).get('cards', -1)))
    for kind, run in r['runs'].items():
        rec = run['rec']
        out('%s check: %s, %s, %d parts; events announced %d; signals opened %d; STRONG at every rank %d; not taken %d, by code %s; notes %d; '
            'zones %d' % (kind, 'quiet' if rec['quiet'] else 'loud', 'one line' if rec['one_line'] else 'full', len(run['sent']),
                          len(rec['events']), len(rec['opened']), len(rec['strong_all']), len(rec['excluded']),
                          json.dumps(sorted({c for _c, _s, c in rec['excluded_codes']})), len(rec['notes']), len(rec['zones'])))


def render_checks(r, same):
    """G-RENDER: what the service copy's bot sent for each command and each check, read against its own registry rebuilt by this
    checker, its allocations against this checker's arithmetic, its views against the plans they were made from, its records and its
    constants; counts and labels only."""
    texts, runs, expect = r['texts'], r['runs'], r['expect']
    usdt = expect['usdt']
    events, _b, head, _w = own_chain(r['reg_text'])
    sigs = own_signals(events)
    checks = {
        'every command and both checks answered, no traceback and no failed request in the bot\'s log':
            all(texts.get(k) for k in RENDER_CASES) and set(runs) == {'signal', 'fact'} and 'Traceback' not in r['log']
            and 'failed' not in r['log'],
        'the markup is balanced in every part of every message (b, i)': all(
            html_balanced(t) for ps in list(texts.values()) + [x['sent'] for x in runs.values()] for t, _q, _k in ps),
    }
    reg_c, counts = registry_checks(r['reg_text'], r['records0'], r['calls'], r['daily'], r['fund'], r['reg_state'])
    checks.update(reg_c)
    checks['the seed names the journal the bot read, by SHA-256 and its records'] = bool(events) and events[0].get('journal_sha') == r['jsha'] \
        and events[0].get('records') == len(r['records0'])
    checks.update(opens_checks(events))
    checks.update(model_checks(events, sigs))
    checks.update(alloc_checks(r['allocs']))
    views_ok = len(r['views']) == 2
    for k, (rep, view, prm, new_ids, text) in enumerate(r['views']):
        views_ok &= [t for t, _q, _k in texts.get(RENDER_CASES[k], [])] == own_chunks(text) and len(view['items']) <= prm['n']
        for it in view['items']:
            p = it.get('pos')
            if p:
                views_ok &= ('Маржа <b>%s USDT</b> · плечо %d× изол. → позиция %s USDT' % (usdt(p['margin']), p['leverage'], usdt(p['notional']))
                             in text and 'Потеря на стопе <b>%s USDT</b>' % usdt(p['loss']) in text)
    checks['each «сигнал» reply is the bot\'s own view sent in its parts, each position written as the plan holds it, at most N items'] = views_ok
    p1 = r['views'][1][2] if len(r['views']) == 2 else {}
    sent1 = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[1], []))
    checks['«%s» rests on its parameters - 50,000 USDT, 1 %%, a limit of 2 %%, at most 3 - the defaults unchanged' % RENDER_CASES[1]] = (
        {k: p1.get(k) for k in ('capital', 'risk', 'total', 'stop', 'n', 'set')} == {
            'capital': 50000.0, 'risk': 1.0, 'total': 2.0, 'stop': 14.0, 'n': 3, 'set': ['capital', 'n', 'risk', 'total']}
        and expect['defaults'] == {'capital': CAPITAL, 'risk': RISK, 'total': RISK_TOTAL, 'stop': STOP_MAX, 'n': NEW_MAX, 'set': []}
        and 'Капитал 50 000 USDT · риск 1,0% · лимит 2% · стоп ≤ 14% · до 3 сделок · по запросу: капитал, топ, риск, лимит' in sent1)
    reg_t = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[2], []))
    checks['«реестр»: its counts, the chain whole and its fingerprint, the figures'] = (
        reg_t.startswith('📒 <b>ADV-3 · реестр STRONG</b>') and ('Сигналов %d' % len(sigs)) in reg_t and '🔐 Реестр:' in reg_t
        and 'цепочка нарушена' not in reg_t and '<b>Итоги</b>' in reg_t)
    rk = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[3], []))
    rep_k = (r['case_reps'].get(RENDER_CASES[3]) or [None])[0]
    rows_k = rep_k['rows'] if rep_k else {}
    order_k = own_order(rows_k, own_coins()) if rep_k else []
    listed = re.findall(r'^\d+\. [🟢🔴] (\S+) (?:LONG|SHORT) · z [^·\n]+· знаки [^·\n]+(· ★)?', rk, re.M)
    checks['«рейтинг»: the rule\'s first seven by this checker\'s own order, ★ exactly on STRONG at every rank'] = (
        bool(rep_k) and [c for c, _s in listed] == order_k[:7] and all((st == '· ★') == (c in own_strong(rows_k, order_k)) for c, st in listed))
    asst = '\n'.join(t for t, _q, _k in texts.get(RENDER_CASES[4], []))
    checks['«оценка»: the rung and the next readings, the six ratings, the registry\'s figures and that they move no rung'] = all(
        k in asst for k in ('рубеж %d из 5' % RUNG, 'после закрытия 28.10.2027', 'Оценка доверия', 'Реестр сигналов бота',
                            'описывает, а не доказывает'))
    checks['«помощь» and an unknown text answer HELP and nothing else'] = (
        [t for t, _q, _k in texts.get(RENDER_CASES[5], [])] == [expect['help']] == [t for t, _q, _k in texts.get(RENDER_CASES[6], [])])
    checks['every reply carries the keyboard on its last part alone and a notification; no check carries it'] = (
        all(ps and ps[-1][2] and not any(k for _t, _q, k in ps[:-1]) and not any(q for _t, q, _k in ps) for ps in texts.values())
        and not any(k for x in runs.values() for _t, _q, k in x['sent']))
    checks['the signal check\'s flags agree with what it announced, opened and found'] = 'signal' in runs and flags_checks(runs['signal'], 'signal')
    checks['the fact check\'s flags agree with what it announced, opened and found'] = 'fact' in runs and flags_checks(runs['fact'], 'fact')

    def record_ok(run, kind):
        rec, rows = run['rec'], run['rep']['rows']
        order = own_order(rows, own_coins())
        reg = rec['registry']
        return (rec['kind'] == 'check' and rec['slot'].endswith(' ' + kind) and len(rec['state']) == 42 and TRUST_KEYS <= set(rec['trust'])
                and rec['rule'] == H['rule'] and rec['close_of'] == run['rep']['close_of'] and rec['strong_all'] == own_strong(rows, order)
                and all(rec['state'][c]['rank'] == k for k, c in enumerate(order, 1)) and [c['id'] for c in rec['cards']] == rec['opened']
                and all(c['position'] for c in rec['cards']) and rec['excluded_codes'] == sorted([c, s, code] for c, s, code, _w, _d in rec['excluded'])
                and reg['head'] == head_at(r['reg_text'], reg['events']) and reg['broken'] is None
                and rec['params'] == {k: expect['defaults'][k] for k in ('capital', 'risk', 'total', 'stop', 'n')})
    checks['the check records: their slots, every coin\'s state ranked by this checker\'s order, STRONG at every rank, the cards numbered as '
           'opened with their positions, the coins not taken with their codes, the registry\'s head at their events, the defaults and the '
           'six ratings'] = set(runs) == {'signal', 'fact'} and record_ok(runs['signal'], 'signal') and record_ok(runs['fact'], 'fact')
    checks['the scratch journal holds, after the bot\'s own records, request, request, registry, ranking, assess, check, check'] = (
        [x.get('kind') for x in r['records']] == RENDER_KINDS)
    checks['the registry\'s state counts every event announced by the last check and keeps a place for every signal open'] = (
        isinstance(r['reg_state'], dict) and r['reg_state'].get('announced') == len(events)
        and all(str(i) in (r['reg_state'].get('cursor') or {}) for i, s in sigs.items() if s['end'] is None))
    checks['the bot\'s own journal, offset, daily-sent and check-done are as before the run, and no registry is written there'] = same is True
    checks['the bot\'s constants are this TZ\'s: 200,000 USDT, 0.5 % and 1 % a trade, 10 % in all, a stop within 14 %, 7 new a close, a '
           'margin of 0.5 to 4 % of the capital and 3.5 % its exception, 0.5 % of the volume, |z| capped at 3, 0.1 % a side, checks at '
           '00:10 and 15:07 UTC, the rung 1, 1.1 s between parts, |z| 1 for STRONG, candles of 1 and 5 minutes'] = expect['consts'] == (
        CAPITAL, RISK, RISK_MAX, RISK_TOTAL, STOP_MAX, NEW_MAX, MARGIN_MIN, MARGIN_MAX, MARGIN_EXC, LIQ_FRAC, Z_CAP, COST, SLOTS, RUNG,
        PACE, STRONG_Z, K1_MS, K5_MS)
    return checks, counts


def mode_render():
    """G-RENDER: the service copy's bot answers the commands and runs both checks on live data, its Telegram a stand-in, its STATE a
    scratch directory holding a copy of the bot's own journal - so the registry it seeds is the one the unit will seed from the same
    records. Its process's peak resident set and its time are printed (map §7 item 145): the mode is its own wrapper."""
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
    r = render_run(mod, mod.Data())
    same = own == own_files()
    render_print(r)
    checks, counts = render_checks(r, same)
    import resource
    out('replayed: %d events walked; signals whose events differ: %s' % (counts['walked'], counts['mismatches'] or 'none'))
    out('PEAK %d bytes resident; %.2f s of wall, %.2f s of processor' % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
                                                                       time.time() - t0, time.process_time() - c0))
    verdict('RENDER', checks)


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


def seen_journal(raw, t0):
    """The journal as the new process's seed read it - its bytes before the first check record stamped since the kill mark at t0 - by
    SHA-256, its records that parse and its STRONG cards with an entry: {'sha', 'records', 'cards'}."""
    pre_bytes, _found = prefix_before_check(raw, t0)
    objs = journal_objects(pre_bytes.decode('utf-8'))
    return {'sha': sha256_bytes(pre_bytes), 'records': len(objs),
            'cards': {(c, s, d, t) for t, c, s, d, _cd, _k in journal_cards(objs)}}


def mode_first():
    st = load_state()
    pre = st['marks']['kill']
    pid = int(show(BOT, 'MainPID')['MainPID'])
    raw = read(BOTDIR + '/journal.jsonl', 'rb')
    jtext = raw.decode('utf-8')
    recs, tail_ok = records_since(jtext, pre['t'])
    if not [r for r in recs if r.get('kind') == 'check']:
        if time.time() - pre['t'] < FIRST_BOUND:
            raise NotYet()
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    _serving, text, _tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    reg_text = read(BOTDIR + '/registry.jsonl') if os.path.exists(BOTDIR + '/registry.jsonl') else ''
    try:
        reg_state = json.loads(read(BOTDIR + '/registry-state.json'))
    except (OSError, ValueError):
        reg_state = None
    seen = seen_journal(raw, pre['t'])
    events = own_chain(reg_text)[0]
    sigs = own_signals(events)
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    out('first check: %s, %s, %d messages; events announced %d; signals opened %d; STRONG at every rank %d; not taken %d; check-done %s; '
        'registry %d events, %d signals - %d legacy, %d open; the journal the seed read: %d records, %d STRONG cards, %s… (the kill '
        'mark\'s %s…)' % ('quiet' if r.get('quiet') else 'loud', 'one line' if r.get('one_line') else 'full', len(r.get('message_ids') or []),
                         len(r.get('events') or []), len(r.get('opened') or []), len(r.get('strong_all') or []), len(r.get('excluded') or []),
                         done_text or '-', len(events), len(sigs), sum(bool(s.get('legacy')) for s in sigs.values()),
                         sum(s['end'] is None for s in sigs.values()), seen['records'], len(seen['cards']), seen['sha'][:12],
                         pre['journal_sha'][:12]))
    verdict('FIRST', first_checks(pre, recs, done_text, text, pid, tail_ok, reg_text, reg_state, seen))


def kept_files():
    """The work tree's files a report keeps by name: state.json, the two files B-DEPLOY saves, the registry's files B-ASIDE set aside -
    each named with .rolled - where a rollback came after the signal, and every file under logs/; relative to WORK, sorted."""
    names = ['state.json', 'bot.before', 'commit.before'] + [f for f in os.listdir(WORK) if f.endswith('.rolled')]
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz42-work--<path with - for />, by exclusive create and
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
        dest = FORENSICS + '/tz42-work--' + rel.replace('/', '--')
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


# ---- the self-test ------------------------------------------------------------------------------------------------

def synthetic(bot):
    """A synthetic market of fourteen coins for the stage's bot, Binance stood in for, its last close yesterday (UTC) and its 1- and
    5-minute candles a path to the present moment; and a journal of the cards TZ-35 to TZ-40 published in the four days before, built so
    that the seed opens eight signals - one stopped, one filled in its first minutes on 1-minute candles, one ended by the rule's exit,
    one expired, one filled and stopped, three that run - and skips a card repeated, a card of a coin still open, one not STRONG, one
    without an entry, one broken, one an allocation did not place and one of a record it does not read; and the present close holds a
    coin no longer STRONG with its signal open, one near its stop, one with a stop beyond 14 %, one too thin to trade and one that runs out
    of its zone at the fact check. Returns the Data stand-in."""
    a = bot.adv3
    utc = dt.timezone.utc
    last = dt.datetime.now(utc).date() - DAY
    coins = a.COINS[:14]
    cs, funds, slope = {}, {}, {}
    for n, coin in enumerate(coins):
        c, x = {}, 100.0 + n
        slope[coin] = (0.004 + 0.0015 * n) * (1 if n % 2 == 0 else -1)
        wide = 0.09 if coin == 'UNI' else 0.02
        for i in range(160):
            d = last - (159 - i) * DAY
            prev = x
            x *= (1 + slope[coin]) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            if coin == 'BTC' and d == last:
                x = prev * 0.93
            c[d] = (prev, max(prev, x) * (1 + wide), min(prev, x) * (1 - wide), x)
        cs[coin] = c
        funds[coin] = (lambda d: 0.0003) if n % 2 == 0 else (lambda d: 0.0)

    def close_on(coin, d):
        if d <= last:
            return cs[coin][d][3]
        return cs[coin][last][3] * (1 + slope[coin]) ** (d - last).days

    def path(coin, t):
        d = dt.datetime.fromtimestamp(t / 1000, utc).date()
        f = (t - midnight(d)) / DAY_MS
        lo, hi = close_on(coin, d - DAY), close_on(coin, d)
        return lo * (hi / lo) ** f * (1 + 0.002 * math.sin(2 * math.pi * t / 3_600_000))

    def unit_of(coin):
        days = sorted(cs[coin])
        return a.unit(cs[coin], days, len(days) - 1)

    D = last - 4 * DAY
    at = lambda d, h, m=0, s=0: int(dt.datetime.combine(d, dt.time(h, m, s), tzinfo=utc).timestamp() * 1000)
    iso_ = lambda ms: dt.datetime.fromtimestamp(ms / 1000, utc).isoformat(timespec='seconds')

    def card(coin, side, mode, t, close_of, k_e=1.0, k_s=None, k_t=(1.001, 1.5, 2.0), strong=True):
        P = path(coin, t)
        E = P * k_e
        C = close_on(coin, close_of)
        return {'coin': coin, 'side': side, 'strong': strong, 'mode': mode, 'entry': E, 'stop': E * (k_s or (0.5 if side > 0 else 1.5)),
                'targets': [E * k for k in k_t], 'close': C, 'U': C * 0.05, 'since': str(close_of - 10 * DAY), 'rank': 1}
    t1, t2, t3, t4, t5 = at(D + DAY, 0, 10, 30), at(D + DAY, 9), at(D + 2 * DAY, 0, 10), at(D + 2 * DAY, 9), at(D + 3 * DAY, 6)
    A = card('BTC', -1, 'market', t1, D, k_s=1.003, k_t=(0.99, 0.98, 0.97))
    recs = [{'utc': iso_(t1), 'kind': 'check', 'close_of': str(D), 'signals': {'BTC': 1},
             'cards': [A, card('XMR', 1, 'limit', t1, D, k_e=0.9998, k_s=0.9, k_t=(1.001, 1.003, 1.5))],
             'state': {'XMR': {'z': 2.0, 'sum': 4}}},
            {'utc': iso_(t2), 'kind': 'request', 'close_of': str(D),
             'cards': [dict(A, entry=A['entry'] * 1.001), card('BCH', 1, 'market', t2, D, k_t=(2.0, 3.0, 4.0)),
                       card('SKY', 1, 'limit', t2, D, k_e=0.95, k_s=0.9), card('LIT', 1, 'limit', t2, D, k_e=0.9985, k_s=0.99985),
                       card('NEAR', -1, 'market', t2, D, strong=False), dict(card('GRAM', -1, 'market', t2, D), mode='none', entry=None),
                       {'coin': 'ETH'}]},
            {'utc': iso_(t3), 'kind': 'check', 'close_of': str(D + DAY),
             'cards': [card('XMR', 1, 'market', t3, D + DAY), card('BTC', 1, 'market', t3, D + DAY)]},
            {'utc': iso_(t4), 'kind': 'alloc', 'close_of': str(D + DAY), 'alloc': {'items': [{'coin': 'HBAR'}], 'more': []},
             'cards': [card('HBAR', 1, 'market', t4, D + DAY), card('GRAM', -1, 'market', t4, D + DAY)]},
            {'utc': iso_(t4 + 3_600_000), 'kind': 'assess', 'close_of': str(D + DAY), 'cards': [card('XLM', -1, 'market', t4, D + DAY)]},
            {'utc': iso_(t5), 'kind': 'daily', 'close_of': str(D + 2 * DAY),
             'cards': [card('ZEC', -1, 'market', t5, D + 2 * DAY, k_t=(0.999, 0.5, 0.3))]}]
    with open(bot.STATE + '/journal.jsonl', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(recs[0]) + '\nnot json\n' + ''.join(json.dumps(r) + '\n' for r in recs[1:]))
    seen = {'premium': 0}
    U_ena = unit_of('ENA')

    def mark(coin):
        C = cs[coin][last][3]
        if coin == 'ENA':
            return C - 1.9 * U_ena
        if coin == 'SKY' and seen['premium'] >= 7:
            return C * 1.05
        return C

    def fake_fapi(path_, **p):
        if path_ == '/fapi/v1/premiumIndex':
            seen['premium'] += 1
            return [{'symbol': c + 'USDT', 'markPrice': str(mark(c)), 'lastFundingRate': '0.0001'} for c in coins]
        if path_ == '/fapi/v1/fundingInfo':
            return []
        assert path_ == '/fapi/v1/klines', path_
        coin = p['symbol'][:-4]
        if p['interval'] == '1d':
            vol = {'MORPHO': '1e5', 'LIT': '1e6'}.get(coin, '1e12')
            return [[midnight(last - k * DAY), '1', '1', '1', '1', '0', midnight(last - k * DAY + DAY) - 1, vol] for k in range(8)][::-1]
        step = {'1m': K1_MS, '5m': K5_MS}[p['interval']]
        now_ms = int(time.time() * 1000)
        t, out_ = -(-int(p['startTime']) // step) * step, []
        while t <= now_ms and len(out_) < int(p['limit']):
            o_, c_ = path(coin, t), path(coin, min(t + step, now_ms))
            out_.append([t, repr(o_), repr(max(o_, c_) * 1.0005), repr(min(o_, c_) * 0.9995), repr(c_), '0', t + step - 1, '0'])
            t += step
        return out_

    class Stub:
        def __init__(self):
            self.cs, self.funds, self.missing = cs, funds, []

        def fresh(self):
            return self.cs, self.funds

    a.fapi = fake_fapi
    return Stub()


def rechain(events):
    """A registry's text from its events, each line's n and prev rewritten so that the chain is whole - for the negative controls,
    which must fail on what they change and not on the chain."""
    lines, prev = [], GENESIS
    for k, e in enumerate(events, 1):
        e = dict(e, n=k, prev=prev)
        line = json.dumps(e, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        lines.append(line)
        prev = hashlib.sha256(line.encode('utf-8')).hexdigest()
    return ''.join(x + '\n' for x in lines)


def mode_selftest():
    import copy
    import tempfile
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    # ---- the pure readings, each with its negative controls -------------------------------------------------------------
    mp = ('**Revision string:** `%s`\n\n| anchor | value |\n|---|---|\n| `A1` — observation set | `229a944f2d51` |\n'
          '| `A3` — phase | `x / y` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n|---|---|---|---|---|\n'
          '| `SYSTEM-MAP.md` | — | — | reported | self-reference |\n| `a/b.py` | 1,135 | 50,928 | frozen | `%s` |\n'
          '| `c.py` | 7 | 8 | tracked | `%s` |\n\n---\n\n## 1. Repository\n| `z.py` | 1 | 1 | frozen | `%s` |\n') % (MAP_REV, 'a' * 64, 'b' * 64, 'c' * 64)
    rev, anchors, rows = parse_map(mp)
    ok(rev == MAP_REV and anchors == {'A1': '229a944f2d51', 'A3': 'x / y'}, 'parse_map: the revision and the anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', None), ('a/b.py', 1135, 50928, 'frozen', 'a' * 64), ('c.py', 7, 8, 'tracked', 'b' * 64)],
       'parse_map: the table\'s rows, thousands separators read, the next section left out')
    old = 'X = 1\nA, B = 1, 2\ndef a():\n    return 1\ndef b():\n    return 2\nclass K:\n    def m(self):\n        return 1\nCMD = 5\ndef gone():\n    pass\n'
    new = 'X = 1\nA, B = 1, 3\ndef a():\n    return 1\ndef b():\n    return 3\nclass K:\n    def m(self):\n        return 1\nNEWC = 0\ndef c():\n    return 0\n'
    T = (({'b'}, {'c'}, {'gone'}), ({'(A, B)'}, {'NEWC'}, {'CMD'}), ('a',))
    good = tree_checks('f', old, new, *T)
    ok(all(good.values()) and len(good) == 3, 'tree_checks: exactly the named definitions and assignments differ - a tuple target named as '
                                              'ast.unparse writes it - the rule\'s among the same, 3 of 3')
    for label, src in (('a definition that should be the same changed', new.replace('def a():\n    return 1', 'def a():\n    return 9')),
                       ('a definition named changed that did not', new.replace('def b():\n    return 3', 'def b():\n    return 2')),
                       ('an extra definition', new + 'def d():\n    return 0\n'),
                       ('an assignment changed and not named', new.replace('X = 1', 'X = 2'))):
        ok(not all(tree_checks('f', old, src, *T).values()), 'tree_checks: %s reads FAIL' % label)
    sd_a = strip_docs('def f():\n    """one"""\n    return 1\ndef g():\n    return 2\n')
    sd_b = strip_docs('def f():\n    """two"""\n    return 1\ndef g():\n    """new"""\n    return 3\n')
    ok(sd_a['f'] == sd_b['f'] and sd_a['g'] != sd_b['g'], 'strip_docs: a docstring alone is the same code; a changed body is not')
    ok(journal_lines('a\nb\r\nc\rd\n') == ['a', 'b', 'c', 'd'] and journal_lines('a\nb') == ['a', 'b']
       and journal_objects('{"k": 1}\n[1]\nx\n{"k": 2}\r\n') == [{'k': 1}, {'k': 2}],
       'journal_lines and journal_objects: universal newlines, as the bot\'s text file reads them; an object a record, a list or a broken line not')
    t_m = calendar.timegm(time.strptime('2026-11-03T09:00:00', '%Y-%m-%dT%H:%M:%S'))
    jl = ('{"utc": "2026-11-03T06:00:00+00:00", "kind": "daily"}\n{"utc": "2026-11-03T09:00:30+00:00", "kind": "request"}\n'
          '{"utc": "2026-11-03T09:00:40+00:00", "kind": "check"}\n{"utc": "2026-11-03T15:07:00+00:00", "kind": "check"}\n')
    rs, okj = records_since(jl, t_m)
    ok([r['kind'] for r in rs] == ['request', 'check', 'check'] and okj and not records_since(jl + 'broken\n', t_m)[1]
       and not records_since(jl.rstrip('\n'), t_m)[1] and records_since('broken\n' + jl, t_m)[1],
       'records_since: the records since the mark; a broken line after it or no final newline reads FAIL, one before it does not')
    ok(count_kind(jl + 'x\n{"kind": "check"}\n', 'check') == 3 and count_kind('', 'check') == 0, 'count_kind: the kind counted, a broken line left out')
    pb, found = prefix_before_check(jl.encode(), t_m)
    ok(found and pb == jl.encode()[:jl.index('{"utc": "2026-11-03T09:00:40')] and prefix_before_check(jl.encode(), t_m + 86400)
       == (jl.encode(), False), 'prefix_before_check: the bytes before the first check record since the mark - a request before it kept')
    ok(own_chunks('a\nb', 3) == ['a\nb'] and own_chunks('aa\nbb\ncc', 5) == ['aa\nbb', 'cc'] and own_chunks('a\n\nb', 1) == ['a', 'b']
       and own_chunks('x' * 9, 4) == ['x' * 9], 'own_chunks: parts at line ends, an empty line beginning a part left out, a long line whole')
    evs0 = [{'type': 'seed', 'utc': 'x'}, {'type': 'open', 'id': 1}, {'type': 'fill', 'id': 1, 'price': 1.0}]
    txt = rechain(evs0)
    e_, br, hd, wh = own_chain(txt)
    ok(br is None and wh and len(e_) == 3 and hd == head_at(txt, 3) and head_at(txt, 0) == GENESIS
       and hd == hashlib.sha256(txt.split('\n')[2].encode()).hexdigest(), 'own_chain and head_at: a whole chain, its head the last line\'s SHA-256')
    lines_ = txt.split('\n')
    ok(own_chain(txt.replace('"price":1.0', '"price":2.0'))[1] is None and own_chain('\n'.join([lines_[0], lines_[2], '']))[1] == 2
       and own_chain(lines_[0] + '\n' + lines_[1].replace('"id":1', '"id":2') + '\n' + lines_[2] + '\n')[1] == 3
       and own_chain(txt + '{"type"')[3] is False, 'own_chain: a removed line breaks it there, an edited one at the line after it; a torn end is not whole')
    d0 = dt.date(2026, 1, 1)
    closes = [100 * 1.01 ** i for i in range(150)] + [100 * 1.01 ** 149 * 0.98 ** k for k in range(1, 40)]
    days = [d0 + i * DAY for i in range(len(closes))]
    daily = [(d, (cl, cl * 1.002, cl * 0.998, cl)) for d, cl in zip(days, closes)]
    ok(sign_sum(days, closes, 120) == 4 and sign_sum(days, closes, 100) is None, 'sign_sum: four agreeing signs on a rising line, none before 112 days')
    DD = days[149]
    iss = midnight(DD + DAY) + 600_000
    o = {'side': 1, 'entry': 100.0, 'stop': 90.0, 'targets': [110.0, 120.0, 130.0], 'utc': iso_of(iss), 'valid': iso_of(midnight(DD + 2 * DAY)),
         'close_of': str(DD), 'mode': 'market'}
    K = lambda *rows, start=iss, w=K5_MS, closed=True: [(start + k * w, *r, closed) for k, r in enumerate(rows)]
    zero = lambda d: 0.0
    kind_of = lambda evs: [(e[0], e[1], e[3]) for e in evs]
    ev1, _s = own_walk(o, K((100, 105, 98, 104), (104, 111, 103, 110), (110, 121, 108, 120), (120, 121, 89, 95)), daily, zero)
    ok(kind_of(ev1) == [('target', 1, 110), ('target', 2, 120), ('stop', None, 90)] and abs(ev1[2][4] - (-10 - 0.001 * 190) / 10) < 1e-12
       and abs(ev1[2][5] - (-10.19)) < 1e-12, 'own_walk: two targets then the stop at 90, -1.019 R, -10.19 a unit')
    ok(kind_of(own_walk(o, K((100, 111, 89, 95)), daily, zero)[0]) == [('stop', None, 90)]
       and kind_of(own_walk(o, K((85, 86, 80, 82)), daily, zero)[0]) == [('stop', None, 85)]
       and kind_of(own_walk(o, K((112, 113, 89, 95)), daily, zero)[0]) == [('target', 1, 110), ('stop', None, 90)],
       'own_walk: a target and the stop in one candle the stop alone; an open beyond the stop ends there; an open past a target credits it first')
    ol = dict(o, mode='limit')
    ok(kind_of(own_walk(ol, K((105, 106, 101, 102), (102, 103, 99, 100)), daily, zero)[0]) == [('fill', None, 100.0)]
       and kind_of(own_walk(ol, K((98, 99, 97, 98)), daily, zero)[0]) == [('fill', None, 98)]
       and kind_of(own_walk(ol, K((101, 101, 89, 90)), daily, zero)[0]) == [('fill', None, 100.0), ('stop', None, 90)],
       'own_walk: a limit filled at itself, at an open past it, and filled and stopped in one candle')
    ev9, _s = own_walk(ol, K(*[(105, 105.5, 104.5, 105)] * 300), [], zero)
    ok(kind_of(ev9) == [('expire', None, None)] and ev9[0][2] == midnight(DD + 2 * DAY), 'own_walk: a limit not reached expires at its validity')
    x_i = next(i for i in range(150, len(closes)) if sign_sum(days, closes, i) < 2)
    E_ = closes[149]
    ox = dict(o, entry=E_, stop=E_ * 0.5, targets=[E_ * 2, E_ * 3, E_ * 4])
    evx, _s = own_walk(ox, K(*[(E_, E_ * 1.0001, E_ * 0.9999, E_)] * ((x_i - 149 + 2) * 288)), daily, lambda d: 0.0003)
    fund_ = sum(0.0003 * closes[i] for i in range(150, x_i + 1))
    ok(kind_of(evx) == [('exit', None, closes[x_i])] and evx[0][2] == midnight(days[x_i] + DAY)
       and abs(evx[0][4] - ((closes[x_i] - E_) - 0.001 * (E_ + closes[x_i]) - fund_) / (E_ * 0.5)) < 1e-12,
       'own_walk: a long ends at the first close whose sum of signs leaves +2, at that close, the funding of every close held paid')
    o2 = dict(o, utc=iso_of(iss + 20_000))
    st2 = start_of(o2)
    M = lambda *rows: K(*rows, start=st2['t'], w=K1_MS)
    ev12, _s = own_walk(o2, K((100, 111, 99, 110), start=iss + K5_MS), daily, zero, k1=M((100, 101, 99, 100), (100, 100, 89, 91)))
    ev13, s13 = own_walk(o2, K((100, 111, 99, 110), start=iss + K5_MS), daily, zero, k1=M(*[(100, 101, 99, 100)] * 4))
    ok(st2['t'] == iss + K1_MS and kind_of(ev12) == [('stop', None, 90)] and ev12[0][2] == iss + 2 * K1_MS
       and kind_of(ev13) == [('target', 1, 110)] and ev13[0][2] == iss + K5_MS and s13['t'] == iss + 2 * K5_MS,
       'own_walk and start_of: an issue at 00:10:20 starts at 00:11, its first minutes on 1-minute candles, then 5-minute ones')
    ev15, s15 = own_walk(o2, K((100, 111, 99, 110), start=iss + K5_MS), daily, zero, until=iss + 3 * K1_MS + 1,
                         k1=M(*[(100, 101, 99, 100)] * 4))
    ok(ev15 == [] and s15['t'] == iss + 3 * K1_MS, 'own_walk: until stops at the candle closing after it')
    rec_j = [{'utc': '2026-11-01T00:10:30+00:00', 'kind': 'check', 'close_of': '2026-10-31',
              'cards': [{'coin': 'BTC', 'side': 1, 'strong': True, 'mode': 'market', 'entry': 100.0, 'stop': 90.0, 'targets': [110, 120, 130],
                         'close': 100.0, 'U': 5.0},
                        {'coin': 'BTC', 'side': 1, 'strong': False, 'mode': 'market', 'entry': 100.0, 'stop': 90.0, 'targets': [1, 2, 3],
                         'close': 1, 'U': 1},
                        {'coin': 'ETH', 'side': 1, 'strong': True, 'mode': 'none', 'entry': None},
                        {'coin': 'DOGE', 'side': 1, 'strong': True, 'mode': 'market', 'entry': 1.0, 'stop': 0.9, 'targets': [1, 2, 3], 'close': 1, 'U': 1},
                        {'coin': 'ETH', 'side': 1, 'strong': True, 'mode': 'limit', 'entry': 1.0, 'stop': 1.1, 'targets': [1, 2, 3], 'close': 1, 'U': 1}]},
             {'utc': '2026-11-01T09:00:00.700+00:00', 'kind': 'alloc', 'close_of': '2026-10-31', 'alloc': {'items': [{'coin': 'SOL'}], 'more': []},
              'cards': [{'coin': c, 'side': 1, 'strong': True, 'mode': 'market', 'entry': 1.0, 'stop': 0.9, 'targets': [1, 2, 3], 'close': 1, 'U': 1}
                        for c in ('SOL', 'XRP')]},
             {'utc': '2026-11-01T10:00:00+00:00', 'kind': 'assess', 'close_of': '2026-10-31', 'cards': rec_j_cards()}]
    jc = journal_cards(rec_j)
    ok([(c, k) for _t, c, _s, _d, _cd, k in jc] == [('BTC', 'check'), ('SOL', 'alloc')] and jc[1][0] % 1000 == 0,
       'journal_cards: a STRONG card with an entry of the 42, its stop on its side, of a record the seed reads - of an allocation the coin '
       'placed - at its record\'s second; not STRONG, no entry, not of the 42, a stop on the wrong side, not placed, an assess record left out')
    cdj, ncj = coin_days(rec_j, ms_of('2026-11-03T09:00:00+00:00'))
    ok(ncj == 2 and abs(cdj - ((ms_of('2026-11-03T09:00:00+00:00') - ms_of('2026-11-01T00:10:30+00:00'))
                               + (ms_of('2026-11-03T09:00:00+00:00') - ms_of('2026-11-01T09:00:00+00:00'))) / DAY_MS) < 1e-9,
       'coin_days: each coin\'s days from its first card, summed')
    calls_s = [{'caller': 'seed', 'coin': 'BTC', 'start': 0, 'step': K5_MS, 'rows': K((100, 101, 99, 100)), 'n_before': 1}]
    rec_s = [{'utc': iso_of(iss), 'kind': 'daily', 'close_of': str(DD), 'cards': [dict(jc[0][4], entry=100.0)]},
             {'utc': iso_of(iss + 60_000), 'kind': 'request', 'close_of': str(DD), 'cards': [dict(jc[0][4], entry=101.0)]},
             {'utc': iso_of(iss + 120_000), 'kind': 'request', 'close_of': str(DD + DAY), 'cards': [dict(jc[0][4], entry=102.0)]},
             {'utc': iso_of(iss + 30 * K5_MS), 'kind': 'check', 'close_of': str(DD + DAY), 'cards': [dict(jc[0][4], entry=103.0, stop=102.9)]}]
    opened, states = own_seed(rec_s, union_k5(calls_s), {}, {'BTC': daily}, lambda c: zero)
    ok([x[2] for x in opened] == [str(DD)] and len(states) == 1,
       'own_seed: one signal of a coin, side and close; a card of another close while it is open is not a new signal')
    rows_o = {'A': {'signal': 1, 'z': 2.0, 'sum': 4, 'U': 1.0}, 'B': {'signal': -1, 'z': -3.0, 'sum': -4, 'U': 1.0},
              'C': {'signal': 1, 'z': 2.0, 'sum': 2, 'U': 1.0}, 'D': {'signal': 0, 'z': 9.0, 'sum': 0, 'U': 1.0},
              'E': {'signal': 1, 'z': 0.9, 'sum': 4, 'U': 1.0}, 'F': {'signal': -1, 'z': None, 'sum': None, 'U': 1.0}, 'G': {'signal': None}}
    ord_o = own_order(rows_o, list(rows_o))
    ok(ord_o == ['B', 'A', 'C', 'E'] and own_strong(rows_o, ord_o) == ['B', 'A'],
       'own_order and own_strong: by |z|, ties in the coins\' order; STRONG four agreeing signs and |z| at least 1')
    r_l = {'signal': 1, 'close': 100.0, 'U': 8.0}
    ok(own_entry(dict(r_l, mark=101.0)) == (101.0, 92.0) and own_entry(dict(r_l, mark=103.0)) == (102.0, 92.0)
       and own_entry(dict(r_l, mark=93.5))[0] is None and own_entry(dict(r_l, mark=None)) == (100.0, 92.0)
       and own_entry(dict(r_l, signal=-1, mark=97.0)) == (98.0, 108.0) and abs(own_stop_pct(dict(r_l, mark=101.0)) - 100 * 9 / 101) < 1e-12
       and own_lev(100.0, 92.0) == 7 and own_lev(100.0, 1.0) == 0,
       'own_entry, own_stop_pct and own_lev: at market in the zone, a limit at its edge past it, none near the stop, the close without a mark, '
       'a short mirrored; the rule\'s leverage')
    pz = {'notional': 12195, 'leverage': 7, 'margin': 1743, 'loss': 12195 * 0.082, 'risk_pct': 100 * 12195 * 0.082 / CAPITAL, 'qty': 121.95}
    ok(pos_ok(pz, 100.0, 92.0, CAPITAL, 7), 'pos_ok: 12,195 USDT at 7x, a margin of 1,743, the loss with both sides\' costs')
    for label, bad_p in (('a margin under 0.5 %', dict(pz, leverage=13, margin=939)), ('a margin above 4 %', dict(pz, notional=63000, margin=9000)),
                         ('a leverage above the rule\'s', dict(pz, leverage=8, margin=1525)), ('a loss not the arithmetic\'s', dict(pz, loss=900.0)),
                         ('a fractional notional', dict(pz, notional=12195.5)), ('a quantity not the notional\'s', dict(pz, qty=120.0))):
        ok(not pos_ok(bad_p, 100.0, 92.0, CAPITAL, 7), 'pos_ok: %s reads FAIL' % label)
    t_k = calendar.timegm(time.strptime('2026-11-03T09:00:00', '%Y-%m-%dT%H:%M:%S'))
    ok([latest_slot_text(t_k), latest_slot_text(t_k + 4 * 3600), latest_slot_text(t_k - 9 * 3600 + 1), latest_slot_text(t_k + 7 * 3600, SLOTS),
        replay_text(t_k), replay_text(t_k + 7 * 3600)]
       == ['2026-11-03 signal', '2026-11-03 fact', '2026-11-02 fact', '2026-11-03 fact', '2026-11-02 fact', '2026-11-02 fact'],
       'latest_slot_text and replay_text: the running code\'s 00:10 and 12:10, the new 15:07; the replay the day before\'s fact')
    ok(slot_instant('2026-11-03 fact') - slot_instant('2026-11-03 fact', OLD_SLOTS) == 2 * 3600 + 57 * 60 and slot_instant('x') is None,
       'slot_instant: the fact slot at 15:07 under the new schedule, 12:10 under the old; a text not a slot None')
    srv = ('2026-11-03T09:01:00Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-02 fact\n'
           '2026-11-03T09:01:01Z serving the pinned chat: pid 12 offset 9 check-done -')
    ok(served_from(srv, 11) == '2026-11-02 fact' and served_from(srv, 12) == '-' and served_from(srv, 13) is None,
       'served_from: the check-done a process logged at its start, \'-\' for none, None for a pid that did not serve')
    mk = lambda slot, u: {'kind': 'check', 'slot': slot, 'utc': u}
    good_c = [{'kind': 'daily', 'utc': '2026-11-01T06:00:00+00:00'}, mk('2026-11-01 signal', '2026-11-01T06:51:46+00:00'),
              mk('2026-11-01 fact', '2026-11-01T12:10:09+00:00'), mk('2026-11-01 signal', '2026-11-01T18:06:27+00:00'),
              mk('2026-11-02 signal', '2026-11-02T00:10:12+00:00'), {'kind': 'request', 'utc': '2026-11-02T08:00:00+00:00'},
              mk('2026-11-02 fact', '2026-11-02T12:15:30+00:00')]
    ck_, dl_ = clock_checks(good_c, '2026-11-02 fact')
    ok(all(ck_.values()) and len(ck_) == 3 and [round(x) for x in dl_] == [12, 330],
       'clock_checks: from TZ-40\'s replay - TZ-39\'s first and its fact before it not read - slots each once, each after its instant: 3 of 3')
    for label, recs_, done_ in (('a slot twice', good_c + [mk('2026-11-02 fact', '2026-11-02T12:20:00+00:00')], '2026-11-02 fact'),
                                ('a check before its slot', good_c[:4] + [mk('2026-11-02 signal', '2026-11-02T00:09:00+00:00')], '2026-11-02 signal'),
                                ('no check after TZ-40\'s replay', good_c[:4], '2026-11-01 fact'), ('no replay', good_c[4:], '2026-11-02 fact'),
                                ('a check-done not the last', good_c, '2026-11-02 signal'), ('no check-done', good_c, None)):
        ok(not all(clock_checks(recs_, done_)[0].values()), 'clock_checks: %s reads FAIL' % label)
    ok(all(window_reading(TZ41_EDGE - 1, False, False).values()) and all(window_reading(TZ41_EDGE + 1, True, False).values())
       and not all(window_reading(TZ41_EDGE, False, False).values()) and not all(window_reading(0, True, True).values()),
       'window_reading: before 2026-11-08 07:00 UTC or after TZ-41\'s report, never beside its work tree')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '2'}, 'read_done': '2026-11-02 fact',
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '3', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'serving': True, 'read': '2026-11-02 fact', 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('read', '2026-11-03 signal', 'a process that read another check-done'), ('start', 1200.0, 'a start 200 s after the mark'),
                            ('sha_bot', H['bot_old'], 'the old bot'), ('traceback', True, 'a traceback'), ('procs', [11, 12], 'a second process'),
                            ('serving', False, 'no serving line'), ('sha_unit', 'x', 'another unit file')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    ok(not all(unit_checks('new', pre, dict(now, caps={u: dict(c, NRestarts='1') for u, c in pre['caps'].items()})).values())
       and all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'])).values()), 'unit_checks: a capture restarted reads FAIL; the rollback the old bot')
    t0 = calendar.timegm(time.strptime('2026-11-02T14:00:00', '%Y-%m-%dT%H:%M:%S'))
    pre_f = dict(pre, t=float(t0), read_done='2026-11-01 fact', journal_sha='j')
    ev_f = [{'type': 'seed', 'utc': '2026-11-02T14:00:40+00:00', 'journal_sha': 'j' * 64, 'records': 3, 'cards': 1},
            {'type': 'open', 'id': 1, 'utc': '2026-11-01T00:10:30+00:00', 'coin': 'BTC', 'side': 1, 'close_of': '2026-10-31', 'legacy': True},
            {'type': 'fill', 'id': 1, 'utc': '2026-11-01T00:10:30+00:00', 'price': 1.0},
            {'type': 'open', 'id': 2, 'utc': '2026-11-02T14:00:45+00:00', 'coin': 'ETH', 'side': 1, 'close_of': '2026-11-01', 'legacy': False}]
    rt = rechain(ev_f)
    seen = {'sha': 'j' * 64, 'records': 3, 'cards': {('BTC', 1, '2026-10-31', ms_of('2026-11-01T00:10:30+00:00'))}}
    rec = {'utc': '2026-11-02T14:00:50+00:00', 'kind': 'check', 'slot': '2026-11-02 signal', 'close_of': '2026-11-01', 'rule': H['rule'],
           'message_ids': [5, 6], 'state': {str(k): {} for k in range(42)}, 'trust': {k: 0 for k in TRUST_KEYS}, 'strong_all': [],
           'cards': [{'id': 2, 'position': {'notional': 1}}], 'opened': [2], 'excluded_codes': [], 'events': [],
           'registry': {'events': 4, 'head': head_at(rt, 4), 'seeded': 1}, 'quiet': False}
    log_f = ('2026-11-02T14:00:35Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-01 fact\n'
             '2026-11-02T14:00:50Z check sent: 2026-11-02 signal for the close of 2026-11-01 | events 0 | new 1 | loud | full')
    rstate = {'announced': 4, 'cursor': {'1': {}, '2': {}}}
    fargs = ([rec], '2026-11-02 signal', log_f, 11, True, rt, rstate, seen)
    good = first_checks(pre_f, *fargs)
    ok(all(good.values()) and len(good) == 10, 'first_checks: the replayed signal check after a 14:00 restart, the registry it seeded, 10 of 10')
    ok(all(first_checks(dict(pre_f, t=float(t0 + 2 * 3600)), [rec], '2026-11-02 fact', log_f.replace('14:00:35', '16:00:35'), 11, True,
                        rt, rstate, seen).values()), 'first_checks: a 16:00 restart, after 15:07, wants check-done at the fact slot')
    for label, k, v in (('no check record', 0, []), ('two check records', 0, [rec, rec]), ('another slot', 0, [dict(rec, slot='2026-11-02 fact')]),
                        ('no message ids', 0, [dict(rec, message_ids=[])]), ('a quiet check that opened a signal', 0, [dict(rec, quiet=True)]),
                        ('cards not as opened', 0, [dict(rec, opened=[3])]), ('a head not the registry\'s', 0,
                                                                              [dict(rec, registry=dict(rec['registry'], head='x'))]),
                        ('check-done at the fact before 15:07', 1, '2026-11-02 fact'), ('a failed check in the log', 2, log_f + '\ncheck failed: x'),
                        ('another pid serving', 3, 12), ('a broken journal', 4, False), ('a broken registry', 5, rt.replace('"price":1.0', '"price":2.0', 1)),
                        ('a seed naming another journal', 7, dict(seen, sha='k' * 64)), ('a legacy signal not of the journal', 7, dict(seen, cards=set())),
                        ('a state that does not count the events', 6, {'announced': 3, 'cursor': {'1': {}, '2': {}}}),
                        ('no place for a signal open', 6, {'announced': 4, 'cursor': {'1': {}}})):
        a_ = list(fargs)
        a_[k] = v
        ok(not all(first_checks(pre_f, *a_).values()), 'first_checks: %s reads FAIL' % label)
    log = ('2026-10-31T06:00:01Z daily sent\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 check-done -\n'
           'Traceback (most recent call last):\n  File x\n2026-10-31T09:00:30Z check sent: 2026-10-31 signal')
    t_l = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    s_, text_, tb_ = log_since(log, t_l, 11)
    ok(s_ and tb_ and 'daily sent' not in text_ and '  File x' in text_ and not log_since(log, t_l, 12)[0],
       'log_since: the lines since the mark, a traceback\'s with them, the serving pid found')
    ok(memory_gate(MEM_FLOOR, None) == (True, MEM_FLOOR) and memory_gate(MEM_FLOOR - 1, MEM_FLOOR) == (True, MEM_FLOOR)
       and memory_gate(MEM_FLOOR - 1, MEM_FLOOR - 2) == (False, MEM_FLOOR - 2), 'memory_gate: a first read below the floor is decided by the second')
    ok(all(number_reading([TZ_FILE, 'CryptoTZ/TZ-41-x.md']).values()) and not all(number_reading([TZ_FILE, 'CryptoTZ/TZ-42-other.md']).values())
       and not all(number_reading([TZ_FILE, 'CryptoReports/TZ-42-x-report.md']).values()), 'number: one file of the number PASS; two, or a report, FAIL')
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        os.makedirs(tmp + '/render-state')
        for rel in ('state.json', 'bot.before', 'adv3.before', 'commit.before', 'registry.jsonl.rolled', 'registry-state.json.tmp.rolled',
                    'logs/01-a.log', 'logs/sub/02-b.log', 'x.txt', 'render-state/journal.jsonl'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        saved_work = WORK
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['bot.before', 'commit.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'registry-state.json.tmp.rolled', 'registry.jsonl.rolled',
               'state.json'],
       'kept_files: the named files, a registry set aside, and the logs; nothing else - not adv3.before, which B-DEPLOY no longer saves, '
       'nor the render\'s scratch journal')

    # ---- G-RENDER on the stage's own bot and a synthetic market ---------------------------------------------------------
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
            data = synthetic(bot)
            r = render_run(bot, data)
        finally:
            bot.adv3.fapi = real_fapi
            time.sleep = real_sleep
    checks, counts = render_checks(r, True)
    ok(all(checks.values()) and len(checks) == 34, 'render_checks: the stage\'s bot on a synthetic market reads 34 of 34 - %s'
       % [k for k, v in checks.items() if not v])
    events = own_chain(r['reg_text'])[0]
    sigs = own_signals(events)
    ok({e['type'] for e in events} == {'seed', 'open', 'fill', 'target', 'stop', 'exit', 'expire'} and not counts['mismatches']
       and [s['coin'] for _i, s in sorted(sigs.items()) if s.get('legacy')] == ['BTC', 'XMR', 'BCH', 'SKY', 'LIT', 'BTC', 'HBAR', 'ZEC']
       and [(s['end'], s['hit'] > 0) for _i, s in sorted(sigs.items()) if s.get('legacy')]
       == [('stop', False), (None, True), ('exit', False), ('expire', False), ('stop', False), (None, True), (None, True), (None, True)],
       'the synthetic registry meets every event: the seed\'s eight legacy signals - stopped, filled and two targets on, ended by the rule\'s '
       'exit, expired, filled and stopped, three a target and on - and the cards it skips')
    xmr = next(s for s in sigs.values() if s['coin'] == 'XMR' and s.get('legacy'))
    fill = next(e for e in events if e.get('id') == xmr['id'] and e['type'] == 'fill')
    ok(ms_of(fill['utc']) % K5_MS != 0 and ms_of(fill['utc']) < ceil_to(ms_of(xmr['utc']), K5_MS)
       and any(c['step'] == K1_MS and c['caller'] == 'seed' for c in r['calls']),
       'the first minutes: a limit filled on a 1-minute candle before the first 5-minute boundary after its issue, read by the seed')
    codes = {code for x in (r['runs']['signal']['rec'], r['runs']['fact']['rec']) for _c, _s, code in x['excluded_codes']}
    v_codes = {code for _rep, v, _p, _n, _t in r['views'] for _c, _s, code, _w, _d in v['excluded']} | {
        it.get('code') for _rep, v, _p, _n, _t in r['views'] for it in v['items'] if it.get('code')}
    ok({'margin', 'count', 'near', 'stop'} <= codes and {'room', 'top'} <= v_codes and r['runs']['signal']['rec']['notes']
       and r['runs']['fact']['rec']['zones'] and len([s for s in sigs.values() if not s.get('legacy')]) == 6,
       'the synthetic market meets every reason: the model\'s margin, count, near and stop; the request\'s room - a signal of the close '
       'kept without a position - and top; a note and a zone; six model signals')

    def bad(fn):
        r2 = copy.deepcopy({k: v for k, v in r.items() if k != 'fund'})
        r2['fund'] = r['fund']
        fn(r2)
        return not all(render_checks(r2, True)[0].values())

    def ev_edit(fn):
        def go(r2):
            evs = own_chain(r2['reg_text'])[0]
            fn(evs)
            r2['reg_text'] = rechain(evs)
        return go
    stop_ev = next(i for i, e in enumerate(events) if e['type'] == 'stop')
    tgt_ev = next(i for i, e in enumerate(events) if e['type'] == 'target')
    leg_ev = next(i for i, e in enumerate(events) if e['type'] == 'open' and e.get('legacy'))
    mod_ev = next(i for i, e in enumerate(events) if e['type'] == 'open' and not e.get('legacy'))
    ok(bad(ev_edit(lambda evs: evs[stop_ev].update(price=evs[stop_ev]['price'] * 1.01))), 'render_checks: a stop at another price reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[stop_ev].update(R=evs[stop_ev]['R'] + 0.01))), 'render_checks: a result in R not the walk\'s reads FAIL')
    ok(bad(ev_edit(lambda evs: evs.pop(tgt_ev))), 'render_checks: a target the walk finds and the registry lacks reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[leg_ev].update(entry=evs[leg_ev]['entry'] * 1.001))), 'render_checks: a legacy signal not its card\'s reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[mod_ev].update(margin=evs[mod_ev]['margin'] + 1))), 'render_checks: a signal\'s margin not its arithmetic\'s reads FAIL')
    ok(bad(ev_edit(lambda evs: evs[mod_ev].update(valid=iso_of(ms_of(evs[mod_ev]['valid']) + DAY_MS)))),
       'render_checks: a validity a day late reads FAIL')
    ok(bad(lambda r2: r2.update(reg_text=r2['reg_text'].replace('"type":"fill"', '"type":"fill","x":1', 1))),
       'render_checks: a registry line edited after it was written reads FAIL')
    oid = str(min(i for i, s_ in sigs.items() if s_['end'] is None))
    ok(bad(lambda r2: r2['reg_state']['cursor'][oid].update(t=r2['reg_state']['cursor'][oid]['t'] - K5_MS)),
       'render_checks: the place of a signal open not the replay\'s reads FAIL')
    a0 = next(k for k, c in enumerate(r['allocs']) if any(it.get('pos') for it in c['items']))
    i0 = next(k for k, it in enumerate(r['allocs'][a0]['items']) if it.get('pos'))
    ok(bad(lambda r2: r2['allocs'][a0]['items'][i0]['pos'].update(leverage=r2['allocs'][a0]['items'][i0]['pos']['leverage'] + 1)),
       'render_checks: an allocation\'s leverage above the rule\'s reads FAIL')
    ok(bad(lambda r2: r2['allocs'][a0]['items'][i0]['pos'].update(want=r2['allocs'][a0]['items'][i0]['pos']['want'] * 1.1)),
       'render_checks: a wanted risk not the shares\' reads FAIL')
    ok(bad(lambda r2: r2['allocs'][a0].update(room=0.0)), 'render_checks: risk taken beyond the room reads FAIL')
    sig0 = r['texts'][RENDER_CASES[0]]
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[0]: [(sig0[0][0].replace('Маржа <b>', 'Маржа <b>1', 1),) + sig0[0][1:]] + sig0[1:]})),
       'render_checks: a «сигнал» reply not its view\'s reads FAIL')
    ok(bad(lambda r2: r2['runs']['signal']['rec'].update(quiet=not r2['runs']['signal']['rec']['quiet'])),
       'render_checks: a check whose quiet flag disagrees with what it announced reads FAIL')
    ok(bad(lambda r2: r2['runs']['fact']['rec'].update(one_line=True)), 'render_checks: one line beside a zone left reads FAIL')
    ok(bad(lambda r2: r2['runs']['signal']['rec'].update(strong_all=r2['runs']['signal']['rec']['strong_all'][:-1])),
       'render_checks: a record whose STRONG at every rank is not the checker\'s reads FAIL')
    ok(bad(lambda r2: r2.update(records=r2['records'][:-1])), 'render_checks: a journal lacking a record reads FAIL')
    ok(bad(lambda r2: r2['expect'].update(consts=(150000.0,) + r2['expect']['consts'][1:])), 'render_checks: another capital reads FAIL')
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[5]: [('x', False, True)]})), 'render_checks: «помощь» not HELP reads FAIL')
    rk = r['texts'][RENDER_CASES[3]]
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[3]: [(rk[0][0].replace(' · ★', '', 1),) + rk[0][1:]] + rk[1:]})),
       'render_checks: a STRONG coin of the ranking without its ★ reads FAIL')
    ok(bad(lambda r2: r2['texts'].update({RENDER_CASES[2]: [t[:2] + (False,) for t in r2['texts'][RENDER_CASES[2]]]})),
       'render_checks: a reply without its keyboard reads FAIL')
    ok(not all(render_checks(r, False)[0].values()), 'render_checks: the bot\'s own record changed reads FAIL')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def rec_j_cards():
    return [{'coin': 'XRP', 'side': 1, 'strong': True, 'mode': 'market', 'entry': 1.0, 'stop': 0.9, 'targets': [1, 2, 3], 'close': 1, 'U': 1}]


def ceil_to(ms, step):
    return -(-ms // step) * step


def main(argv):
    if not argv:
        sys.exit('usage: tz42-advisor-registry.py MODE [ARG]')
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
