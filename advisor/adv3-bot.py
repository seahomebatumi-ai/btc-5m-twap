#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands, the daily message at 06:00 UTC
# (10:00 in Batumi), and a journal of every message sent. Standard library only; adv3.py lies beside it.
# Modes: --serve (the unit's), --probe, --find-chat, --hello, --selftest.
# Exits: 0 or SIGTERM, restarted by systemd; 3 without a token or a chat id and 4 where glibc refuses its two
# settings, neither restarted; 1, an unexpected exception, restarted.
import argparse, ctypes, datetime as dt, html, json, os, re, sys, time, traceback, urllib.error, urllib.request
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
CMD = re.compile(r'^\s*/?(сигнал|signal)(?:@\w+)?\b(.*)$', re.I | re.S)
HELP = ('<b>ADV-3 · сигналы Binance Futures</b>\n'
        '«сигнал» — сигналы сейчас: депозит 10 000 USDT, риск 0,5% на сделку.\n'
        '«сигнал 15000 0.5» — со своим депозитом и риском (риск не больше 1%).\n'
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


def parse(text):
    """(deposit, risk) from «сигнал [deposit] [risk]», or None where the text is not that command."""
    m = CMD.match(text or '')
    if not m:
        return None
    rest_text = re.sub(r'(?<=\d)[ \u00a0\u202f](?=\d{3}(?!\d))', '', m.group(2))   # 15 000 -> 15000
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', rest_text)]
    deposit = next((x for x in nums if x >= 100), adv3.DEPOSIT)
    rest = [x for x in nums if x < 100]
    risk = rest[0] if rest else adv3.RISK
    return min(deposit, 10_000_000.0), min(max(risk, 0.05), adv3.RISK_MAX)


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


def journal(kind, rep, ids):
    rec = {'utc': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'],
           'close_of': rep['close_of'], 'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'],
           'strong': rep['strong'], 'message_ids': ids,
           'signals': {k: v.get('signal') for k, v in rep['rows'].items()},
           'cards': [{k: cd[k] for k in ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U')}
                     for cd in rep['cards']]}
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
    cmd = parse(text)
    try:
        if cmd:
            rep, msg = make(data, *cmd)
            ids = tg.send(msg)
            try:
                journal('request', rep, ids)
            except Exception:
                log('request record failed\n' + traceback.format_exc())
            log('request answered for the close of', rep['close_of'])
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
    """The bot's own checks, offline: the command, the chunks, the files, the log, the HTML fallback, glibc."""
    done = []

    def check(name, ok):
        done.append(name)
        assert ok, name

    for text, want in (('сигнал', (adv3.DEPOSIT, adv3.RISK)), ('Сигнал 15000 0,5%', (15000.0, 0.5)),
                       ('/signal@adv3_bot 5000 0.8', (5000.0, 0.8)), ('signal 0.3', (adv3.DEPOSIT, 0.3)),
                       ('сигнал 20000 3', (20000.0, adv3.RISK_MAX)), ('сигнал 20 000 0,5', (20000.0, 0.5)),
                       ('signal 5000 0.5%', (5000.0, 0.5)), ('сигнал 12000 0.01', (12000.0, 0.05)),
                       ('привет', None), ('сигналы', None), ('', None)):
        check(f'parse {text!r}', parse(text) == want)
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
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params['text']:
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    check('HTML sent as HTML', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML')
    check('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
          and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    SECRETS.append('123456:SECRET')
    import contextlib, io
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
