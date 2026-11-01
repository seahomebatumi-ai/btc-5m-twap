#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands; two checks a day by the unit's own scheduler, at
# 00:10 UTC (04:10 in Batumi) the close's signals and at 12:10 UTC (16:10) the facts of the moment - the stops of the trades the
# cards offered, the entry zones, the STRONG candidates - each loud only for an alert and one quiet line where it finds nothing;
# and a journal of every check's state and every message sent. Standard library only; adv3.py lies beside it.
# Modes: --serve (the unit's), --probe, --find-chat, --hello, --selftest.
# Exits: 0 or SIGTERM, restarted by systemd; 3 without a token or a chat id and 4 where glibc refuses its two
# settings, neither restarted; 1, an unexpected exception, restarted.
import argparse, ctypes, datetime as dt, html, json, math, os, re, sys, time, traceback, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adv3  # noqa: E402

TOKEN_FILE = '/etc/adv3-bot/token'
CHAT_FILE = '/etc/adv3-bot/chat-id'
STATE = '/var/lib/adv3-bot'
TG = 'https://api.telegram.org/bot{token}/{method}'
UA = 'adv3-bot/1'
# TZ-39's two checks a day (CANON PART VII). The rule changes state only at a daily close: the check of 00:10 UTC reads the close's
# signals, ten minutes after it - the margin kept for the day's last funding settlement; the check of 12:10 reads facts alone and
# never a signal of a half-formed candle.
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
BATUMI = dt.timedelta(hours=4)
POLL, RETRY, LIMIT = 50, 300, 4000
OPEN = ('сигнал', 'сигналы', 'signal', 'signals', 'топ', 'top', 'стратегия', 'стратегию', 'strategy')
ASSESS = ('оценка', 'оценки', 'оценку', 'rating')
HEAD = re.compile(r'^\s*/?([^\W\d_]+)')
TOPN = re.compile(r'(?:топ|top)[\s\-\u2013]*(\d{1,2})(?!\d)', re.I)
# The allocation view (TZ-37): the stop's limit in percent of the entry - the Boss's 14 % since TZ-39 - the smallest position, the
# share of a coin's mean daily quote volume a position may take, the discount for same-way correlation, the strength's cap, the
# days of volume.
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS = 14.0, 5.0, 0.001, 0.5, 3.0, 7
LIST_MAX = 7   # the longest list «сигнал топ N» shows; STRONG stays a label of the TOP-3
SIDE, DOT = {1: 'LONG', -1: 'SHORT'}, {1: '🟢', -1: '🔴'}
FOOTER = '<i>Не инвестиционный совет · «оценка» — на чём держится уверенность</i>'
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — ТОП-3 правила сейчас: вход, стоп, цели и размер при депозите 10 000 USDT и риске 0,5% на сделку.\n'
        '«сигнал топ 7» — то же для семи сильнейших, от 1 до 7; ★ STRONG бывает только в ТОП-3.\n'
        '«сигнал 10000 топ 3» — распределить 10 000 USDT между сделками STRONG со стопом не дальше 14% входа; подошло меньше — '
        'покажу меньше, ни одной — скажу. Риск — 0,5% бюджета на сделку, не больше 1%: «сигнал 10000 топ 3 1». Чего нельзя '
        'разместить без превышения риска, остаётся свободным.\n'
        '«оценка» — шесть оценок доверия и на чём они держатся.\n'
        'Проверки — в 04:10 и 16:10 по Батуми: в 04:10 сигналы закрытия дня, в 16:10 стопы и зоны входа. Со звуком — только '
        'когда задет стоп сделки, которую предлагала карточка, её сигнал закончился или появился новый STRONG, проходящий '
        'лимиты; остальное приходит тихо, а проверка без событий — одной строкой.')


SECRETS = []   # the token, never written to the log


def log(*parts):
    line = ' '.join(str(p) for p in parts)
    for secret in SECRETS:
        line = line.replace(secret, '<token>')
    print(dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), line, flush=True)


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read().strip()


def put(path, text):
    """Replace path's content in one rename, so a kill mid-write leaves the old content or the new."""
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def malloc_tune():
    """glibc's mmap threshold at 128 KiB and its arenas at two, as the project's long-lived units fix them; True if
    glibc took both."""
    try:
        libc = ctypes.CDLL('libc.so.6')
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


class Telegram:
    """The Bot API through one request function: every call is a JSON POST with UA as its User-Agent."""

    def __init__(self, token, chat=None):
        self.token, self.chat = token, chat

    def call(self, method, http_timeout=30, **params):
        req = urllib.request.Request(TG.format(token=self.token, method=method), data=json.dumps(params).encode(),
                                     headers={'User-Agent': UA, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=http_timeout) as r:
                out = json.loads(r.read())
        except urllib.error.HTTPError as e:
            out = json.loads(e.read() or b'{}')
        if not out.get('ok'):
            raise RuntimeError(f"telegram {method}: {out.get('error_code')} {out.get('description')}")
        return out['result']

    def send(self, text, quiet=False):
        """The text as HTML, in parts of at most LIMIT characters; a part Telegram cannot parse goes as plain text. quiet sends
        every part without a notification (the Bot API's disable_notification)."""
        ids, extra = [], ({'disable_notification': True} if quiet else {})
        for part in chunks(text):
            try:
                ids.append(self.call('sendMessage', chat_id=self.chat, text=part, parse_mode='HTML',
                                     disable_web_page_preview=True, **extra)['message_id'])
            except RuntimeError as e:
                if 'parse entities' not in str(e):
                    raise
                plain = html.unescape(re.sub(r'</?[bi]>', '', part))
                ids.append(self.call('sendMessage', chat_id=self.chat, text=plain,
                                     disable_web_page_preview=True, **extra)['message_id'])
        return ids


def chunks(text, limit=LIMIT):
    """Telegram takes at most 4,096 characters a message: split at line ends, never inside a line."""
    out, cur = [], ''
    for line in text.split('\n'):
        if cur and len(cur) + 1 + len(line) > limit:
            out.append(cur)
            cur = line
        else:
            cur = f'{cur}\n{line}' if cur else line
    if cur:
        out.append(cur)
    return out


def numbers(text):
    """(budget, risk) from the numbers in text: the first of 100 or more is the budget, None where there is none, the
    first below 100 the risk in percent, at least 0.05 and at most the rule's 1; 15 000 reads 15000, and 10k, 10к and 10 тыс
    read 10000."""
    text = re.sub(r'(?<=\d)[ \u00a0\u202f](?=\d{3}(?!\d))', '', text)
    text = re.sub(r'(\d+(?:[.,]\d+)?)[ \u00a0]?(?:тыс\.?|[кk])(?![^\W\d_])',
                  lambda m: f"{float(m.group(1).replace(',', '.')) * 1000:.0f}", text, flags=re.I)
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', text)]
    budget = next((x for x in nums if x >= 100), None)
    small = [x for x in nums if x < 100]
    risk = small[0] if small else adv3.RISK
    return (None if budget is None else min(budget, 10_000_000.0)), min(max(risk, 0.05), adv3.RISK_MAX)


def route(text):
    """('signal', None, n, risk) for «сигнал [топ N] [risk]», the rule's first n coins - n read after «топ» or «top», 1 to
    LIST_MAX, default TOP_N; ('alloc', budget, n, risk) where a budget of 100 or more is given - «сигнал 10000 топ 3», «сигнал
    15000 топ 5», «сигнал 10000», «топ 3 на 10000» - the allocation view, n likewise; ('assess', None, None, None) for «оценка»;
    None where the text is none of them. risk is the percent of the deposit or budget a trade may lose at its stop (default
    0.5, at most 1)."""
    text = text or ''
    m = HEAD.match(text)
    if not m:
        return None
    word = m.group(1).lower()
    if word in ASSESS:
        return ('assess', None, None, None)
    if word not in OPEN:
        return None
    s = re.sub(r'@\w+', ' ', text)
    top = TOPN.search(s)
    n = adv3.TOP_N
    if top:
        n = min(max(int(top.group(1)), 1), LIST_MAX)
        s = s[:top.start()] + ' ' + s[top.end():]
    budget, risk = numbers(s)
    return ('signal', None, n, risk) if budget is None else ('alloc', budget, n, risk)


class Data:
    """The closed candles and funding of every coin, fetched from fapi.binance.com once per close. A coin whose
    candles fail is reported missing and the rest go on; where every coin fails, the fetch raises."""

    def __init__(self):
        self.cs = self.funds = self.close = self.at = None
        self.missing = []

    def fresh(self):
        """Refetched when a newer close exists, and once more where the last fetch fell in the first ten minutes
        after midnight UTC, before the day's last funding settlement was surely published."""
        now = dt.datetime.now(dt.timezone.utc)
        midnight = dt.datetime.combine(now.date(), dt.time(0, 0), tzinfo=dt.timezone.utc)
        early = self.at is not None and midnight <= self.at < midnight + dt.timedelta(minutes=10) <= now
        if self.close is None or self.close < (now - dt.timedelta(days=1)).date() or early:
            now_ms = int(now.timestamp() * 1000)

            def safe(fn, *args):
                try:
                    return fn(*args)
                except Exception as e:
                    log('fetch failed:', args[0], repr(e)[:300])
                    return None

            with ThreadPoolExecutor(6) as pool:
                got = list(pool.map(lambda k: safe(adv3.fapi_candles, k + 'USDT', now_ms), adv3.COINS))
                fs = list(pool.map(lambda k: safe(adv3.fapi_funding, k + 'USDT', adv3.FORWARD_FROM - adv3.DAY),
                                   adv3.COINS))
            cs = {k: v or {} for k, v in zip(adv3.COINS, got)}
            if not any(cs.values()):
                raise RuntimeError('fapi.binance.com served no candles')
            self.cs, self.missing = cs, [k for k, v in zip(adv3.COINS, got) if not v]
            self.funds = {k: adv3.funding_of(v, lambda d: d >= adv3.FORWARD_FROM) for k, v in zip(adv3.COINS, fs)
                          if v is not None}
            self.close = max(max(c) for c in cs.values() if c)
            self.at = now
            log('candles refreshed to the close of', self.close, '| missing', ','.join(self.missing) or '-')
        return self.cs, self.funds


def live_report(data, deposit, risk):
    """The report of the latest close at this moment: the closed candles and funding Data holds, the mark prices and funding
    intervals read now; marks that fail leave the cards on the close."""
    cs, funds = data.fresh()
    try:
        marks = adv3.fapi_marks()
    except Exception as e:
        log('marks failed:', repr(e)[:300])
        marks = {}
    try:
        intervals = adv3.fapi_intervals()
    except Exception as e:
        log('funding intervals failed:', repr(e)[:300])
        intervals = None
    return adv3.report(cs, funds, marks, deposit, risk, int(time.time() * 1000), data.missing, intervals)


def ranked(rep):
    """Every LONG or SHORT coin of the report in the rule's order: adv3.ranking applied again to the coins it has not yet
    placed, so the first three are the report's TOP-3 and no order is written here."""
    rest = [(coin, (r['signal'], r.get('z'), r.get('sum'), r.get('U'), r.get('close'))) for coin in adv3.COINS
            for r in (rep['rows'][coin],) if r.get('signal') in (1, -1)]
    out = []
    while rest:
        top, _ = adv3.ranking(rest)
        if not top:
            break
        out += top
        rest = [x for x in rest if x[0] not in top]
    return out


def top_n(rep, n):
    """The report with the cards of the rule's first n coins: the TOP-3's own cards, then adv3.card for the rest at the report's
    deposit and risk, STRONG only within the TOP-3; each card its rank of n; the ratings recomputed over them."""
    have = {cd['coin']: cd for cd in rep['cards']}
    cards = [have.get(coin) or adv3.card(coin, rep['rows'][coin], False, rep['deposit'], rep['risk_pct'])
             for coin in ranked(rep)[:n]]
    out = dict(rep, cards=[dict(cd, rank=k, of=n) for k, cd in enumerate(cards, 1)], n=n)
    out['trust'] = adv3.trust(out)
    return out


def make(data, deposit, risk, n=adv3.TOP_N):
    """The report of the rule's first n coins and its message at this moment."""
    rep = top_n(live_report(data, deposit, risk), n)
    return rep, adv3.message(rep, adv3.FACTS)


def returns_of(c, last, days=adv3.VOL_DAYS):
    """{day: log return} of one coin's last `days` closed days up to last."""
    ds = sorted(d for d in c if d <= last)[-(days + 1):]
    return {ds[k]: math.log(c[ds[k]][3] / c[ds[k - 1]][3]) for k in range(1, len(ds))}


def correlation(a, b):
    """Pearson correlation of two {day: return} series on their common days; None below 30 days or for a flat series."""
    days = sorted(set(a) & set(b))
    if len(days) < 30:
        return None
    x, y = [a[d] for d in days], [b[d] for d in days]
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sxx, syy = sum((u - mx) ** 2 for u in x), sum((v - my) ** 2 for v in y)
    if sxx <= 0 or syy <= 0:
        return None
    return sum((u - mx) * (v - my) for u, v in zip(x, y)) / math.sqrt(sxx * syy)


def liquidity(coin, now_ms):
    """The mean quote volume in USDT of the coin's last LIQ_DAYS closed days, from fapi.binance.com, or None."""
    try:
        rows = adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval='1d', limit=LIQ_DAYS + 1)
        vols = [float(r[7]) for r in rows if int(r[6]) < now_ms][-LIQ_DAYS:]
        return sum(vols) / len(vols) if vols else None
    except Exception as e:
        log('liquidity failed:', coin, repr(e)[:200])
        return None


def plan(rep, cs, budget, n, risk, liq):
    """TZ-37's allocation of one report. Qualifying: a STRONG coin of the report, current prices served, an entry, a stop no
    farther than STOP_MAX percent of the entry, among the first n by rank; a weaker setup never fills a place. Each qualifying
    trade's share is its strength (at most Z_CAP) discounted by CROWD times its mean same-way correlation with the others
    (an unknown correlation counts as 1); its loss at the stop, costs of both sides included, is k * risk percent of the
    budget times the share, at most the rule's RISK_MAX, and all together at most RISK_ALL; its position is that loss over
    (stop + 2 * COST), at most LIQ_FRAC of the coin's mean daily volume where known, the whole at most the budget, in whole
    USDT rounded down; below MIN_NOTIONAL it is dropped. Leverage is the rule's; margin and loss round up."""
    last = dt.date.fromisoformat(rep['close_of'])
    cards, rejected = [], []
    for coin in [c for c in rep['top'] if c in rep['strong']]:
        cd = adv3.card(coin, rep['rows'][coin], True, budget, risk)
        side = 'LONG' if cd['side'] > 0 else 'SHORT'
        if not rep['marks_ok']:
            rejected.append((coin, side, 'нет текущей цены Binance'))
        elif cd['mode'] == 'none':
            rejected.append((coin, side, 'цена у стопа, входа нет'))
        elif cd['stop_pct'] > STOP_MAX:
            rejected.append((coin, side, f"стоп {adv3.pct(cd['stop_pct'])}% дальше {adv3.pct(STOP_MAX)}%"))
        elif len(cards) >= n:
            rejected.append((coin, side, f'сверх запрошенных {n}'))
        else:
            cards.append(cd)
    k = len(cards)
    rate = [cd['stop_pct'] / 100 + 2 * adv3.COST for cd in cards]
    items, rho = [], {}
    if k:
        ret = {cd['coin']: returns_of(cs[cd['coin']], last) for cd in cards}
        for a in range(k):
            for b in range(a + 1, k):
                rho[a, b] = rho[b, a] = correlation(ret[cards[a]['coin']], ret[cards[b]['coin']])
        kap = [[(1.0 if rho.get((a, b)) is None else rho[a, b]) * cards[a]['side'] * cards[b]['side'] for b in range(k)] for a in range(k)]
        crowd = [max(0.0, sum(kap[a][b] for b in range(k) if b != a) / (k - 1)) if k > 1 else 0.0 for a in range(k)]
        q = [min(abs(cd['z']), Z_CAP) for cd in cards]
        w = [q[a] / sum(q) * (1 - CROWD * crowd[a]) for a in range(k)]
        share = [x / sum(w) for x in w]
        pct_ = [min(adv3.RISK_MAX, k * risk * share[a]) for a in range(k)]
        if sum(pct_) > adv3.RISK_ALL:
            pct_ = [x * adv3.RISK_ALL / sum(pct_) for x in pct_]
        raw, capped = [], []
        for a, cd in enumerate(cards):
            r = pct_[a] / 100 * budget / rate[a]
            v = liq.get(cd['coin'])
            capped.append(bool(v) and r > LIQ_FRAC * v)
            raw.append(min(r, LIQ_FRAC * v) if v else r)
        scaled = sum(raw) > budget
        if scaled:
            raw = [x * budget / sum(raw) for x in raw]
        for a, cd in enumerate(cards):
            notional = math.floor(raw[a])
            if notional < MIN_NOTIONAL:
                rejected.append((cd['coin'], 'LONG' if cd['side'] > 0 else 'SHORT', f'позиция меньше {adv3.num(MIN_NOTIONAL, 2)} USDT'))
                continue
            items.append({'card': cd, 'notional': notional, 'leverage': cd['leverage'], 'margin': math.ceil(notional / cd['leverage']),
                          'loss': math.ceil(notional * rate[a] - 1e-9), 'loss_exact': notional * rate[a], 'risk_pct': pct_[a],
                          'share': share[a], 'crowd': crowd[a], 'capped': capped[a], 'rank': 0})
        for number, it in enumerate(items, 1):
            it['rank'] = number
    allocated = sum(it['notional'] for it in items)
    return {'budget': budget, 'n': n, 'risk': risk, 'items': items, 'rejected': rejected, 'k': k,
            'plain': [c for c in rep['top'] if c not in rep['strong']], 'allocated': allocated, 'free': budget - allocated,
            'margin': sum(it['margin'] for it in items), 'loss': sum(it['loss'] for it in items),
            'loss_exact': sum(it['loss_exact'] for it in items), 'avg_trade': budget * risk / 100, 'cap_trade': budget * adv3.RISK_MAX / 100,
            'cap_all': budget * adv3.RISK_ALL / 100}


def strong_shares():
    """The reach shares a STRONG trade's targets carry: TZ-38's STRONG shares where Gate S stands, else the rule's (adv3.PIT)."""
    return adv3.PIT['strong' if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else 'base']['mfe']


def item_lines(it, k, number=None):
    """One placed trade of an allocation: direction and quality, entry, stop, targets with their shares, capital, leverage, margin,
    loss at the stop, invalidation, and its confidence with the note that the sizes are the Architect's formula, unproven."""
    usdt, pct, price = adv3.usdt, adv3.pct, adv3.price
    cd, mfe = it['card'], strong_shares()
    lo, hi = cd['zone']
    ref = cd['entry']
    conf = adv3.RELIABILITY if cd['mode'] != 'none' else 0
    lines = [f"{f'{number}) ' if number else ''}{DOT[cd['side']]} <b>{cd['coin']} · {SIDE[cd['side']]}</b> · ★ STRONG",
             f"Качество: z {adv3.signed(cd['z'])} · сумма знаков {adv3.signed(cd['sum'], 0)} из ±4 · доля {pct(100 * it['share'], 0)}%"
             + (f" · корреляция с остальными {adv3.signed(it['crowd'])}" if k > 1 else ''),
             (f"Вход: <b>по рынку</b> ≈ {price(ref)}, зона {price(lo)}–{price(hi)}" if cd['mode'] == 'market'
              else f"Вход: <b>лимит {price(ref)}</b> — ждать отката, цена {price(cd['mark'])} ушла от зоны"),
             f"⛔ Стоп: <b>{price(cd['stop'])}</b> ({'−' if cd['side'] > 0 else '+'}{pct(cd['stop_pct'])}%)"]
    for n, t in zip((1, 2, 3), cd['targets']):
        lines.append(f"🎯 {price(t)} ({'+' if (t - ref) > 0 else ''}{pct(100 * (t - ref) / ref)}%) · дошли {pct(100 * mfe[n], 0)}%")
    lines += [f"Капитал: <b>{usdt(it['notional'])} USDT</b>{' (ограничен ликвидностью)' if it['capped'] else ''} · плечо {it['leverage']}× изол. · маржа {usdt(it['margin'])} USDT",
              f"Потеря на стопе: {usdt(it['loss'])} USDT с комиссиями",
              f"Инвалидация: {'цена ≤' if cd['side'] > 0 else 'цена ≥'} {price(cd['stop'])} или закрытие дня с суммой знаков "
              f"{'ниже +2' if cd['side'] > 0 else 'выше −2'}",
              f"Уверенность: <b>{conf}/5</b> — {adv3.LADDER[adv3.RELIABILITY][0]} · размеры — формула Архитектора, не доказана"]
    return lines


def plan_parts(rep, p):
    """The allocation view as one message: the budget and the limits in money, the result, each placed trade, the rejected and the
    weaker named, and the note that the sizes are unproven. The six ratings are the assessment's, «оценка» (TZ-39)."""
    last = dt.date.fromisoformat(rep['close_of'])
    usdt, pct, num = adv3.usdt, adv3.pct, adv3.num
    lines = ['💼 <b>ADV-3 · распределение капитала</b>', f"Закрытие дня {adv3.ddmm(rep['close_of'])} (UTC) · действует до 04:00 {last + 2 * adv3.DAY:%d.%m} по Батуми",
             f"Бюджет {num(p['budget'], 6)} USDT · до {p['n']} {adv3.plural(p['n'], 'сделки', 'сделок', 'сделок')} · только STRONG, стоп не дальше {pct(STOP_MAX)}% входа",
             f"Риск на стопе: в среднем {pct(p['risk'])}% бюджета на сделку ({usdt(p['avg_trade'])} USDT), у сильнейшей не больше {pct(adv3.RISK_MAX, 0)}% "
             f"({usdt(p['cap_trade'])} USDT), на все не больше {pct(adv3.RISK_ALL, 0)}% ({usdt(p['cap_all'])} USDT)"]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: вход и размер не определены, ничего не распределяю')
    lines += ['', '<b>Итог</b>']
    if p['items']:
        lines += [f"Подходящих сделок: {len(p['items'])} из {p['n']} запрошенных",
                  f"Размещено {usdt(p['allocated'])} USDT · маржа {usdt(p['margin'])} USDT",
                  f"Потеря на стопах {usdt(p['loss'])} USDT = {pct(100 * p['loss'] / p['budget'], 2)}% бюджета",
                  f"Свободно {usdt(p['free'])} USDT — больше без превышения лимитов риска не разместить: размер сделки = допустимая потеря "
                  f"на её стопе / расстояние до стопа"]
    else:
        lines += ['Подходящих сделок нет — ничего не размещаю', f"Размещено 0 USDT · свободно {usdt(p['budget'])} USDT"]
    for it in p['items']:
        lines += [''] + item_lines(it, p['k'], it['rank'])
    if p['rejected']:
        lines += ['', 'Отклонены: ' + '; '.join(f'{c} {s} — {why}' for c, s, why in p['rejected'])]
    if p['plain']:
        lines.append('В ТОП-3 без STRONG — не берутся: ' + ', '.join(p['plain']))
    if p['n'] > adv3.TOP_N:
        lines.append(f'STRONG бывает только в ТОП-3: больше {adv3.TOP_N} сделок не будет')
    lines += ['', 'Размеры — формула Архитектора (сила тренда, поправка на корреляцию, ликвидность, лимиты риска), не доказанная: '
                  'форвард-запись проверяет правило, а не этот отбор и не эти размеры.', FOOTER]
    return ['\n'.join(lines)]


# ---- the schedule: two slots a day, each sent once ----------------------------------------------------------------

def slot_key(slot):
    return slot[0], [k for k, _ in SLOTS].index(slot[1])


def slot_at(slot):
    return dt.datetime.combine(slot[0], dict(SLOTS)[slot[1]], tzinfo=dt.timezone.utc)


def slot_text(slot):
    return f'{slot[0].isoformat()} {slot[1]}'


def slot_parse(text):
    """The slot a check-done file names, 'YYYY-MM-DD signal' or 'YYYY-MM-DD fact'; None for anything else."""
    try:
        day, kind = text.split()
        return (dt.date.fromisoformat(day), kind) if kind in dict(SLOTS) else None
    except ValueError:
        return None


def latest_slot(now):
    """The last slot whose instant is at or before now."""
    for kind, at in reversed(SLOTS):
        if now >= dt.datetime.combine(now.date(), at, tzinfo=dt.timezone.utc):
            return now.date(), kind
    return now.date() - adv3.DAY, SLOTS[-1][0]


def due(now, done):
    """The slot to run now, or None: the latest slot unless done holds it or a later one; where the latest is a day's fact
    check and that day's signal check is not done, the signal check - 12:10 repeats 00:10 where it failed."""
    last = latest_slot(now)
    if done is not None and slot_key(done) >= slot_key(last):
        return None
    if last[1] == 'fact' and (done is None or slot_key(done) < slot_key((last[0], 'signal'))):
        return last[0], 'signal'
    return last


def done_after(slot, now):
    """What a check marks done: itself, or - a signal check that ends at or after its day's 12:10 - that day's fact check too."""
    if slot[1] == 'signal' and now >= slot_at((slot[0], 'fact')):
        return slot[0], 'fact'
    return slot


def next_at(now):
    """The first slot instant after now."""
    for day in (now.date(), now.date() + adv3.DAY):
        for kind, at in SLOTS:
            t = dt.datetime.combine(day, at, tzinfo=dt.timezone.utc)
            if t > now:
                return t


def hhmm(t):
    return (t + BATUMI).strftime('%H:%M')


# ---- the journal and the trades the cards offered -----------------------------------------------------------------

CARD_KEYS = ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'since', 'rank', 'of')


def journal_records():
    """Every record of journal.jsonl that parses as an object, in order, one at a time - a year's journal is never held whole;
    a line that does not parse is left out."""
    path = os.path.join(STATE, 'journal.jsonl')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if isinstance(rec, dict):
                    yield rec


def journal_scan():
    """(offers, alerted, the last check record) of the journal, in one pass that keeps those three alone."""
    offs, done, prev = {}, set(), None
    for rec in journal_records():
        offers((rec,), offs)
        done |= alerted((rec,))
        if rec.get('kind') == 'check':
            prev = rec
    return offs, done, prev


def append(rec):
    with open(os.path.join(STATE, 'journal.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + '\n')


def base_record(kind, rep, ids, cards=None, at=None):
    """A journal record: its instant, kind, rule, close, deposit, risk, TOP-3, STRONG, message ids, every coin's signal, and the
    cards the message offered (the report's, unless cards names others), each with its confidence."""
    cards = rep['cards'] if cards is None else cards
    conf = adv3.trust(dict(rep, cards=cards))['cards']
    return {'utc': (at or dt.datetime.now(dt.timezone.utc)).isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'],
            'close_of': rep['close_of'], 'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'],
            'strong': rep['strong'], 'message_ids': ids, 'signals': {k: v.get('signal') for k, v in rep['rows'].items()},
            'cards': [dict({k: cd.get(k) for k in CARD_KEYS}, confidence=conf.get(cd['coin'])) for cd in cards]}


def offers(records, out=None):
    """The trades the bot's cards offered (TZ-39): every card a journal record carries whose entry was offered - at market or
    as a limit - keyed by its coin, side and the close it was made from, the first record's kept; of an allocation record only
    the coins its plan placed (TZ-37's records carry the report's cards beside the plan). {key: offer}, in the records' order,
    added to out where it is given."""
    out = {} if out is None else out
    for rec in records:
        close_of = rec.get('close_of')
        placed = None
        if rec.get('kind') == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {i.get('coin') for i in rec['alloc'].get('items') or [] if isinstance(i, dict)}
        for cd in rec.get('cards') or []:
            try:
                if cd.get('mode') not in ('market', 'limit') or (placed is not None and cd['coin'] not in placed):
                    continue
                side, C, U = int(cd['side']), float(cd['close']), float(cd['U'])
                dt.date.fromisoformat(close_of)
                key = (cd['coin'], side, close_of)
                if cd['coin'] in adv3.COINS and side in (1, -1) and U > 0 and key not in out:
                    out[key] = {'coin': cd['coin'], 'side': side, 'close_of': close_of, 'close': C, 'U': U, 'stop': C - side * U,
                                'mode': cd['mode'], 'first': rec.get('utc')}
            except (AttributeError, KeyError, TypeError, ValueError):
                continue
    return out


def alerted(records):
    """{(coin, side, close_of, kind)} of every alert a check record holds: each alert is sent once."""
    out = set()
    for rec in records:
        if rec.get('kind') != 'check':
            continue
        for a in rec.get('alerts') or []:
            try:
                out.add((a['coin'], int(a['side']), a.get('close_of'), a['kind']))
            except (KeyError, TypeError, ValueError):
                pass
    return out


def follow(offs, cs, funds, last, forming=None, done=frozenset()):
    """Each offered trade held by the rule's own functions from the day after its close to the close of last - adv3.open_at at the
    card's close and unit, adv3.hold for its stop inside a day, adv3.signal for its end at a close and adv3.close_at for that exit -
    then, where forming holds the coin's candle of the day after last, whether that candle has reached the stop. An offer whose
    stop or signal alert was sent is closed and not held again. [{key, coin, side, close_of, close, U, stop, state, day, price, R}],
    state 'open', 'stop', 'signal', 'touch' (the forming candle), 'closed' or 'unknown' (no candle of its close)."""
    out = []
    for key, off in offs.items():
        coin, side, close_of = key
        f = dict(off, key=key, state='open', day=None, price=None, R=None)
        if (coin, side, close_of, 'stop') in done or (coin, side, close_of, 'signal') in done:
            out.append(dict(f, state='closed'))
            continue
        c = cs.get(coin) or {}
        D = dt.date.fromisoformat(close_of)
        if D not in c or D > last:
            out.append(dict(f, state='unknown'))
            continue
        days = sorted(d for d in c if d <= last)
        closes = [c[d][3] for d in days]
        pos = adv3.open_at(side, off['close'], off['U'], D)
        fund = funds.get(coin) or (lambda d: 3 * adv3.BASE_F)
        for i in range(days.index(D) + 1, len(days)):
            d = days[i]
            _, stopped = adv3.hold(pos, c[d], closes[i - 1], fund(d), d)
            if stopped:
                f.update(state='stop', day=str(d), price=pos['X'])
                break
            if adv3.signal(days, closes, i) != side:
                adv3.close_at(pos, closes[i], d)
                f.update(state='signal', day=str(d), price=closes[i])
                break
        f['R'] = pos['R']
        if f['state'] == 'open' and forming and forming.get(coin):
            _o, h, l, _c = forming[coin]
            if (l <= pos['S']) if side > 0 else (h >= pos['S']):
                f.update(state='touch', day=str(last + adv3.DAY), price=l if side > 0 else h)
        out.append(f)
    return out


def forming_candles(coins, day):
    """{coin: (open, high, low, last)} of each coin's daily candle that opened at day's 00:00 UTC, from fapi.binance.com - the
    candle the fact check reads the stops in, never a signal; a coin whose candle fails or is not served is left out."""
    out = {}
    for coin in coins:
        try:
            for r in adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval='1d', limit=2):
                if adv3.ms_day(r[0]) == day:
                    out[coin] = (float(r[1]), float(r[2]), float(r[3]), float(r[4]))
        except Exception as e:
            log('forming candle failed:', coin, repr(e)[:200])
    return out


def candidates(p):
    """The STRONG coins an allocation places, as (coin, side): those that pass its limits."""
    return [(it['card']['coin'], it['card']['side']) for it in p['items']]


def alerts_of(fol, passing, prev_passing, done, rep, p):
    """The check's alerts, each with the price it fired at against the close it rests on: a followed trade stopped - by a closed
    candle or the forming one - or ended by its signal at a close, each once; and every STRONG candidate the allocation places
    now that it did not place at the check before."""
    out = []
    for f in fol:
        kind = {'stop': 'stop', 'touch': 'stop', 'signal': 'signal'}.get(f['state'])
        if kind and (f['coin'], f['side'], f['close_of'], kind) not in done:
            out.append({'kind': kind, 'coin': f['coin'], 'side': f['side'], 'close_of': f['close_of'], 'close': f['close'],
                        'level': f['stop'] if kind == 'stop' else f['price'], 'price': f['price'], 'day': f['day'],
                        'touch': f['state'] == 'touch', 'mark': (rep['rows'].get(f['coin']) or {}).get('mark')})
    placed = {(it['card']['coin'], it['card']['side']): it['card'] for it in p['items']}
    for coin, side in passing:
        if (coin, side) not in prev_passing:
            cd = placed[coin, side]
            out.append({'kind': 'candidate', 'coin': coin, 'side': side, 'close_of': rep['close_of'], 'close': cd['close'],
                        'level': cd['stop'], 'price': cd['entry'], 'day': None, 'touch': False, 'mark': cd['mark']})
    return out


def weakened(fol, rep, cs):
    """The trades the cards offered, open by the rule, whose coin's sum of signs fell from ±4 at the close before to ±2 at this
    close with the signal kept - shown as information and never as an exit (CANON PART VII): [(coin, side)], the coins' order.
    The close before's sum is adv3.strength's."""
    last = dt.date.fromisoformat(rep['close_of'])
    out = []
    for coin, side in sorted({(f['coin'], f['side']) for f in fol if f['state'] == 'open'}, key=lambda x: (adv3.COINS.index(x[0]), -x[1])):
        row = rep['rows'].get(coin) or {}
        c = cs.get(coin) or {}
        days = sorted(d for d in c if d <= last)
        if row.get('signal') != side or row.get('sum') != 2 * side or len(days) < 2 or days[-1] != last:
            continue
        st = adv3.strength(days, [c[d][3] for d in days], len(days) - 2)
        if st and st[1] == 4 * side:
            out.append((coin, side))
    return out


def zones_left(rep, offs, fol):
    """The entries this close's cards offered at market that the price of the moment has left - each card made again from the
    report's row at the current mark: a limit where the price ran past the zone, none where it stands near the stop. Only
    trades still open by the rule are read."""
    open_ = {f['key'] for f in fol if f['state'] == 'open'}
    out = []
    for key, off in offs.items():
        row = rep['rows'].get(off['coin']) or {}
        if (off['close_of'] != rep['close_of'] or off['mode'] != 'market' or key not in open_ or not rep['marks_ok']
                or row.get('signal') != off['side']):
            continue
        cd = adv3.card(off['coin'], row, False, rep['deposit'], rep['risk_pct'])
        if cd['mode'] != 'market':
            out.append({'coin': off['coin'], 'side': off['side'], 'mode': cd['mode'], 'mark': cd['mark'], 'zone': list(cd['zone']),
                        'entry': cd['entry'], 'stop': cd['stop']})
    return out


# ---- a check's message --------------------------------------------------------------------------------------------

def event_lines(al, p, fact=False):
    """The alerts as lines: stops, then signal exits by coin, side and close, then STRONG candidates - at the fact check each
    with its entry plan, at the signal check pointing to the candidates below."""
    if not al:
        return []
    price, ddmm = adv3.price, adv3.ddmm
    lines = ['🔔 <b>События</b>']
    for a in al:
        if a['kind'] == 'stop':
            when = (f"сегодня ({'минимум' if a['side'] > 0 else 'максимум'} дня {price(a['price'])})" if a['touch']
                    else ddmm(a['day']))
            lines.append(f"⛔ {a['coin']} {SIDE[a['side']]}, карточка {ddmm(a['close_of'])}: стоп {price(a['level'])} задет "
                         f"{when} — по правилу сделка закрыта по стопу")
    exits = {}
    for a in al:
        if a['kind'] == 'signal':
            exits.setdefault((a['coin'], a['side'], a['day']), []).append(a)
    for (coin, side, day), group in exits.items():
        cards = ', '.join(ddmm(a['close_of']) for a in group)
        mark = group[0]['mark']
        lines.append(f"🚪 {coin} {SIDE[side]}, {'карточка' if len(group) == 1 else 'карточки'} {cards}: сигнал закончился на "
                     f"закрытии {ddmm(day)} — по правилу выход по закрытию {price(group[0]['level'])}"
                     + (f"; сейчас {price(mark)}" if mark else ''))
    placed = {(it['card']['coin'], it['card']['side']): it for it in p['items']}
    for a in al:
        if a['kind'] == 'candidate':
            if fact:
                lines += [f"🆕 STRONG {a['coin']} {SIDE[a['side']]} теперь проходит лимиты распределения ({adv3.num(p['budget'], 6)} "
                          f"USDT, риск {adv3.pct(p['risk'])}%):"] + item_lines(placed[a['coin'], a['side']], p['k'])
            else:
                lines.append(f"🆕 STRONG: {a['coin']} {SIDE[a['side']]} проходит лимиты распределения — план ниже")
    return lines


def candidate_lines(rep, p, new):
    """The close's STRONG candidates at the default budget: each placed one with its capital, leverage, margin and loss at the
    stop, each other named with its reason; 🆕 marks a candidate the check before did not place."""
    strong = [c for c in rep['top'] if c in rep['strong']]
    if not strong:
        return ['<b>STRONG-кандидатов нет</b>']
    usdt = adv3.usdt
    lines = [f"<b>STRONG-кандидаты</b> — распределение {adv3.num(p['budget'], 6)} USDT, риск {adv3.pct(p['risk'])}%, стоп не "
             f"дальше {adv3.pct(STOP_MAX, 0)}%"]
    placed = {it['card']['coin']: it for it in p['items']}
    why = {c: r for c, _s, r in p['rejected']}
    for coin in strong:
        side = rep['rows'][coin]['signal']
        if coin in placed:
            it = placed[coin]
            lines.append(f"{'🆕 ' if (coin, side) in new else ''}{coin} {SIDE[side]} — проходит: капитал {usdt(it['notional'])} USDT · "
                         f"плечо {it['leverage']}× изол. · маржа {usdt(it['margin'])} USDT · потеря на стопе {usdt(it['loss'])} USDT")
        else:
            lines.append(f"{coin} {SIDE[side]} — не проходит: {why.get(coin, 'вне распределения')}")
    return lines


def followed_lines(fol):
    """The trades the cards offered that are open by the rule, by coin and side: the cards' closes and their stops."""
    groups = {}
    for f in fol:
        if f['state'] == 'open':
            groups.setdefault((f['coin'], f['side']), []).append(f)
    if not groups:
        return ['<b>Сделки по карточкам бота:</b> открытых по правилу нет']
    lines = ['<b>Сделки по карточкам бота</b> — бот не видит ваш счёт; открыты по правилу:']
    for (coin, side), fs in sorted(groups.items(), key=lambda kv: (adv3.COINS.index(kv[0][0]), -kv[0][1])):
        fs = sorted(fs, key=lambda f: f['close_of'])
        one = len(fs) == 1
        lines.append(f"{DOT[side]} {coin} {SIDE[side]} — {'карточка' if one else 'карточки'} "
                     f"{', '.join(adv3.ddmm(f['close_of']) for f in fs)} · {'стоп' if one else 'стопы'} "
                     f"{' · '.join(adv3.price(f['stop']) for f in fs)}")
    return lines


def zone_lines(zones, rep):
    """The entries whose zone the price has left, each with what to do instead."""
    if not zones:
        return []
    price = adv3.price
    lines = [f"<b>Зоны входа карточек закрытия {adv3.ddmm(rep['close_of'])}</b>"]
    for z in zones:
        lo, hi = z['zone']
        if z['mode'] == 'limit':
            lines.append(f"{z['coin']} {SIDE[z['side']]} — цена {price(z['mark'])} ушла из зоны {price(lo)}–{price(hi)}: "
                         f"лимит {price(z['entry'])}, не догонять")
        else:
            lines.append(f"{z['coin']} {SIDE[z['side']]} — цена {price(z['mark'])} у стопа {price(z['stop'])}: не входить")
    return lines


def weak_lines(weak):
    """The weakened trades, one line: information, not an exit."""
    if not weak:
        return []
    return ['ℹ️ Ослабление: ' + ', '.join(f'{coin} {SIDE[side]}' for coin, side in weak) + ' — сумма знаков упала с ±4 до ±2, '
            'сигнал держится; по правилу это не выход']


def quiet_line(slot, rep, fol, now):
    """The one line of a check that finds nothing, sent without a notification so that silence is never read as the bot down."""
    n = sum(f['state'] == 'open' for f in fol)
    head = f"✓ {hhmm(now)} по Батуми · закрытие {adv3.ddmm(rep['close_of'])}"
    if slot[1] == 'signal':
        return (f"{head}: без изменений — ТОП-3 тот же ({', '.join(rep['top']) or 'пуст'}), сигналы не менялись; сделок по "
                f"карточкам открыто {n}, стопы не задеты; новых STRONG нет · карточки дня — «сигнал»")
    return (f"{head}: событий нет — стопы {n} {adv3.plural(n, 'сделки', 'сделок', 'сделок')} по карточкам не задеты, зоны входа "
            f"на месте, новых STRONG нет · следующая проверка {hhmm(next_at(now))}")


def compose(slot, rep, fol, al, p, zones, prev, now, weak=()):
    """(text, quiet, one line, cards offered) of a check. It notifies only for an alert. The signal check is the close's
    message - events, changes, cards, STRONG candidates, the trades the cards offered and those weakened - or one line where it
    finds nothing: no alert, no weakening, no change of signal among the coins, the TOP-3 with its sides and STRONG as at the
    check before. The fact check is its events and the zones left, or one line where it finds neither."""
    loud = bool(al)
    new = {(a['coin'], a['side']) for a in al if a['kind'] == 'candidate'}
    if slot[1] == 'signal':
        same = (prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                and all((prev.get('signals') or {}).get(c) == rep['rows'][c].get('signal') for c in rep['top']))
        if not loud and not weak and same and not any(adv3.changes(rep)):
            return quiet_line(slot, rep, fol, now), True, True, []
        tail = candidate_lines(rep, p, new) + [''] + followed_lines(fol) + weak_lines(weak)
        return adv3.message(rep, adv3.FACTS, head=event_lines(al, p), tail=tail), not loud, False, rep['cards']
    if not loud and not zones:
        return quiet_line(slot, rep, fol, now), True, True, []
    lines = [f"🕓 <b>ADV-3 · проверка {hhmm(now)} по Батуми</b> · закрытие {adv3.ddmm(rep['close_of'])} (UTC)"]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: зоны входа не проверены')
    for block in (event_lines(al, p, fact=True), zone_lines(zones, rep)):
        if block:
            lines += [''] + block
    n = sum(f['state'] == 'open' for f in fol)
    lines += ['', f"Сделок по карточкам открыто: {n} · следующая проверка {hhmm(next_at(now))} по Батуми", FOOTER]
    offered = [it['card'] for it in p['items'] if (it['card']['coin'], it['card']['side']) in new]
    return '\n'.join(lines), not loud, False, offered


def check_record(slot, rep, fol, al, p, zones, ids, quiet, one_line, offered, at, weak=()):
    """The check's journal record (CANON PART VII's internal log; it measures and tunes nothing): every coin's signal, sum of
    signs, strength, rank, unit, close and mark; the trades the cards offered that this check read, with their state; the
    alerts with the price each fired at against the close it rests on; the trades weakened; the STRONG coins the allocation
    placed at the default budget; the zones left; the six ratings; and the cards the message offered."""
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    rec = base_record('check', rep, ids, offered, at)
    rec.update(slot=slot_text(slot), quiet=quiet, one_line=one_line,
               state={coin: {'signal': r.get('signal'), 'sum': r.get('sum'), 'z': r.get('z'), 'rank': rank.get(coin), 'U': r.get('U'),
                             'close': r.get('close'), 'mark': r.get('mark')} for coin, r in rep['rows'].items()},
               followed=[{k: f.get(k) for k in ('coin', 'side', 'close_of', 'close', 'U', 'stop', 'state', 'day', 'price', 'R')}
                         for f in fol if f['state'] != 'closed'],
               alerts=al, weakened=[[c, s] for c, s in weak], passing=[[c, s] for c, s in candidates(p)], zones_left=zones,
               trust=rep['trust'],
               alloc={'budget': p['budget'], 'n': p['n'], 'risk': p['risk'], 'allocated': p['allocated'], 'free': p['free'],
                      'loss': p['loss'], 'items': [{'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'],
                                                    'leverage': it['leverage'], 'margin': it['margin'], 'loss': it['loss']} for it in p['items']],
                      'rejected': p['rejected']})
    return rec


def check(tg, data, slot, now):
    """One scheduled check (TZ-39): the report at the default deposit and risk, the trades the cards offered held by the rule, the
    candle forming since the close at the fact check, the allocation at the default budget, the alerts, the weakened trades at
    the signal check, the message - sent quiet unless it holds an alert - and its record, returned for the journal once the
    message is sent."""
    rep = top_n(live_report(data, adv3.DEPOSIT, adv3.RISK), adv3.TOP_N)
    last = dt.date.fromisoformat(rep['close_of'])
    offs, done, prev = journal_scan()
    forming = {}
    if slot[1] == 'fact':
        held = sorted({k[0] for k in offs if (*k, 'stop') not in done and (*k, 'signal') not in done})
        forming = forming_candles(held, last + adv3.DAY)
    fol = follow(offs, data.cs, data.funds, last, forming, done)
    p = plan(rep, data.cs, adv3.DEPOSIT, adv3.TOP_N, adv3.RISK, {c: liquidity(c, rep['made_at_ms']) for c in rep['strong']})
    prev_passing = {(c, s) for c, s in (prev or {}).get('passing') or []}
    al = alerts_of(fol, candidates(p), prev_passing, done, rep, p)
    zones = zones_left(rep, offs, fol) if slot[1] == 'fact' else []
    weak = weakened(fol, rep, data.cs) if slot[1] == 'signal' else []
    text, quiet, one_line, offered = compose(slot, rep, fol, al, p, zones, prev, now, weak)
    ids = tg.send(text, quiet=quiet)
    return check_record(slot, rep, fol, al, p, zones, ids, quiet, one_line, offered, now, weak)


def serve():
    try:
        token, chat = read(TOKEN_FILE), int(read(CHAT_FILE))
    except (OSError, ValueError) as e:
        log('no token or chat id:', repr(e))
        sys.exit(3)
    SECRETS.append(token)
    if not malloc_tune():
        log('glibc refused its two settings')
        sys.exit(4)
    os.makedirs(STATE, exist_ok=True)
    tg, data = Telegram(token, chat), Data()
    off_path, done_path = os.path.join(STATE, 'offset'), os.path.join(STATE, 'check-done')
    offset = int(read(off_path)) if os.path.exists(off_path) else 0
    done = slot_parse(read(done_path)) if os.path.exists(done_path) else None
    retry_at = 0.0
    log('serving the pinned chat: pid', os.getpid(), 'offset', offset, 'check-done', slot_text(done) if done else '-')
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        slot = due(now, done)
        if slot and time.time() >= retry_at:
            try:
                rec = check(tg, data, slot, now)
            except Exception:
                retry_at = time.time() + RETRY
                log('check failed:', slot_text(slot), '- retry in', RETRY, 's\n' + traceback.format_exc())
            else:
                done = done_after(slot, dt.datetime.now(dt.timezone.utc))   # sent: never again, whatever its record does
                try:
                    put(done_path, slot_text(done))
                    append(rec)
                except Exception:
                    log('check record failed\n' + traceback.format_exc())
                log('check sent:', slot_text(slot), 'for the close of', rec['close_of'], '| alerts', len(rec['alerts']),
                    '| quiet' if rec['quiet'] else '| loud', '| one line' if rec['one_line'] else '| full')
        now = dt.datetime.now(dt.timezone.utc)
        if due(now, done):
            wait = min(POLL, max(1, int(retry_at - time.time())))
        else:
            wait = min(POLL, max(1, int((next_at(now) - now).total_seconds())))
        try:
            updates = tg.call('getUpdates', http_timeout=wait + 20, offset=offset, timeout=wait,
                              allowed_updates=['message'])
        except Exception:
            log('getUpdates failed\n' + traceback.format_exc())
            time.sleep(15)
            continue
        for u in updates:
            offset = u['update_id'] + 1
            msg = u.get('message') or {}
            if (msg.get('chat') or {}).get('id') != chat:
                continue
            handle(tg, data, msg.get('text') or '')
        if updates:
            put(off_path, str(offset))


def handle(tg, data, text):
    cmd = route(text)
    try:
        if cmd:
            kind, budget, n, risk = cmd
            if kind == 'assess':
                rep = top_n(live_report(data, adv3.DEPOSIT, adv3.RISK), adv3.TOP_N)
                rec = base_record('assess', rep, tg.send(adv3.assessment(rep, adv3.FACTS)), [])
                rec['trust'] = rep['trust']
            elif kind == 'alloc':
                rep = top_n(live_report(data, budget, risk), adv3.TOP_N)
                p = plan(rep, data.cs, budget, n, risk, {c: liquidity(c, rep['made_at_ms']) for c in rep['strong']})
                ids = [i for part in plan_parts(rep, p) for i in tg.send(part)]
                rec = base_record('alloc', rep, ids, [it['card'] for it in p['items']])
                rec['alloc'] = {'budget': budget, 'n': n, 'risk': risk, 'allocated': p['allocated'], 'free': p['free'], 'loss': p['loss'],
                                'items': [{'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'],
                                           'leverage': it['leverage'], 'margin': it['margin'], 'loss': it['loss']} for it in p['items']],
                                'rejected': p['rejected']}
            else:
                rep, msg = make(data, adv3.DEPOSIT, risk, n)
                rec = base_record('request', rep, tg.send(msg))
                rec['n'] = n
            try:
                append(rec)
            except Exception:
                log('request record failed\n' + traceback.format_exc())
            log('request answered for the close of', rep['close_of'], '| kind', kind)
        else:
            tg.send(HELP)
            log('help sent')
    except Exception:
        log('request failed\n' + traceback.format_exc())
        try:
            tg.send('Binance или Telegram не ответили — повторите «сигнал» через минуту.')
        except Exception:
            log('apology failed\n' + traceback.format_exc())


def probe():
    """P-START: one live request per endpoint through the process's own request functions, each asserted served
    and parsed - the klines endpoint read for the closed candles and for the candle forming since 00:00 UTC. Prints counts,
    dates and the bot's name; never the token or a chat id."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    c = adv3.fapi_candles('BTCUSDT', now_ms)
    assert c and max(c) >= today - 2 * adv3.DAY and all(len(v) == 4 and v[3] > 0 for v in c.values()), 'klines'
    f = forming_candles(['BTC'], today).get('BTC')
    assert f and len(f) == 4 and f[1] >= max(f[0], f[3]) and 0 < f[2] <= min(f[0], f[3]), 'the forming candle'
    print('P-KLINES served:', len(c), 'closed daily candles of BTCUSDT, the last', max(c), '- and the candle forming since', today)
    f = adv3.fapi_funding('BTCUSDT', adv3.FORWARD_FROM - adv3.DAY)
    assert f and all(isinstance(x, float) for x in f.values()), 'fundingRate'
    print('P-FUNDING served:', len(f), 'settlement days of BTCUSDT since', adv3.FORWARD_FROM - adv3.DAY)
    marks = adv3.fapi_marks()
    missing = [k for k in adv3.COINS if not (marks.get(k + 'USDT') or (0,))[0] > 0]
    assert not missing, f'premiumIndex lacks {missing}'
    print('P-MARKS served:', len(marks), 'perpetuals, all', len(adv3.COINS), 'coins among them with a mark price')
    iv = adv3.fapi_intervals()
    assert all(isinstance(h, int) and h > 0 for h in iv.values()), 'fundingInfo'
    print('P-INTERVALS served:', len(iv), 'perpetuals with an adjusted funding interval,',
          sum(k + 'USDT' in iv for k in adv3.COINS), 'of the coins among them')
    me = Telegram(read(TOKEN_FILE)).call('getMe')
    assert me.get('is_bot') is True and me.get('username'), 'getMe'
    print('P-TELEGRAM served: bot @' + me['username'])
    print('READING P-START: served - 5 of 5 endpoints')


def find_chat(wait_s=1800):
    """The one private chat that sent /start to the bot, pinned to CHAT_FILE. Waits up to wait_s for a /start;
    exit 1 where two chats sent one, or none did in time. Prints counts only, never a chat id."""
    tg = Telegram(read(TOKEN_FILE))
    deadline, said, offset = time.time() + wait_s, False, {}
    while True:
        ups = tg.call('getUpdates', http_timeout=80, timeout=50, allowed_updates=['message'], **offset)
        chats = {(u['message']['chat']['id'], u['message']['chat'].get('type'))
                 for u in ups if 'message' in u and (u['message'].get('text') or '').startswith('/start')}
        private = sorted(cid for cid, t in chats if t == 'private')
        if len(private) == 1:
            break                       # the /start stays unconfirmed: the service's first poll answers it
        if len(private) > 1 or time.time() >= deadline:
            print('updates', len(ups), '| private chats that sent /start:', len(private))
            sys.exit(1)
        if ups:                         # none a /start: confirmed, so the next poll waits for a new update
            offset = {'offset': ups[-1]['update_id'] + 1}
        if not said:
            print('no /start among', len(ups), 'pending updates; waiting up to', wait_s, 's for the Boss\'s /start',
                  flush=True)
            said = True
    old = os.umask(0o077)
    try:
        put(CHAT_FILE, f'{private[0]}\n')
    finally:
        os.umask(old)
    print('updates', len(ups), '| private chats that sent /start: 1 | chat pinned to', CHAT_FILE)


def hello():
    ids = Telegram(read(TOKEN_FILE), int(read(CHAT_FILE))).send(
        'ADV-3 подключён к этому чату. Напишите «сигнал» — или ждите проверок в 04:10 и 16:10 по Батуми.')
    assert ids and all(isinstance(x, int) for x in ids), ids
    print('G-HELLO sent: message ids', ids)


def selftest():
    """The bot's own checks, offline: the commands, the schedule, the trades the cards offered held by the rule, the alerts,
    the scanner, a check's message and record and three checks end to end, the TOP-N list, the allocation (golden cases computed
    by hand, the limits over random scenarios), the replies, the chunks, the files, the log, the HTML fallback and the quiet
    flag, glibc. Every expectation is computed here by hand or by a formula of its own, never by the code under test."""
    import contextlib, io, random, shutil, tempfile
    done = []

    def chk(name, ok):
        done.append(name)
        assert ok, name

    R, RM, T3 = adv3.RISK, adv3.RISK_MAX, adv3.TOP_N
    A_ = ('assess', None, None, None)
    for text, want in (('сигнал', ('signal', None, T3, R)), ('Сигнал 0,5%', ('signal', None, T3, 0.5)),
                       ('signal 0.3', ('signal', None, T3, 0.3)), ('сигналы', ('signal', None, T3, R)),
                       ('сигнал топ 3', ('signal', None, 3, R)), ('сигнал топ 5', ('signal', None, 5, R)),
                       ('сигнал топ 7', ('signal', None, 7, R)), ('топ 7', ('signal', None, 7, R)), ('сигнал топ 10', ('signal', None, 7, R)),
                       ('сигнал топ 0', ('signal', None, 1, R)), ('сигнал топ-5 1', ('signal', None, 5, 1.0)), ('сигнал 99', ('signal', None, T3, RM)),
                       ('сигнал 10000 топ 3', ('alloc', 10000.0, 3, R)), ('сигнал 15000 топ 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 10000', ('alloc', 10000.0, 3, R)), ('Сигнал 15 000 топ 5 1', ('alloc', 15000.0, 5, 1.0)),
                       ('/signal@adv3_bot 5000 top 2', ('alloc', 5000.0, 2, R)), ('signal 5000 top2', ('alloc', 5000.0, 2, R)),
                       ('топ 3 на 10000', ('alloc', 10000.0, 3, R)), ('топ3 10000', ('alloc', 10000.0, 3, R)),
                       ('сигнал 10к топ 3', ('alloc', 10000.0, 3, R)), ('signal 15k top 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 1,5 тыс', ('alloc', 1500.0, 3, R)), ('сигнал 10 коинов', ('signal', None, T3, RM)),
                       ('сигнал 10000 топ-3', ('alloc', 10000.0, 3, R)), ('сигнал 10000 топ 3 0,3', ('alloc', 10000.0, 3, 0.3)),
                       ('стратегия 7000 топ 2', ('alloc', 7000.0, 2, R)), ('сигнал 20000 топ 3 3', ('alloc', 20000.0, 3, RM)),
                       ('сигнал 12000 0.01', ('alloc', 12000.0, 3, 0.05)), ('сигнал 10000 usdt топ 1', ('alloc', 10000.0, 1, R)),
                       ('сигнал 10000 топ 0', ('alloc', 10000.0, 1, R)), ('сигнал 10000 топ 50', ('alloc', 10000.0, 7, R)),
                       ('signal 200000000', ('alloc', 10_000_000.0, 3, R)), ('сигнал 100 топ 3', ('alloc', 100.0, 3, R)),
                       ('оценка', A_), ('Оценка', A_), ('/оценка', A_), ('оценки доверия', A_), ('rating', A_),
                       ('привет', None), ('сигнализация', None), ('', None), ('12345', None), ('все', None), ('eth', None),
                       ('оценочный', None)):
        chk(f'route {text!r}', route(text) == want)
    chk('HELP names the commands, the list to 7, the 14 % filter, the checks at 04:10 and 16:10 and the quiet rule, in one part',
        all(k in HELP for k in ('«сигнал»', '«сигнал топ 7»', '«сигнал 10000 топ 3»', '«оценка»', '14%', 'STRONG', 'не больше 1%',
                                '04:10', '16:10', 'одной строкой')) and len(chunks(HELP)) == 1)
    long_text = '\n'.join(f'line {i} ' + 'x' * 90 for i in range(200))
    parts = chunks(long_text)
    chk('chunks: 5 parts under the limit, joined back whole',
        len(parts) == 5 and all(len(p) <= LIMIT for p in parts) and '\n'.join(parts) == long_text)
    tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'.selftest-{os.getpid()}')
    os.mkdir(tmp)
    try:
        f = os.path.join(tmp, 'offset')
        put(f, '41')
        put(f, '42')
        chk('put replaces in one rename', read(f) == '42' and sorted(os.listdir(tmp)) == ['offset'])
    finally:
        for name in os.listdir(tmp):
            os.remove(os.path.join(tmp, name))
        os.rmdir(tmp)

    class Fake(Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.calls = []

        def call(self, method, http_timeout=30, **params):
            self.calls.append(params)
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params.get('text', ''):
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    chk('HTML sent as HTML, with a notification', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML'
        and 'disable_notification' not in fk.calls[0])
    chk('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
        and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000]), quiet=True)
    fk.send('<b>bad quiet</b>', quiet=True)
    chk('quiet: every part, the plain fallback among them, without a notification',
        len(fk.calls) == n0 + 4 and all(c.get('disable_notification') is True for c in fk.calls[n0:]))
    SECRETS.append('123456:SECRET')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        log('url https://api.telegram.org/bot123456:SECRET/getMe failed')
    SECRETS.remove('123456:SECRET')
    chk('the token never reaches the log', 'SECRET' not in buf.getvalue() and '<token>' in buf.getvalue())

    # ---- the schedule ---------------------------------------------------------------------------------------------
    X = dt.date(2026, 11, 5)
    at = lambda d, h, m, s=0: dt.datetime.combine(d, dt.time(h, m, s), tzinfo=dt.timezone.utc)
    sig, fac = (X, 'signal'), (X, 'fact')
    chk('latest_slot: 00:09:59 is the day before\'s fact, 00:10 the signal, 12:09:59 still the signal, 12:10 the fact',
        [latest_slot(at(X, 0, 9, 59)), latest_slot(at(X, 0, 10)), latest_slot(at(X, 12, 9, 59)), latest_slot(at(X, 12, 10)),
         latest_slot(at(X, 23, 59, 59))] == [(X - adv3.DAY, 'fact'), sig, sig, fac, fac])
    chk('due: nothing done runs the day\'s signal, at 00:10 and at 14:00 alike (12:10 repeats 00:10)',
        due(at(X, 0, 10), None) == sig and due(at(X, 14, 0), None) == sig)
    chk('due: the signal done, nothing before 12:10, the fact at 12:10; the fact done, nothing until 00:10',
        due(at(X, 11, 0), sig) is None and due(at(X, 12, 10), sig) == fac and due(at(X, 23, 0), fac) is None
        and due(at(X + adv3.DAY, 0, 10), fac) == (X + adv3.DAY, 'signal'))
    chk('due: the day\'s signal failed until 12:10 - the 12:10 slot runs the signal', due(at(X, 12, 10), (X - adv3.DAY, 'fact')) == sig)
    chk('done_after: a signal ended before 12:10 is itself; at or after 12:10 it covers the fact; a fact is itself',
        done_after(sig, at(X, 0, 10, 30)) == sig and done_after(sig, at(X, 12, 10)) == fac and done_after(fac, at(X, 13, 0)) == fac)
    chk('next_at: 00:10, then 12:10, then 00:10 of the next day',
        [next_at(at(X, 0, 9)), next_at(at(X, 0, 10)), next_at(at(X, 12, 10)), next_at(at(X, 23, 0))]
        == [at(X, 0, 10), at(X, 12, 10), at(X + adv3.DAY, 0, 10), at(X + adv3.DAY, 0, 10)])
    chk('slot_text and slot_parse: a round trip, and nothing else parsed', slot_parse(slot_text(fac)) == fac
        and slot_parse('2026-11-05 daily') is None and slot_parse('garbage') is None and slot_parse('') is None)
    runs, d_, t = [], None, at(X, 13, 0)
    while t < at(X + 3 * adv3.DAY, 23, 59):
        s = due(t, d_)
        fail = s == (X + adv3.DAY, 'signal') and t < at(X + adv3.DAY, 12, 30)
        if s and not fail:
            runs.append((slot_text(s), t.strftime('%d %H:%M')))
            d_ = done_after(s, t)
        t += dt.timedelta(minutes=1)
    chk('three days minute by minute from a first start at 13:00: each slot once, a signal failing until 12:30 covering its fact',
        runs == [('2026-11-05 signal', '05 13:00'), ('2026-11-06 signal', '06 12:30'), ('2026-11-07 signal', '07 00:10'),
                 ('2026-11-07 fact', '07 12:10'), ('2026-11-08 signal', '08 00:10'), ('2026-11-08 fact', '08 12:10')])

    # ---- the trades the cards offered, held by the rule ---------------------------------------------------------------
    d0 = dt.date(2026, 1, 1)

    def candles(closes, width=0.01, start=d0, opens=None):
        """Candles from closes: high and low width around each close, the open the close before unless opens names it."""
        out, prev = {}, closes[0]
        for i, cl in enumerate(closes):
            o = (opens or {}).get(i, prev)
            out[start + i * adv3.DAY] = (o, max(o, cl) * (1 + width), min(o, cl) * (1 - width), cl)
            prev = cl
        return out

    def sum_signs(closes, i):
        """The sum of the four signs, written here: the close against those 14, 28, 56 and 112 days before."""
        return sum((closes[i] > closes[i - L]) - (closes[i] < closes[i - L]) for L in (14, 28, 56, 112))

    rise = [100 * 1.01 ** i for i in range(150)]
    fall = rise + [rise[-1] * 0.998 ** k for k in range(1, 40)]
    c_fall = candles(fall, 0.002)
    D = d0 + 145 * adv3.DAY
    expect_exit = next(i for i in range(146, len(fall)) if sum_signs(fall, i) < 2)
    off_sig = {('BTC', 1, str(D)): {'coin': 'BTC', 'side': 1, 'close_of': str(D), 'close': fall[145], 'U': 60.0,
                                    'stop': fall[145] - 60.0, 'mode': 'market', 'first': None}}
    f1 = follow(off_sig, {'BTC': c_fall}, {}, d0 + (len(fall) - 1) * adv3.DAY)[0]
    chk('follow: a long whose sum of signs falls below +2 ends at that close, its price the close',
        f1['state'] == 'signal' and f1['day'] == str(d0 + expect_exit * adv3.DAY) and f1['price'] == fall[expect_exit])
    gap = candles(rise, 0.002, opens={148: rise[147] * 0.95})
    off_stop = {('ETH', 1, str(D)): {'coin': 'ETH', 'side': 1, 'close_of': str(D), 'close': rise[145], 'U': rise[145] * 0.02,
                                     'stop': rise[145] * 0.98, 'mode': 'market', 'first': None}}
    f2 = follow(off_stop, {'ETH': gap}, {}, d0 + 149 * adv3.DAY)[0]
    chk('follow: a gap through the stop exits at the open, on the gap\'s day', f2['state'] == 'stop' and f2['day'] == str(d0 + 148 * adv3.DAY)
        and f2['price'] == rise[147] * 0.95)
    wick = candles(rise, 0.002)
    S = rise[145] * 0.995
    wick[d0 + 147 * adv3.DAY] = (rise[146], rise[147] * 1.002, S * 0.999, rise[147])
    f3 = follow({('ETH', 1, str(D)): dict(off_stop[('ETH', 1, str(D))], U=rise[145] - S, stop=S)}, {'ETH': wick}, {},
                d0 + 149 * adv3.DAY)[0]
    chk('follow: a wick through the stop exits at the stop', f3['state'] == 'stop' and f3['day'] == str(d0 + 147 * adv3.DAY)
        and abs(f3['price'] - S) < 1e-9)
    c_open = candles(rise, 0.002)
    last_o = d0 + 149 * adv3.DAY
    k_open = ('SOL', -1, str(D))
    off_short = {k_open: {'coin': 'SOL', 'side': -1, 'close_of': str(D), 'close': rise[145], 'U': 1000.0, 'stop': rise[145] + 1000.0,
                          'mode': 'limit', 'first': None}}
    f4 = follow(off_short, {'SOL': c_open}, {}, last_o)[0]
    chk('follow: a short on a rising series ends at the first close whose sum of signs is above -2', f4['state'] == 'signal'
        and f4['day'] == str(D + adv3.DAY))
    off_long = {('BTC', 1, str(last_o - adv3.DAY)): {'coin': 'BTC', 'side': 1, 'close_of': str(last_o - adv3.DAY), 'close': rise[148],
                                                     'U': 5.0, 'stop': rise[148] - 5.0, 'mode': 'market', 'first': None}}
    S4 = rise[148] - 5.0
    f5 = follow(off_long, {'BTC': c_open}, {}, last_o)[0]
    f6 = follow(off_long, {'BTC': c_open}, {}, last_o, {'BTC': (rise[149], rise[149], S4 - 0.01, S4 + 1)})[0]
    f7 = follow(off_long, {'BTC': c_open}, {}, last_o, {'BTC': (rise[149], rise[149] + 1, S4 + 0.01, S4 + 1)})[0]
    chk('follow: an open long; the candle forming after the close reaching its stop is a touch, its low the price; one above it is not',
        f5['state'] == 'open' and f6['state'] == 'touch' and f6['day'] == str(last_o + adv3.DAY) and f6['price'] == S4 - 0.01
        and f7['state'] == 'open')
    k_long = next(iter(off_long))
    chk('follow: an alerted offer is closed and not held; an offer of a close with no candle is unknown',
        follow(off_long, {'BTC': c_open}, {}, last_o, None, {k_long + ('stop',)})[0]['state'] == 'closed'
        and follow({('BTC', 1, '2025-01-01'): dict(off_long[k_long], close_of='2025-01-01')}, {'BTC': c_open}, {}, last_o)[0]['state'] == 'unknown')
    recs = [{'kind': 'daily', 'close_of': '2026-10-29', 'cards': [
                {'coin': 'BTC', 'side': 1, 'mode': 'market', 'close': 100.0, 'U': 8.0, 'stop': 92.0},
                {'coin': 'ETH', 'side': -1, 'mode': 'none', 'close': 50.0, 'U': 4.0, 'stop': 54.0},
                {'coin': 'NOPE', 'side': 1, 'mode': 'market', 'close': 1.0, 'U': 0.1},
                {'coin': 'SOL'}]},
            {'kind': 'alloc', 'close_of': '2026-10-30', 'alloc': {'items': [{'coin': 'XRP'}]}, 'cards': [
                {'coin': 'XRP', 'side': 1, 'mode': 'limit', 'close': 2.0, 'U': 0.2}, {'coin': 'ADA', 'side': 1, 'mode': 'market', 'close': 0.5, 'U': 0.05}]},
            {'kind': 'request', 'close_of': '2026-10-29', 'cards': [{'coin': 'BTC', 'side': 1, 'mode': 'limit', 'close': 101.0, 'U': 9.0}]},
            {'kind': 'check', 'close_of': '2026-10-30', 'cards': [{'coin': 'BTC', 'side': 1, 'mode': 'market', 'close': 104.0, 'U': 8.5}],
             'alerts': [{'kind': 'stop', 'coin': 'XRP', 'side': 1, 'close_of': '2026-10-30'}, {'kind': 'candidate', 'coin': 'BTC', 'side': 1,
                                                                                            'close_of': '2026-10-30'}, {'bad': 1}]},
            {'kind': 'check', 'close_of': 'x', 'cards': [{'coin': 'BTC', 'side': 1, 'mode': 'market', 'close': 1.0, 'U': 1.0}]}]
    offs = offers(recs)
    chk('offers: entries offered at market or as a limit, by coin, side and close, the first kept; no entry, an unknown coin, a '
        'broken card, an allocation\'s unplaced coin and a bad close left out', list(offs) == [('BTC', 1, '2026-10-29'), ('XRP', 1, '2026-10-30'),
                                                                                            ('BTC', 1, '2026-10-30')]
        and offs[('BTC', 1, '2026-10-29')]['stop'] == 92.0 and offs[('BTC', 1, '2026-10-29')]['mode'] == 'market')
    chk('alerted: the alerts of check records alone, a broken one left out',
        alerted(recs) == {('XRP', 1, '2026-10-30', 'stop'), ('BTC', 1, '2026-10-30', 'candidate')})

    # ---- a synthetic market: twelve coins, trends of several strengths -----------------------------------------------
    dm = dt.date(2026, 6, 1)
    cs, funds = {}, {}
    for n, coin in enumerate(adv3.COINS[:12]):
        c, x = {}, 100.0 + n
        slope = (0.004 + 0.0015 * n) * (1 if n % 2 == 0 else -1)
        for i in range(160):
            x *= (1 + slope) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            c[dm + dt.timedelta(days=i)] = (x, x * 1.02, x * 0.98, x)
        cs[coin] = c
        funds[coin] = lambda d: 0.0
    last = max(cs['BTC'])
    marks = {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}
    rep0 = adv3.report(cs, funds, marks, 10000.0, 0.5, int(at(last + adv3.DAY, 0, 10).timestamp() * 1000))
    order = ranked(rep0)
    active = [c for c in adv3.COINS if rep0['rows'][c].get('signal') in (1, -1) and rep0['rows'][c].get('z') is not None]
    by_hand = sorted(active, key=lambda c: (-abs(rep0['rows'][c]['z']), adv3.COINS.index(c)))
    chk('ranked: every active coin by |z|, ties in the coins\' order, its first three the report\'s TOP-3',
        order == by_hand and order[:3] == rep0['top'] and len(order) == 12)
    r7 = top_n(rep0, 7)
    chk('top_n: seven cards ranked 1 to 7 of 7, the TOP-3\'s own cards first, STRONG only among them, the ratings over all seven',
        [cd['coin'] for cd in r7['cards']] == order[:7] and [(cd['rank'], cd['of']) for cd in r7['cards']] == [(k, 7) for k in range(1, 8)]
        and all(dict(cd, rank=None, of=None) == dict(c0, rank=None, of=None) for cd, c0 in zip(r7['cards'], rep0['cards']))
        and not any(cd['strong'] for cd in r7['cards'][3:]) and len(r7['trust']['cards']) == 7 and r7['n'] == 7)
    r1 = top_n(rep0, 1)
    m7, m1 = adv3.message(r7, adv3.FACTS), adv3.message(r1, adv3.FACTS)
    chk('the TOP-7 message: seven cards, each its confidence, the label ТОП-7, the other signals without the seven; TOP-1 one card',
        m7.count('Основание: сумма знаков') == 7 and m7.count('Уверенность: <b>1/5</b>') == 7 and 'ТОП-7 по силе тренда' in m7
        and m7.count('ранг 7 из 7') == 1 and m1.count('Основание: сумма знаков') == 1 and len(r1['cards']) == 1
        and not any(f'{c},' in m7.split('Остальные сигналы')[1] or m7.split('Остальные сигналы')[1].rstrip().endswith(c) for c in order[:7]))

    # ---- the allocation: golden cases by hand, the selection with the 14 % limit, the limits at random ------------------
    D2 = adv3.DEPOSIT
    base = adv3.report(cs, funds, marks, 10000.0, 0.5, 1_793_000_000_000)

    def series(rets):
        """Candles whose daily log returns are rets, the last of them on `last`; closes from 100."""
        out, x = {}, 100.0
        ds = [last - dt.timedelta(days=len(rets) - k) for k in range(len(rets) + 1)]
        out[ds[0]] = (x, x, x, x)
        for d, r in zip(ds[1:], rets):
            x *= math.exp(r)
            out[d] = (x, x, x, x)
        return out

    A = [0.01 * (-1) ** k for k in range(60)]
    Bs = [0.01 * (1, 1, -1, -1)[k % 4] for k in range(60)]
    Cs = [0.01 * (1, -1, -1, 1)[k % 4] for k in range(60)]
    Ds = [-x for x in A]

    def scenario(spec, marks_ok=True, rets=None):
        rows = dict(base['rows'])
        for coin, side, z, stop, strong in spec:
            rows[coin] = {'signal': side, 'z': z, 'sum': 4 * side, 'U': stop, 'close': 100.0, 'prev': side, 'since': str(last),
                          'stop': 100.0 - side * stop, 'mark': 100.0, 'funding': 0.0001, 'funding_h': 8}
        r = dict(base, rows=rows, top=[c for c, *_ in spec], strong=[c for c, *_, st in spec if st], marks_ok=marks_ok, cards=[])
        return r, {c: series((rets or {}).get(c, A)) for c, *_ in spec}

    def pl(spec, budget=10000.0, n=3, risk=0.5, liq=None, rets=None, marks_ok=True):
        r, c = scenario(spec, marks_ok, rets)
        return r, plan(r, c, budget, n, risk, liq or {})

    r1_, p1 = pl([('ETH', 1, 2.0, 8.0, True)])
    it = p1['items'][0]
    chk('golden 1: one trade at an 8 % stop and 0,5 % risk is 609 USDT, leverage 7, margin 87, loss 50',
        (it['notional'], it['leverage'], it['margin'], it['loss']) == (609, 7, 87, 50) and p1['allocated'] == 609 and p1['free'] == 9391)
    r2_, p2 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 1.0, 10.0, True)], rets={'ETH': A, 'SOL': Bs})
    a, b = p2['items']
    chk('golden 2: two uncorrelated trades of strength 2 and 1 take two thirds and one third of the risk: 813 and 326 USDT',
        (a['notional'], b['notional']) == (813, 326) and (a['leverage'], b['leverage']) == (7, 6) and (a['margin'], b['margin']) == (117, 55)
        and (a['loss'], b['loss']) == (67, 34) and p2['allocated'] == 1139 and p2['loss'] == 101)
    r3_, p3 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 2.0, 8.0, True), ('XRP', 1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A, 'XRP': Bs})
    chk('golden 3: a correlated pair is discounted and the independent trade takes more: shares 0.3, 0.3, 0.4; 548, 548 and 731 USDT',
        [round(x['share'], 6) for x in p3['items']] == [0.3, 0.3, 0.4] and [x['notional'] for x in p3['items']] == [548, 548, 731])
    r4_, p4 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', -1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A})
    chk('golden 4: opposite sides on one series are no crowding: equal shares, 0.5 % each', [x['crowd'] for x in p4['items']] == [0.0, 0.0]
        and [x['notional'] for x in p4['items']] == [609, 609])
    r5_, p5 = pl([('ETH', 1, 2.0, 14.0, True)])
    it5 = p5['items'][0]
    chk('golden 5: a stop at the limit, 14 %: 352 USDT, leverage 4, margin 88, loss 50 - a wider stop, a smaller position, the same loss',
        (it5['notional'], it5['leverage'], it5['margin'], it5['loss']) == (352, 4, 88, 50))
    sel = [('ETH', 1, 3.0, 8.0, True), ('SOL', -1, 2.5, 15.0, True), ('XRP', 1, 2.0, 13.9, True), ('BTC', 1, 1.5, 6.0, False)]
    r6_, p6 = pl(sel, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs, 'BTC': Ds})
    chk('selection: STRONG only; 13.9 % placed, 15 % rejected with its reason against 14 %; a weaker setup never fills a place',
        [x['card']['coin'] for x in p6['items']] == ['ETH', 'XRP'] and p6['rejected'] == [('SOL', 'SHORT', 'стоп 15,0% дальше 14,0%')]
        and p6['plain'] == ['BTC'])
    r7_, p7 = pl(sel[:3], n=1, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs})
    chk('selection: only n are taken, the rest named', [x['card']['coin'] for x in p7['items']] == ['ETH']
        and ('XRP', 'LONG', 'сверх запрошенных 1') in p7['rejected'])
    r9_, p9 = pl([('ETH', 1, 2.0, 8.0, True)], marks_ok=False)
    chk('selection: without current prices nothing is placed', p9['items'] == [] and p9['rejected'] == [('ETH', 'LONG', 'нет текущей цены Binance')])
    r10_, p10 = pl([('ETH', 1, 2.0, 8.0, True)], liq={'ETH': 200_000.0})
    chk('liquidity: a position takes at most 0.1 % of the coin\'s mean daily volume, and says so',
        p10['items'][0]['notional'] == 200 and p10['items'][0]['capped'] is True and p1['items'][0]['capped'] is False)
    r12_, p12 = pl([('ETH', 1, 2.0, 8.0, True)], budget=50.0)
    chk('minimum: a position under 5 USDT is dropped with its reason', p12['items'] == [] and p12['rejected'] == [('ETH', 'LONG', 'позиция меньше 5 USDT')])
    rnd, bad = random.Random(39), []
    for trial in range(400):
        k = rnd.randint(1, 3)
        spec = [(adv3.COINS[m + 12], rnd.choice((1, -1)), rnd.uniform(1.0, 6.0), rnd.uniform(0.3, 18.0), rnd.random() < 0.85) for m in range(k)]
        rets = {c: [rnd.gauss(0, 0.03) if rnd.random() < 0.8 else x for x in A] for c, *_ in spec}
        budget, risk, n = rnd.choice((100.0, 777.0, 10000.0, 250000.0, 3e6)), rnd.choice((0.05, 0.3, 0.5, 1.0)), rnd.randint(1, 7)
        liq = {c: rnd.choice((None, 5e4, 1e6, 1e9)) for c, *_ in spec}
        r, pp = pl(spec, budget, n, risk, liq, rets)
        elig = [c for c, side, z, stop, st in spec if st and stop <= 14.0]
        got = [x['card']['coin'] for x in pp['items']]
        ok = (len(got) <= min(n, len(elig)) and set(got) <= set(elig) and all(float(x['notional']).is_integer() and 5 <= x['notional'] <= budget for x in pp['items'])
              and all(x['loss_exact'] <= budget * RM / 100 + 1e-9 for x in pp['items']) and pp['loss_exact'] <= budget * adv3.RISK_ALL / 100 + 1e-9
              and pp['allocated'] <= budget and pp['free'] == budget - pp['allocated']
              and all(x['margin'] * x['leverage'] >= x['notional'] and 1 <= x['leverage'] <= 20 for x in pp['items'])
              and all(x['card']['stop_pct'] <= 14.0 and x['card']['entry'] is not None for x in pp['items']))
        if not ok:
            bad.append(trial)
    chk('limits over 400 random scenarios: STRONG only and within n, stops within 14 %, each loss at the stop within 1 % of the budget, '
        'all within 5 %, positions whole and within the budget, margin covers the leverage', not bad)
    fr, stage = scenario([('ETH', 1, 3.0, 8.0, True), ('XRP', 1, 2.0, 10.0, True), ('SOL', -1, 2.5, 15.0, True), ('BTC', 1, 1.5, 6.0, False)],
                         rets={'ETH': A, 'XRP': Cs, 'SOL': Bs, 'BTC': Ds})
    pf = plan(fr, stage, 10000.0, 3, 0.5, {})
    view = plan_parts(fr, pf)
    first = view[0]
    chk('plan_parts: one message with the Boss\'s fields - budget, count and ranking, quality, entry, stop, targets with TZ-38\'s '
        'shares, capital, leverage, margin, loss, invalidation, unallocated', len(view) == 1 and all(k in first for k in (
            'Бюджет 10 000 USDT', 'стоп не дальше 14,0% входа', 'Подходящих сделок: 2 из 3 запрошенных', '1) 🟢 <b>ETH · LONG</b> · ★ STRONG',
            '2) 🟢 <b>XRP · LONG</b>', 'Качество: z', 'Вход:', '⛔ Стоп:', '· дошли 47%', 'Капитал:', 'плечо', 'маржа', 'Потеря на стопе:',
            'Свободно', 'Размещено', 'Инвалидация:')))
    chk('plan_parts: each trade its confidence with the note that the sizes are unproven; no six ratings; the rejected and the weaker named',
        first.count('Уверенность: <b>1/5</b> — правило не доказано · размеры — формула Архитектора, не доказана') == 2
        and 'Оценка доверия' not in first and 'Отклонены: SOL SHORT — стоп 15,0% дальше 14,0%' in first
        and 'В ТОП-3 без STRONG — не берутся: BTC' in first and 'не доказанная' in first)
    chk('plan_parts: one Telegram part, balanced markup; five requested says STRONG is at most three; none qualifying says so',
        len(chunks(first)) == 1 and all(first.count('<%s>' % t) == first.count('</%s>' % t) for t in ('b', 'i'))
        and 'больше 3 сделок не будет' in plan_parts(fr, plan(fr, stage, 15000.0, 5, 0.5, {}))[0]
        and 'Подходящих сделок нет' in plan_parts(*pl([('SOL', -1, 2.5, 15.0, True)], rets={'SOL': A}))[0])

    wk = [100 * 1.01 ** i for i in range(150)]
    wk.append(wk[-1] * 0.86)
    c_wk = candles(wk, 0.002)
    lw = d0 + 150 * adv3.DAY
    by_hand = [sum_signs(wk, 149), sum_signs(wk, 150)]
    rep_wk = {'close_of': str(lw), 'rows': {'BTC': {'signal': 1, 'sum': by_hand[1]}, 'ETH': {'signal': 1, 'sum': 2}}}
    fol_wk = [{'coin': 'BTC', 'side': 1, 'state': 'open'}, {'coin': 'BTC', 'side': 1, 'state': 'open'},
              {'coin': 'ETH', 'side': 1, 'state': 'open'}, {'coin': 'SOL', 'side': 1, 'state': 'stop'}]
    chk('weakened: a sum of signs from +4 at the close before to +2 at this one, the signal kept, is a weakening, once a coin; a sum '
        'that was not +4 before is not', by_hand == [4, 2] and weakened(fol_wk, rep_wk, {'BTC': c_wk, 'ETH': candles([100.0] * 151)}) == [('BTC', 1)]
        and weakened(fol_wk, dict(rep_wk, rows={'BTC': {'signal': 1, 'sum': 4}}), {'BTC': c_wk}) == []
        and weak_lines([('BTC', 1)]) == ['ℹ️ Ослабление: BTC LONG — сумма знаков упала с ±4 до ±2, сигнал держится; по правилу это не выход'])

    # ---- alerts, zones and the check's message ------------------------------------------------------------------------
    p_ = plan(rep0, cs, D2, 3, 0.5, {})
    placed = candidates(p_)
    chk('the synthetic market has STRONG coins the allocation places', len(placed) >= 1 and set(c for c, _ in placed) <= set(rep0['strong']))
    c0 = placed[0]
    fol0 = [dict(f5, key=k_long, state='stop', day=str(last), price=90.0, close=100.0, stop=91.0),
            dict(f5, key=('ETH', 1, '2026-11-01'), coin='ETH', close_of='2026-11-01', state='touch', day=str(last + adv3.DAY), price=1.0, stop=2.0),
            dict(f5, key=('SOL', -1, '2026-11-01'), coin='SOL', side=-1, close_of='2026-11-01', state='signal', day=str(last), price=5.0),
            dict(f5, key=('XRP', 1, '2026-11-02'), coin='XRP', close_of='2026-11-02', state='open')]
    al = alerts_of(fol0, placed, set(), {(k_long[0], 1, k_long[2], 'stop')}, rep0, p_)
    chk('alerts_of: a stop once, a touch as a stop, a signal exit, each candidate the check before did not place; prices against closes',
        [(x['kind'], x['coin']) for x in al] == [('stop', 'ETH'), ('signal', 'SOL')] + [('candidate', c) for c, _ in placed]
        and al[0]['touch'] is True and al[0]['level'] == 2.0 and al[1]['level'] == 5.0 and al[2]['level'] == p_['items'][0]['card']['stop'])
    chk('alerts_of: a candidate placed at the check before is not new', [x['kind'] for x in alerts_of([], placed, set(placed), set(), rep0, p_)] == [])
    coin_z = rep0['top'][0]
    row = rep0['rows'][coin_z]
    k_z = (coin_z, row['signal'], rep0['close_of'])
    off_z = {k_z: {'coin': coin_z, 'side': row['signal'], 'close_of': rep0['close_of'], 'close': row['close'], 'U': row['U'],
                   'stop': row['close'] - row['signal'] * row['U'], 'mode': 'market', 'first': None}}
    fol_z = [{'key': k_z, 'state': 'open'}]
    zone_hi = row['close'] + row['signal'] * 0.3 * row['U']
    run = dict(rep0, rows=dict(rep0['rows'], **{coin_z: dict(row, mark=zone_hi)}))
    near = dict(rep0, rows=dict(rep0['rows'], **{coin_z: dict(row, mark=row['close'] - row['signal'] * 0.8 * row['U'])}))
    zl, zn = zones_left(run, off_z, fol_z), zones_left(near, off_z, fol_z)
    chk('zones_left: past the zone a limit at its edge, near the stop no entry, inside it nothing, another close nothing',
        [z['mode'] for z in zl] == ['limit'] and abs(zl[0]['entry'] - (row['close'] + row['signal'] * 0.25 * row['U'])) < 1e-9
        and [z['mode'] for z in zn] == ['none'] and zones_left(rep0, off_z, fol_z) == []
        and zones_left(run, {k_z: dict(off_z[k_z], close_of='2026-01-01')}, fol_z) == [])
    now0 = at(last + adv3.DAY, 0, 10)
    prev_same = {'top': rep0['top'], 'strong': rep0['strong'], 'signals': {c: rep0['rows'][c].get('signal') for c in adv3.COINS}}
    still = dict(rep0, rows={c: dict(r, prev=r.get('signal')) for c, r in rep0['rows'].items()})
    t1, q1, o1, cards1 = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], prev_same, now0)
    t1w, q1w, o1w, _c = compose((last + adv3.DAY, 'signal'), still, [], [], p_, [], prev_same, now0, [(order[0], 1)])
    chk('compose: a signal check that finds nothing is one quiet line naming the TOP-3, offering no card; a weakening makes it full and quiet',
        q1 and o1 and cards1 == [] and '\n' not in t1 and t1.startswith('✓ 04:10 по Батуми') and ', '.join(rep0['top']) in t1
        and q1w and not o1w and 'ℹ️ Ослабление' in t1w)
    flip = order[-1]
    moved = dict(still, rows=dict(still['rows'], **{flip: dict(still['rows'][flip], prev=-still['rows'][flip]['signal'])}))
    t2, q2, o2, cards2 = compose((last + adv3.DAY, 'signal'), moved, fol0, [], p_, [], prev_same, now0)
    chk('compose: a signal check with the day\'s changes is the full message, quiet without an alert, its cards offered, no methodology',
        q2 and not o2 and cards2 == rep0['cards'] and 'STRONG-кандидаты' in t2 and 'Сделки по карточкам бота' in t2 and '🔄 Разворот' in t2
        and 'XRP LONG — карточка' in t2 and 'Оценка доверия' not in t2 and 'Форвард с' not in t2 and '🔔' not in t2)
    t3, q3, o3, _ = compose((last + adv3.DAY, 'signal'), still, fol0, al, p_, [], prev_same, now0)
    chk('compose: an alert makes the signal check loud and full, the events right after the header, a new candidate marked',
        not q3 and not o3 and t3.index('🔔 <b>События</b>') < t3.index('Изменения за день') and '⛔ ETH LONG' in t3
        and '🚪 SOL SHORT' in t3 and f'🆕 {c0[0]} {SIDE[c0[1]]} — проходит' in t3)
    nowf = at(last + adv3.DAY, 12, 10)
    t4, q4, o4, cards4 = compose((last + adv3.DAY, 'fact'), rep0, fol0[3:], [], p_, [], prev_same, nowf)
    t5, q5, o5, cards5 = compose((last + adv3.DAY, 'fact'), rep0, fol0[3:], [], p_, zl, prev_same, nowf)
    t6, q6, o6, cards6 = compose((last + adv3.DAY, 'fact'), rep0, fol0, al, p_, [], prev_same, nowf)
    chk('compose: a fact check that finds nothing is one quiet line naming the next check; zones alone are quiet and several lines',
        q4 and o4 and cards4 == [] and t4.startswith('✓ 16:10 по Батуми') and 'следующая проверка 04:10' in t4 and '\n' not in t4
        and q5 and not o5 and 'Зоны входа карточек закрытия' in t5 and 'не догонять' in t5 and cards5 == [])
    chk('compose: a fact check with alerts is loud, carries each new candidate\'s plan and offers its card, no other card',
        not q6 and not o6 and '🔔 <b>События</b>' in t6 and 'теперь проходит лимиты' in t6 and t6.count('Капитал:') == len(placed)
        and [cd['coin'] for cd in cards6] == [c for c, _ in placed] and 'сегодня (минимум дня' in t6)
    chk('compose: every message balances its markup and fits one Telegram part', all(
        len(chunks(t)) == 1 and t.count('<b>') == t.count('</b>') and t.count('<i>') == t.count('</i>') for t in (t1, t2, t3, t4, t5, t6)))
    recq = check_record((last + adv3.DAY, 'signal'), rep0, fol0 + [dict(fol0[0], state='closed')], al, p_, [], [7, 8], False, False, cards2, now0,
                        [('XRP', 1)])
    chk('check_record: kind, slot, flags, every coin\'s state with the ranks, the followed trades but the closed, the alerts with their '
        'prices, the placed coins, the six ratings, the cards with their confidence', recq['kind'] == 'check' and recq['slot'] == slot_text((last + adv3.DAY, 'signal'))
        and recq['quiet'] is False and recq['one_line'] is False and len(recq['state']) == len(adv3.COINS)
        and [c for c in adv3.COINS if recq['state'][c]['rank']] == [c for c in adv3.COINS if c in order]
        and all(recq['state'][c]['rank'] == order.index(c) + 1 for c in order) and len(recq['followed']) == 4
        and recq['alerts'] == al and recq['passing'] == [list(x) for x in placed] and recq['message_ids'] == [7, 8] and recq['weakened'] == [['XRP', 1]]
        and set(recq['trust']) >= {'system', 'strong_justified', 'cards', 'quality', 'expectancy_established'}
        and [c['confidence'] for c in recq['cards']] == [rep0['trust']['cards'][cd['coin']] for cd in cards2]
        and json.loads(json.dumps(recq, default=str))['utc'] == now0.isoformat(timespec='seconds'))

    # ---- three checks end to end: Binance and Telegram stood in for, the journal in a scratch directory ------------------
    class Cap(Telegram):
        def __init__(self, down=False):
            super().__init__('123456:SECRET', 777)
            self.sent, self.down = [], down

        def call(self, method, http_timeout=30, **params):
            if self.down:
                raise RuntimeError('telegram sendMessage: 502 Bad Gateway')
            self.sent.append((params['text'], params.get('disable_notification', False)))
            return {'message_id': len(self.sent)}

    class Stub:
        def __init__(self, cs, funds):
            self.cs, self.funds, self.missing = cs, funds, []

        def fresh(self):
            return self.cs, self.funds

    ms = lambda d: int(dt.datetime.combine(d, dt.time(0), tzinfo=dt.timezone.utc).timestamp() * 1000)
    forming = {}

    def fake_fapi(path, **params):
        if path == '/fapi/v1/premiumIndex':
            return [{'symbol': c + 'USDT', 'markPrice': str(m[0]), 'lastFundingRate': '0.0001'} for c, m in ((k[:-4], v) for k, v in marks.items())]
        if path == '/fapi/v1/fundingInfo':
            return []
        coin = params['symbol'][:-4]
        if params.get('limit') == 2:
            o, h, l, c_ = forming.get(coin) or (cs[coin][last][3],) * 4
            return [[ms(last), '1', '1', '1', '1', '0', ms(last + adv3.DAY) - 1, '0'],
                    [ms(last + adv3.DAY), str(o), str(h), str(l), str(c_), '0', ms(last + 2 * adv3.DAY) - 1, '0']]
        return [[ms(last - k * adv3.DAY), '1', '1', '1', '1', '0', ms(last - k * adv3.DAY + adv3.DAY) - 1, '1e12'] for k in range(8)]

    state = tempfile.mkdtemp(prefix='.selftest-', dir=os.path.dirname(os.path.abspath(__file__)))
    saved = (globals()['STATE'], adv3.fapi)
    globals()['STATE'], adv3.fapi = state, fake_fapi
    try:
        top0 = rep0['top'][0]
        r0 = rep0['rows'][top0]
        old = {'utc': '2026-10-29T06:00:00+00:00', 'kind': 'daily', 'close_of': str(last), 'cards': [
            {'coin': top0, 'side': r0['signal'], 'mode': 'market', 'close': r0['close'], 'U': r0['U'] * 0.25,
             'stop': r0['close'] - r0['signal'] * r0['U'] * 0.25}]}
        with open(os.path.join(state, 'journal.jsonl'), 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(old) + '\nnot json\n')
        stub, cap = Stub(cs, funds), Cap()
        with contextlib.redirect_stdout(io.StringIO()):
            e1 = check(cap, stub, (last + adv3.DAY, 'signal'), now0)
            append(e1)
            S_ = r0['close'] - r0['signal'] * r0['U'] * 0.25
            touch = S_ * (0.999 if r0['signal'] > 0 else 1.001)
            forming[top0] = (r0['close'], max(r0['close'], touch), min(r0['close'], touch), r0['close'])
            e2 = check(cap, stub, (last + adv3.DAY, 'fact'), nowf)
            append(e2)
            e3 = check(cap, stub, (last + adv3.DAY, 'fact'), nowf)
        n_sent = len(cap.sent)
        chk('end to end: the signal check sends the full message, quiet with no alert, records 42 states, its cards and the placed coins',
            e1['kind'] == 'check' and e1['slot'] == slot_text((last + adv3.DAY, 'signal')) and not e1['one_line']
            and e1['quiet'] == (not e1['alerts']) == cap.sent[0][1] and len(e1['state']) == 42 and e1['cards']
            and e1['passing'] == [list(x) for x in placed] and all(a['kind'] == 'candidate' for a in e1['alerts'])
            and len(e1['alerts']) == len(placed))
        chk('end to end: the fact check reads the forming candle through the stop of the offer the old daily record made - one loud alert',
            [(a['kind'], a['coin'], a['touch']) for a in e2['alerts']] == [('stop', top0, True)] and e2['quiet'] is False
            and cap.sent[1][1] is False and 'задет сегодня' in cap.sent[1][0] and e2['one_line'] is False)
        chk('end to end: the same fact check again sends no second alert - the offer is closed - and finds the candidates placed before',
            e3['alerts'] == [] and e3['quiet'] is True and n_sent == 3 and not [f for f in e3['followed'] if f['coin'] == top0 and f['close_of'] == str(last)
                                                                                and f['U'] == r0['U'] * 0.25])
        recs2 = list(journal_records())
        chk('end to end: the journal parses past its broken line, holds the old record and the two checks, in order',
            [r['kind'] for r in recs2] == ['daily', 'check', 'check'] and recs2[1]['utc'] == now0.isoformat(timespec='seconds'))

        def fake_make_fail(*a_, **k_):
            raise RuntimeError('fapi.binance.com served no candles')

        cap2 = Cap()
        with contextlib.redirect_stdout(io.StringIO()):
            for text in ('сигнал', 'сигнал топ 7', 'оценка', 'сигнал 10000 топ 3', 'привет'):
                handle(cap2, stub, text)
            kinds = [r['kind'] for r in list(journal_records())[3:]]
            saved_lr = globals()['live_report']
            globals()['live_report'] = fake_make_fail
            try:
                handle(cap2, stub, 'сигнал')
                handle(Cap(down=True), stub, 'сигнал')
            finally:
                globals()['live_report'] = saved_lr
        texts = [t for t, _q in cap2.sent]
        recs3 = list(journal_records())
        chk('handle: «сигнал» three cards, «сигнал топ 7» seven, «оценка» the assessment, the allocation one message, an unknown text HELP',
            texts[0].count('Основание:') == 3 and texts[1].count('Основание:') == 7 and texts[2].startswith('🧭') and 'Оценка доверия' in texts[2]
            and texts[3].startswith('💼') and texts[4] == HELP and all(q is False for _t, q in cap2.sent[:5]))
        chk('handle: the journal holds request, request, assess, alloc, each with its cards; an unknown text no record',
            kinds == ['request', 'request', 'assess', 'alloc'] and recs3[3]['n'] == 3 and recs3[4]['n'] == 7
            and recs3[5]['cards'] == [] and 'trust' in recs3[5] and len(recs3[6]['cards']) == len(placed))
        chk('handle: Binance down gets the apology, Telegram down raises nothing', texts[-1].startswith('Binance или Telegram не ответили'))
    finally:
        globals()['STATE'], adv3.fapi = saved
        shutil.rmtree(state)
    chk('glibc takes its two settings', malloc_tune())
    print(f'SELFTEST PASS: {len(done)} of {len(done)} checks passed')


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    for m in ('serve', 'probe', 'find-chat', 'hello', 'selftest'):
        g.add_argument('--' + m, action='store_true')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if a.probe:
        probe()
    elif a.find_chat:
        find_chat()
    elif a.hello:
        hello()
    elif a.selftest:
        selftest()
    else:
        serve()


if __name__ == '__main__':
    main()
