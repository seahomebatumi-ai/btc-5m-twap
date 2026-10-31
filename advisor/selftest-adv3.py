#!/usr/bin/env python3
# selftest-adv3.py - the Architect's checks of adv3.py's mechanics on synthetic candles; no network.
# Every expectation is computed here by hand or by an independent formula, never by adv3.py itself.
import datetime as dt, importlib.util, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('adv3', os.path.join(HERE, 'adv3.py'))
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
CHECKS = []


def check(name, ok):
    CHECKS.append(name)
    assert ok, name


D0 = dt.date(2020, 1, 1)
DAY = dt.timedelta(days=1)

# 1. a rising line, stopped by a gap down at day 150, then flat: the trade, its R, the day's R and the excursion
c = {}
for i in range(200):
    cl = 100.0 + i
    c[D0 + i * DAY] = (cl - 1, cl + 1, cl - 2, cl)
c[D0 + 150 * DAY] = (150.0, 151.0, 140.0, 145.0)
for i in range(151, 200):
    c[D0 + i * DAY] = (145.0, 145.0, 145.0, 145.0)
trades, daily, pos = a.simulate(c, lambda d: 0.0003, D0, D0 + 199 * DAY)
t0 = trades[0]
check('entry at the first close with a 112-day lookback', t0['entry'] == D0 + 112 * DAY and t0['E'] == 212.0)
check('U = 2 x the mean true range of 20 days', abs(t0['U'] - 6.0) < 1e-12)
check('a gap through the stop exits at the open', t0['why'] == 'stop' and t0['X'] == 150.0
      and t0['exit'] == D0 + 150 * DAY)
# R: price move 150 - 212, costs 0.1% a side at 212 and 150, funding 0.03% a day on the closes held, in units of U
fund = 0.0003 * sum(212.0 + k for k in range(1, 38))
check('the trade R with costs and funding', abs(t0['R'] - (-62 - 0.001 * 362 - fund) / 6) < 1e-9)
check('the first held day R', abs(daily[D0 + 113 * DAY] - (1 - 0.0003 * 213) / 6) < 1e-12)
check('the excursion leaves out the stop day', abs(t0['mfe'] - (250 - 212) / 6) < 1e-12)
check('re-entry short on the stop day', pos['d'] == -1 and pos['entry'] == D0 + 150 * DAY and abs(pos['U'] - 16.6) < 1e-9)

# 2. the strength against an independent formula on a noisy rising series
random.seed(7)
c2, x = {}, 100.0
for i in range(300):
    x *= math.exp(0.004 + random.gauss(0, 0.02))
    c2[D0 + i * DAY] = (x, x * 1.01, x * 0.99, x)
days = sorted(c2)
closes = [c2[d][3] for d in days]
z, ssum = a.strength(days, closes, 299)
rets = [math.log(closes[k] / closes[k - 1]) for k in range(244, 300)]
m = sum(rets) / 56
sd = math.sqrt(sum((r - m) ** 2 for r in rets) / 55)
zz = sum(math.log(closes[299] / closes[299 - L]) / (sd * math.sqrt(L)) for L in (14, 28, 56, 112)) / 4
check('z equals the independent formula', abs(z - zz) < 1e-12)
check('the sum of signs is the four signs', ssum == sum((closes[299] > closes[299 - L]) - (closes[299] < closes[299 - L])
                                                      for L in (14, 28, 56, 112)))
check('no strength before 56 returns', a.strength(days, closes, 120) is not None and a.strength(days, closes, 55) is None)

# 3. the ranking: the three largest |z| among LONG and SHORT; STRONG needs four agreeing signs and |z| >= 1
st = [('A', (1, 2.0, 4, 1.0, 10.0)), ('B', (-1, -0.5, -4, 1.0, 10.0)), ('C', (1, 1.5, 2, 1.0, 10.0)),
      ('D', (0, 3.0, 0, 1.0, 10.0)), ('E', (-1, -1.2, -4, 1.0, 10.0))]
top, strong = a.ranking(st)
check('TOP-3 by |z|, FLAT left out', top == ['A', 'C', 'E'])
check('STRONG: four signs and |z| >= 1', strong == ['A', 'E'])

# 4. the card: zone C +/- 0.25U, the entry modes, the stop C -/+ U, size = 0.5% x 10,000 / |entry - stop|
row = {'signal': 1, 'close': 100.0, 'U': 8.0, 'stop': None, 'mark': 101.0, 'z': 2.0, 'since': '2026-10-20',
       'funding': 0.0001}
cd = a.card('A', row, True, 10000, 0.5)
check('LONG inside the zone: at market', cd['mode'] == 'market' and cd['stop'] == 92.0 and abs(cd['qty'] - 50 / 9.0) < 1e-12)
check('leverage floor(1 / (1.5 x 9/101 + 0.01)) = 6', cd['leverage'] == 6)
cd = a.card('A', dict(row, mark=103.0), True, 10000, 0.5)
check('LONG above the zone: a limit at its top', cd['mode'] == 'limit' and cd['entry'] == 102.0
      and abs(cd['qty'] - 50 / 10.0) < 1e-12)
cd = a.card('A', dict(row, mark=93.5), True, 10000, 0.5)
check('LONG within 0.25U of the stop: no entry', cd['mode'] == 'none' and cd['entry'] is None)
cd = a.card('A', dict(row, mark=97.0), True, 10000, 0.5)
check('LONG below the zone, clear of the stop: at market', cd['mode'] == 'market' and cd['entry'] == 97.0)
cd = a.card('A', dict(row, signal=-1, mark=99.0), False, 10000, 0.5)
check('SHORT mirrored: stop and targets', cd['mode'] == 'market' and cd['stop'] == 108.0
      and cd['targets'] == [92.0, 84.0, 76.0])
cd = a.card('A', dict(row, signal=-1, mark=97.0), False, 10000, 0.5)
check('SHORT below the zone: a limit at its bottom', cd['mode'] == 'limit' and cd['entry'] == 98.0)

# 5. the message's numbers, Russian style
check('num: spaces between thousands, a decimal comma', a.num(15000, 6) == '15 000' and a.num(0.5) == '0,5')
check('usdt: whole above 100', a.usdt(663.7) == '664' and a.usdt(86.43) == '86,4')
check('plural of монета', [a.plural(n, '1', '2', '5') for n in (1, 2, 5, 11, 12, 21, 22, 25, 111)]
      == ['1', '2', '5', '5', '5', '1', '2', '5', '5'])

# 6. a report and its message on six synthetic coins: three cards, every section present
cs, funds = {}, {}
for n, coin in enumerate(a.COINS[:6]):
    cc, x = {}, 100.0 + n
    for i in range(160):
        x *= (1.012 if n % 2 == 0 else 0.988) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
        cc[dt.date(2026, 6, 1) + i * DAY] = (x, x * 1.02, x * 0.98, x)
    cs[coin] = cc
    funds[coin] = lambda d: 0.0
rep = a.report(cs, funds, {}, 10000.0, 0.5, 0)
msg = a.message(rep, a.FACTS)
check('three cards, each with size 50 USDT of risk', len(rep['cards']) == 3
      and all(abs(cd['qty'] * abs(cd['entry'] - cd['stop']) - 50) < 1e-9 for cd in rep['cards']))
check('the message holds its sections', all(k in msg for k in ('ТОП-3', '⛔ Стоп', '🎯', 'Действует до 04:00',
                                                               'Уверенность', 'Остальные сигналы')))
check('each card holds its basis and its invalidation, ranks 1 to 3', msg.count('Основание: сумма знаков') == 3
      and msg.count('Инвалидация: цена') == 3 and [cd['rank'] for cd in rep['cards']] == [1, 2, 3])
check('the message holds the forward book and the six ratings', all(k in msg for k in (
    'Форвард с 28.10', 'Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:',
    'STRONG обоснован: <b>нет</b>', 'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>',
    'Инвалидация: у каждой карточки')))
bk = rep['book']['base']
check('the book: opened is closed plus open, and the total is the sum of its two parts',
      bk['opened'] == bk['closed'] + bk['open'] and abs(bk['total_R'] - (bk['closed_R'] + bk['open_R'])) < 1e-9)
strong_card = dict(rep['cards'][0], strong=True)
plain_card = dict(rep['cards'][0], strong=False)
check('a STRONG card shows the STRONG shares 48 / 28 / 18%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(strong_card, a.FACTS) if 'дошли' in l] == ['48%', '28%', '18%'])
check('another card shows the rule\'s shares 23 / 13 / 8%',
      [l.rsplit('дошли ', 1)[1] for l in a.card_lines(plain_card, a.FACTS) if 'дошли' in l] == ['23%', '13%', '8%'])

# 7. G-HISTORY's comparison: equal facts read equal, one changed fact reads DIFFERENT
h = {k: {'trades': f['trades'], 'wins': f['wins'], 'mean_R': f['mean_R'] + 1e-6, 'median_days': f['median_days'],
         'mfe': dict(f['mfe']), 'gate_H': f.get('gate_H'), 'gate_S': f.get('gate_S'), 'p_up': f['p_up'] + 1e-6,
         'top5_share': f['top5_share'] - 1e-6} for k, f in a.FACTS.items()}
check('G-HISTORY: 20 facts, all equal', len(a.facts_checks(h)) == 20 and all(ok for ok, _, _ in a.facts_checks(h).values()))
h['strong']['wins'] += 1
check('G-HISTORY: a changed fact reads DIFFERENT', [k for k, (ok, _, _) in a.facts_checks(h).items() if not ok]
      == ['strong wins'])
h['strong']['wins'] -= 1
h['strong']['top5_share'] = None
check('G-HISTORY: a top-5 share not derived reads DIFFERENT, never an error', [k for k, (ok, _, _) in a.facts_checks(h).items()
                                                                              if not ok] == ['strong top-5 share'])

# 8. the live readers on stand-in replies: funding paged by 1,000, intervals 8 h unless adjusted, marks and the card
calls = []
t_first = int(dt.datetime(2026, 10, 27, tzinfo=dt.timezone.utc).timestamp() * 1000)


def fake_fapi(path, **params):
    calls.append((path, params))
    if path == '/fapi/v1/fundingRate':
        s0 = params['startTime']
        n = 1000 if s0 == t_first else 5
        return [{'fundingTime': s0 + 3_600_000 * (k + 1), 'fundingRate': '0.0001'} for k in range(n)]
    if path == '/fapi/v1/fundingInfo':
        return [{'symbol': 'BTWUSDT', 'fundingIntervalHours': 4}]
    return [{'symbol': 'XMRUSDT', 'markPrice': '610.5', 'lastFundingRate': '0.00010000'}]


real_fapi, a.fapi = a.fapi, fake_fapi
try:
    per_day = a.fapi_funding('BTWUSDT', dt.date(2026, 10, 27))
    intervals, marks = a.fapi_intervals(), a.fapi_marks()
finally:
    a.fapi = real_fapi
check('funding: a second page from the last settlement + 1 ms', [p['startTime'] for _, p in calls[:2]]
      == [t_first, t_first + 3_600_000 * 1000 + 1])
check('funding: 1,005 hourly settlements summed by holding day, 24 in (27.10 00:00, 28.10 00:00]', abs(sum(per_day.values()) - 1005 * 0.0001) < 1e-12
      and abs(per_day[dt.date(2026, 10, 27)] - 24 * 0.0001) < 1e-12)
check('intervals and marks parsed', intervals == {'BTWUSDT': 4} and marks == {'XMRUSDT': (610.5, 0.0001)})
rep2 = a.report(cs, funds, {k + 'USDT': (cs[k][max(cs[k])][3], 0.0001) for k in cs}, 10000.0, 0.5, 0, (),
                {a.COINS[0] + 'USDT': 4})
hours = {cd['coin']: cd['funding_h'] for cd in rep2['cards']}
check('a card carries its funding interval: 4 h adjusted, 8 h otherwise',
      all(h == (4 if c == a.COINS[0] else 8) for c, h in hours.items()) and rep2['marks_ok'])

# 9. the forward book of check 1's series by hand: one closed stop, one open short that only collects funding
fb = a.forward_book(trades, daily, [pos])
open_R = (-0.001 * 145.0 + 49 * 0.0003 * 145.0) / 16.6   # entry cost at 145; 49 flat days a short is paid 0.03% a day
check('the book of one stop and one open short', fb['opened'] == 2 and fb['closed'] == 1 and fb['stops'] == 1
      and fb['open'] == 1 and fb['days'] == 200)
check('the book: the closed R is the trade\'s by hand, the open R is the short\'s by hand',
      abs(fb['closed_R'] - (-62 - 0.001 * 362 - fund) / 6) < 1e-9 and abs(fb['open_R'] - open_R) < 1e-9)
check('the book: the total over the days is the two parts\' sum', abs(fb['total_R'] - (fb['closed_R'] + fb['open_R'])) < 1e-9)

# 10. the ratings: a function of recorded facts alone
base = {'cards': [{'coin': 'A', 'mode': 'market'}, {'coin': 'B', 'mode': 'none'}, {'coin': 'C', 'mode': 'limit'}],
        'missing': [], 'marks_ok': True, 'close_of': '2026-10-30',
        'made_at_ms': int(dt.datetime(2026, 10, 31, 7, 0, tzinfo=dt.timezone.utc).timestamp() * 1000)}
tr = a.trust(base)
check('trust: the system 1, a trade the system\'s or 0 where no entry is offered, STRONG not justified',
      tr['system'] == 1 and tr['cards'] == {'A': 1, 'B': 0, 'C': 1} and tr['strong_justified'] is False)
check('trust: quality low while unproven, the expectancy not established, the close of the day before fresh',
      tr['quality'] == 'low' and not tr['expectancy_established'] and tr['served'] == len(a.COINS) and tr['fresh'])
check('trust: a close two days old, or a report with no instant, is not fresh',
      not a.trust(dict(base, close_of='2026-10-29'))['fresh'] and not a.trust(dict(base, made_at_ms=0))['fresh'])
check('trust: no mark prices, no trade confidence', set(a.trust(dict(base, marks_ok=False))['cards'].values()) == {0})
a.RELIABILITY = 4
try:
    t4 = a.trust(base)
    t4m = a.trust(dict(base, missing=['XMR']))
    t4s = a.trust(dict(base, close_of='2026-10-29'))
finally:
    a.RELIABILITY = 1
check('trust at reliability 4: quality high where fresh and complete, medium where a coin is missing or the close is old, '
      'the expectancy established', t4['quality'] == 'high' and t4m['quality'] == 'medium' and t4s['quality'] == 'medium'
      and t4['expectancy_established'] and t4m['served'] == 41)

print(f'SELFTEST-ADV3 PASS: {len(CHECKS)} of {len(CHECKS)} checks passed')
