---
name: binance-trend-signal
description: Binance Futures LONG, SHORT or FLAT from the frozen ADV-1 trend rule, with stop, size and its live record. Use for «сигнал», «лонг или шорт», «что брать», entry, stop or position-size questions.
---

# binance-trend-signal — the ADV-1 advisor

ADV-1 is one trend rule for the Boss's own manual trading on Binance Futures (CANON PART VII). Its text was frozen on
2026-10-28 08:04 UTC, before any of its results was computed (SHA-256 `396c573d…ab628a0`), and `adv1.py` below is its
only implementation. It claims no edge: its history can only disqualify it, and only its forward record, from the close
of 2026-10-28, can show one.

## Run

1. Extract the script byte for byte from this file, never retyped — `<dir>` is this skill's base directory:
   `awk '/^```python adv1.py$/{f=1;next} f&&/^```$/{exit} f' "<dir>/SKILL.md" > adv1.py`
   Only where the file cannot be read, write the block below exactly as it stands.
2. `sha256sum adv1.py` must print `e93dd416d692c7a973c4e643bd8d04263bf9116d3f9f01154468ccced3a91326`. Otherwise stop
   and tell the Boss the skill's copy is damaged. Never run, repair or write another script.
3. `python3 adv1.py --deposit <USDT> --risk <percent>` — the Boss's deposit and risk where he gave them, else the
   defaults, 1000 and 0.5; risk is capped at 1. Add `--history` only when he asks for the record or the history: it
   takes about a minute. The script reads `data-api.binance.vision` and `data.binance.vision`; where a fetch fails, say
   which host failed and stop.
4. Answer from the script's JSON alone. Never change a number, and never add a direction, a level or a forecast the
   script did not print.

## The answer — Russian, phone-first, nothing else

- Header: `ADV-1 · закрытие DD.MM (UTC)` from `close_of`.
- First, every change against `signal_prev_close`: a new LONG or SHORT, or an exit — FLAT after a side, or the side
  reversed. Where nothing changed, the first line says «Без изменений».
- A table of the coins whose signal is LONG or SHORT: coin · side, with `rule_position.since` · stop distance `U` in
  price and `U_pct` — below the entry for LONG, above it for SHORT · size `qty` and `notional` for the deposit · isolated
  leverage at most `isolated_leverage_max`.
- One line for the FLAT coins: «Вне рынка: …».
- Three short lines: the entry is at market, once a day after the 00:00 UTC close; the stop is placed at once, `U` from
  the Boss's own entry price, and hitting it costs exactly the risk chosen; the exit is the stop, or the signal changing
  at a close. Where `open_risk_pct_if_all` exceeds 5, say that all signals together risk more than 5% of the deposit.
- The forward record from `forward`: days, closed trades, total R — R is a trade's result in units of its own risk,
  −1 R being the stop — and that it is read once, after the close of 2027-10-28.
- One line of history from the facts below, and the last line: «Не инвестиционный совет: правило показывает состояние
  рынка; решение и риск — ваши.»

## Fixed facts — Gate H, read 2026-10-28 on the history to the close of 2026-10-27

Eight coins, after costs and funding: 1,803 trades, 35% profitable, total +718 R. The top 1% of trades, 17 of them, carry 81% of
it — those entered in 2020–21, 53% — and 2021 alone 46%; closed trades of 2025 −1 R, of 2026 to the cut +25 R; shorts +25 R over nine years against +692 R
for longs; the worst realized stretch −47 R, 22 losing trades in a row. **NOT DISQUALIFIED — which confirms nothing:**
that crypto trended was known before the rule was chosen. At the history's Sharpe, 0.93, the forward reading at 365
days reads PROVEN with probability about 0.05, and 0.80 needs about thirteen and a half years. The history line, in Russian:
«История 2017–2026 — не доказательство: 35% сделок в плюс, 81% прибыли дали 17 крупнейших сделок, больше половины —
2020–21 годы; 2025 год около нуля, шорты за девять лет около нуля.»

## adv1.py

```python adv1.py
#!/usr/bin/env python3
# adv1.py - ADV-1, the Boss's trend advisor for Binance Futures. Standard library only.
# Rule text RULE-ADV-1, SHA-256 396c573d454126d51a86aa9edf551d5c15e164a5cc7a9a9c826f87487ab628a0,
# frozen 2026-10-28 08:04 UTC before any of its results was computed. Prices: Binance spot daily
# candles (data-api.binance.vision); funding: Binance USD-M archive (data.binance.vision).
import argparse, bisect, datetime as dt, io, json, math, sys, time, urllib.error, urllib.request, zipfile
from concurrent.futures import ThreadPoolExecutor

RULE = '396c573d454126d51a86aa9edf551d5c15e164a5cc7a9a9c826f87487ab628a0'
COINS = ('BTC', 'ETH', 'SOL', 'XRP', 'BNB', 'DOGE', 'ADA', 'LINK')
LOOKBACKS, ATR_DAYS, STOP_N, COST, BASE_F = (14, 28, 56, 112), 20, 2.0, 0.001, 0.0001
HISTORY_TO, FORWARD_FROM, PERPS_FROM = dt.date(2026, 10, 27), dt.date(2026, 10, 28), dt.date(2019, 9, 1)
UA = {'User-Agent': 'adv1-advisor/1'}
KL = 'https://data-api.binance.vision/api/v3/klines?symbol={s}USDT&interval=1d&startTime={t}&limit=1000'
FR = ('https://data.binance.vision/data/futures/um/monthly/fundingRate/{s}USDT/'
      '{s}USDT-fundingRate-{y:04d}-{m:02d}.zip')
DAY = dt.timedelta(days=1)


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


def candles(coin, now_ms):
    """Closed daily candles {date: (open, high, low, close)}, from the pair's first day."""
    out, t = {}, 0
    while True:
        rows = json.loads(get(KL.format(s=coin, t=t)))
        for r in rows:
            if int(r[6]) < now_ms:
                d = dt.datetime.fromtimestamp(int(r[0]) / 1000, dt.timezone.utc).date()
                out[d] = (float(r[1]), float(r[2]), float(r[3]), float(r[4]))
        if len(rows) < 1000:
            return out
        t = int(rows[-1][0]) + 86_400_000


def months(a, b):
    y, m = a.year, a.month
    while (y, m) <= (b.year, b.month):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def funding(coin, first, last):
    """Daily funding sum by holding day: a settlement at T belongs to the day whose (open, close] holds T.
    Days the archive does not cover get the base rate, three settlements of +0.01%."""
    def one(ym):
        b = get(FR.format(s=coin, y=ym[0], m=ym[1]))
        if b is None:
            return ym, None
        z = zipfile.ZipFile(io.BytesIO(b))
        rows = [line.split(',') for line in z.read(z.namelist()[0]).decode().splitlines()]
        return ym, [(int(p[0]), float(p[2])) for p in rows if p[0].strip().isdigit()]
    with ThreadPoolExecutor(12) as ex:
        got = dict(ex.map(one, list(months(max(first, PERPS_FROM), last))))
    per_day, first_settle = {}, None
    for rows in got.values():
        for ms, f in rows or ():
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--history', action='store_true', help='Gate H and the history, all funding months')
    ap.add_argument('--deposit', type=float, default=1000.0)
    ap.add_argument('--risk', type=float, default=0.5, help='percent of the deposit a trade, at most 1')
    a = ap.parse_args()
    risk = min(a.risk, 1.0) / 100
    now_ms = int(time.time() * 1000)
    rows, port_f, port_h, trades_f, trades_h = [], {}, {}, [], []
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
        name = {1: 'LONG', -1: 'SHORT', 0: 'FLAT'}
        U = unit(c, days, len(days) - 1)
        px = closes[-1]
        qty = risk * a.deposit / U
        row = {'coin': coin, 'close_of': str(last), 'signal': name[sig],
               'signal_prev_close': name[signal(days, closes, len(days) - 2)],
               'price': px, 'U': U, 'U_pct': 100 * U / px,
               'stop_if_entered_at_close': px - sig * U if sig else None,
               'qty': qty if sig else 0.0, 'notional': qty * px if sig else 0.0,
               'eff_leverage': qty * px / a.deposit if sig else 0.0,
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
    out = {'rule': RULE, 'deposit': a.deposit, 'risk_pct': 100 * risk, 'signals': rows,
           'open_risk_pct_if_all': 100 * risk * sum(r['signal'] != 'FLAT' for r in rows),
           'forward': stats(trades_f, port_f) | {'from_close_of': str(FORWARD_FROM)}}
    if a.history:
        h = stats(trades_h, port_h)
        h['gate_H'] = 'NOT DISQUALIFIED' if h['total_R'] > 0 else 'DISQUALIFIED'
        h['to_close_of'] = str(HISTORY_TO)
        out['history'] = h
    if out.get('history', {}).get('gate_H') == 'DISQUALIFIED':
        for r in rows:
            r.update(signal='WITHHELD', qty=0.0, notional=0.0, eff_leverage=0.0)
    json.dump(out, sys.stdout, indent=1, default=str)
    print()


if __name__ == '__main__':
    main()
```
