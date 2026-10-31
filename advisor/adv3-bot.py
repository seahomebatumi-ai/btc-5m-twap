#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands, the daily message at 06:00 UTC
# (10:00 in Batumi), and a journal of every message sent. Standard library only; adv3.py lies beside it.
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
DAILY = dt.time(6, 0)
POLL, RETRY, LIMIT = 50, 300, 4000
OPEN = ('сигнал', 'сигналы', 'signal', 'signals', 'топ', 'top', 'стратегия', 'стратегию', 'strategy')
HEAD = re.compile(r'^\s*/?([^\W\d_]+)')
TOPN = re.compile(r'(?:топ|top)[\s\-\u2013]*(\d{1,2})(?!\d)', re.I)
# TZ-37's allocation view: the stop's limit in percent of the entry, the smallest position, the share of a coin's mean
# daily quote volume a position may take, the discount for same-way correlation, the strength's cap, the days of volume.
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS = 11.1, 5.0, 0.001, 0.5, 3.0, 7
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — сигналы сейчас: ТОП-3 правила, депозит 10 000 USDT и риск 0,5% на сделку — пример размера.\n'
        '«сигнал 10000 топ 3» — распределить 10 000 USDT между сильнейшими сделками: только STRONG, стоп не дальше 11,1% '
        'цены входа; подошло две — покажу две, ни одной — скажу, что нет. STRONG бывает только в ТОП-3, больше трёх не будет.\n'
        '«сигнал 15000 топ 5» — то же на 15 000 USDT; «сигнал 10000» — то же, до трёх сделок.\n'
        'Риск на сделку — 0,5% бюджета, не больше 1%: «сигнал 10000 топ 3 1». Чего нельзя разместить без превышения риска, '
        'остаётся свободным — ответ скажет, сколько.\n'
        'Каждый день в 10:00 по Батуми сигналы приходят сами.')


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

    def send(self, text):
        """The text as HTML, in parts of at most LIMIT characters; a part Telegram cannot parse goes as plain text."""
        ids = []
        for part in chunks(text):
            try:
                ids.append(self.call('sendMessage', chat_id=self.chat, text=part, parse_mode='HTML',
                                     disable_web_page_preview=True)['message_id'])
            except RuntimeError as e:
                if 'parse entities' not in str(e):
                    raise
                plain = html.unescape(re.sub(r'</?[bi]>', '', part))
                ids.append(self.call('sendMessage', chat_id=self.chat, text=plain,
                                     disable_web_page_preview=True)['message_id'])
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
    """('signal', None, None, risk) for «сигнал [risk]», the TOP-3 message; ('alloc', budget, n, risk) where a budget of
    100 or more is given - «сигнал 10000 топ 3», «сигнал 15000 топ 5», «сигнал 10000» (n = 3), «топ 3 на 10000» - the
    allocation view; None where the text is neither. n is read after «топ» or «top» (1 to 10); risk is the percent of
    the budget a trade may lose at its stop (default 0.5, at most 1)."""
    text = text or ''
    m = HEAD.match(text)
    if not m or m.group(1).lower() not in OPEN:
        return None
    s = re.sub(r'@\w+', ' ', text)
    top = TOPN.search(s)
    if top:
        s = s[:top.start()] + ' ' + s[top.end():]
    budget, risk = numbers(s)
    if budget is None:
        return ('signal', None, None, risk)
    return ('alloc', budget, min(max(int(top.group(1)), 1), 10) if top else adv3.TOP_N, risk)


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


def make(data, deposit, risk):
    """The report and the message at this moment; mark prices that fail leave the cards on the close."""
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
    rep = adv3.report(cs, funds, marks, deposit, risk, int(time.time() * 1000), data.missing, intervals)
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


def plan_parts(rep, p):
    """The allocation view as two messages: the trades with their figures, then the six ratings."""
    last = dt.date.fromisoformat(rep['close_of'])
    usdt, pct, num, price = adv3.usdt, adv3.pct, adv3.num, adv3.price
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
        cd = it['card']
        side, dot = ('LONG', '🟢') if cd['side'] > 0 else ('SHORT', '🔴')
        lo, hi = cd['zone']
        ref = cd['entry']
        mfe = adv3.FACTS['strong'].get('mfe') if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else adv3.FACTS['base'].get('mfe')
        lines += ['', f"{it['rank']}) {dot} <b>{cd['coin']} · {side}</b> · ★ STRONG",
                  f"Качество: z {adv3.signed(cd['z'])} · сумма знаков {adv3.signed(cd['sum'], 0)} из ±4 · доля {pct(100 * it['share'], 0)}%"
                  + (f" · корреляция с остальными {adv3.signed(it['crowd'])}" if p['k'] > 1 else ''),
                  (f"Вход: <b>по рынку</b> ≈ {price(ref)}, зона {price(lo)}–{price(hi)}" if cd['mode'] == 'market'
                   else f"Вход: <b>лимит {price(ref)}</b> — ждать отката, цена {price(cd['mark'])} ушла от зоны"),
                  f"⛔ Стоп: <b>{price(cd['stop'])}</b> ({'−' if cd['side'] > 0 else '+'}{pct(cd['stop_pct'])}%)"]
        for number, t in zip((1, 2, 3), cd['targets']):
            lines.append(f"🎯 {price(t)} ({'+' if (t - ref) > 0 else ''}{pct(100 * (t - ref) / ref)}%)" + (f" · дошли {pct(100 * mfe[number], 0)}%" if mfe else ''))
        lines += [f"Капитал: <b>{usdt(it['notional'])} USDT</b>{' (ограничен ликвидностью)' if it['capped'] else ''} · плечо {it['leverage']}× изол. · маржа {usdt(it['margin'])} USDT",
                  f"Потеря на стопе: {usdt(it['loss'])} USDT с комиссиями",
                  f"Инвалидация: {'цена ≤' if cd['side'] > 0 else 'цена ≥'} {price(cd['stop'])} или закрытие дня с суммой знаков "
                  f"{'ниже +2' if cd['side'] > 0 else 'выше −2'}"]
    if p['rejected']:
        lines += ['', 'Отклонены: ' + '; '.join(f'{c} {s} — {why}' for c, s, why in p['rejected'])]
    if p['plain']:
        lines.append('В ТОП-3 без STRONG — не берутся: ' + ', '.join(p['plain']))
    if p['n'] > adv3.TOP_N:
        lines.append(f'STRONG бывает только в ТОП-3: больше {adv3.TOP_N} сделок не будет')
    own = dict(rep, cards=[it['card'] for it in p['items']])
    for it in p['items']:
        it['card']['rank'] = it['rank']
    own['trust'] = adv3.trust(own)
    second = adv3.trust_lines(own, adv3.FACTS) + ['', 'Размеры — формула ТЗ-37 (сила тренда, поправка на корреляцию, ликвидность, лимиты риска), не доказанная: форвард-запись '
                                                  'проверяет правило, а не этот отбор и не эти размеры.',
              '<i>Не инвестиционный совет: правило показывает состояние рынка; решение и риск — ваши.</i>']
    return ['\n'.join(lines), '\n'.join(second)]


def journal(kind, rep, ids, extra=None):
    rec = {'utc': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'],
           'close_of': rep['close_of'], 'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'],
           'strong': rep['strong'], 'message_ids': ids,
           'signals': {k: v.get('signal') for k, v in rep['rows'].items()},
           'cards': [{k: cd[k] for k in ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U')}
                     for cd in rep['cards']]}
    rec.update(extra or {})
    with open(os.path.join(STATE, 'journal.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + '\n')


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
    off_path, day_path = os.path.join(STATE, 'offset'), os.path.join(STATE, 'daily-sent')
    offset = int(read(off_path)) if os.path.exists(off_path) else 0
    sent = read(day_path) if os.path.exists(day_path) else ''
    retry_at = 0.0
    log('serving the pinned chat: pid', os.getpid(), 'offset', offset, 'daily-sent', sent or '-')
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        due = dt.datetime.combine(now.date(), DAILY, tzinfo=dt.timezone.utc)
        if now >= due and sent != now.date().isoformat() and time.time() >= retry_at:
            try:
                rep, msg = make(data, adv3.DEPOSIT, adv3.RISK)
                ids = tg.send(msg)
            except Exception:
                retry_at = time.time() + RETRY
                log('daily failed, retry in', RETRY, 's\n' + traceback.format_exc())
            else:
                sent = now.date().isoformat()      # sent: never again today, whatever its record does
                try:
                    put(day_path, sent)
                    journal('daily', rep, ids)
                except Exception:
                    log('daily record failed\n' + traceback.format_exc())
                log('daily sent for the close of', rep['close_of'])
        if sent == now.date().isoformat():
            wait = POLL
        elif now < due:
            wait = min(POLL, max(1, int((due - now).total_seconds())))
        else:
            wait = min(POLL, max(1, int(retry_at - time.time())))
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
            rep, msg = make(data, budget or adv3.DEPOSIT, risk)
            extra, parts = None, [msg]
            if kind == 'alloc':
                p = plan(rep, data.cs, budget, n, risk, {c: liquidity(c, rep['made_at_ms']) for c in rep['strong']})
                parts = plan_parts(rep, p)
                extra = {'alloc': {'budget': budget, 'n': n, 'risk': risk, 'allocated': p['allocated'], 'free': p['free'], 'loss': p['loss'],
                                   'items': [{'coin': it['card']['coin'], 'side': it['card']['side'], 'notional': it['notional'],
                                              'leverage': it['leverage'], 'margin': it['margin'], 'loss': it['loss']} for it in p['items']],
                                   'rejected': p['rejected']}}
            ids = [i for part in parts for i in tg.send(part)]
            try:
                journal(kind if kind == 'alloc' else 'request', rep, ids, extra)
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
    and parsed. Prints counts, dates and the bot's name; never the token or a chat id."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    c = adv3.fapi_candles('BTCUSDT', now_ms)
    assert c and max(c) >= today - 2 * adv3.DAY and all(len(v) == 4 and v[3] > 0 for v in c.values()), 'klines'
    print('P-KLINES served:', len(c), 'closed daily candles of BTCUSDT, the last', max(c))
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
        'ADV-3 подключён к этому чату. Напишите «сигнал» — или ждите сигналов в 10:00 по Батуми.')
    assert ids and all(isinstance(x, int) for x in ids), ids
    print('G-HELLO sent: message ids', ids)


def selftest():
    """The bot's own checks, offline: the commands, the allocation (golden cases computed by hand, the limits over random
    scenarios), the replies, the chunks, the files, the log, the HTML fallback, glibc."""
    import contextlib, io, random, shutil, tempfile
    done = []

    def check(name, ok):
        done.append(name)
        assert ok, name

    D, R, RM = adv3.DEPOSIT, adv3.RISK, adv3.RISK_MAX
    for text, want in (('сигнал', ('signal', None, None, R)), ('Сигнал 0,5%', ('signal', None, None, 0.5)),
                       ('signal 0.3', ('signal', None, None, 0.3)), ('сигналы', ('signal', None, None, R)),
                       ('сигнал топ 3', ('signal', None, None, R)), ('сигнал 99', ('signal', None, None, RM)),
                       ('сигнал 10000 топ 3', ('alloc', 10000.0, 3, R)), ('сигнал 15000 топ 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 10000', ('alloc', 10000.0, 3, R)), ('Сигнал 15 000 топ 5 1', ('alloc', 15000.0, 5, 1.0)),
                       ('/signal@adv3_bot 5000 top 2', ('alloc', 5000.0, 2, R)), ('signal 5000 top2', ('alloc', 5000.0, 2, R)),
                       ('топ 3 на 10000', ('alloc', 10000.0, 3, R)), ('топ3 10000', ('alloc', 10000.0, 3, R)),
                       ('сигнал 10к топ 3', ('alloc', 10000.0, 3, R)), ('signal 15k top 5', ('alloc', 15000.0, 5, R)),
                       ('сигнал 1,5 тыс', ('alloc', 1500.0, 3, R)), ('сигнал 10 коинов', ('signal', None, None, RM)),
                       ('сигнал 10000 топ-3', ('alloc', 10000.0, 3, R)), ('сигнал 10000 топ 3 0,3', ('alloc', 10000.0, 3, 0.3)),
                       ('стратегия 7000 топ 2', ('alloc', 7000.0, 2, R)), ('сигнал 20000 топ 3 3', ('alloc', 20000.0, 3, RM)),
                       ('сигнал 12000 0.01', ('alloc', 12000.0, 3, 0.05)), ('сигнал 10000 usdt топ 1', ('alloc', 10000.0, 1, R)),
                       ('сигнал 10000 топ 0', ('alloc', 10000.0, 1, R)), ('сигнал 10000 топ 50', ('alloc', 10000.0, 10, R)),
                       ('signal 200000000', ('alloc', 10_000_000.0, 3, R)), ('сигнал 100 топ 3', ('alloc', 100.0, 3, R)),
                       ('привет', None), ('сигнализация', None), ('', None), ('12345', None), ('все', None), ('eth', None)):
        check(f'route {text!r}', route(text) == want)
    check('HELP names the commands, the filter, the cap of three and the defaults, in one Telegram part',
          all(k in HELP for k in ('«сигнал»', '«сигнал 10000 топ 3»', '«сигнал 15000 топ 5»', '«сигнал 10000»', '11,1%', 'STRONG',
                                  'не больше 1%', '10:00')) and len(chunks(HELP)) == 1)
    long_text = '\n'.join(f'line {i} ' + 'x' * 90 for i in range(200))
    parts = chunks(long_text)
    check('chunks: 5 parts under the limit, joined back whole',
          len(parts) == 5 and all(len(p) <= LIMIT for p in parts) and '\n'.join(parts) == long_text)
    tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'.selftest-{os.getpid()}')
    os.mkdir(tmp)
    try:
        f = os.path.join(tmp, 'offset')
        put(f, '41')
        put(f, '42')
        check('put replaces in one rename', read(f) == '42' and sorted(os.listdir(tmp)) == ['offset'])
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
    check('HTML sent as HTML', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML')
    check('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
          and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    SECRETS.append('123456:SECRET')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        log('url https://api.telegram.org/bot123456:SECRET/getMe failed')
    SECRETS.remove('123456:SECRET')
    check('the token never reaches the log', 'SECRET' not in buf.getvalue() and '<token>' in buf.getvalue())
    d0 = dt.date(2026, 6, 1)
    cs, funds = {}, {}
    for n, coin in enumerate(adv3.COINS[:6]):
        c, x = {}, 100.0 + n
        for i in range(160):
            x *= (1.012 if n % 2 == 0 else 0.988) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            c[d0 + dt.timedelta(days=i)] = (x, x * 1.02, x * 0.98, x)
        cs[coin] = c
        funds[coin] = lambda d: 0.0
    rep = adv3.report(cs, funds, {}, 15000.0, 0.5, 0)
    msg = adv3.message(rep, adv3.FACTS)
    check('a synthetic report: 3 cards at 75 USDT of risk each', len(rep['cards']) == 3 and all(
        cd['mode'] == 'market' and abs(cd['qty'] * abs(cd['entry'] - cd['stop']) - 75) < 1e-9 for cd in rep['cards']))
    check('its message fits one Telegram message', len(chunks(msg)) == 1 and 'Депозит 15 000 USDT' in msg)
    last = max(cs['BTC'])
    marks = {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}
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

    A = [0.01 * (-1) ** k for k in range(60)]                       # alternating
    Bs = [0.01 * (1, 1, -1, -1)[k % 4] for k in range(60)]          # orthogonal to A over 56 days, both of mean zero
    Cs = [0.01 * (1, -1, -1, 1)[k % 4] for k in range(60)]          # orthogonal to A and to Bs
    Ds = [-x for x in A]

    def scenario(spec, marks_ok=True, rets=None):
        """A report whose rows are spec = [(coin, side, z, stop percent, strong)] in rank order, entry = close = 100, so the stop is at
        stop percent of the entry; and candles for the coins from rets."""
        rows = dict(base['rows'])
        for coin, side, z, stop, strong in spec:
            rows[coin] = {'signal': side, 'z': z, 'sum': 4 * side, 'U': stop, 'close': 100.0, 'prev': side, 'since': str(last),
                          'stop': 100.0 - side * stop, 'mark': 100.0, 'funding': 0.0001, 'funding_h': 8}
        r = dict(base, rows=rows, top=[c for c, *_ in spec], strong=[c for c, *_, st in spec if st], marks_ok=marks_ok, cards=[])
        return r, {c: series((rets or {}).get(c, A)) for c, *_ in spec}

    def pl(spec, budget=10000.0, n=3, risk=0.5, liq=None, rets=None, marks_ok=True):
        r, c = scenario(spec, marks_ok, rets)
        return r, plan(r, c, budget, n, risk, liq or {})

    # G1: one STRONG trade, stop 8 %, 10,000 USDT, 0,5 %: 50 USDT of loss over 0.082 -> 609 USDT; leverage 7; margin 87; loss 50
    r1, p1 = pl([('ETH', 1, 2.0, 8.0, True)])
    it = p1['items'][0]
    check('golden 1: one trade at an 8 % stop and 0,5 % risk is 609 USDT, leverage 7, margin 87, loss 50',
          (it['notional'], it['leverage'], it['margin'], it['loss']) == (609, 7, 87, 50) and p1['allocated'] == 609 and p1['free'] == 9391
          and p1['margin'] == 87 and p1['loss'] == 50 and p1['k'] == 1)
    # G2: two uncorrelated trades, z 2 and 1, stops 8 % and 10 %: losses 66.67 and 33.33 -> 813 and 326
    r2, p2 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 1.0, 10.0, True)], rets={'ETH': A, 'SOL': Bs})
    a, b = p2['items']
    check('golden 2: two uncorrelated trades of strength 2 and 1 take two thirds and one third of the risk: 813 and 326 USDT',
          (a['notional'], b['notional']) == (813, 326) and (a['leverage'], b['leverage']) == (7, 6) and (a['margin'], b['margin']) == (117, 55)
          and (a['loss'], b['loss']) == (67, 34) and p2['allocated'] == 1139 and p2['loss'] == 101 and a['rank'] == 1 and b['rank'] == 2)
    # G3: A and B the same series, C orthogonal: the pair is discounted, C takes 0.4 of the risk -> 45, 45, 60 USDT of loss
    r3, p3 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 2.0, 8.0, True), ('XRP', 1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A, 'XRP': Bs})
    check('golden 3: a correlated pair is discounted and the independent trade takes more: shares 0.3, 0.3, 0.4; 548, 548 and 731 USDT',
          [round(x['share'], 6) for x in p3['items']] == [0.3, 0.3, 0.4] and [x['notional'] for x in p3['items']] == [548, 548, 731]
          and [round(x['risk_pct'], 6) for x in p3['items']] == [0.45, 0.45, 0.6])
    # G4: a LONG and a SHORT on the same series hedge each other: no discount
    r4, p4 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', -1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A})
    check('golden 4: opposite sides on one series are no crowding: equal shares, 0.5 % each', [x['crowd'] for x in p4['items']] == [0.0, 0.0]
          and [round(x['share'], 6) for x in p4['items']] == [0.5, 0.5] and [x['notional'] for x in p4['items']] == [609, 609])
    r5, p5 = pl([('ETH', 1, 2.0, 8.0, True), ('SOL', 1, 2.0, 8.0, True)], rets={'ETH': A, 'SOL': A})
    check('golden 5: two longs on one series are discounted alike, so their shares stay equal', [round(x['crowd'], 6) for x in p5['items']] == [1.0, 1.0]
          and [round(x['share'], 6) for x in p5['items']] == [0.5, 0.5])
    # selection
    sel = [('ETH', 1, 3.0, 8.0, True), ('SOL', -1, 2.5, 13.0, True), ('XRP', 1, 2.0, 10.0, True), ('BTC', 1, 1.5, 6.0, False)]
    r6, p6 = pl(sel[:3] + [('BTC', 1, 1.5, 6.0, False)], rets={'ETH': A, 'SOL': Bs, 'XRP': Cs, 'BTC': Ds})
    check('selection: STRONG only, a stop beyond 11.1 % rejected with its reason, a weaker setup never fills a place',
          [x['card']['coin'] for x in p6['items']] == ['ETH', 'XRP'] and p6['rejected'] == [('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%')]
          and p6['plain'] == ['BTC'] and p6['k'] == 2)
    r7, p7 = pl(sel[:3], n=1, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs})
    check('selection: only n are taken, the rest named', [x['card']['coin'] for x in p7['items']] == ['ETH']
          and ('XRP', 'LONG', 'сверх запрошенных 1') in p7['rejected'])
    r8, p8 = pl([('SOL', -1, 2.5, 13.0, True)], rets={'SOL': A})
    check('selection: no qualifying trade is no allocation, the whole budget free', p8['items'] == [] and p8['free'] == 10000.0 and p8['allocated'] == 0 and p8['loss'] == 0)
    r9, p9 = pl([('ETH', 1, 2.0, 8.0, True)], marks_ok=False)
    check('selection: without current prices nothing is placed', p9['items'] == [] and p9['rejected'] == [('ETH', 'LONG', 'нет текущей цены Binance')])
    rA, cA = scenario([('ETH', 1, 2.0, 8.0, True)])
    rA['rows']['ETH'] = dict(rA['rows']['ETH'], mark=100.0 - 8.0 + 1.0)
    pA = plan(rA, cA, 10000.0, 3, 0.5, {})
    check('selection: a price at the stop gives no entry and no position', pA['items'] == [] and pA['rejected'][0][2] == 'цена у стопа, входа нет')
    r10, p10 = pl([('ETH', 1, 2.0, 8.0, True)], liq={'ETH': 200_000.0})
    check('liquidity: a position takes at most 0.1 % of the coin\'s mean daily volume, and says so',
          p10['items'][0]['notional'] == 200 and p10['items'][0]['capped'] is True and p1['items'][0]['capped'] is False)
    r11, p11 = pl([('ETH', 1, 2.0, 0.5, True), ('SOL', 1, 2.0, 0.5, True), ('XRP', 1, 2.0, 0.5, True)], budget=1000.0, rets={'ETH': A, 'SOL': Bs, 'XRP': Cs})
    check('budget: positions that would exceed the budget are scaled to it, risk only falling', sum(x['notional'] for x in p11['items']) <= 1000
          and all(x['loss_exact'] <= 1000 * 0.01 for x in p11['items']))
    r12, p12 = pl([('ETH', 1, 2.0, 8.0, True)], budget=50.0)
    check('minimum: a position under 5 USDT is dropped with its reason', p12['items'] == [] and p12['rejected'] == [('ETH', 'LONG', 'позиция меньше 5 USDT')])
    # the limits over random scenarios
    rnd, bad = random.Random(37), []
    for trial in range(400):
        k = rnd.randint(1, 3)
        spec = [(adv3.COINS[m + 6], rnd.choice((1, -1)), rnd.uniform(1.0, 6.0), rnd.uniform(0.3, 14.0), rnd.random() < 0.85) for m in range(k)]
        rets = {c: [rnd.gauss(0, 0.03) if rnd.random() < 0.8 else x for x in A] for c, *_ in spec}
        budget, risk, n = rnd.choice((100.0, 777.0, 10000.0, 250000.0, 3e6)), rnd.choice((0.05, 0.3, 0.5, 1.0)), rnd.randint(1, 6)
        liq = {c: rnd.choice((None, 5e4, 1e6, 1e9)) for c, *_ in spec}
        r, pp = pl(spec, budget, n, risk, liq, rets)
        elig = [c for c, side, z, stop, st in spec if st and stop <= STOP_MAX]
        got = [x['card']['coin'] for x in pp['items']]
        ok = (len(got) <= min(n, len(elig)) and set(got) <= set(elig) and all(float(x['notional']).is_integer() and MIN_NOTIONAL <= x['notional'] <= budget for x in pp['items'])
              and all(x['loss_exact'] <= budget * adv3.RISK_MAX / 100 + 1e-9 for x in pp['items'])
              and pp['loss_exact'] <= budget * adv3.RISK_ALL / 100 + 1e-9 and pp['allocated'] <= budget and pp['free'] == budget - pp['allocated']
              and all(x['margin'] * x['leverage'] >= x['notional'] and 1 <= x['leverage'] <= 20 for x in pp['items'])
              and all(x['loss'] >= x['loss_exact'] - 1e-9 for x in pp['items'])
              and all((not x['capped']) or x['notional'] <= LIQ_FRAC * liq[x['card']['coin']] for x in pp['items'])
              and all(x['card']['stop_pct'] <= STOP_MAX and x['card']['entry'] is not None for x in pp['items'])
              and pp['allocated'] == sum(x['notional'] for x in pp['items']) and pp['loss'] == sum(x['loss'] for x in pp['items']))
        if not ok:
            bad.append(trial)
    check('limits over 400 random scenarios: STRONG only and within n, each loss at the stop within 1 % of the budget, all within 5 %, '
          'positions whole and within the budget, margin covers the leverage, the liquidity cap held', not bad)
    fr, stage = scenario([('ETH', 1, 3.0, 8.0, True), ('XRP', 1, 2.0, 10.0, True), ('SOL', -1, 2.5, 13.0, True), ('BTC', 1, 1.5, 6.0, False)],
                         rets={'ETH': A, 'XRP': Cs, 'SOL': Bs, 'BTC': Ds})
    pf = plan(fr, stage, 10000.0, 3, 0.5, {})
    first, second = plan_parts(fr, pf)
    check('plan_parts: the Boss\'s fields - budget, qualifying count and ranking, direction, quality, entry, stop, targets, capital, leverage, margin, loss, unallocated',
          all(k in first for k in ('Бюджет 10 000 USDT', 'Подходящих сделок: 2 из 3 запрошенных', '1) 🟢 <b>ETH · LONG</b> · ★ STRONG', '2) 🟢 <b>XRP · LONG</b>', 'Качество: z', 'Вход:',
                                   '⛔ Стоп:', '🎯', 'Капитал:', 'плечо', 'маржа', 'Потеря на стопе:', 'Свободно', 'Размещено', 'Инвалидация:')))
    check('plan_parts: the rejected and the weaker named, the ratings, the note that the sizes are unproven and the disclaimer in the second message',
          'Отклонены: SOL SHORT — стоп 13,0% дальше 11,1%' in first and 'В ТОП-3 без STRONG — не берутся: BTC' in first
          and 'Оценка доверия' in second and 'ETH 1/5 · XRP 1/5' in second and 'не доказанная' in second and second.rstrip().endswith('решение и риск — ваши.</i>'))
    check('plan_parts: each message is one Telegram part and the markup balances', len(chunks(first)) == 1 and len(chunks(second)) == 1
          and all(t.count('<b>') == t.count('</b>') and t.count('<i>') == t.count('</i>') for t in (first, second)))
    empty = plan_parts(r8, p8)
    check('plan_parts: no qualifying trade says so, with the whole budget free and the ratings', 'Подходящих сделок нет' in empty[0] and 'Размещено 0 USDT · свободно 10 000 USDT' in empty[0]
          and 'сделок нет' in empty[1])
    check('plan_parts: five requested says that STRONG is at most three', 'больше 3 сделок не будет' in plan_parts(*(lambda r, c: (r, plan(r, c, 15000.0, 5, 0.5, {})))(*scenario([('ETH', 1, 3.0, 8.0, True)])))[0])

    class Cap(Telegram):
        def __init__(self, down=False):
            super().__init__('123456:SECRET', 777)
            self.texts, self.down = [], down

        def call(self, method, http_timeout=30, **params):
            if self.down:
                raise RuntimeError('telegram sendMessage: 502 Bad Gateway')
            self.texts.append(params['text'])
            return {'message_id': len(self.texts)}

    class Stub:
        pass

    stub = Stub()
    stub.cs = stage

    def fake_make(data, deposit, risk):
        return fr, 'PLAIN MESSAGE'

    def no_binance(data, deposit, risk):
        raise RuntimeError('fapi.binance.com served no candles')

    state = tempfile.mkdtemp(prefix='.selftest-', dir=os.path.dirname(os.path.abspath(__file__)))
    saved = (globals()['make'], globals()['STATE'], globals()['liquidity'])
    globals()['make'], globals()['STATE'], globals()['liquidity'] = fake_make, state, lambda coin, now_ms: 1e9
    try:
        cap = Cap()
        with contextlib.redirect_stdout(io.StringIO()):
            handle(cap, stub, 'сигнал 10000 топ 3')
            n1 = len(cap.texts)
            handle(cap, stub, 'сигнал')
            n2 = len(cap.texts)
            handle(cap, stub, 'сигнал 10000')
            n3 = len(cap.texts)
            handle(cap, stub, 'привет')
            records = [json.loads(line) for line in open(os.path.join(state, 'journal.jsonl'), encoding='utf-8')]
            globals()['make'] = no_binance
            handle(cap, stub, 'сигнал 10000 топ 3')
            handle(Cap(down=True), stub, 'сигнал')
        check('handle: «сигнал 10000 топ 3» answers with the allocation in two messages', n1 == 2 and 'распределение капитала' in cap.texts[0] and 'Оценка доверия' in cap.texts[1])
        check('handle: «сигнал» answers with the plain message and «сигнал 10000» as «сигнал 10000 топ 3»', cap.texts[n1] == 'PLAIN MESSAGE'
              and n3 - n2 == 2 and cap.texts[n2] == cap.texts[0])
        check('handle: an unknown text gets HELP and no record', cap.texts[n3] == HELP and len(records) == 3)
        check('handle: the journal holds an allocation record with its figures and a plain request record, each of its kind',
              [r['kind'] for r in records] == ['alloc', 'request', 'alloc'] and records[0]['alloc']['allocated'] == pf['allocated']
              and records[0]['alloc']['items'][0]['coin'] == 'ETH' and records[0]['alloc']['budget'] == 10000.0 and 'alloc' not in records[1])
        check('handle: Binance down gets the apology, Telegram down raises nothing', cap.texts[-1].startswith('Binance или Telegram не ответили'))
    finally:
        globals()['make'], globals()['STATE'], globals()['liquidity'] = saved
        shutil.rmtree(state)
    check('glibc takes its two settings', malloc_tune())
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
