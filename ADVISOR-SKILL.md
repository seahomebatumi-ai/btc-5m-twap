---
name: binance-trend-signal
description: Binance Futures LONG, SHORT or FLAT for 18 coins from the frozen ADV-2 trend rule, with stops, sizes and its live record. Use for «сигнал», «лонг или шорт», «что брать», entry, stop or position-size questions.
---

# binance-trend-signal — the ADV-2 advisor

ADV-2 is one trend rule for the Boss's own manual trading on Binance Futures (CANON PART VII): ADV-1's rule on eighteen
coins. Its text was frozen on 2026-10-28 09:26 UTC, before any of its results was computed (SHA-256
`1808ade9…b316f8b`), and `adv2.py` below is its only implementation. It claims no edge: its history can only
disqualify it, and only its forward record, from the close of 2026-10-28, can show one.

## Run — one command, because every step spends the Boss's usage

`<dir>` is this skill's base directory. Add `--deposit <USDT>` and `--risk <percent>` only where the Boss gave
them; the defaults are 1000 and 0.4, risk is capped at 1 and scaled down so that all open signals together risk at
most 5%.

    cd "$(mktemp -d)" && awk '/^```python adv2.py$/{f=1;next} f&&/^```$/{exit} f' "<dir>/SKILL.md" > adv2.py && echo "4db8d393f30788771ce4fda4b6b0a35f81d2de2b9b35f24cc96e8fe88a4a79d4  adv2.py" | sha256sum -c --quiet - && python3 adv2.py

- A failed checksum means the skill's copy is damaged: say so and stop. Never run, repair or write another script.
- A failed fetch names its host — `data-api.binance.vision` or `data.binance.vision`: say which, and stop.
- Reply with the script's output exactly as printed, nothing before it and nothing after it.
- Where the Boss asks about one coin, answer from the same command run with `--json`, and never add a direction, a
  level or a forecast the script did not print. `--history` takes about a minute: only when he asks for the history.

## Fixed facts — Gate H, read 2026-10-28 on the history to the close of 2026-10-27

Eighteen coins, after costs and funding: 3,113 trades, 34% profitable, total +980 R. The top 1% of trades, 31 of them,
carry 92% of it — those entered in 2020–21, 49% — and 2021 alone 40%; closed trades of 2025 +25 R; shorts +17 R over
nine years against +962 R for longs; the worst realized stretch −64 R, 32 losing trades in a row. The ten coins added
to ADV-1's eight were named in 2026 as promising, so their history, +261 R, was chosen after the fact. **NOT
DISQUALIFIED — which confirms nothing.** At the history's Sharpe, 0.97, the forward reading at 365 days reads PROVEN
with probability about 0.05, and 0.80 needs about twelve and a half years.

## adv2.py

```python adv2.py
#!/usr/bin/env python3
# adv2.py - ADV-2, the Boss's trend advisor for Binance Futures. Standard library only.
# Rule text RULE-ADV-2, SHA-256 1808ade97e0bd4987d36db4e14bc979b4935043d416fb2f58ad33f3e1b316f8b,
# frozen 2026-10-28 09:26 UTC before any of its results was computed: ADV-1's rule on eighteen coins.
# Prices: Binance spot daily candles (data-api.binance.vision), HYPE's days before its spot pair from the
# USD-M archive; funding: Binance USD-M archive (data.binance.vision). Prints the Boss's message in
# Russian; --json prints the numbers, --history adds Gate H's history.
import argparse, bisect, datetime as dt, io, json, math, sys, time, urllib.error, urllib.request, zipfile
from concurrent.futures import ThreadPoolExecutor

RULE = '1808ade97e0bd4987d36db4e14bc979b4935043d416fb2f58ad33f3e1b316f8b'
COINS = ('BTC', 'ETH', 'SOL', 'XRP', 'BNB', 'DOGE', 'ADA', 'LINK',
         'HYPE', 'SUI', 'ZEC', 'ONDO', 'AAVE', 'TAO', 'AVAX', 'HBAR', 'XLM', 'NEAR')
BACKFILL = {'HYPE': dt.date(2025, 5, 1)}
LOOKBACKS, ATR_DAYS, STOP_N, COST, BASE_F = (14, 28, 56, 112), 20, 2.0, 0.001, 0.0001
HISTORY_TO, FORWARD_FROM, PERPS_FROM = dt.date(2026, 10, 27), dt.date(2026, 10, 28), dt.date(2019, 9, 1)
RISK_DEFAULT, RISK_MAX, RISK_ALL = 0.4, 1.0, 5.0
UA = {'User-Agent': 'adv2-advisor/1'}
KL = 'https://data-api.binance.vision/api/v3/klines?symbol={s}USDT&interval=1d&startTime={t}&limit=1000'
FR = ('https://data.binance.vision/data/futures/um/monthly/fundingRate/{s}USDT/'
      '{s}USDT-fundingRate-{y:04d}-{m:02d}.zip')
PK = 'https://data.binance.vision/data/futures/um/monthly/klines/{s}USDT/1d/{s}USDT-1d-{y:04d}-{m:02d}.zip'
DAY = dt.timedelta(days=1)
HISTORY_LINE = ('История 2017–2026 — не доказательство: 34% сделок в плюс, 92% прибыли дали 31 крупнейшая '
                'сделка, почти половину — 2020–21 годы; шорты за девять лет около нуля; худшая серия −64 R.')


def get(url):
    err = None
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            err = e
        except OSError as e:
            err = e
        time.sleep(1 + 2 * k)
    raise SystemExit(f'FETCH FAILED {url}: {err!r}')


def months(a, b):
    y, m = a.year, a.month
    while (y, m) <= (b.year, b.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def archive_rows(url_of, first, last):
    """Every data row of the archive's monthly files from first's month to last's, by month; None where absent."""
    def one(ym):
        b = get(url_of(ym))
        if b is None:
            return ym, None
        z = zipfile.ZipFile(io.BytesIO(b))
        rows = [line.split(',') for line in z.read(z.namelist()[0]).decode().splitlines()]
        return ym, [p for p in rows if p[0].strip().isdigit()]
    with ThreadPoolExecutor(12) as ex:
        return dict(ex.map(one, list(months(first, last))))


def candles(coin, now_ms):
    """Closed daily candles {date: (open, high, low, close)}: the spot pair from its first day, and for a coin in
    BACKFILL the perpetual's candles for the days before it."""
    out, t = {}, 0
    while True:
        rows = json.loads(get(KL.format(s=coin, t=t)))
        for r in rows:
            if int(r[6]) < now_ms:
                d = dt.datetime.fromtimestamp(int(r[0]) / 1000, dt.timezone.utc).date()
                out[d] = (float(r[1]), float(r[2]), float(r[3]), float(r[4]))
        if len(rows) < 1000:
            break
        t = int(rows[-1][0]) + 86_400_000
    if coin in BACKFILL:
        first = min(out)
        got = archive_rows(lambda ym: PK.format(s=coin, y=ym[0], m=ym[1]), BACKFILL[coin], first)
        for rows in got.values():
            for p in rows or ():
                ms = int(p[0]) // 1000 if int(p[0]) > 10 ** 14 else int(p[0])
                d = dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).date()
                if d < first:
                    out[d] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]))
    return out


def funding(coin, first, last):
    """Daily funding sum by holding day: a settlement at T belongs to the day whose (open, close] holds T.
    Days the archive does not cover get the base rate, three settlements of +0.01%."""
    got = archive_rows(lambda ym: FR.format(s=coin, y=ym[0], m=ym[1]), max(first, PERPS_FROM), last)
    per_day, first_settle = {}, None
    for rows in got.values():
        for p in rows or ():
            ms, f = int(p[0]), float(p[2])
            d = (dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc) - dt.timedelta(milliseconds=1)).date()
            per_day[d] = per_day.get(d, 0.0) + f
            first_settle = d if first_settle is None or d < first_settle else first_settle

    def f(d):
        if first_settle is not None and d >= first_settle and got.get((d.year, d.month)) is not None:
            return per_day.get(d, 0.0)
        return 3 * BASE_F
    return f


def signal(days, closes, i):
    """+1 LONG, -1 SHORT, 0 FLAT at the close of days[i]; None before the longest lookback exists."""
    s = 0
    for L in LOOKBACKS:
        j = bisect.bisect_right(days, days[i] - L * DAY) - 1
        if j < 0:
            return None
        s += (closes[i] > closes[j]) - (closes[i] < closes[j])
    return 1 if s >= 2 else -1 if s <= -2 else 0


def true_range(c, days, i):
    h, l, pc = c[days[i]][1], c[days[i]][2], c[days[i - 1]][3]
    return max(h, pc) - min(l, pc)


def unit(c, days, i):
    """U = 2 N at the close of days[i]: twice the mean true range of the last 20 days; None before them."""
    if i < ATR_DAYS:
        return None
    return STOP_N * sum(true_range(c, days, j) for j in range(i - ATR_DAYS + 1, i + 1)) / ATR_DAYS


def simulate(c, fund, first_entry, last_day):
    """The rule on one pair. Returns (closed trades, {day: R}, open position or None)."""
    days = sorted(d for d in c if d <= last_day)
    closes = [c[d][3] for d in days]
    trades, daily, pos = [], {}, None
    for i, d in enumerate(days):
        o, h, l, cl = c[d]
        r = 0.0
        if i:
            pc = closes[i - 1]
            if pos:
                k, U, S = pos['d'], pos['U'], pos['S']
                if (l <= S) if k > 0 else (h >= S):
                    X = o if ((o <= S) if k > 0 else (o >= S)) else S
                    r = (k * (X - pc) - COST * X) / U
                    pos.update(R=pos['R'] + r, X=X, exit=d, why='stop')
                    trades.append(pos)
                    pos = None
                else:
                    r = (k * (cl - pc) - k * fund(d) * cl) / U
                    pos['R'] += r
        sig = signal(days, closes, i)
        if pos and sig != pos['d']:
            x = -COST * cl / pos['U']
            r += x
            pos.update(R=pos['R'] + x, X=cl, exit=d, why='signal')
            trades.append(pos)
            pos = None
        if pos is None and sig in (1, -1) and d >= first_entry and i >= ATR_DAYS:
            U = unit(c, days, i)
            x = -COST * cl / U
            pos = {'d': sig, 'E': cl, 'U': U, 'S': cl - sig * U, 'entry': d, 'R': x}
            r += x
        if d >= first_entry:
            daily[d] = r
    return trades, daily, pos


def stats(trades, daily):
    R = [t['R'] for t in trades]
    out = {'trades': len(R), 'wins': sum(x > 0 for x in R), 'total_R': sum(R), 'days': len(daily)}
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


def num(x, sig=3):
    """x to sig significant digits, Russian style: a space between thousands, a decimal comma, a true minus."""
    if x == 0:
        return '0'
    digits = max(0, sig - 1 - math.floor(math.log10(abs(x))))
    return f'{x:,.{digits}f}'.replace(',', ' ').replace('.', ',').replace('-', '−')


def pct(x, places=1):
    """A percentage to at most `places` decimals, trailing zeros dropped, decimal comma."""
    s = f'{x:.{places}f}'
    return (s.rstrip('0').rstrip('.') if '.' in s else s).replace('.', ',')


def ddmm(day):
    return f'{day[8:10]}.{day[5:7]}'


def message(out):
    """The Boss's message, in Russian, from the run's numbers alone."""
    side = {'LONG': 'ЛОНГ', 'SHORT': 'ШОРТ'}
    side_of = {'LONG': 'лонга', 'SHORT': 'шорта'}
    rows = out['signals']
    deposit = f"{round(out['deposit']):,}".replace(',', ' ')
    lines = [f"**ADV-2 · закрытие {ddmm(rows[0]['close_of'])} (UTC)** · депозит {deposit} USDT · "
             f"риск {pct(out['risk_pct_effective'], 2)}% на сделку", '']
    changes = []
    for r in rows:
        now, before, pos = r['signal'], r['signal_prev_close'], r['rule_position']
        if now in side and before not in side:
            changes.append(f"{r['coin']} — новый {side[now]}")
        elif now not in side and before in side:
            changes.append(f"{r['coin']} — выход из {side_of[before]}")
        elif now in side and before in side and now != before:
            changes.append(f"{r['coin']} — разворот в {side[now]}")
        elif now in side and pos and pos['since'] == r['close_of']:
            changes.append(f"{r['coin']} — стоп сработал, новый {side[now]}")
    lines += [('Изменения: ' + '; '.join(changes) + '.') if changes else 'Без изменений.', '']
    active = [r for r in rows if r['signal'] in side]
    if active:
        lines += ['| Монета | Сигнал | Стоп от входа | Размер | Плечо ≤ |', '|---|---|---|---|---|']
        for r in sorted(active, key=lambda r: r['signal'] != 'LONG'):
            sign = '−' if r['signal'] == 'LONG' else '+'
            since = f" с {ddmm(r['rule_position']['since'])}" if r['rule_position'] else ''
            stop = f"{r['U_pct']:.1f}".replace('.', ',')
            lines.append(f"| {r['coin']} | {side[r['signal']]}{since} | {sign}{stop}% ({sign}{num(r['U'])}) "
                         f"| {num(r['qty'])} {r['coin']} ≈ {num(r['notional'], 2)} USDT | {r['isolated_leverage_max']}× |")
        lines.append('')
    flat = [r['coin'] for r in rows if r['signal'] == 'FLAT']
    if flat:
        lines.append('Вне рынка: ' + ', '.join(flat) + '.')
    none = [r['coin'] for r in rows if r['signal'] not in side and r['signal'] != 'FLAT']
    if none:
        lines.append('Без сигнала, истории меньше 112 дней: ' + ', '.join(none) + '.')
    lines += ['', 'Вход — по рынку после закрытия в 00:00 UTC (04:00 по Батуми). Стоп — сразу, на указанном расстоянии '
              'от вашей цены входа: его срабатывание стоит ровно выбранный риск. Выход — стоп или смена сигнала на '
              'закрытии. «Плечо ≤» — для изолированной маржи: ликвидация дальше стопа.']
    if out['risk_pct_effective'] < out['risk_pct']:
        lines.append(f"Сигналов {len(active)}: риск на сделку снижен до {pct(out['risk_pct_effective'], 2)}%, "
                     f"чтобы все вместе не превышали {pct(RISK_ALL)}% депозита.")
    fw = out['forward']
    if fw['days']:
        total = ('+' if fw['total_R'] > 0 else '') + num(fw['total_R'])
        lines.append(f"Форвард с 28.10: {fw['days']} дн., закрыто сделок {fw['trades']}, итог {total} R "
                     '(R — результат в единицах риска сделки, −1 R — стоп). Доказанность проверяется после 28.10.2027.')
    else:
        lines.append('Форвард начинается с закрытия 28.10; доказанность проверяется после 28.10.2027.')
    if HISTORY_LINE:
        lines.append(HISTORY_LINE)
    lines.append('Не инвестиционный совет: правило показывает состояние рынка; решение и риск — ваши.')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true', help='print the numbers instead of the message')
    ap.add_argument('--history', action='store_true', help='Gate H and the history, all funding months; implies --json')
    ap.add_argument('--deposit', type=float, default=1000.0)
    ap.add_argument('--risk', type=float, default=RISK_DEFAULT, help='percent of the deposit a trade, 0.4 by default, at most 1')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    risk = min(a.risk, RISK_MAX)
    now_ms = int(time.time() * 1000)
    rows, port_f, port_h, trades_f, trades_h = [], {}, {}, [], []
    name = {1: 'LONG', -1: 'SHORT', 0: 'FLAT', None: 'NO HISTORY'}
    with ThreadPoolExecutor(len(COINS)) as ex:
        allc = dict(zip(COINS, ex.map(lambda k: candles(k, now_ms), COINS)))
    for coin in COINS:
        c = allc[coin]
        days = sorted(c)
        last = days[-1]
        fund = funding(coin, days[0] if a.history else FORWARD_FROM, last)
        _, _, pos = simulate(c, fund, days[0], last)
        closes = [c[d][3] for d in days]
        sig = signal(days, closes, len(days) - 1)
        U = unit(c, days, len(days) - 1)
        px = closes[-1]
        row = {'coin': coin, 'close_of': str(last), 'signal': name[sig],
               'signal_prev_close': name[signal(days, closes, len(days) - 2)],
               'price': px, 'U': U, 'U_pct': 100 * U / px,
               'stop_if_entered_at_close': px - sig * U if sig else None,
               'isolated_leverage_max': min(20, math.floor(1 / (1.5 * U / px + 0.01))),
               'rule_position': None if pos is None else
               {'side': 'LONG' if pos['d'] > 0 else 'SHORT', 'since': str(pos['entry']),
                'entry': pos['E'], 'stop': pos['S']}}
        rows.append(row)
        tf, df, pf = simulate(c, fund, FORWARD_FROM, last)
        row['forward_position'] = None if pf is None else {
            'side': 'LONG' if pf['d'] > 0 else 'SHORT', 'since': str(pf['entry']), 'entry': pf['E'],
            'stop': pf['S'], 'R_so_far': pf['R']}
        trades_f += tf
        for d, x in df.items():
            port_f[d] = port_f.get(d, 0.0) + x
        if a.history:
            th, dh, ph = simulate(c, fund, days[0], HISTORY_TO)
            if ph:
                ph = dict(ph, R=ph['R'] - COST * c[max(d for d in c if d <= HISTORY_TO)][3] / ph['U'],
                          why='open at the history cut')
                th = th + [ph]
            for t in th:
                t['coin'] = coin
            trades_h += th
            for d, x in dh.items():
                port_h[d] = port_h.get(d, 0.0) + x
            row['history'] = stats(th, dh) | {'from': str(days[0])}
    n_active = sum(r['signal'] in ('LONG', 'SHORT') for r in rows)
    eff = min(risk, RISK_ALL / n_active) if n_active else risk
    for r in rows:
        on = r['signal'] in ('LONG', 'SHORT')
        qty = eff / 100 * a.deposit / r['U'] if on else 0.0
        r.update(qty=qty, notional=qty * r['price'], eff_leverage=qty * r['price'] / a.deposit)
    out = {'rule': RULE, 'deposit': a.deposit, 'risk_pct': risk, 'risk_pct_effective': eff, 'signals': rows,
           'open_risk_pct_if_all': eff * n_active,
           'forward': stats(trades_f, port_f) | {'from_close_of': str(FORWARD_FROM)}}
    if a.history:
        h = stats(trades_h, port_h)
        h['gate_H'] = 'NOT DISQUALIFIED' if h['total_R'] > 0 else 'DISQUALIFIED'
        h['to_close_of'] = str(HISTORY_TO)
        out['history'] = h
        if h['gate_H'] == 'DISQUALIFIED':
            for r in rows:
                r.update(signal='WITHHELD', qty=0.0, notional=0.0, eff_leverage=0.0)
    if a.json or a.history:
        json.dump(out, sys.stdout, indent=1, default=str)
        print()
    else:
        print(message(out))


if __name__ == '__main__':
    main()
```
