#!/usr/bin/env python3
# adv3.py - ADV-3, the Boss's advisor for Binance Futures (CANON PART VII). Standard library only.
# Rule text RULE-ADV-3, SHA-256 ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169, frozen
# 2026-10-28 16:14 UTC before any of its results was computed: ADV-1's rule on the Boss's perpetuals' own
# candles, with a strength ranking (TOP-3, STRONG) whose claim has its own gate. Candles and funding come from
# Binance's archive (data.binance.vision) or live from fapi.binance.com; both give the same closed candles.
# Modes: the message of the latest close (--source fapi, the default, or archive; --json for the report);
# --history PATH, Gate H, Gate S and the display facts re-derived from the archive and read against FACTS (G-HISTORY);
# --compare, the archive's last 14 daily candles against fapi.binance.com's (G-SAME). The bot imports this file.
import argparse, bisect, datetime as dt, hashlib, html, io, json, math, statistics, sys, time, urllib.error, \
    urllib.parse, urllib.request, zipfile
from concurrent.futures import ThreadPoolExecutor

RULE = 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169'
COINS = ('BTC', 'BCH', 'SKY', 'XLM', 'XMR', 'MORPHO', 'LIT', 'NEAR', 'HBAR', 'GRAM', 'ENA', 'UNI', 'ARB', 'ZEC',
         'HYPE', 'SUI', 'ADA', 'RENDER', 'TAO', 'FET', 'YFI', 'XRP', 'SOL', 'ONDO', 'LINK', 'ALGO', 'TRX', 'BNB',
         'AAVE', 'AVAX', 'ETH', 'INJ', 'LTC', 'XAU', 'DASH', 'PYTH', 'WLD', 'BTW', 'QNT', 'PUMP', 'VVV', 'EGLD')
LOOKBACKS, ATR_DAYS, STOP_N, COST, BASE_F, VOL_DAYS = (14, 28, 56, 112), 20, 2.0, 0.001, 0.0001, 56
TOP_N, STRONG_Z, STRONG_MAX, ZONE, NEAR_STOP = 3, 1.0, 3, 0.25, 0.25
HISTORY_TO, FORWARD_FROM, ARCHIVE_FROM = dt.date(2026, 10, 27), dt.date(2026, 10, 28), dt.date(2019, 9, 1)
FUNDING_TO = (2026, 9)   # the archive's monthly funding files as published at the freeze, 2026-10-28
DEPOSIT, RISK, RISK_MAX, RISK_ALL = 10000.0, 0.5, 1.0, 5.0
UA = {'User-Agent': 'adv3-advisor/1'}
ARCH = 'https://data.binance.vision/data/futures/um/'
FAPI = 'https://fapi.binance.com'
DAY = dt.timedelta(days=1)
# Gate H, Gate S and the display facts, read once on the history to the close of 2026-10-27 (RULE-ADV-3)
FACTS = {'base': {'trades': 5265, 'wins': 1708, 'mean_R': 0.1576, 'median_days': 3, 'gate_H': 'NOT DISQUALIFIED',
                  'mfe': {1: 0.2325, 2: 0.1297, 3: 0.0819}},
         'strong': {'trades': 253, 'wins': 83, 'mean_R': 0.5473, 'median_days': 19, 'gate_S': 'NOT DISQUALIFIED',
                    'mfe': {1: 0.4783, 2: 0.2846, 3: 0.1779}}}


# ---- fetching ----------------------------------------------------------------------------------------------

def get(url, tries=4):
    """The body of url, or None where the server answers 404. A network error, 418, 429 or 5xx is tried again
    after 1, 3 and 5 s; any other answer raises at once."""
    err = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (418, 429) and e.code < 500:
                raise RuntimeError(f'FETCH REFUSED {url}: HTTP {e.code}') from None
            err = e
        except OSError as e:
            err = e
        if k + 1 < tries:
            time.sleep(1 + 2 * k)
    raise RuntimeError(f'FETCH FAILED {url}: {err!r}')


def months(a, b):
    y, m = a.year, a.month
    while (y, m) <= (b.year, b.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def zip_rows(body):
    z = zipfile.ZipFile(io.BytesIO(body))
    rows = [line.split(',') for line in z.read(z.namelist()[0]).decode().splitlines()]
    return [p for p in rows if p[0].strip().isdigit()]


def ms_day(ms):
    ms = int(ms)
    ms = ms // 1000 if ms > 10 ** 14 else ms
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).date()


def holding_day(ms):
    """The day whose (open, close] holds a settlement at ms."""
    ms = int(ms)
    ms = ms // 1000 if ms > 10 ** 14 else ms
    return (dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc) - dt.timedelta(milliseconds=1)).date()


def archive_candles(sym, last_day, pool, first=ARCHIVE_FROM):
    """The perpetual's closed daily candles from first's month to last_day from the archive: monthly files, then
    daily files for the months whose monthly file is not out yet."""
    ms = list(months(first, last_day))
    url_m = lambda ym: f'{ARCH}monthly/klines/{sym}/1d/{sym}-1d-{ym[0]:04d}-{ym[1]:02d}.zip'
    got = dict(zip(ms, pool.map(lambda ym: get(url_m(ym)), ms)))
    out = {}
    for ym, body in got.items():
        if body is not None:
            for p in zip_rows(body):
                out[ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
    first_seen = min(out) if out else None
    missing = [ym for ym, body in got.items() if body is None and (first_seen is None or ym >= (first_seen.year, first_seen.month))]
    days = [d for ym in missing for d in (dt.date(ym[0], ym[1], k) for k in range(1, 32) if _valid(ym, k)) if d <= last_day]
    url_d = lambda d: f'{ARCH}daily/klines/{sym}/1d/{sym}-1d-{d.isoformat()}.zip'
    for d, body in zip(days, pool.map(lambda d: get(url_d(d)), days)):
        if body is not None:
            for p in zip_rows(body):
                out[ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
    return {d: v for d, v in out.items() if d <= last_day}


def _valid(ym, k):
    try:
        dt.date(ym[0], ym[1], k)
        return True
    except ValueError:
        return False


def archive_funding(sym, first, last, pool):
    """{holding day: sum of the perpetual's settlements} from the archive's monthly files, and the covered months."""
    ms = list(months(max(first, ARCHIVE_FROM), last))
    url = lambda ym: f'{ARCH}monthly/fundingRate/{sym}/{sym}-fundingRate-{ym[0]:04d}-{ym[1]:02d}.zip'
    per_day, covered = {}, set()
    for ym, body in zip(ms, pool.map(lambda ym: get(url(ym)), ms)):
        if body is not None:
            covered.add(ym)
            for p in zip_rows(body):
                d = holding_day(p[0])
                per_day[d] = per_day.get(d, 0.0) + float(p[2])
    return per_day, covered


def fapi(path, **params):
    return json.loads(get(f'{FAPI}{path}?{urllib.parse.urlencode(params)}' if params else f'{FAPI}{path}'))


def fapi_candles(sym, now_ms):
    """The perpetual's closed daily candles from fapi.binance.com, the last 1,500 days."""
    out = {}
    for r in fapi('/fapi/v1/klines', symbol=sym, interval='1d', limit=1500):
        if int(r[6]) < now_ms:
            out[ms_day(r[0])] = (float(r[1]), float(r[2]), float(r[3]), float(r[4]))
    return out


def fapi_funding(sym, first):
    """{holding day: sum of settlements} from fapi.binance.com since first, page after page of 1,000."""
    start = int(dt.datetime(first.year, first.month, first.day, tzinfo=dt.timezone.utc).timestamp() * 1000)
    per_day = {}
    for _ in range(100):
        rows = fapi('/fapi/v1/fundingRate', symbol=sym, startTime=start, limit=1000)
        for r in rows:
            d = holding_day(r['fundingTime'])
            per_day[d] = per_day.get(d, 0.0) + float(r['fundingRate'])
        if len(rows) < 1000:
            break
        start = int(rows[-1]['fundingTime']) + 1
    return per_day


def fapi_intervals():
    """{symbol: funding interval in hours} for the perpetuals whose interval Binance has adjusted; 8 h elsewhere."""
    return {r['symbol']: int(r['fundingIntervalHours']) for r in fapi('/fapi/v1/fundingInfo')}


def fapi_marks():
    """{symbol: (mark price, last funding rate)} for every perpetual, from fapi.binance.com."""
    return {r['symbol']: (float(r['markPrice']), float(r['lastFundingRate'])) for r in fapi('/fapi/v1/premiumIndex')}


# ---- the rule ----------------------------------------------------------------------------------------------

def signs(days, closes, i):
    """The four signs of the close against the closes 14, 28, 56 and 112 days before; None before they exist."""
    out = []
    for L in LOOKBACKS:
        j = bisect.bisect_right(days, days[i] - L * DAY) - 1
        if j < 0:
            return None
        out.append(((closes[i] > closes[j]) - (closes[i] < closes[j]), j, L))
    return out


def signal(days, closes, i):
    """+1 LONG, -1 SHORT, 0 FLAT at the close of days[i]; None before the longest lookback exists."""
    s = signs(days, closes, i)
    if s is None:
        return None
    t = sum(x for x, _, _ in s)
    return 1 if t >= 2 else -1 if t <= -2 else 0


def strength(days, closes, i):
    """(z, sum of the four signs) at the close of days[i]; None before both exist."""
    s = signs(days, closes, i)
    if s is None or i < VOL_DAYS:
        return None
    rets = [math.log(closes[k] / closes[k - 1]) for k in range(i - VOL_DAYS + 1, i + 1)]
    sd = statistics.stdev(rets)
    if sd <= 0:
        return None
    z = sum(math.log(closes[i] / closes[j]) / (sd * math.sqrt(L)) for _, j, L in s) / len(s)
    return z, sum(x for x, _, _ in s)


def true_range(c, days, i):
    h, l, pc = c[days[i]][1], c[days[i]][2], c[days[i - 1]][3]
    return max(h, pc) - min(l, pc)


def unit(c, days, i):
    """U = 2 N at the close of days[i]: twice the mean true range of the last 20 days; None before them."""
    if i < ATR_DAYS:
        return None
    return STOP_N * sum(true_range(c, days, j) for j in range(i - ATR_DAYS + 1, i + 1)) / ATR_DAYS


def open_at(side, close, U, day):
    return {'d': side, 'E': close, 'U': U, 'S': close - side * U, 'entry': day, 'R': -COST * close / U, 'mfe': 0.0}


def hold(pos, candle, pc, fund_d, day):
    """One day of an open position: its R for the day, and whether its stop closed it."""
    o, h, l, cl = candle
    k, U, S = pos['d'], pos['U'], pos['S']
    if (l <= S) if k > 0 else (h >= S):
        X = o if ((o <= S) if k > 0 else (o >= S)) else S
        r = (k * (X - pc) - COST * X) / U
        pos.update(R=pos['R'] + r, X=X, exit=day, why='stop')
        return r, True
    r = (k * (cl - pc) - k * fund_d * cl) / U
    pos['R'] += r
    pos['mfe'] = max(pos['mfe'], k * ((h if k > 0 else l) - pos['E']) / U)
    return r, False


def close_at(pos, close, day):
    x = -COST * close / pos['U']
    pos.update(R=pos['R'] + x, X=close, exit=day, why='signal')
    return x


def simulate(c, fund, first_entry, last_day):
    """The rule on one pair. Returns (closed trades, {day: R}, open position or None)."""
    days = sorted(d for d in c if d <= last_day)
    closes = [c[d][3] for d in days]
    trades, daily, pos = [], {}, None
    for i, d in enumerate(days):
        r = 0.0
        if i and pos:
            dr, stopped = hold(pos, c[d], closes[i - 1], fund(d), d)
            r += dr
            if stopped:
                trades.append(pos)
                pos = None
        sig = signal(days, closes, i)
        if pos and sig != pos['d']:
            r += close_at(pos, closes[i], d)
            trades.append(pos)
            pos = None
        U = unit(c, days, i) if pos is None and sig in (1, -1) and d >= first_entry else None
        if U:
            pos = open_at(sig, closes[i], U, d)
            r += pos['R']
        if d >= first_entry:
            daily[d] = r
    return trades, daily, pos


def states(c, last_day, since=None):
    """{day: (signal, z, sum of signs, U, close)} for every closed day of one pair to last_day; before since, the
    close alone, (None, None, None, None, close), which no ranking admits."""
    days = sorted(d for d in c if d <= last_day)
    closes = [c[d][3] for d in days]
    out = {}
    for i, d in enumerate(days):
        if since is not None and d < since:
            out[d] = (None, None, None, None, closes[i])
            continue
        st = strength(days, closes, i)
        out[d] = (signal(days, closes, i), st[0] if st else None, st[1] if st else None, unit(c, days, i), closes[i])
    return out


def ranking(day_states):
    """TOP-3 and STRONG for one close: day_states is [(coin, (signal, z, sum, U, close))] in universe order."""
    active = [(coin, s) for coin, s in day_states if s[0] in (1, -1) and s[1] is not None and s[3]]
    top = sorted(active, key=lambda cs: -abs(cs[1][1]))[:TOP_N]
    strong = [coin for coin, s in top if s[2] == 4 * s[0] and abs(s[1]) >= STRONG_Z]
    return [coin for coin, _ in top], strong


def simulate_strong(cs, st, funds, first_entry, last_day):
    """The STRONG strategy over all pairs: returns (closed trades, {day: R}, open trades)."""
    all_days = sorted({d for coin in cs for d in cs[coin] if d <= last_day})
    prev = {}
    trades, daily, open_ = [], {}, {}
    for d in all_days:
        r = 0.0
        for coin in list(open_):
            if d in cs[coin] and coin in prev:
                dr, stopped = hold(open_[coin], cs[coin][d], prev[coin], funds[coin](d), d)
                r += dr
                if stopped:
                    trades.append(open_.pop(coin))
        today = [(coin, st[coin][d]) for coin in COINS if coin in cs and d in st[coin]]
        for coin, s in today:
            if coin in open_ and s[0] != open_[coin]['d']:
                r += close_at(open_[coin], s[4], d)
                trades.append(open_.pop(coin))
        if d >= first_entry:
            _, strong = ranking(today)
            sd = dict(today)
            for coin in strong:
                if coin not in open_ and len(open_) < STRONG_MAX:
                    s = sd[coin]
                    open_[coin] = open_at(s[0], s[4], s[3], d)
                    open_[coin]['coin'] = coin
                    r += open_[coin]['R']
            daily[d] = r
        for coin, s in today:
            prev[coin] = s[4]
    return trades, daily, open_


def stats(trades, daily):
    R = [t['R'] for t in trades]
    out = {'trades': len(R), 'wins': sum(x > 0 for x in R), 'total_R': sum(R),
           'mean_R': sum(R) / len(R) if R else 0.0, 'days': len(daily)}
    held = [(t['exit'] - t['entry']).days for t in trades if 'exit' in t]
    if held:
        out['median_days'] = statistics.median(held)
    if R:
        out['mfe'] = {k: sum(t['mfe'] >= k for t in trades) / len(trades) for k in (1, 2, 3)}
    xs = [daily[d] for d in sorted(daily)]
    if len(xs) > 1:
        m = sum(xs) / len(xs)
        sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
        run = peak = dd = 0.0
        for x in xs:
            run += x
            peak = max(peak, run)
            dd = min(dd, run - peak)
        t = m / sd * math.sqrt(len(xs)) if sd > 0 else 0.0
        out.update(sharpe=m / sd * math.sqrt(365) if sd > 0 else 0.0, t=t,
                   p_up=0.5 * math.erfc(t / math.sqrt(2)), max_dd_R=dd)
    return out


def funding_of(per_day, covered_days):
    """The rule's funding by day: the published sum where the source covers the day, else the base rate."""
    return lambda d: per_day.get(d, 0.0) if covered_days(d) else 3 * BASE_F


# ---- the history and the gates -----------------------------------------------------------------------------

def history():
    """Gate H, Gate S and the display facts on the archive's history to the close of HISTORY_TO."""
    with ThreadPoolExecutor(16) as pool:
        cs = {coin: archive_candles(coin + 'USDT', HISTORY_TO, pool) for coin in COINS}
        funds = {}
        for coin in COINS:
            if not cs[coin]:
                continue
            first = min(cs[coin])
            per_day, covered = archive_funding(coin + 'USDT', first, HISTORY_TO, pool)
            covered = {ym for ym in covered if ym <= FUNDING_TO}
            per_day = {d: x for d, x in per_day.items() if (d.year, d.month) in covered}
            settled = [d for d in per_day]
            first_settle = min(settled) if settled else None
            funds[coin] = funding_of(per_day, lambda d, fs=first_settle, cv=covered:
                                     fs is not None and d >= fs and (d.year, d.month) in cv)
    cs = {k: v for k, v in cs.items() if v}
    base_trades, base_daily, per_coin = [], {}, {}
    for coin, c in cs.items():
        days = sorted(c)
        th, dh, ph = simulate(c, funds[coin], days[0], HISTORY_TO)
        if ph:
            th = th + [dict(ph, R=ph['R'] - COST * c[days[-1]][3] / ph['U'], why='open at the history cut')]
        for t in th:
            t['coin'] = coin
        base_trades += th
        for d, x in dh.items():
            base_daily[d] = base_daily.get(d, 0.0) + x
        per_coin[coin] = stats(th, dh) | {'from': str(days[0]), 'days_of_candles': len(days)}
    st = {coin: states(c, HISTORY_TO) for coin, c in cs.items()}
    s_trades, s_daily, s_open = simulate_strong(cs, st, funds, min(min(c) for c in cs.values()), HISTORY_TO)
    for coin, t in s_open.items():
        last = max(d for d in cs[coin] if d <= HISTORY_TO)
        s_trades.append(dict(t, R=t['R'] - COST * cs[coin][last][3] / t['U'], why='open at the history cut'))
    base, strong = stats(base_trades, base_daily), stats(s_trades, s_daily)
    base['gate_H'] = 'NOT DISQUALIFIED' if base['total_R'] > 0 else 'DISQUALIFIED'
    strong['gate_S'] = ('NOT DISQUALIFIED' if strong['total_R'] > 0 and strong['mean_R'] > base['mean_R']
                        else 'DISQUALIFIED')
    return {'rule': RULE, 'to_close_of': str(HISTORY_TO), 'base': base, 'strong': strong, 'per_coin': per_coin}


# ---- live: the signals of the latest close -----------------------------------------------------------------

def report(cs, funds, marks, deposit, risk, now_ms, missing=(), intervals=None):
    """Everything the Boss's message needs, from closed candles, funding and mark prices; missing names the coins
    whose candles the source did not serve, and intervals the funding periods (None where unread)."""
    risk = min(risk, RISK_MAX)
    last = max(max(c) for c in cs.values() if c)
    st = {coin: states(c, last, min(FORWARD_FROM, last) - DAY) for coin, c in cs.items() if c}
    today = [(coin, st[coin][last]) for coin in COINS if coin in st and last in st[coin]]
    top, strong = ranking(today)
    rows = {}
    for coin, s in today:
        c = cs[coin]
        days = sorted(c)
        _, _, pos = simulate(c, funds.get(coin, lambda d: 3 * BASE_F), days[0], last)
        prev = st[coin].get(days[-2]) if len(days) > 1 else None
        rows[coin] = {'signal': s[0], 'z': s[1], 'sum': s[2], 'U': s[3], 'close': s[4],
                      'prev': prev[0] if prev else None,
                      'since': str(pos['entry']) if pos else None, 'stop': pos['S'] if pos else None,
                      'mark': marks.get(coin + 'USDT', (None, None))[0],
                      'funding': marks.get(coin + 'USDT', (None, None))[1],
                      'funding_h': None if intervals is None else intervals.get(coin + 'USDT', 8)}
    for coin in COINS:
        if coin not in rows:
            rows[coin] = {'signal': None, 'missing': coin in missing}
    s_trades, s_daily, s_open = simulate_strong({k: v for k, v in cs.items() if v}, st, funds, FORWARD_FROM, last)
    b_trades, b_daily = [], {}
    for coin, c in cs.items():
        if not c:
            continue
        tf, df, _ = simulate(c, funds.get(coin, lambda d: 3 * BASE_F), FORWARD_FROM, last)
        b_trades += tf
        for d, x in df.items():
            b_daily[d] = b_daily.get(d, 0.0) + x
    cards = [card(coin, rows[coin], coin in strong, deposit, risk) for coin in top]
    return {'rule': RULE, 'close_of': str(last), 'deposit': deposit, 'risk_pct': risk, 'top': top, 'strong': strong,
            'cards': cards, 'rows': rows, 'strong_open': {k: str(v['entry']) for k, v in s_open.items()},
            'forward': {'base': stats(b_trades, b_daily), 'strong': stats(s_trades, s_daily)},
            'missing': [c for c in COINS if c in missing], 'marks_ok': bool(marks), 'made_at_ms': now_ms}


def card(coin, row, is_strong, deposit, risk):
    """One TOP-3 trade entered at this close: entry, stop, targets, size and leverage by RULE-ADV-3's display rules."""
    k, C, U = row['signal'], row['close'], row['U']
    S = C - k * U
    P = row['mark'] if row['mark'] else C
    lo, hi = C - ZONE * U, C + ZONE * U
    if k > 0:
        mode, entry = (('limit', hi) if P > hi else ('market', P) if P > S + NEAR_STOP * U else ('none', None))
    else:
        mode, entry = (('limit', lo) if P < lo else ('market', P) if P < S - NEAR_STOP * U else ('none', None))
    out = {'coin': coin, 'side': k, 'strong': is_strong, 'z': row['z'], 'close': C, 'U': U, 'stop': S, 'mark': P,
           'zone': (lo, hi), 'mode': mode, 'entry': entry, 'since': row['since'], 'funding': row['funding'],
           'funding_h': row.get('funding_h'),
           'targets': [C + k * n * U for n in (1, 2, 3)]}
    if entry is not None:
        dist = abs(entry - S)
        qty = risk / 100 * deposit / dist
        out.update(qty=qty, notional=qty * entry, stop_pct=100 * dist / entry,
                   leverage=min(20, math.floor(1 / (1.5 * dist / entry + 0.01))))
    return out


# ---- the message -------------------------------------------------------------------------------------------

def num(x, sig=3):
    """x to sig significant digits, Russian style: thin-free spaces between thousands, a decimal comma."""
    if x == 0:
        return '0'
    digits = max(0, sig - 1 - math.floor(math.log10(abs(x))))
    s = f'{x:,.{digits}f}'
    if digits:
        s = s.rstrip('0').rstrip('.')
    return s.replace(',', ' ').replace('.', ',').replace('-', '−')


def price(x):
    return num(x, 5)


def usdt(x):
    return f'{round(x):,}'.replace(',', ' ') if x >= 100 else num(x, 3)


def plural(n, one, few, many):
    if n % 10 == 1 and n % 100 != 11:
        return one
    return few if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else many


def pct(x, places=1):
    return f'{x:.{places}f}'.replace('.', ',').replace('-', '−')


def ddmm(day):
    return f'{day[8:10]}.{day[5:7]}'


def message(rep, facts):
    """The Boss's message in Russian, as Telegram HTML, from the report and the frozen history facts."""
    e = html.escape
    last = dt.date.fromisoformat(rep['close_of'])
    until = last + 2 * DAY
    lines = ['📊 <b>ADV-3 · сигналы Binance Futures</b>',
             f"Закрытие дня {ddmm(rep['close_of'])} (UTC)",
             f"⏱ Действует до 04:00 {until:%d.%m} по Батуми — до следующего закрытия",
             f"Депозит {num(rep['deposit'], 6)} USDT · риск {pct(rep['risk_pct'])}% = "
             f"{num(rep['deposit'] * rep['risk_pct'] / 100, 4)} USDT на сделку · все сделки вместе ≤ {pct(RISK_ALL, 0)}%"]
    if not rep.get('marks_ok', True):
        lines.append('⚠️ Текущие цены Binance недоступны: вход посчитан от цены закрытия')
    lines.append('')
    rows = rep['rows']
    word = {1: 'ЛОНГ', -1: 'ШОРТ'}
    new, out_long, out_short, flips = [], [], [], []
    for coin in COINS:
        now, before = rows[coin].get('signal'), rows[coin].get('prev')
        if now in word and before not in word:
            new.append(f'{coin} {word[now]}')
        elif now not in word and before in word:
            (out_long if before > 0 else out_short).append(coin)
        elif now in word and before in word and now != before:
            flips.append(f'{coin} в {word[now]}')
    lines.append('<b>Изменения за день</b>')
    if new:
        lines.append('🆕 Новые: ' + ', '.join(new))
    if out_long or out_short:
        parts = ([', '.join(out_long) + ' из лонга'] if out_long else []) + ([', '.join(out_short) + ' из шорта']
                                                                           if out_short else [])
        lines.append('🚪 Выход: ' + ' · '.join(parts))
    if flips:
        lines.append('🔄 Разворот: ' + ', '.join(flips))
    if not (new or out_long or out_short or flips):
        lines.append('Изменений нет.')
    lines.append('')
    if rep['cards']:
        lines.append('<b>ТОП-3 по силе тренда</b>')
        for cd in rep['cards']:
            lines += [''] + card_lines(cd, facts)
    else:
        lines.append('<b>Открытых сигналов нет</b> — все монеты вне рынка.')
    if rep['strong_open']:
        held = ', '.join(f'{k} с {ddmm(v)}' for k, v in rep['strong_open'].items())
        lines += ['', f'<b>Открытые STRONG-сделки правила:</b> {e(held)}']
    longs = [c for c in COINS if rows[c].get('signal') == 1 and c not in rep['top']]
    shorts = [c for c in COINS if rows[c].get('signal') == -1 and c not in rep['top']]
    flat = [c for c in COINS if rows[c].get('signal') == 0]
    young = [c for c in COINS if rows[c].get('signal') is None and not rows[c].get('missing')]
    lost = [c for c in COINS if rows[c].get('missing')]
    lines += ['', '<b>Остальные сигналы</b>']
    if longs:
        lines.append('🟢 ЛОНГ: ' + ', '.join(longs))
    if shorts:
        lines.append('🔴 ШОРТ: ' + ', '.join(shorts))
    lines.append(f'⚪ Вне рынка: {len(flat)} {plural(len(flat), "монета", "монеты", "монет")}')
    if young:
        lines.append('⏳ Мало истории для сигнала: ' + ', '.join(young))
    if lost:
        lines.append('⚠️ Binance не отдал данные: ' + ', '.join(lost))
    lines += ['', '<b>Уверенность</b> — история 2020–2026, не доказательство']
    if facts:
        s, b = facts['strong'], facts['base']
        if s.get('gate_S') == 'NOT DISQUALIFIED':
            lines.append(f"STRONG: {pct(100 * s['wins'] / s['trades'], 0)}% сделок в плюс, в среднем "
                         f"{'+' if s['mean_R'] > 0 else ''}{pct(s['mean_R'], 2)} R, держатся ~{s['median_days']:.0f} дн.")
        lines.append(f"Все сигналы: {pct(100 * b['wins'] / b['trades'], 0)}% в плюс, в среднем "
                     f"{'+' if b['mean_R'] > 0 else ''}{pct(b['mean_R'], 2)} R, держатся ~{b['median_days']:.0f} дн.")
        lines.append('Прибыль дают редкие длинные тренды; большинство сделок закрывается небольшим убытком.')
    fb, fs = rep['forward']['base'], rep['forward']['strong']
    if fb['days']:
        lines.append(f"Форвард с 28.10: {fb['days']} дн. · все сигналы {num(fb['total_R'], 3)} R · STRONG "
                     f"{num(fs['total_R'], 3)} R. Доказанность проверяется после 28.10.2027.")
    else:
        lines.append('Форвард начинается с закрытия 28.10; доказанность проверяется после 28.10.2027.')
    lines += ['', '<i>«Дошли» — доля прошлых сделок того же класса (★ STRONG или обычных), цена которых дошла до '
              'цели до выхода. R — результат в единицах риска сделки: −1 R — сработал стоп. Не инвестиционный '
              'совет: правило показывает состояние рынка; решение и риск — ваши.</i>']
    return '\n'.join(lines)


def card_lines(cd, facts):
    """One TOP-3 card: a line each for entry, stop, the three targets with their measured shares, and size."""
    side = 'LONG' if cd['side'] > 0 else 'SHORT'
    dot = '🟢' if cd['side'] > 0 else '🔴'
    out = [f"{dot} <b>{cd['coin']} · {side}</b>" + (' · ★ STRONG' if cd['strong'] else '')]
    lo, hi = cd['zone']
    if cd['mode'] == 'market':
        out += [f"Вход: <b>по рынку</b> ≈ {price(cd['entry'])}", f"   зона входа {price(lo)}–{price(hi)}"]
    elif cd['mode'] == 'limit':
        out += [f"Вход: <b>лимит {price(cd['entry'])}</b> — ждать отката", f"   цена {price(cd['mark'])} ушла от зоны, не догонять"]
    else:
        out += ['Вход: <b>не входить</b> — цена у стопа', f"   цена {price(cd['mark'])}"]
    ref = cd['entry'] if cd['entry'] is not None else cd['close']
    stop_pct = 100 * abs(ref - cd['stop']) / ref
    out.append(f"⛔ Стоп: <b>{price(cd['stop'])}</b> ({'−' if cd['side'] > 0 else '+'}{pct(stop_pct)}%)")
    shares, whose = None, ''
    if facts:
        use_strong = cd['strong'] and facts['strong'].get('gate_S') == 'NOT DISQUALIFIED'
        shares = (facts['strong'] if use_strong else facts['base']).get('mfe')
    for n, t in zip((1, 2, 3), cd['targets']):
        move = 100 * (t - ref) / ref
        share = f' · дошли {pct(100 * shares[n], 0)}%' if shares else ''
        out.append(f"🎯 {price(t)} ({'+' if move > 0 else ''}{pct(move)}%){share}")
    if cd['entry'] is not None:
        out.append(f"Объём: {num(cd['qty'])} {cd['coin']} ≈ {usdt(cd['notional'])} USDT · плечо ≤ {cd['leverage']}× изол.")
    extra = []
    if cd['since']:
        extra.append(f"Сигнал с {ddmm(cd['since'])}")
    if cd['funding'] is not None:
        period = f"/{cd['funding_h']} ч" if cd.get('funding_h') else ' за период'
        extra.append(f"фандинг {'+' if cd['funding'] >= 0 else ''}{pct(100 * cd['funding'], 3)}%{period}")
    if extra:
        out.append(' · '.join(extra))
    return out


# ---- command line ------------------------------------------------------------------------------------------

def live(source, deposit, risk):
    """The report of the latest close, from the archive or fapi.binance.com."""
    now_ms = int(time.time() * 1000)
    with ThreadPoolExecutor(16) as pool:
        if source == 'fapi':
            cs = dict(zip(COINS, pool.map(lambda k: fapi_candles(k + 'USDT', now_ms), COINS)))
            fs = dict(zip(COINS, pool.map(lambda k: fapi_funding(k + 'USDT', FORWARD_FROM - DAY), COINS)))
            funds = {k: funding_of(v, lambda d: d >= FORWARD_FROM) for k, v in fs.items()}
            marks, intervals = fapi_marks(), fapi_intervals()
        else:
            today = dt.datetime.now(dt.timezone.utc).date()
            cs = {k: archive_candles(k + 'USDT', today - DAY, pool) for k in COINS}
            funds, marks, intervals = {}, {}, None
    return report(cs, funds, marks, deposit, risk, now_ms, (), intervals)


def facts_checks(h):
    """G-HISTORY: each frozen fact against the history just derived - counts and verdicts exact, shares and mean R
    at FACTS' four decimals. {name: (equal, derived, FACTS)}."""
    out = {}
    for k in ('base', 'strong'):
        f, x = FACTS[k], h[k]
        out[f'{k} trades'] = (x['trades'] == f['trades'], x['trades'], f['trades'])
        out[f'{k} wins'] = (x['wins'] == f['wins'], x['wins'], f['wins'])
        out[f'{k} mean R'] = (round(x['mean_R'], 4) == f['mean_R'], x['mean_R'], f['mean_R'])
        out[f'{k} median days'] = (x['median_days'] == f['median_days'], x['median_days'], f['median_days'])
        for n in (1, 2, 3):
            out[f'{k} share +{n}R'] = (round(x['mfe'][n], 4) == f['mfe'][n], x['mfe'][n], f['mfe'][n])
    out['gate H'] = (h['base']['gate_H'] == FACTS['base']['gate_H'], h['base']['gate_H'], FACTS['base']['gate_H'])
    out['gate S'] = (h['strong']['gate_S'] == FACTS['strong']['gate_S'], h['strong']['gate_S'],
                     FACTS['strong']['gate_S'])
    return out


def compare(days_back=14):
    """G-SAME: for every coin, the archive's daily file and fapi.binance.com's candle of each of the last days_back
    closed days, compared field by field where both exist. Returns ([(coin, compared, archive files absent)],
    [mismatching (coin, day, archive, fapi)])."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    days = [today - k * DAY for k in range(days_back, 0, -1)]
    url = lambda sym, d: f'{ARCH}daily/klines/{sym}/1d/{sym}-1d-{d.isoformat()}.zip'
    rows, bad = [], []
    with ThreadPoolExecutor(8) as pool:
        for coin in COINS:
            sym = coin + 'USDT'
            live_c = fapi_candles(sym, now_ms)
            n = absent = 0
            for d, body in zip(days, pool.map(lambda d: get(url(sym, d)), days)):
                if body is None:
                    absent += 1
                    continue
                for p in zip_rows(body):
                    day, arch = ms_day(p[0]), (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
                    n += 1
                    if day != d or live_c.get(day) != arch:
                        bad.append((coin, str(day), arch, live_c.get(day)))
            rows.append((coin, n, absent))
    return rows, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--history', metavar='PATH', help='Gate H, Gate S and the display facts as JSON to PATH, '
                    'then G-HISTORY: each fact read against FACTS')
    ap.add_argument('--compare', action='store_true', help='G-SAME: the archive against fapi.binance.com')
    ap.add_argument('--source', choices=('fapi', 'archive'), default='fapi')
    ap.add_argument('--json', action='store_true', help='print the report instead of the message')
    ap.add_argument('--deposit', type=float, default=DEPOSIT)
    ap.add_argument('--risk', type=float, default=RISK)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if a.history:
        h = history()
        text = json.dumps(h, indent=1, default=str) + '\n'
        with open(a.history, 'x', encoding='utf-8') as f:
            f.write(text)
        print('history written:', a.history, len(text.encode()), 'bytes, SHA-256',
              hashlib.sha256(text.encode()).hexdigest())
        checks = facts_checks(h)
        for k, (ok, got, want) in checks.items():
            print(f'G-HISTORY {k:<20} {got!s:<22} FACTS {want!s:<10} {"equal" if ok else "DIFFERENT"}')
        for k in ('base', 'strong'):
            x = h[k]
            print(f"printed, gating nothing: {k} total {x['total_R']:.4f} R, Sharpe {x['sharpe']:.4f}, t {x['t']:.4f}, "
                  f"p {x['p_up']:.6f}, worst drawdown {x['max_dd_R']:.4f} R")
        n = sum(ok for ok, _, _ in checks.values())
        print(f"READING G-HISTORY: {'PASS' if n == len(checks) else 'FAIL'} - {n} of {len(checks)} equal")
        sys.exit(0 if n == len(checks) else 1)
    if a.compare:
        rows, bad = compare()
        print('G-SAME per coin, candles compared / archive files absent:',
              ' '.join(f'{coin} {k}/{m}' for coin, k, m in rows))
        for b in bad:
            print('MISMATCH', *b)
        least = min(k for _, k, _ in rows)
        verdict = 'FAIL' if bad else 'PASS' if least >= 12 else 'UNDECIDABLE'
        print(f'READING G-SAME: {verdict} - {len(rows)} coins, {sum(k for _, k, _ in rows)} candles compared, '
              f'the least {least} for one coin, {len(bad)} mismatches')
        sys.exit(0 if verdict == 'PASS' else 1)
    rep = live(a.source, a.deposit, a.risk)
    if a.json:
        json.dump(rep, sys.stdout, indent=1, default=str)
        print()
    else:
        print(message(rep, FACTS))


if __name__ == '__main__':
    main()
