#!/usr/bin/env python3
# adv3-bot.py - ADV-3's Telegram side (CANON PART VII): the Boss's commands; two checks a day by the unit's own scheduler, at
# 00:10 UTC (04:10 in Batumi) the close's signals and at 15:07 UTC (19:07) the facts of the moment, each loud only for an alert and
# one quiet line where it finds nothing; and, since TZ-42, the registry of every STRONG signal the bot published - registry.jsonl,
# append-only and hash-chained - each signal walked forward on Binance's 1- and 5-minute candles to its fill, its targets and its end
# by the rule's own exit; beside the journal of every check's state and every message sent. Standard library only; adv3.py beside it.
# TZ-42, the Boss's specification of 2026-11-05: the model's defaults - a calculation base of 200,000 USDT, never his balance; 0.5 %
# a trade at its stop, 1 % at most; 10 % for every open signal together; a stop within 14 % of the entry - a request's overrides
# narrowing them for that request alone; the risk shared by the strength of the trend, the strongest the most; the leverage the rule's
# ceiling, lowered only to keep the margin at 0.5 % of the capital or more, never raised; STRONG at every rank, at most 7 new signals
# a close; a reply keyboard. The frozen rule's STRONG, its strategy and its records stay the TOP-3's: the registry measures nothing.
# Modes: --serve (the unit's), --probe, --find-chat, --hello, --selftest.
# Exits: 0 or SIGTERM, restarted by systemd; 3 without a token or a chat id and 4 where glibc refuses its two
# settings, neither restarted; 1, an unexpected exception, restarted.
import argparse, ctypes, datetime as dt, hashlib, html, json, math, os, re, sys, time, traceback, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adv3  # noqa: E402

TOKEN_FILE = '/etc/adv3-bot/token'
CHAT_FILE = '/etc/adv3-bot/chat-id'
STATE = '/var/lib/adv3-bot'
TG = 'https://api.telegram.org/bot{token}/{method}'
UA = 'adv3-bot/1'
# The two checks a day (TZ-39; the second at 15:07 UTC, 19:07 in Batumi, since TZ-42 - the Boss's of 2026-11-05). The rule changes
# state only at a daily close: the check of 00:10 UTC reads the close's signals, ten minutes after it - the margin kept for the day's
# last funding settlement; the check of 15:07 reads facts alone and never a signal of a half-formed candle.
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(15, 7)))
BATUMI = dt.timedelta(hours=4)
POLL, RETRY, LIMIT = 50, 300, 4000
OPEN = ('сигнал', 'сигналы', 'signal', 'signals', 'топ', 'top', 'стратегия', 'стратегию', 'strategy')
ASSESS = ('оценка', 'оценки', 'оценку', 'rating')
REGISTRY = ('реестр', 'registry')
RANKING = ('рейтинг', 'ranking')
HELPS = ('помощь', 'help', 'start', 'команды', 'меню', 'menu')
HEAD = re.compile(r'^\s*/?([^\W\d_]+)')
TOPN = re.compile(r'(?<![^\W\d_])(?:топ|top)[\s\-\u2013]*(\d{1,2})(?!\d)', re.I)   # «стоп 12» holds no «топ»
NUMBER = r'(\d+(?:[.,]\d+)?)'
KEYWORDS = (('risk', re.compile(r'(?<![^\W\d_])(?:риск|risk)\s*[:=]?\s*' + NUMBER, re.I)),
            ('total', re.compile(r'(?<![^\W\d_])(?:лимит|limit|всего|total)\s*[:=]?\s*' + NUMBER, re.I)),
            ('stop', re.compile(r'(?<![^\W\d_])(?:стоп|stop)\s*[:=]?\s*' + NUMBER, re.I)))
# The model's defaults, the Boss's of 2026-11-05 (CANON PART VII): the capital - a calculation base, never his balance or his margin;
# the risk of all open signals together, in percent of it; the stop's farthest distance from the entry, in percent; the new signals one
# close may hold. The risk of one trade is adv3.RISK, at most adv3.RISK_MAX. The margin's floor, its ceiling and its exceptional
# ceiling, in percent of the capital: 1,000, 7,000 and 8,000 USDT at 200,000.
CAPITAL, RISK_TOTAL, STOP_MAX, NEW_MAX = 200000.0, 10.0, 14.0, 7
MARGIN_MIN, MARGIN_MAX, MARGIN_EXC = 0.5, 3.5, 4.0
# The share of a coin's mean daily quote volume of LIQ_DAYS days a position may take - TZ-37's 0.1 %, 0.5 % since TZ-42 at the
# capital of 200,000 USDT - and the strength's cap in the risk shares.
LIQ_FRAC, Z_CAP, LIQ_DAYS = 0.005, 3.0, 7
RANK_LIST, RANK_MAX = 7, 42   # «рейтинг»: the rule's first 7 coins by default, all 42 at most
# The candles a signal is walked on, their length in ms: its first minutes - from its issue to the next 5-minute boundary - on 1-minute
# candles, then 5-minute ones; a page of fapi's klines.
K1_MS, K5_MS, K5_PAGE = 60_000, 300_000, 1000
INTERVAL = {K1_MS: '1m', K5_MS: '5m'}
DAY_MS = 86_400_000
PACE = 1.1     # seconds between the parts of one message: Telegram asks for at most one message a second in a chat (TZ-40)
REG_FILE, REG_STATE, GENESIS = 'registry.jsonl', 'registry-state.json', '0' * 64
SIDE, DOT = {1: 'LONG', -1: 'SHORT'}, {1: '🟢', -1: '🔴'}
# A legacy signal's open event: the fields the seed writes, in the shape register writes a model signal's.
LEGACY_KEYS = ('utc', 'coin', 'side', 'close_of', 'source', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'z', 'sum', 'rank', 'since',
               'btc', 'breadth', 'valid', 'capital', 'risk_pct', 'loss', 'notional', 'qty', 'leverage', 'margin', 'legacy')
# The Boss's statuses (his specification of 2026-11-05, §3) and their Russian labels; PENDING is a limit not yet filled.
LABEL = {'PENDING': 'ждёт входа', 'ACTIVE': 'активен', 'TARGET 1 REACHED': 'цель 1', 'TARGET 2 REACHED': 'цель 2',
         'TARGET 3 REACHED': 'цель 3', 'PARTIAL TARGET COMPLETION': 'цели частично', 'STOPPED OUT': 'стоп',
         'INVALIDATED': 'инвалидация', 'EXPIRED': 'истёк'}
CARD_KEYS = ('coin', 'side', 'strong', 'mode', 'entry', 'stop', 'targets', 'close', 'U', 'since', 'z', 'sum', 'mark')
KEYBOARD = {'keyboard': [[{'text': 'Сигнал'}, {'text': 'Реестр'}], [{'text': 'Рейтинг'}, {'text': 'Оценка'}, {'text': 'Помощь'}]],
            'resize_keyboard': True, 'is_persistent': True}
COMMANDS = [{'command': 'signal', 'description': 'STRONG-сигналы, позиции и риск модели'},
            {'command': 'registry', 'description': 'Реестр STRONG-сигналов и итоги'},
            {'command': 'ranking', 'description': 'Рейтинг правила по 42 монетам'},
            {'command': 'rating', 'description': 'Уверенность и статистика реестра'},
            {'command': 'help', 'description': 'Команды и параметры'}]
DEFAULTS = {'capital': CAPITAL, 'risk': adv3.RISK, 'total': RISK_TOTAL, 'stop': STOP_MAX, 'n': NEW_MAX, 'set': []}
HELP = ('<b>ADV-3 · STRONG-сигналы Binance Futures</b>\n'
        '«Сигнал» — STRONG этого закрытия с позициями, открытые сигналы, риск модели и почему монета не взята. Модель: капитал '
        '200 000 USDT — база расчёта, не ваш баланс; риск 0,5% на сделку, у сильнейшей больше, не больше 1%; все открытые сигналы '
        'вместе ≤ 10%; стоп ≤ 14% от входа; до 7 новых за закрытие.\n'
        'На один запрос: «сигнал 50000 риск 0,75 лимит 8 стоп 12 топ 3» — капитал, риск на сделку (≤ 1%), общий лимит (≤ 10%), '
        'предел стопа (≤ 14%), число сделок (≤ 7). Умолчания не меняются; ограничения можно только ужесточить.\n'
        '«Реестр» — все STRONG-сигналы бота: открытые, завершённые, итоги.\n'
        '«Рейтинг» — рейтинг правила по 42 монетам; «рейтинг 15».\n'
        '«Оценка» — уверенность и статистика реестра.\n'
        'Проверки — в 04:10 и 19:07 по Батуми. Со звуком — новый STRONG, стоп, выход по сигналу, неисполненный лимит; остальное '
        'приходит тихо, проверка без событий — одной строкой.')


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


class TooMany(RuntimeError):
    """Telegram's 429: too many requests, and the seconds it asks to wait (TZ-40)."""

    def __init__(self, text, retry_after):
        super().__init__(text)
        self.retry_after = retry_after


class Telegram:
    """The Bot API through one request function: every call is a JSON POST with UA as its User-Agent."""

    def __init__(self, token, chat=None):
        self.token, self.chat = token, chat

    def call(self, method, http_timeout=30, **params):
        """One call; a reply not ok raises - TooMany, with the retry_after Telegram names (5 s where it names none), for a 429."""
        req = urllib.request.Request(TG.format(token=self.token, method=method), data=json.dumps(params).encode(),
                                     headers={'User-Agent': UA, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=http_timeout) as r:
                out = json.loads(r.read())
        except urllib.error.HTTPError as e:
            out = json.loads(e.read() or b'{}')
        if not out.get('ok'):
            text = f"telegram {method}: {out.get('error_code')} {out.get('description')}"
            if out.get('error_code') == 429:
                raise TooMany(text, int((out.get('parameters') or {}).get('retry_after') or 5))
            raise RuntimeError(text)
        return out['result']

    def send(self, text, quiet=False, keyboard=False):
        """The text as HTML, in parts of at most LIMIT characters, PACE seconds apart; a part Telegram cannot parse goes as plain
        text, and a part refused as too many requests waits the retry_after named, at most 60 s, and goes again, twice at most
        (TZ-40). quiet sends every part without a notification (the Bot API's disable_notification); keyboard attaches the reply
        keyboard, KEYBOARD, to the last part (TZ-42)."""
        ids, extra = [], ({'disable_notification': True} if quiet else {})
        parts = chunks(text)
        for k, part in enumerate(parts):
            if k:
                time.sleep(PACE)
            more = dict(extra, reply_markup=KEYBOARD) if keyboard and k == len(parts) - 1 else extra
            for attempt in range(3):
                try:
                    ids.append(self.send_part(part, more))
                    break
                except TooMany as e:
                    if attempt == 2:
                        raise
                    time.sleep(min(e.retry_after, 60) + 1)
        return ids

    def send_part(self, part, extra):
        """One part as HTML, or as plain text where Telegram cannot parse it; its message id."""
        try:
            return self.call('sendMessage', chat_id=self.chat, text=part, parse_mode='HTML', disable_web_page_preview=True,
                             **extra)['message_id']
        except TooMany:
            raise
        except RuntimeError as e:
            if 'parse entities' not in str(e):
                raise
        plain = html.unescape(re.sub(r'</?[bi]>', '', part))
        return self.call('sendMessage', chat_id=self.chat, text=plain, disable_web_page_preview=True, **extra)['message_id']


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


def params(text):
    """A request's parameters (TZ-42): {'capital', 'risk', 'total', 'stop', 'n', 'set' - the names the text gave}, each the model's
    default unless the text names it. «риск X», «лимит X» («всего X»), «стоп X» and «топ N» name theirs; of the other numbers the
    first of 100 or more is the capital and the first below 100 the risk, as TZ-37 read them; 15 000 reads 15000, and 10k, 10к and
    10 тыс read 10000. An override narrows a limit and never widens it: the risk at most the rule's 1 %, the total at most 10 %, the
    stop at most 14 %, N at most 7; the capital 100 to 10,000,000 USDT, the risk at least 0.05 %, the total 0.5 %, the stop 2 %, N 1."""
    s = re.sub(r'@\w+', ' ', text or '')
    s = re.sub(r'(?<=\d)[ \u00a0\u202f](?=\d{3}(?!\d))', '', s)
    s = re.sub(r'(\d+(?:[.,]\d+)?)[ \u00a0]?(?:тыс\.?|[кk])(?![^\W\d_])',
               lambda m: f"{float(m.group(1).replace(',', '.')) * 1000:.0f}", s, flags=re.I)
    got = {}
    m = TOPN.search(s)
    if m:
        got['n'] = int(m.group(1))
        s = s[:m.start()] + ' ' + s[m.end():]
    for name, rx in KEYWORDS:
        m = rx.search(s)
        if m:
            got[name] = float(m.group(1).replace(',', '.'))
            s = s[:m.start()] + ' ' + s[m.end():]
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', s)]
    big = next((x for x in nums if x >= 100), None)
    small = next((x for x in nums if x < 100), None)
    if big is not None:
        got['capital'] = big
    if small is not None and 'risk' not in got:
        got['risk'] = small
    return {'capital': min(max(got.get('capital', CAPITAL), 100.0), 10_000_000.0),
            'risk': min(max(got.get('risk', adv3.RISK), 0.05), adv3.RISK_MAX),
            'total': min(max(got.get('total', RISK_TOTAL), 0.5), RISK_TOTAL),
            'stop': min(max(got.get('stop', STOP_MAX), 2.0), STOP_MAX),
            'n': min(max(int(got.get('n', NEW_MAX)), 1), NEW_MAX), 'set': sorted(got)}


def route(text):
    """(kind, argument) of a text (TZ-42): ('signal', params(text)) for «сигнал …» and «топ N …»; ('registry', None) for «реестр»;
    ('ranking', n) for «рейтинг [N]», n 1 to RANK_MAX, default RANK_LIST; ('assess', None) for «оценка»; ('help', None) for «помощь»,
    /start and the like; None where the text is none of them."""
    text = text or ''
    m = HEAD.match(text)
    if not m:
        return None
    word = m.group(1).lower()
    if word in ASSESS:
        return ('assess', None)
    if word in REGISTRY:
        return ('registry', None)
    if word in HELPS:
        return ('help', None)
    if word in RANKING:
        nums = re.findall(r'\d+', text[m.end():])
        return ('ranking', min(max(int(nums[0]), 1), RANK_MAX) if nums else RANK_LIST)
    if word in OPEN:
        return ('signal', params(text))
    return None


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


def strong_all(rep):
    """STRONG at every rank (TZ-40): every coin of the rule's order whose four signs agree with its side and whose |z| is at least
    the rule's STRONG_Z - the frozen rule's condition without its TOP-3, so that its members among the TOP-3 are the report's
    STRONG. In the rule's order."""
    rows = rep['rows']
    return [coin for coin in ranked(rep) if rows[coin].get('sum') == 4 * rows[coin]['signal'] and abs(rows[coin]['z']) >= adv3.STRONG_Z]


def liquidity(coin, now_ms):
    """The mean quote volume in USDT of the coin's last LIQ_DAYS closed days, from fapi.binance.com, or None."""
    try:
        rows = adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval='1d', limit=LIQ_DAYS + 1)
        vols = [float(r[7]) for r in rows if int(r[6]) < now_ms][-LIQ_DAYS:]
        return sum(vols) / len(vols) if vols else None
    except Exception as e:
        log('liquidity failed:', coin, repr(e)[:200])
        return None


def volumes(coins, now_ms):
    """{coin: liquidity(coin, now_ms)} for coins, six requests at a time (TZ-40: an allocation reads every STRONG coin's)."""
    with ThreadPoolExecutor(6) as pool:
        return dict(zip(coins, pool.map(lambda coin: liquidity(coin, now_ms), coins)))


# ---- time ----------------------------------------------------------------------------------------------------------

def ms_at(t):
    """A datetime as epoch milliseconds."""
    return int(t.timestamp() * 1000)


def iso(ms):
    """Epoch milliseconds as an ISO instant in UTC, to the second."""
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).isoformat(timespec='seconds')


def from_iso(text):
    """An ISO instant as epoch milliseconds."""
    return int(dt.datetime.fromisoformat(text).timestamp() * 1000)


def day_ms(day):
    """The epoch milliseconds of a UTC day's 00:00."""
    return int(dt.datetime.combine(day, dt.time(0), tzinfo=dt.timezone.utc).timestamp() * 1000)


def ceil5(ms):
    """The first 5-minute candle's open at or after ms."""
    return -(-int(ms) // K5_MS) * K5_MS


def ceil1(ms):
    """The first 1-minute candle's open at or after ms."""
    return -(-int(ms) // K1_MS) * K1_MS


def second(ms):
    """ms to its whole second, as an event's instant is written: a signal's issue, its place and its fill rest on the same instant."""
    return int(ms) - int(ms) % 1000


def bat(text):
    """An ISO instant as dd.mm HH:MM in Batumi."""
    return (dt.datetime.fromisoformat(text) + BATUMI).strftime('%d.%m %H:%M')


# ---- the registry of STRONG signals (TZ-42) -------------------------------------------------------------------------

def line_hash(line):
    return hashlib.sha256(line.encode('utf-8')).hexdigest()


def event_line(ev):
    """An event as its one line: compact JSON, keys sorted, Cyrillic as it is."""
    return json.dumps(ev, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def base_fund(_day):
    """The rule's funding where the source served none: +0.01 % per 8 h, three settlements a day (RULE-ADV-3)."""
    return 3 * adv3.BASE_F


class Registry:
    """The STRONG signals the bot published (TZ-42): registry.jsonl in its directory, one event a line - seed, open, fill, target,
    stop, exit, expire - each with its number n, the instant it was written (at) and the SHA-256 of the line before it (prev, GENESIS
    for the first), so that a line changed, inserted or removed breaks the chain at the line after it; and registry-state.json, each
    open signal's place on the 5-minute candles and the last event a message announced, written in one rename and rebuilt from the
    log where it is lost. A torn last line - a write cut short - is cut at load. The signals are derived from the events alone."""

    def __init__(self, folder):
        self.path, self.state_path = os.path.join(folder, REG_FILE), os.path.join(folder, REG_STATE)
        self.events, self.sig, self.cursor = [], {}, {}
        self.head, self.broken, self.torn, self.announced = GENESIS, None, 0, 0
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'rb') as fh:
                data = fh.read()
            if data and not data.endswith(b'\n'):
                cut = data.rfind(b'\n') + 1
                self.torn = len(data) - cut
                with open(self.path, 'r+b') as fh:
                    fh.truncate(cut)
                data = data[:cut]
            prev = GENESIS
            for raw in data.decode('utf-8').splitlines():
                try:
                    ev = json.loads(raw)
                except ValueError:
                    ev = None
                if not isinstance(ev, dict):
                    self.broken = self.broken or len(self.events) + 1
                elif ev.get('prev') != prev or ev.get('n') != len(self.events) + 1:
                    self.broken = self.broken or len(self.events) + 1
                if isinstance(ev, dict):
                    self.events.append(ev)
                    self.apply(ev)
                prev = line_hash(raw)
            self.head = prev
        if os.path.exists(self.state_path):
            try:
                st = json.loads(read(self.state_path))
                self.cursor = {int(k): dict(v) for k, v in st['cursor'].items()}
                self.announced = int(st['announced'])
            except (KeyError, TypeError, ValueError, AttributeError):
                self.cursor, self.announced = {}, len(self.events)
        else:
            self.announced = len(self.events)

    def apply(self, ev):
        """One event's effect on the signals."""
        kind, i = ev.get('type'), ev.get('id')
        if kind == 'open':
            self.sig[i] = new_signal(ev)
        elif i in self.sig:
            advance(self.sig[i], ev)

    def append(self, ev, at):
        """One event written: its number, the instant it is written and the chain's prev added, the line flushed to the disk before
        it is applied. Returns the event as written."""
        ev = dict(ev, n=len(self.events) + 1, prev=self.head, at=at.isoformat(timespec='seconds'))
        line = event_line(ev)
        with open(self.path, 'a', encoding='utf-8') as fh:
            fh.write(line + '\n')
            fh.flush()
            os.fsync(fh.fileno())
        self.events.append(ev)
        self.apply(ev)
        self.head = line_hash(line)
        return ev

    def save_state(self):
        put(self.state_path, json.dumps({'cursor': {str(k): v for k, v in sorted(self.cursor.items())},
                                         'announced': self.announced}, sort_keys=True))

    def next_id(self):
        return 1 + max(self.sig, default=0)

    def cursor_of(self, s):
        """A signal's place on its candles: the first minute not yet walked as closed (t), the last daily close its walk passed (b) and
        its largest favourable excursion in R (mfe); from its issue where none is kept - the first 1-minute candle at or after it."""
        cur = self.cursor.get(s['id'])
        if cur is None:
            issued = from_iso(s['utc'])
            cur = {'t': ceil1(issued), 'b': issued, 'mfe': 0.0}
        return cur

    def live(self):
        """The signals open or waiting for their limit, by number."""
        return [s for _i, s in sorted(self.sig.items()) if s['status'] in ('pending', 'open')]


def new_signal(ev):
    """A signal from its open event: waiting for its entry, no target, no end."""
    s = dict(ev, status='pending', fill=None, fill_utc=None, hit=0, hits={}, exit=None, exit_utc=None, why=None, R=None, pnl=None)
    for k in ('type', 'n', 'at', 'prev'):
        s.pop(k, None)
    return s


def advance(s, ev):
    """One event's effect on its signal: a fill opens it, a target raises its hit, a stop or the rule's exit closes it, an expiry ends
    a limit not filled."""
    kind = ev.get('type')
    if kind == 'fill':
        s.update(status='open', fill=ev['price'], fill_utc=ev['utc'])
    elif kind == 'target':
        s['hit'] = max(s['hit'], ev['k'])
        s['hits'][str(ev['k'])] = ev['utc']
    elif kind in ('stop', 'exit'):
        s.update(status='closed', exit=ev['price'], exit_utc=ev['utc'], why='stop' if kind == 'stop' else 'signal', R=ev['R'], pnl=ev['pnl'])
    elif kind == 'expire':
        s.update(status='expired', exit_utc=ev['utc'], why='expire')


def status_of(s):
    """The Boss's status of a signal (his specification of 2026-11-05, §3): PENDING, ACTIVE or TARGET k REACHED while it lives; at
    its end TARGET 3 REACHED, PARTIAL TARGET COMPLETION (a target and not the third), STOPPED OUT or INVALIDATED (the rule's exit at a
    close, before a target), EXPIRED (a limit not filled by its validity)."""
    if s['status'] == 'pending':
        return 'PENDING'
    if s['status'] == 'expired':
        return 'EXPIRED'
    if s['status'] == 'open':
        return 'TARGET %d REACHED' % s['hit'] if s['hit'] else 'ACTIVE'
    if s['hit'] == 3:
        return 'TARGET 3 REACHED'
    if s['hit']:
        return 'PARTIAL TARGET COMPLETION'
    return 'STOPPED OUT' if s['why'] == 'stop' else 'INVALIDATED'


def open_risk(reg, skip_close=None):
    """The risk at their stops of the signals open or waiting, in percent of each one's capital, by side - those of skip_close left
    out where it is given: {1: the longs', -1: the shorts'}."""
    out = {1: 0.0, -1: 0.0}
    for s in reg.live():
        if s['close_of'] != skip_close:
            out[s['side']] += s['risk_pct']
    return out


def klines(coin, start_ms, now_ms, step=K5_MS, count=None):
    """The coin's candles of step ms - 5 minutes, or 1 - from fapi.binance.com from the one opening at start_ms on: count of them in
    one request where count is given, else page after page of K5_PAGE to now_ms. [(open ms, open, high, low, close, closed)], closed
    where the candle's close time is before now_ms; a start after now_ms asks nothing, no candle opening there yet."""
    out, t = [], int(start_ms)
    for _ in range(0 if t > now_ms else 1 if count else 400):
        n = count or K5_PAGE
        rows = adv3.fapi('/fapi/v1/klines', symbol=coin + 'USDT', interval=INTERVAL[step], startTime=t, limit=n)
        for r in rows:
            if int(r[0]) >= t:
                out.append((int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), int(r[6]) < now_ms))
        if len(rows) < n:
            break
        t = int(rows[-1][0]) + step
        if t > now_ms:
            break
    return out


def first_window(coin, cur, now_ms):
    """A signal's first minutes on 1-minute candles (TZ-42): where its place is not on a 5-minute boundary - it was issued inside a
    5-minute candle, whose range mixes the minutes before the issue with those after it - the 1-minute candles from its place to the
    next boundary, in one request; else none."""
    t = cur['t']
    return klines(coin, t, now_ms, K1_MS, (ceil5(t) - t) // K1_MS) if t % K5_MS else []


def walk(s, cur, c, fund, k5, until=None, k1=()):
    """One signal walked forward on its coin's candles (TZ-42), in time order: the events of its fill, its targets and its end, and
    its new place. s is the signal; cur its place; c the coin's closed daily candles; fund, day -> the day's funding sum; k1 the
    1-minute candles of its first minutes (first_window), then k5 the 5-minute ones, each [(open ms, o, h, l, c, closed)]; until, where
    given, the instant past which nothing is walked - no candle closing after it is read. Each daily close the walk passes
    ends a filled signal whose rule signal at that close is not its side, at that close's price (the rule's exit, adv3.signal); the
    validity's end - the close after the card's - ends a limit not yet filled, whether its daily candle is served or not. Each candle fills a waiting limit it reaches - at the limit,
    or at the open where the open is already past it - and then reads only the stop; a filled signal's candle credits each target its
    open is already past, then ends the signal at the stop it reaches - at the open where the open is already beyond the stop - a target
    touched later in that candle not credited; else it credits each target it reaches. A candle not yet closed is read and not walked
    past. The result of an end: the move from the fill, both sides' costs (adv3.COST) and the funding of every close held, per unit,
    in R of the planned risk |entry - stop| and in USDT at the signal's quantity."""
    side, E, S, T = s['side'], s['entry'], s['stop'], s['targets']
    days = sorted(c)
    closes = [c[d][3] for d in days]
    D = dt.date.fromisoformat(s['close_of'])
    valid = from_iso(s['valid'])
    t, b, mfe = cur['t'], cur['b'], cur.get('mfe', 0.0)
    status, hit, fp = s['status'], s['hit'], s['fill']
    fill_ms = from_iso(s['fill_utc']) if s['fill_utc'] else None
    risk = abs(E - S)
    bounds = [(day_ms(d) + DAY_MS, i) for i, d in enumerate(days) if d > D and day_ms(d) + DAY_MS > b]
    out = []

    def funding(end_ms):
        return sum(side * fund(d) * closes[i] for i, d in enumerate(days) if fill_ms < day_ms(d) + DAY_MS <= end_ms)

    def end(kind, at_ms, X):
        unit_ = side * (X - fp) - adv3.COST * (fp + X) - funding(at_ms)
        out.append({'type': kind, 'id': s['id'], 'utc': iso(at_ms), 'price': X, 'R': unit_ / risk, 'pnl': unit_ * s['qty']})

    def at_close(B, i):
        nonlocal status
        if status == 'open' and adv3.signal(days, closes, i) != side:
            end('exit', B, closes[i])
            status = 'closed'
        return status not in ('open', 'pending')

    def expire():
        nonlocal status
        out.append({'type': 'expire', 'id': s['id'], 'utc': iso(valid)})
        status = 'expired'

    def place():
        return {'t': t, 'b': b, 'mfe': mfe}

    bi = 0
    for width, (o_ms, o, h, lo, _cl, closed) in [(K1_MS, x) for x in k1] + [(K5_MS, x) for x in k5]:
        if o_ms < t:
            continue
        if until is not None and o_ms + width > until:
            break
        while bi < len(bounds) and bounds[bi][0] <= o_ms:
            B, i = bounds[bi]
            bi, b = bi + 1, B
            if at_close(B, i):
                return out, place()
        if status == 'pending' and o_ms >= valid:
            expire()
            return out, place()
        if status == 'pending':
            if (lo <= E) if side > 0 else (h >= E):
                fp = min(o, E) if side > 0 else max(o, E)
                fill_ms, status = o_ms, 'open'
                out.append({'type': 'fill', 'id': s['id'], 'utc': iso(o_ms), 'price': fp})
                if (lo <= S) if side > 0 else (h >= S):
                    end('stop', o_ms, o if ((o <= S) if side > 0 else (o >= S)) else S)
                    return out, place()
        else:
            for k in (1, 2, 3):
                if k > hit and ((o >= T[k - 1]) if side > 0 else (o <= T[k - 1])):
                    out.append({'type': 'target', 'id': s['id'], 'utc': iso(o_ms), 'k': k, 'price': T[k - 1]})
                    hit = k
            gap = (o <= S) if side > 0 else (o >= S)
            if gap or ((lo <= S) if side > 0 else (h >= S)):
                end('stop', o_ms, o if gap else S)
                return out, place()
            for k in (1, 2, 3):
                if k > hit and ((h >= T[k - 1]) if side > 0 else (lo <= T[k - 1])):
                    out.append({'type': 'target', 'id': s['id'], 'utc': iso(o_ms), 'k': k, 'price': T[k - 1]})
                    hit = k
            mfe = max(mfe, side * ((h if side > 0 else lo) - fp) / risk)
        if closed:
            t = o_ms + width
    while bi < len(bounds) and bounds[bi][0] <= t and (until is None or bounds[bi][0] <= until):
        B, i = bounds[bi]
        bi, b = bi + 1, B
        if at_close(B, i):
            return out, place()
    if status == 'pending' and t >= valid and (until is None or valid <= until):
        expire()
    return out, place()


def reconcile(reg, cs, funds, now_ms, at):
    """Every signal open or waiting walked to now (TZ-42): each coin's 5-minute candles fetched once from the earliest 5-minute
    boundary any of its signals' places reaches, and a signal's first minutes on their 1-minute candles where its place is still among
    them; the events appended in time order, the places saved. A coin or a signal whose candles fail stays where it was, logged.
    Returns the events appended."""
    groups = {}
    for s in reg.live():
        groups.setdefault(s['coin'], []).append(s)
    new = []
    for coin in sorted(groups, key=adv3.COINS.index):
        sigs = groups[coin]
        try:
            k5 = klines(coin, min(ceil5(reg.cursor_of(s)['t']) for s in sigs), now_ms)
        except Exception as e:
            log('5-minute candles failed:', coin, repr(e)[:200])
            continue
        for s in sigs:
            cur = reg.cursor_of(s)
            try:
                k1 = first_window(coin, cur, now_ms)
            except Exception as e:
                log('1-minute candles failed:', coin, repr(e)[:200])
                continue
            evs, reg.cursor[s['id']] = walk(s, cur, cs.get(coin) or {}, funds.get(coin) or base_fund, k5, k1=k1)
            new += evs
    new.sort(key=lambda e: (e['utc'], e['id']))
    written = [reg.append(e, at) for e in new]
    reg.save_state()
    return written


def seed(reg, cs, funds, now_ms, at):
    """The registry's first event, and the STRONG signals the journal's records published before it (TZ-42): every STRONG card with an
    entry, at market or as a limit, of a daily, request, allocation or check record - of an allocation only the coins it placed - in
    the order the records were written, each a signal issued at its record's instant, to the second, unless its coin holds a signal
    still open then, walked on its candles to that instant: a card repeated within one signal's life is that signal shown again. Each
    is sized as one trade at the default risk on the default capital and marked legacy. The cards are read one coin at a time - its
    candles fetched once and let go before the next coin's - and the signals and their events written in the order of the cards.
    Returns the signals opened."""
    path = os.path.join(STATE, 'journal.jsonl')
    sha = None
    if os.path.exists(path):
        h = hashlib.sha256()
        with open(path, 'rb') as fh:
            for block in iter(lambda: fh.read(1 << 20), b''):
                h.update(block)
        sha = h.hexdigest()
    records, cards = 0, []
    for rec in journal_records():
        records += 1
        kind = rec.get('kind')
        if kind not in ('daily', 'request', 'alloc', 'check'):
            continue
        try:
            t_ms, close_of = second(from_iso(rec['utc'])), str(dt.date.fromisoformat(rec['close_of']))
        except (KeyError, TypeError, ValueError):
            continue
        placed = None
        if kind == 'alloc' and isinstance(rec.get('alloc'), dict):
            placed = {x.get('coin') for x in (rec['alloc'].get('items') or []) + (rec['alloc'].get('more') or []) if isinstance(x, dict)}
        state = rec.get('state') if isinstance(rec.get('state'), dict) else {}
        btc = (rec.get('signals') or {}).get('BTC') if isinstance(rec.get('signals'), dict) else None
        for cd in rec.get('cards') or []:
            try:
                if (not cd.get('strong') or cd.get('mode') not in ('market', 'limit') or cd.get('entry') is None
                        or (placed is not None and cd['coin'] not in placed)):
                    continue
                coin, side = cd['coin'], int(cd['side'])
                E, S, C, U = float(cd['entry']), float(cd['stop']), float(cd['close']), float(cd['U'])
                T = [float(x) for x in cd['targets']]
                if coin not in adv3.COINS or side not in (1, -1) or len(T) != 3 or min(E, S, C, U) <= 0 or side * (E - S) <= 0:
                    continue
            except (AttributeError, KeyError, TypeError, ValueError):
                continue
            st = state.get(coin) if isinstance(state.get(coin), dict) else {}
            cards.append((t_ms, coin, side, close_of, cd, st, kind, btc))
    reg.append({'type': 'seed', 'utc': iso(now_ms), 'journal_sha': sha, 'records': records, 'cards': len(cards)}, at)
    cards.sort(key=lambda x: x[0])
    acts = []   # (the card's place, 0 an event of the walk to it - 1 the open it makes, the signal, the event)
    for coin in sorted({x[1] for x in cards}, key=adv3.COINS.index):
        mine = [(k, x) for k, x in enumerate(cards) if x[1] == coin]
        try:
            k5 = klines(coin, ceil5(mine[0][1][0]), now_ms)
        except Exception as e:
            log('5-minute candles failed:', coin, repr(e)[:200])
            k5 = None
        sigs = []
        for k, (t_ms, _coin, side, close_of, cd, st, kind, btc) in mine:
            if any(s['side'] == side and s['close_of'] == close_of for s in sigs):
                continue
            live = [s for s in sigs if s['status'] in ('pending', 'open')]
            if live and k5 is not None:
                for s in live:
                    try:
                        k1 = first_window(coin, s['place'], now_ms)
                    except Exception as e:
                        log('1-minute candles failed:', coin, repr(e)[:200])
                        continue
                    evs, s['place'] = walk(s, s['place'], cs.get(coin) or {}, funds.get(coin) or base_fund, k5, until=t_ms, k1=k1)
                    for e in evs:
                        advance(s, e)
                        acts.append((k, 0, s, e))
                live = [s for s in sigs if s['status'] in ('pending', 'open')]
            if live:
                continue
            E, S = float(cd['entry']), float(cd['stop'])
            d = abs(E - S) / E
            pos, _why = position({'stop_pct': 100 * d, 'leverage': min(20, math.floor(1 / (1.5 * d + 0.01))), 'entry': E},
                                 adv3.RISK, CAPITAL, None)
            if pos is None:
                continue
            D = dt.date.fromisoformat(close_of)
            s = new_signal({'type': 'open', 'id': None, 'utc': iso(t_ms), 'coin': coin, 'side': side, 'close_of': close_of,
                            'source': 'journal:' + kind, 'mode': cd['mode'], 'entry': E, 'stop': S, 'targets': [float(x) for x in cd['targets']],
                            'close': float(cd['close']), 'U': float(cd['U']), 'z': st.get('z'), 'sum': st.get('sum'), 'rank': cd.get('rank'),
                            'since': cd.get('since'), 'btc': btc, 'breadth': None, 'valid': iso(day_ms(D + 2 * adv3.DAY)), 'capital': CAPITAL,
                            'risk_pct': pos['risk_pct'], 'loss': pos['loss'], 'notional': pos['notional'], 'qty': pos['qty'],
                            'leverage': pos['leverage'], 'margin': pos['margin'], 'legacy': True})
            if cd['mode'] == 'market':
                advance(s, {'type': 'fill', 'price': E, 'utc': iso(t_ms)})
            s['place'] = {'t': ceil1(t_ms), 'b': t_ms, 'mfe': 0.0}
            sigs.append(s)
            acts.append((k, 1, s, None))
    acts.sort(key=lambda a: (a[0], a[1]))
    opened = []
    for _k, what, s, e in acts:
        if what == 1:
            s['id'] = reg.next_id()
            reg.append({k: s[k] for k in LEGACY_KEYS} | {'type': 'open', 'id': s['id']}, at)
            if s['mode'] == 'market':
                reg.append({'type': 'fill', 'id': s['id'], 'utc': s['utc'], 'price': s['entry']}, at)
            opened.append(s)
        else:
            reg.append(dict(e, id=s['id']), at)
    for s in opened:
        reg.cursor[s['id']] = s['place']
    reg.save_state()
    return len(opened)


# ---- the plan: the STRONG signals of a close, their positions within the limits (TZ-42) --------------------------------

def notional_of(cd, risk_pct, capital, volume):
    """The notional the loss at the stop allows at risk_pct percent of the capital (TZ-42), both sides' costs included, at most LIQ_FRAC
    of the coin's mean daily volume where known, in whole USDT rounded down: (notional, the loss per USDT of it, whether the volume
    capped it)."""
    rate = cd['stop_pct'] / 100 + 2 * adv3.COST
    raw = risk_pct / 100 * capital / rate
    capped = bool(volume) and raw > LIQ_FRAC * volume
    return math.floor(LIQ_FRAC * volume if capped else raw), rate, capped


def position(cd, risk_pct, capital, volume):
    """One position at risk_pct percent of the capital (TZ-42): notional_of's notional; the leverage the rule's ceiling - the card's -
    lowered only to keep the margin at MARGIN_MIN percent of the capital or more, never raised; a notional under that floor is no
    position, for the risk is never raised to meet it; the margin at most MARGIN_EXC percent of the capital in whole USDT, the notional
    cut where it would pass it. (position, None) or (None, the reason)."""
    notional, rate, capped = notional_of(cd, risk_pct, capital, volume)
    floor_m = MARGIN_MIN / 100 * capital
    if cd['leverage'] < 1:
        return None, 'плечо правила меньше 1×'
    if notional < floor_m:
        return None, 'позиция меньше минимальной маржи %s USDT' % adv3.usdt(floor_m) + (' — по ликвидности' if capped else '')
    lev = min(cd['leverage'], math.floor(notional / floor_m))
    margin = math.ceil(notional / lev)
    top = math.floor(MARGIN_EXC / 100 * capital)
    cut = margin > top
    if cut:
        notional, margin = top * lev, top
    loss = notional * rate
    return {'notional': notional, 'leverage': lev, 'lmax': cd['leverage'], 'margin': margin, 'loss': loss,
            'risk_pct': 100 * loss / capital, 'qty': notional / cd['entry'], 'capped': capped,
            'over': margin > MARGIN_MAX / 100 * capital, 'cut': cut}, None


def allocate(items, prm, room, liq):
    """The risk shared by strength (TZ-42): each item without a reason against it takes a share min(|z|, Z_CAP) over all of them -
    k times prm's risk times its share, at most the rule's RISK_MAX - then, in the rule's order, that risk or what the room still
    holds, sized by position(). An item gets a reason and a code where it has no position: 'room' where the room cut its risk, else
    'margin', its position under the margin's floor. Each item sized gets pos, with its wanted risk and whether the room cut it."""
    live = [it for it in items if not it.get('why')]
    if not live:
        return
    q = [min(abs(it['card']['z']), Z_CAP) for it in live]
    for it, qi in zip(live, q):
        want = min(adv3.RISK_MAX, len(live) * prm['risk'] * qi / sum(q))
        take = max(0.0, min(want, room))
        pos, why = position(it['card'], take, prm['capital'], liq.get(it['coin'])) if take > 1e-9 else (None, None)
        if pos is None:
            if take < want - 1e-9:
                it['code'], it['why'], it['detail'] = 'room', 'лимит общего риска %s%% исчерпан' % pct0(prm['total']), ''
            else:
                it['code'], it['why'], it['detail'] = 'margin', why, '%s USDT' % adv3.usdt(
                    notional_of(it['card'], take, prm['capital'], liq.get(it['coin']))[0])
            continue
        pos.update(want=want, short=take < want - 1e-9)
        it['pos'] = pos
        room -= pos['risk_pct']


def pct0(x):
    """A percent without a needless ',0': 10 -> '10', 12.5 -> '12,5'."""
    return adv3.pct(x, 1).replace(',0', '')


def candidates(rep, reg, prm):
    """The STRONG coins of the report's close at prm (TZ-42), in the rule's order: the signals of this close the registry holds open or
    waiting ('mine'), the coins that may be new - current prices, an entry, a stop within prm's limit, no signal of the coin open from
    an earlier close and none of this close already ended - and the rest named, (coin, side, code, reason). Each item {'coin', 'side',
    'rank', 'card' at prm's capital and risk, 'sig' - the registry's or None - 'code' and 'why' - None, or why it has no position now}.
    A coin open from an earlier close belongs to the open list, not to the candidates."""
    rows, close_of = rep['rows'], rep['close_of']
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    live = {s['coin']: s for s in reg.live()}
    this = {(s['coin'], s['side']): s for s in reg.sig.values() if s['close_of'] == close_of}
    mine, new, excluded = [], [], []
    for coin in strong_all(rep):
        side = rows[coin]['signal']
        if coin in live and live[coin]['close_of'] != close_of:
            continue
        s = this.get((coin, side))
        if s is not None and s['status'] not in ('pending', 'open'):
            excluded.append((coin, side, 'ended', 'сигнал этого закрытия уже завершён', '#%d %s' % (s['id'], LABEL[status_of(s)])))
            continue
        it = carded(rep, coin, rank[coin], prm, s)
        if s is not None:
            mine.append(it)
        elif it['why']:
            excluded.append((coin, side, it['code'], it['why'], it['detail']))
        else:
            new.append(it)
    return mine, new, excluded


def carded(rep, coin, rank, prm, sig=None):
    """One STRONG coin's item at prm: its card at prm's capital and risk, and the reason, if any, it has no position now - no current
    price, no entry, a stop beyond prm's limit."""
    row = rep['rows'][coin]
    cd = dict(adv3.card(coin, row, True, prm['capital'], prm['risk']), sum=row.get('sum'))
    code = why = None
    detail = ''
    if not rep['marks_ok']:
        code, why = 'marks', 'нет текущей цены Binance'
    elif cd['mode'] == 'none':
        code, why = 'near', 'цена у стопа — входа нет'
    elif cd['stop_pct'] > prm['stop'] + 1e-9:
        code, why, detail = 'stop', 'стоп дальше %s%%' % pct0(prm['stop']), '%s%%' % adv3.pct(cd['stop_pct'])
    return {'coin': coin, 'side': row['signal'], 'rank': rank, 'card': cd, 'sig': sig, 'code': code, 'why': why, 'detail': detail}


def model_plan(rep, reg, liq):
    """The model's new signals at this moment (TZ-42): the new candidates at the defaults, the first NEW_MAX a close counting those the
    registry holds of this close, sized by allocate within the room every open signal leaves under RISK_TOTAL; with the signals of
    this close the registry holds open ('mine') and the coins not taken, each (coin, side, code, reason, detail) - those beyond the
    first NEW_MAX the room's where the room stopped one of the first, else the count's."""
    mine, new, excluded = candidates(rep, reg, DEFAULTS)
    allowed = max(0, NEW_MAX - sum(1 for s in reg.sig.values() if s['close_of'] == rep['close_of']))
    risk = open_risk(reg)
    head = new[:allowed]
    allocate(head, DEFAULTS, RISK_TOTAL - risk[1] - risk[-1], liq)
    excluded += [(it['coin'], it['side'], it['code'], it['why'], it['detail']) for it in head if it.get('why')]
    full = any(it.get('code') == 'room' for it in head)
    for it in new[allowed:]:
        if full:
            excluded.append((it['coin'], it['side'], 'room', 'лимит общего риска %s%% исчерпан' % pct0(RISK_TOTAL), ''))
        else:
            excluded.append((it['coin'], it['side'], 'count', 'сверх %d новых сигналов за закрытие' % NEW_MAX, ''))
    return {'new': [it for it in head if it.get('pos')], 'mine': mine, 'excluded': excluded, 'risk': risk}


def view_plan(rep, reg, liq, prm, model):
    """A request's plan (TZ-42): the signals of this close the registry holds open and the model's new ones, carded at prm, in the
    rule's order, those beyond prm's N named; a coin prm excludes - beyond its stop limit, without an entry - named with prm's reason,
    one the model did not take with the model's; the rest sized at prm, the risk shared by strength within the room the signals of
    earlier closes leave under prm's total. A signal of the registry stays in the plan without a position where it has none now, its
    card saying why; the request writes no signal the model did not take."""
    mine, new, excluded = candidates(rep, reg, prm)
    taken = {it['coin'] for it in model['new']}
    why = {c: (code, w, detail) for c, _s, code, w, detail in model['excluded']}
    for it in new:
        if it['coin'] not in taken:
            code, w, detail = why.get(it['coin'], ('model', 'модель не взяла', ''))
            excluded.append((it['coin'], it['side'], code, w, detail))
    items = sorted(mine + [it for it in new if it['coin'] in taken], key=lambda x: x['rank'])
    for it in items[prm['n']:]:
        excluded.append((it['coin'], it['side'], 'top', 'сверх топ %d запроса' % prm['n'], ''))
    keep = items[:prm['n']]
    older = open_risk(reg, rep['close_of'])
    allocate(keep, prm, prm['total'] - older[1] - older[-1], liq)
    out = []
    for it in keep:
        if it.get('pos') or it['sig'] is not None:
            out.append(it)
        else:
            excluded.append((it['coin'], it['side'], it['code'], it['why'], it['detail']))
    return {'items': out, 'excluded': excluded, 'older': older}


def register(reg, rep, items, at, source):
    """Each new item written as a signal (TZ-42), in the rule's order: 'open' with its card, its position at the defaults and what it
    rests on - the rule's strength and sum, its rank, the day its rule signal began, BTC's signal, how many coins were STRONG at every
    rank - and, an entry at market, 'fill' at that entry and that instant: a market entry is the price the card published. A limit
    waits for its price until the close after the card's. Returns the ids, which are reg.next_id() onwards."""
    rows, ids = rep['rows'], []
    issued = second(ms_at(at))
    D = dt.date.fromisoformat(rep['close_of'])
    breadth = len(strong_all(rep))
    for it in sorted(items, key=lambda x: x['rank']):
        cd, pos = it['card'], it['pos']
        i = reg.next_id()
        reg.append({'type': 'open', 'id': i, 'utc': iso(issued), 'coin': it['coin'], 'side': it['side'], 'close_of': rep['close_of'],
                    'source': source, 'mode': cd['mode'], 'entry': cd['entry'], 'stop': cd['stop'], 'targets': cd['targets'],
                    'close': cd['close'], 'U': cd['U'], 'z': cd['z'], 'sum': cd['sum'], 'rank': it['rank'], 'since': cd['since'],
                    'btc': (rows.get('BTC') or {}).get('signal'), 'breadth': breadth, 'valid': iso(day_ms(D + 2 * adv3.DAY)),
                    'capital': CAPITAL, 'risk_pct': pos['risk_pct'], 'loss': pos['loss'], 'notional': pos['notional'], 'qty': pos['qty'],
                    'leverage': pos['leverage'], 'margin': pos['margin'], 'legacy': False}, at)
        if cd['mode'] == 'market':
            reg.append({'type': 'fill', 'id': i, 'utc': iso(issued), 'price': cd['entry']}, at)
        reg.cursor[i] = {'t': ceil1(issued), 'b': issued, 'mfe': 0.0}
        ids.append(i)
    reg.save_state()
    return ids


def ensure(reg, data, now):
    """The registry brought to now: seeded from the journal where it holds no event yet - its events then counted announced, the
    history's, never news - and every signal open or waiting walked to now. Returns the signals the seed opened, or None."""
    cs, funds = data.fresh()
    now_ms = ms_at(now)
    opened = None
    if not reg.events:
        opened = seed(reg, cs, funds, now_ms, now)
    reconcile(reg, cs, funds, now_ms, now)
    if opened is not None:
        reg.announced = len(reg.events)
        reg.save_state()
    return opened


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
    check and that day's signal check is not done, the signal check - the fact slot repeats the signal slot where it failed."""
    last = latest_slot(now)
    if done is not None and slot_key(done) >= slot_key(last):
        return None
    if last[1] == 'fact' and (done is None or slot_key(done) < slot_key((last[0], 'signal'))):
        return last[0], 'signal'
    return last


def done_after(slot, now):
    """What a check marks done: itself, or - a signal check that ends at or after its day's fact slot - that day's fact check too."""
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


# ---- the journal ---------------------------------------------------------------------------------------------------

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


def last_check():
    """The journal's last check record, or None, read in one pass that keeps it alone."""
    prev = None
    for rec in journal_records():
        if rec.get('kind') == 'check':
            prev = rec
    return prev


def append(rec):
    with open(os.path.join(STATE, 'journal.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + '\n')


def base_record(kind, rep, ids, at):
    """A journal record: its instant, kind, rule, close, the report's deposit and risk, TOP-3, STRONG, message ids and every coin's
    signal."""
    return {'utc': at.isoformat(timespec='seconds'), 'kind': kind, 'rule': rep['rule'], 'close_of': rep['close_of'],
            'deposit': rep['deposit'], 'risk_pct': rep['risk_pct'], 'top': rep['top'], 'strong': rep['strong'], 'message_ids': ids,
            'signals': {k: v.get('signal') for k, v in rep['rows'].items()}}


def item_record(it, i=None):
    """A plan item as a record holds it: its card's fields, its rank, its signal's number and its position."""
    pos = it.get('pos')
    return dict({k: it['card'].get(k) for k in CARD_KEYS}, rank=it['rank'], id=i if i is not None else (it['sig'] or {}).get('id'),
                position={k: pos[k] for k in ('notional', 'leverage', 'margin', 'loss', 'risk_pct')} if pos else None, why=it.get('why'))


# ---- what a message says ------------------------------------------------------------------------------------------

SHOWN = ('fill', 'target', 'stop', 'exit', 'expire')
LOUD = ('stop', 'exit', 'expire')


def signed_usdt(x):
    return ('+' if x >= 0 else '−') + adv3.usdt(abs(x))


def sg(x, places=2):
    """x signed to places decimals, Russian style; a value that rounds to zero is never signed negative."""
    x = round(x, places)
    return adv3.signed(0.0 if x == 0 else x, places)


def footer():
    r = adv3.RELIABILITY
    return f"<i>Уверенность {r}/5 — {adv3.LADDER[r][0]} · размеры — формула Архитектора, не доказана · не инвестиционный совет</i>"


def params_line(prm):
    """The model's parameters a message rests on, and the ones the request overrode."""
    names = {'capital': 'капитал', 'risk': 'риск', 'total': 'лимит', 'stop': 'стоп', 'n': 'топ'}
    pct = adv3.pct
    line = (f"Капитал {adv3.num(prm['capital'], 6)} USDT · риск {pct(prm['risk'])}% · лимит {pct0(prm['total'])}% · "
            f"стоп ≤ {pct0(prm['stop'])}%" + (f" · до {prm['n']} сделок" if 'n' in prm['set'] else ''))
    return line + (' · по запросу: ' + ', '.join(names[k] for k in prm['set']) if prm['set'] else '')


def legend():
    """The targets' line: what the three targets are and how often STRONG trades reached them in TZ-38's history, without survivorship."""
    m = adv3.PIT['strong' if adv3.FACTS['strong'].get('gate_S') == 'NOT DISQUALIFIED' else 'base']['mfe']
    return (f"<i>🎯 — цели +1, +2, +3 U от закрытия; в истории STRONG до них доходили {adv3.pct(100 * m[1], 0)}, "
            f"{adv3.pct(100 * m[2], 0)} и {adv3.pct(100 * m[3], 0)}% сделок</i>")


def card_lines(it, number, new_id=None, mark_new=False):
    """One STRONG item of a plan: its number, coin, side, signal number, rank and strength; entry; stop and targets; and its position
    - the margin, the rule's leverage or less, the notional and the coins, the loss at the stop in USDT and in percent of the capital -
    or why it has none now; a signal of the registry says since when and at what entry it runs."""
    cd, pos, s, side = it['card'], it.get('pos'), it['sig'], it['side']
    price, pct = adv3.price, adv3.pct
    ident = f" #{s['id']}" if s is not None else ((' 🆕' if mark_new else '') + (f" #{new_id}" if new_id else ''))
    lines = [f"{number}) {DOT[side]} <b>{it['coin']} {SIDE[side]}</b>{ident} · ★ ранг {it['rank']}"
             + (' вне ТОП-3' if it['rank'] > adv3.TOP_N else '') + f" · z {sg(cd['z'])}"]
    lo, hi = cd['zone']
    if cd['mode'] == 'market':
        lines.append(f"Вход: <b>по рынку ≈ {price(cd['entry'])}</b> · зона {price(lo)}–{price(hi)}")
    elif cd['mode'] == 'limit':
        lines.append(f"Вход: <b>лимит {price(cd['entry'])}</b> — цена {price(cd['mark'])} ушла от зоны, не догонять")
    else:
        lines.append(f"Вход сейчас: <b>нет</b> — цена {price(cd['mark'])} у стопа")
    if s is not None:
        lines.append(f"Сигнал #{s['id']} с {bat(s['utc'])}: {LABEL[status_of(s)]}" + (f", вход {price(s['fill'])}" if s['fill'] else ''))
    ref = cd['entry'] if cd['entry'] is not None else cd['close']
    lines.append(f"⛔ Стоп <b>{price(cd['stop'])}</b> ({'−' if side > 0 else '+'}{pct(100 * abs(ref - cd['stop']) / ref)}%) · 🎯 "
                 + ' · '.join(price(t) for t in cd['targets']))
    if pos:
        flags = ([' · урезано лимитом риска'] if pos['short'] else []) + ([' · ограничено ликвидностью'] if pos['capped'] else []) \
            + ([' · маржа выше 3,5% капитала — исключение'] if pos['over'] else [])
        lines += [f"Маржа <b>{adv3.usdt(pos['margin'])} USDT</b> · плечо {pos['leverage']}× изол. → позиция {adv3.usdt(pos['notional'])} "
                  f"USDT = {adv3.num(pos['qty'])} {it['coin']}",
                  f"Потеря на стопе <b>{adv3.usdt(pos['loss'])} USDT</b> = {pct(pos['risk_pct'], 2)}% капитала" + ''.join(flags)]
    elif it.get('why'):
        lines.append('Позиции сейчас нет: ' + it['why'])
    return lines


def live_line(s, rows):
    """One signal open or waiting: number, coin, side, the close it is of; its entry, stop, targets reached and where the price
    stands now in R of its planned risk - or the limit it waits for and until when."""
    side, price = s['side'], adv3.price
    head = f"#{s['id']} {DOT[side]} {s['coin']} {SIDE[side]} {adv3.ddmm(s['close_of'])}"
    if s['status'] == 'pending':
        return f"{head} · ждёт лимит {price(s['entry'])} до {bat(s['valid'])} · стоп {price(s['stop'])}"
    mark = (rows.get(s['coin']) or {}).get('mark')
    now = f" · сейчас {sg(side * (mark - s['fill']) / abs(s['entry'] - s['stop']), 1)} R" if mark else ''
    return (f"{head} · вход {price(s['fill'])} · стоп {price(s['stop'])}" + (f" · 🎯{s['hit']}" if s['hit'] else '') + now)


def ended_line(s):
    """One signal ended: number, coin, side, the close it is of; how it ended - the stop, the rule's exit at a close, after which
    target - when, its result in R and in USDT."""
    side, price = s['side'], adv3.price
    head = f"#{s['id']} {DOT[side]} {s['coin']} {SIDE[side]} {adv3.ddmm(s['close_of'])}"
    if s['status'] == 'expired':
        return f"{head} → ⌛ истёк {bat(s['exit_utc'])}: лимит {price(s['entry'])} не исполнен"
    how = '⛔ стоп' if s['why'] == 'stop' else ('🚪 выход по сигналу' if s['hit'] else '🚪 инвалидация — выход по сигналу')
    after = f" после цели {s['hit']}" if s['hit'] else ''
    return f"{head} → {how}{after} {bat(s['exit_utc'])} · {sg(s['R'])} R · {signed_usdt(s['pnl'])} USDT"


def event_lines(evs, reg):
    """The events a message announces, in time order, each with its signal, its price, its instant in Batumi and - an end - its
    result; a limit not filled says to take its order off where it was placed."""
    lines = ['🔔 <b>События</b> · время Батуми']
    price = adv3.price
    for e in evs:
        s = reg.sig.get(e['id'])
        if s is None:
            continue
        who = f"#{s['id']} {s['coin']} {SIDE[s['side']]}"
        if e['type'] == 'fill':
            lines.append(f"✅ {who} — лимит {price(e['price'])} исполнен {bat(e['utc'])}")
        elif e['type'] == 'target':
            lines.append(f"🎯 {who} — цель {e['k']} {price(e['price'])} достигнута {bat(e['utc'])}")
        elif e['type'] == 'stop':
            lines.append(f"⛔ {who} — стоп {price(e['price'])} {bat(e['utc'])} · {sg(e['R'])} R ({signed_usdt(e['pnl'])} USDT)"
                         + (f" · до этого цель {s['hit']}" if s['hit'] else ''))
        elif e['type'] == 'exit':
            day = (dt.datetime.fromisoformat(e['utc']) - dt.timedelta(days=1)).date()
            lines.append(f"🚪 {who} — сигнал закончился на закрытии {day:%d.%m}: выход {price(e['price'])} · {sg(e['R'])} R "
                         f"({signed_usdt(e['pnl'])} USDT)" + (f" · цели {s['hit']}" if s['hit'] else ''))
        elif e['type'] == 'expire':
            lines.append(f"⌛ {who} — лимит {price(s['entry'])} не исполнен до {bat(e['utc'])}: снять ордер, если выставлен")
    return lines


def risk_line(held, new, prm, labels=('открытые', 'новые')):
    """The model's risk at the stops: the signals held and the new ones, in percent of the capital, against the limit, what is left
    in percent and in USDT, and the split by side. held and new are {1: longs, -1: shorts}."""
    pct = adv3.pct
    h, n = held[1] + held[-1], new[1] + new[-1]
    total, free = h + n, max(0.0, prm['total'] - h - n)
    line = f"⚖️ Риск модели: {labels[0]} {pct(h)}%" + (f" + {labels[1]} {pct(n)}% = {pct(total)}%" if n else '')
    line += f" из {pct0(prm['total'])}% · свободно {pct(free)}% = {adv3.usdt(math.floor(free / 100 * prm['capital']))} USDT"
    longs, shorts = held[1] + new[1], held[-1] + new[-1]
    if longs and shorts:
        line += f" · ЛОНГ {pct(longs)}% · ШОРТ {pct(shorts)}%"
    elif total:
        line += ' · все в ' + ('ЛОНГ' if longs else 'ШОРТ')
    return line


def excluded_lines(excluded):
    """The coins not taken, grouped by their reason in the order the reasons first appear: one line a reason, each coin with its
    side's dot and its detail."""
    groups = {}
    for c, s, _code, why, detail in excluded:
        groups.setdefault(why, []).append(f"{DOT[s]}{c}" + (f" {detail}" if detail else ''))
    if not groups:
        return []
    return ['🚫 <b>Не берём</b>'] + [f"· {why} — {', '.join(coins)}" for why, coins in groups.items()]


def chain_line(reg):
    if reg.broken:
        return f"⚠️ Реестр: цепочка нарушена на событии {reg.broken} — записи с него не подтверждены"
    return f"🔐 Реестр: {len(reg.events)} {adv3.plural(len(reg.events), 'событие', 'события', 'событий')} · отпечаток {reg.head[:8]}"


def seed_line(reg, opened):
    """The first message after the registry's seed: what it took from the journal."""
    legacy = [s for s in reg.sig.values() if s.get('legacy')]
    live = sum(s['status'] in ('pending', 'open') for s in legacy)
    ended = sum(s['status'] == 'closed' for s in legacy)
    expired = sum(s['status'] == 'expired' for s in legacy)
    return (f"📒 Реестр создан: из журнала перенесено {opened} {adv3.plural(opened, 'STRONG-сигнал', 'STRONG-сигнала', 'STRONG-сигналов')}"
            f" — открыто {live}, завершено {ended}, истекло {expired}; подробности — «реестр»")


def note_lines(notes):
    return [f"ℹ️ #{i} {coin} {SIDE[side]} — больше не STRONG (сумма знаков {sg(ssum, 0)}, z {sg(z)}): по правилу "
            f"держать до стопа или смены сигнала" for i, coin, side, ssum, z in notes]


def zone_lines(zones):
    if not zones:
        return []
    price = adv3.price
    lines = ['<b>Зоны входа</b> — для тех, кто ещё не вошёл']
    for z in zones:
        lo, hi = z['zone']
        lines.append(f"#{z['id']} {z['coin']} {SIDE[z['side']]} — цена {price(z['mark'])} " + (
            f"ушла из зоны {price(lo)}–{price(hi)}: лимит {price(z['entry'])}, не догонять" if z['mode'] == 'limit'
            else f"у стопа {price(z['stop'])}: не входить"))
    return lines


def notes_of(rep, reg, cs):
    """The signals of earlier closes open or waiting whose coin was STRONG at the close before and is not at this one, its rule signal
    kept: information, never an exit (CANON PART VII). [(id, coin, side, sum, z)], by number."""
    last = dt.date.fromisoformat(rep['close_of'])
    out = []
    for s in reg.live():
        row = rep['rows'].get(s['coin']) or {}
        if s['close_of'] == rep['close_of'] or row.get('signal') != s['side'] or row.get('z') is None:
            continue
        if row.get('sum') == 4 * s['side'] and abs(row['z']) >= adv3.STRONG_Z:
            continue
        c = cs.get(s['coin']) or {}
        days = sorted(d for d in c if d <= last)
        if len(days) < 2 or days[-1] != last:
            continue
        st = adv3.strength(days, [c[d][3] for d in days], len(days) - 2)
        if st and st[1] == 4 * s['side'] and abs(st[0]) >= adv3.STRONG_Z:
            out.append((s['id'], s['coin'], s['side'], row['sum'], row['z']))
    return out


def zones_of(rep, reg):
    """This close's signals entered at market whose zone the price of the moment has left (TZ-39's zones): a limit at the zone's edge
    where it ran past it, no entry where it stands near the stop - for the Boss who has not entered yet."""
    out = []
    for s in reg.live():
        row = rep['rows'].get(s['coin']) or {}
        if s['close_of'] != rep['close_of'] or s['mode'] != 'market' or not rep['marks_ok'] or row.get('signal') != s['side']:
            continue
        cd = adv3.card(s['coin'], row, True, CAPITAL, adv3.RISK)
        if cd['mode'] != 'market':
            out.append({'id': s['id'], 'coin': s['coin'], 'side': s['side'], 'mode': cd['mode'], 'mark': cd['mark'],
                        'zone': list(cd['zone']), 'entry': cd['entry'], 'stop': cd['stop']})
    return out


def by_side(items):
    out = {1: 0.0, -1: 0.0}
    for it in items:
        if it.get('pos'):
            out[it['side']] += it['pos']['risk_pct']
    return out


def compose(slot, rep, reg, model, news, notes, zones, prev, now, new_ids, seeded=None):
    """(text, quiet, one line) of a check (TZ-42). It notifies only for a new signal or an end - a stop, an exit by the rule, a limit not
    filled. The signal check: the events, the new STRONG signals with their positions, the signals open with where each stands, the
    notes, the model's risk, the coins not taken and why, the registry's fingerprint - or one line where it finds no event, no new
    signal, no note and the coins not taken for the reasons of the check before. The fact check: the events, the new signals, the
    zones left and the risk - or one line where it finds none of them."""
    close = adv3.ddmm(rep['close_of'])
    new = sorted(model['new'], key=lambda x: x['rank'])
    loud = bool(new) or any(e['type'] in LOUD for e in news)
    held = model['risk']
    tail = f"активных {len(reg.live())} · риск {adv3.pct(held[1] + held[-1])}% из {pct0(RISK_TOTAL)}%"
    codes = sorted([c, s, code] for c, s, code, _why, _detail in model['excluded'])
    if slot[1] == 'signal':
        same = prev is not None and prev.get('excluded_codes') == codes
        if not news and not new and not notes and same and seeded is None:
            return (f"✓ {hhmm(now)} по Батуми · закрытие {close}: событий нет, новых STRONG нет · {tail} · 🔐 {len(reg.events)} · "
                    f"{reg.head[:8]}", True, True)
        lines = [f"🌅 <b>ADV-3 · проверка {hhmm(now)}</b> по Батуми · закрытие {close} (UTC)", params_line(DEFAULTS)]
    else:
        if not news and not new and not zones and seeded is None:
            return (f"✓ {hhmm(now)} по Батуми: событий нет · {tail} · следующая проверка {hhmm(next_at(now))}", True, True)
        lines = [f"🕖 <b>ADV-3 · проверка {hhmm(now)}</b> по Батуми · закрытие {close} (UTC)"]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: новых позиций нет')
    if seeded is not None:
        lines += ['', seed_line(reg, seeded)]
    if news:
        lines += [''] + event_lines(news, reg)
    if new:
        lines += ['', f"🆕 <b>Новые STRONG</b> — {len(new)} · риск по силе тренда, до 04:00 {dt.date.fromisoformat(rep['close_of']) + 2 * adv3.DAY:%d.%m}"]
        for k, it in enumerate(new, 1):
            lines += [''] + card_lines(it, k, new_ids.get(it['coin']))
    elif slot[1] == 'signal':
        lines += ['', '🆕 Новых STRONG нет']
    if slot[1] == 'signal':
        live = reg.live()
        if live:
            lines += ['', f"📂 <b>Открытые сигналы</b> — {len(live)}"] + [live_line(s, rep['rows']) for s in live]
        if notes:
            lines += note_lines(notes)
    if zones:
        lines += [''] + zone_lines(zones)
    lines += ['', risk_line(held, by_side(new), DEFAULTS)]
    if slot[1] == 'signal':
        lines += excluded_lines(model['excluded'])
    if new:
        lines.append(legend())
        if any(it['rank'] > adv3.TOP_N for it in new):
            lines.append(adv3.BEYOND)
    if slot[1] == 'signal':
        lines.append(chain_line(reg))
    lines += ['', footer()]
    return '\n'.join(lines), not loud, False


def signal_view(rep, reg, view, prm, now, new_ids, seeded=None):
    """The «сигнал» reply (TZ-42): the close, the parameters, the events not yet announced, the STRONG signals of this close - the
    registry's and the new - each with its position at the request's parameters, the signals open from earlier closes, the risk, the
    coins not taken and why."""
    close = adv3.ddmm(rep['close_of'])
    last = dt.date.fromisoformat(rep['close_of'])
    lines = [f"📊 <b>ADV-3 · STRONG</b> · {hhmm(now)} по Батуми", f"Закрытие {close} (UTC) · карточки до 04:00 {last + 2 * adv3.DAY:%d.%m}",
             params_line(prm)]
    if not rep['marks_ok']:
        lines.append('⚠️ Текущие цены Binance недоступны: позиции не рассчитаны')
    if seeded is not None:
        lines += ['', seed_line(reg, seeded)]
    news = [e for e in reg.events if e['n'] > reg.announced and e['type'] in SHOWN]
    if news:
        lines += [''] + event_lines(news, reg)
    items = view['items']
    if items:
        lines += ['', f"📌 <b>STRONG закрытия {close}</b> — {len(items)} · риск по силе тренда"]
        for k, it in enumerate(items, 1):
            lines += [''] + card_lines(it, k, new_ids.get(it['coin']), mark_new=True)
    else:
        lines += ['', f"📌 STRONG закрытия {close}: нет"]
    older = [s for s in reg.live() if s['close_of'] != rep['close_of']]
    if older:
        lines += ['', f"📂 <b>Открытые с прошлых закрытий</b> — {len(older)}"] + [live_line(s, rep['rows']) for s in older]
    lines += ['', risk_line(view['older'], by_side(items), prm, ('прошлые закрытия', 'это закрытие'))]
    lines += excluded_lines(view['excluded'])
    if items:
        lines.append(legend())
        if any(it['rank'] > adv3.TOP_N for it in items):
            lines.append(adv3.BEYOND)
    lines += ['', footer()]
    return '\n'.join(lines)


def wilson(k, n, z=1.96):
    """The 95 % Wilson interval of a share k of n, in percent: (low, high)."""
    p = k / n
    mid, half = p + z * z / (2 * n), z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return 100 * (mid - half) / (1 + z * z / n), 100 * (mid + half) / (1 + z * z / n)


T975 = (12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110,
        2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042)


def t975(df):
    """Student's t at 0.975 with df degrees of freedom: the table to 30, then the Cornish-Fisher expansion about the normal's 1.95996."""
    if df <= 30:
        return T975[df - 1]
    z = 1.959964
    return z + (z ** 3 + z) / (4 * df) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * df ** 2)


def mean_ci(xs):
    """(mean, low, high) of xs with Student's 95 % interval; the interval None below two values."""
    n = len(xs)
    m = sum(xs) / n
    if n < 2:
        return m, None, None
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    h = t975(n - 1) * sd / math.sqrt(n)
    return m, m - h, m + h


def stats_lines(reg, full=False):
    """The registry's figures over its ended signals (TZ-42): the targets reached, the stops before a target, the sum and mean of R
    with the mean's 95 % interval, the result in USDT and in percent of the default capital; full adds the targets against TZ-38's
    history with their Wilson intervals and the mean R by side, by the signal's age at its card and by BTC's signal. Descriptive: it
    moves no rung (CANON PART VII)."""
    closed = [s for _i, s in sorted(reg.sig.items()) if s['status'] == 'closed']
    n = len(closed)
    if not n:
        return ['Завершённых сделок пока нет — итогов нет.']
    pct, signed = adv3.pct, sg
    hits = {k: sum(s['hit'] >= k for s in closed) for k in (1, 2, 3)}
    stops = sum(s['why'] == 'stop' and not s['hit'] for s in closed)
    R = [s['R'] for s in closed]
    m, lo, hi = mean_ci(R)
    pnl = sum(s['pnl'] for s in closed)
    lines = [f"Закрыто {n}: 🎯1 {hits[1]} ({pct(100 * hits[1] / n, 0)}%) · 🎯2 {hits[2]} · 🎯3 {hits[3]} · стоп до цели {stops}",
             f"Сумма {signed(sum(R), 1)} R = {signed_usdt(pnl)} USDT ({signed(100 * pnl / CAPITAL)}% капитала) · средняя {signed(m)} R"
             + (f" (95%: {signed(lo)}…{signed(hi)})" if lo is not None else '')]
    if n < 30:
        lines.append(f"⚠️ {n} {adv3.plural(n, 'сделка', 'сделки', 'сделок')} — мало для выводов: интервал широк, уверенность не меняется")
    if not full:
        return lines
    mfe = adv3.PIT['strong']['mfe']
    lines.append('Цели против истории STRONG: ' + ' · '.join(
        f"🎯{k} {pct(100 * hits[k] / n, 0)}% (95%: {pct(wilson(hits[k], n)[0], 0)}–{pct(wilson(hits[k], n)[1], 0)}) — история "
        f"{pct(100 * mfe[k], 0)}%" for k in (1, 2, 3)))

    def group(title, key, names):
        parts = []
        for name, label in names:
            xs = [s['R'] for s in closed if key(s) == name]
            if xs:
                parts.append(f"{label} {len(xs)} · {signed(sum(xs) / len(xs))} R")
        return [f"{title}: " + '; '.join(parts)] if parts else []

    def age(s):
        try:
            days = (dt.date.fromisoformat(s['close_of']) - dt.date.fromisoformat(s['since'])).days
        except (TypeError, ValueError):
            return None
        return 'young' if days <= 3 else 'mid' if days <= 14 else 'old'

    lines += group('По стороне', lambda s: s['side'], ((1, 'ЛОНГ'), (-1, 'ШОРТ')))
    lines += group('По возрасту сигнала', age, (('young', '≤3 дн'), ('mid', '4–14 дн'), ('old', '>14 дн')))
    lines += group('По рынку (BTC)', lambda s: s.get('btc'), ((1, 'BTC в ЛОНГ'), (-1, 'BTC в ШОРТ'), (0, 'BTC вне рынка')))
    return lines


def registry_view(reg, rep, now):
    """The «реестр» reply (TZ-42): the counts, every signal open or waiting with where it stands, the last ten ended, the figures over
    the ended ones and the chain's state."""
    sigs = [s for _i, s in sorted(reg.sig.items())]
    live = reg.live()
    ended = sorted([s for s in sigs if s['status'] in ('closed', 'expired')], key=lambda s: s['exit_utc'], reverse=True)
    first = min((s['close_of'] for s in sigs), default=None)
    lines = [f"📒 <b>ADV-3 · реестр STRONG</b> · {hhmm(now)} по Батуми",
             f"Сигналов {len(sigs)}" + (f" с {adv3.ddmm(first)}" if first else '') + f" · открыто {len(live)} · закрыто "
             f"{sum(s['status'] == 'closed' for s in sigs)} · истекло {sum(s['status'] == 'expired' for s in sigs)}",
             '<i>Модель бота при капитале 200 000 USDT: рыночный вход — по цене карточки, лимит — когда цена его коснулась; не ваш счёт</i>']
    if live:
        lines += ['', '<b>Открытые</b>'] + [live_line(s, rep['rows']) for s in live]
    if ended:
        lines += ['', f"<b>Завершённые</b> — последние {min(10, len(ended))} из {len(ended)}"] + [ended_line(s) for s in ended[:10]]
    lines += ['', '<b>Итоги</b>'] + stats_lines(reg) + ['', chain_line(reg), '', footer()]
    return '\n'.join(lines)


def ranking_view(rep, reg, n):
    """The «рейтинг» reply (TZ-42): the rule's first n coins in its order, each with its side, strength, sum of signs, ★ where STRONG at
    any rank and its open signal's number; the day's changes; the others counted."""
    rows = rep['rows']
    order = ranked(rep)
    strong = set(strong_all(rep))
    live = {s['coin']: s['id'] for s in reg.live()}
    lines = [f"🏆 <b>ADV-3 · рейтинг правила</b> · закрытие {adv3.ddmm(rep['close_of'])} (UTC)", f"В рынке {len(order)} из {len(adv3.COINS)}", '']
    for k, coin in enumerate(order[:n], 1):
        r = rows[coin]
        lines.append(f"{k}. {DOT[r['signal']]} {coin} {SIDE[r['signal']]} · z {sg(r['z'])} · знаки {sg(r['sum'], 0)}"
                     + (' · ★' if coin in strong else '') + (f" · #{live[coin]}" if coin in live else ''))
    new, out_long, out_short, flips = adv3.changes(rep)
    word = {1: 'ЛОНГ', -1: 'ШОРТ'}
    parts = ([f"🆕 {', '.join(f'{c} {word[k]}' for c, k in new)}"] if new else []) \
        + ([f"🚪 {', '.join(out_long)} из лонга"] if out_long else []) + ([f"🚪 {', '.join(out_short)} из шорта"] if out_short else []) \
        + ([f"🔄 {', '.join(f'{c} в {word[k]}' for c, k in flips)}"] if flips else [])
    lines += ['', 'Изменения за день: ' + (' · '.join(parts) if parts else 'нет')]
    rest = [c for c in order[n:]]
    flat = sum(rows[c].get('signal') == 0 for c in adv3.COINS)
    young = sum(rows[c].get('signal') is None and not rows[c].get('missing') for c in adv3.COINS)
    lost = [c for c in adv3.COINS if rows[c].get('missing')]
    lines.append(f"Дальше в рынке {len(rest)} · вне рынка {flat} · мало истории {young}" + (f" · Binance не отдал: {', '.join(lost)}" if lost else ''))
    lines += ['<i>★ — STRONG: четыре знака совпадают и |z| ≥ 1; #N — открытый сигнал реестра; карточки и позиции — «сигнал»</i>', '', footer()]
    return '\n'.join(lines)


def assess_view(rep, reg):
    """The «оценка» reply: adv3's assessment - the rung, the next readings, the six ratings, the forward record, the history - and, since
    TZ-42, the registry's figures in full, which describe and move no rung."""
    return (adv3.assessment(rep, adv3.FACTS) + '\n\n<b>Реестр сигналов бота</b> — модель при капитале 200 000 USDT, не ваш счёт\n'
            + '\n'.join(stats_lines(reg, full=True)) + '\n<i>Рейтинг двигают только чтения форварда (после 28.10.2027) и PIT (после '
            '31.10.2027); реестр описывает, а не доказывает.</i>')


def check_record(slot, rep, reg, model, news, notes, zones, ids, quiet, one_line, opened, at, seeded=None):
    """The check's journal record (CANON PART VII's internal log; it measures and tunes nothing): every coin's signal, sum of signs,
    strength, rank, unit, close and mark; the coins STRONG at every rank; the new signals with their cards and positions; the coins
    not taken with their reasons and codes; the events announced; the notes and zones; the registry's open signals, risk, size,
    head and state; the six ratings."""
    rank = {coin: k for k, coin in enumerate(ranked(rep), 1)}
    new = sorted(model['new'], key=lambda x: x['rank'])
    rec = base_record('check', rep, ids, at)
    held = open_risk(reg)
    rec.update(slot=slot_text(slot), quiet=quiet, one_line=one_line,
               state={coin: {'signal': r.get('signal'), 'sum': r.get('sum'), 'z': r.get('z'), 'rank': rank.get(coin), 'U': r.get('U'),
                             'close': r.get('close'), 'mark': r.get('mark')} for coin, r in rep['rows'].items()},
               strong_all=strong_all(rep), cards=[item_record(it, i) for it, i in zip(new, opened or [None] * len(new))],
               excluded=[list(x) for x in model['excluded']], excluded_codes=sorted([c, s, code] for c, s, code, _w, _d in model['excluded']),
               events=[e['n'] for e in news], notes=[list(x) for x in notes], zones=zones, opened=opened,
               registry={'events': len(reg.events), 'head': reg.head, 'broken': reg.broken, 'open': [s['id'] for s in reg.live()],
                         'risk': held[1] + held[-1], 'seeded': seeded},
               params={k: DEFAULTS[k] for k in ('capital', 'risk', 'total', 'stop', 'n')}, trust=rep['trust'])
    return rec


def check(tg, data, reg, slot, now):
    """One scheduled check (TZ-42): the report at the model's defaults; the registry brought to now - seeded at its first check, every
    signal open or waiting walked on its candles; the model's new signals; the notes at the signal check and the zones left at
    the fact check; the message, sent quiet unless it holds a new signal or an end; then the new signals written - a signal exists once
    its message is sent - and the events counted announced; its record returned for the journal."""
    rep = live_report(data, CAPITAL, adv3.RISK)
    seeded = ensure(reg, data, now)
    model = model_plan(rep, reg, volumes(strong_all(rep), rep['made_at_ms']))
    news = [e for e in reg.events if e['n'] > reg.announced and e['type'] in SHOWN]
    notes = notes_of(rep, reg, data.cs) if slot[1] == 'signal' else []
    zones = zones_of(rep, reg) if slot[1] == 'fact' else []
    first = reg.next_id()
    new_ids = {it['coin']: first + k for k, it in enumerate(sorted(model['new'], key=lambda x: x['rank']))}
    text, quiet, one_line = compose(slot, rep, reg, model, news, notes, zones, last_check(), now, new_ids, seeded)
    ids = tg.send(text, quiet=quiet)
    opened = []
    try:
        opened = register(reg, rep, model['new'], now, 'check:' + slot_text(slot))
        reg.announced = len(reg.events)
        reg.save_state()
    except Exception:
        log('registry write failed\n' + traceback.format_exc())
    return check_record(slot, rep, reg, model, news, notes, zones, ids, quiet, one_line, opened, now, seeded)


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
    tg, data, reg = Telegram(token, chat), Data(), Registry(STATE)
    off_path, done_path = os.path.join(STATE, 'offset'), os.path.join(STATE, 'check-done')
    offset = int(read(off_path)) if os.path.exists(off_path) else 0
    done = slot_parse(read(done_path)) if os.path.exists(done_path) else None
    retry_at = 0.0
    log('serving the pinned chat: pid', os.getpid(), 'offset', offset, 'check-done', slot_text(done) if done else '-')
    log('registry:', len(reg.events), 'events,', len(reg.sig), 'signals,', len(reg.live()), 'open | head', reg.head[:12],
        '| torn', reg.torn, '| broken', reg.broken or '-')
    try:
        tg.call('setMyCommands', commands=COMMANDS)
    except Exception as e:
        log('setMyCommands refused:', repr(e)[:200])   # the menu is a convenience: the keyboard and the texts answer without it
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        slot = due(now, done)
        if slot and time.time() >= retry_at:
            try:
                rec = check(tg, data, reg, slot, now)
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
                log('check sent:', slot_text(slot), 'for the close of', rec['close_of'], '| events', len(rec['events']), '| new',
                    len(rec['opened']), '| quiet' if rec['quiet'] else '| loud', '| one line' if rec['one_line'] else '| full')
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
            handle(tg, data, reg, msg.get('text') or '')
        if updates:
            put(off_path, str(offset))


def handle(tg, data, reg, text):
    """One message of the Boss's (TZ-42): «сигнал» - the registry brought to now, the model's new signals, the request's plan sent,
    then the new ones it showed written; «реестр» and «оценка» - the registry brought to now and its view; «рейтинг» - the rule's
    order; anything else HELP. Every reply carries the keyboard and leaves one journal record."""
    cmd = route(text)
    try:
        if cmd is None or cmd[0] == 'help':
            tg.send(HELP, keyboard=True)
            log('help sent')
            return
        kind, arg = cmd
        now = dt.datetime.now(dt.timezone.utc)
        rep = live_report(data, CAPITAL, adv3.RISK)
        if kind == 'ranking':
            rec = base_record('ranking', rep, tg.send(ranking_view(rep, reg, arg), keyboard=True), now)
            rec['n'] = arg
        else:
            seeded = ensure(reg, data, now)
            if kind == 'signal':
                liq = volumes(strong_all(rep), rep['made_at_ms'])
                model = model_plan(rep, reg, liq)
                view = view_plan(rep, reg, liq, arg, model)
                shown = {it['coin'] for it in view['items'] if it['sig'] is None and it.get('pos')}
                new = sorted([it for it in model['new'] if it['coin'] in shown], key=lambda x: x['rank'])
                first = reg.next_id()
                new_ids = {it['coin']: first + k for k, it in enumerate(new)}
                ids = tg.send(signal_view(rep, reg, view, arg, now, new_ids, seeded), keyboard=True)
                opened = []
                try:
                    opened = register(reg, rep, new, now, 'request')
                    reg.announced = len(reg.events)
                    reg.save_state()
                except Exception:
                    log('registry write failed\n' + traceback.format_exc())
                rec = base_record('request', rep, ids, now)
                rec.update(params={k: arg[k] for k in ('capital', 'risk', 'total', 'stop', 'n', 'set')}, opened=opened,
                           cards=[item_record(it) for it in view['items']], excluded=[list(x) for x in view['excluded']])
            elif kind == 'registry':
                rec = base_record('registry', rep, tg.send(registry_view(reg, rep, now), keyboard=True), now)
            else:
                rec = base_record('assess', rep, tg.send(assess_view(rep, reg), keyboard=True), now)
                rec['trust'] = rep['trust']
            rec['seeded'] = seeded
        try:
            append(rec)
        except Exception:
            log('request record failed\n' + traceback.format_exc())
        log('request answered for the close of', rep['close_of'], '| kind', kind)
    except Exception:
        log('request failed\n' + traceback.format_exc())
        try:
            tg.send('Binance или Telegram не ответили — повторите через минуту.', keyboard=True)
        except Exception:
            log('apology failed\n' + traceback.format_exc())


def probe():
    """P-START: live requests through the process's own request functions, each asserted served and parsed - six endpoints, eight
    requests: the klines endpoint three times, for the closed daily candles and, since TZ-42, for the 5-minute candles of the last
    hour and the 1-minute ones of the last minutes, which the registry walks on; fundingRate, premiumIndex and fundingInfo once each;
    Telegram's getMe and, since TZ-42, getMyCommands. Prints counts, dates and the bot's name; never the token or a chat id."""
    now_ms = int(time.time() * 1000)
    today = dt.datetime.now(dt.timezone.utc).date()
    c = adv3.fapi_candles('BTCUSDT', now_ms)
    assert c and max(c) >= today - 2 * adv3.DAY and all(len(v) == 4 and v[3] > 0 for v in c.values()), 'klines'
    k5 = klines('BTC', ceil5(now_ms - 13 * K5_MS), now_ms)
    k1 = klines('BTC', ceil1(now_ms - 4 * K1_MS), now_ms, K1_MS, 4)
    for rows, step, lo in ((k5, K5_MS, 10), (k1, K1_MS, 3)):
        assert lo <= len(rows) <= (14 if step == K5_MS else 4) and all(
            len(x) == 6 and x[2] >= max(x[1], x[4]) and 0 < x[3] <= min(x[1], x[4]) for x in rows) \
            and all(a[0] + step == b[0] for a, b in zip(rows, rows[1:])) and all(x[5] for x in rows[:-1]), '%d-minute klines' % (step // K1_MS)
    print('P-KLINES served:', len(c), 'closed daily candles of BTCUSDT, the last', max(c), '-', len(k5), '5-minute candles of the last hour and',
          len(k1), '1-minute candles of the last minutes')
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
    tg = Telegram(read(TOKEN_FILE))
    me = tg.call('getMe')
    cmds = tg.call('getMyCommands')
    assert me.get('is_bot') is True and me.get('username') and isinstance(cmds, list), 'getMe, getMyCommands'
    print('P-TELEGRAM served: bot @' + me['username'] + ',', len(cmds), 'commands in its menu')
    print('READING P-START: served - 6 of 6 endpoints, 8 requests')


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
        'ADV-3 подключён к этому чату. Напишите «сигнал» — или ждите проверок в 04:10 и 19:07 по Батуми.', keyboard=True)
    assert ids and all(isinstance(x, int) for x in ids), ids
    print('G-HELLO sent: message ids', ids)


def selftest():
    """The bot's own checks, offline (TZ-42): the commands and their parameters, the keyboard, the schedule with its 15:07 slot, the
    registry's chain - written, read back, broken by an edit, a removal or a torn line - each signal's walk on 5-minute candles in
    hand-built cases, the position and the shares by hand, the candidates and the model's and a request's plans, the seed from a
    journal, the messages, and checks and requests end to end with Binance and Telegram stood in for; the stats by hand; the chunks,
    the files, the log, the HTML fallback and the quiet flag, the pace and the 429s, glibc. Every expectation is computed here by hand
    or by a formula of its own, never by the code under test."""
    import contextlib, io, random, shutil, tempfile
    done = []

    def chk(name, ok):
        done.append(name)
        assert ok, name

    # ---- the commands -----------------------------------------------------------------------------------------------
    def P(capital=200000.0, risk=0.5, total=10.0, stop=14.0, n=7, given=()):
        return {'capital': capital, 'risk': risk, 'total': total, 'stop': stop, 'n': n, 'set': sorted(given)}
    S_, A_, R_, H_ = 'signal', ('assess', None), ('registry', None), ('help', None)
    for text, want in (('сигнал', (S_, P())), ('Сигнал', (S_, P())), ('Сигнал 0,5%', (S_, P(risk=0.5, given=['risk']))),
                       ('signal 0.3', (S_, P(risk=0.3, given=['risk']))), ('сигналы', (S_, P())), ('сигнал топ 3', (S_, P(n=3, given=['n']))),
                       ('сигнал топ 10', (S_, P(n=7, given=['n']))), ('сигнал топ 0', (S_, P(n=1, given=['n']))), ('топ 5', (S_, P(n=5, given=['n']))),
                       ('сигнал 10000 топ 3', (S_, P(capital=10000.0, n=3, given=['capital', 'n']))),
                       ('Сигнал 15 000 топ 5 1', (S_, P(capital=15000.0, n=5, risk=1.0, given=['capital', 'n', 'risk']))),
                       ('сигнал 10к топ 3', (S_, P(capital=10000.0, n=3, given=['capital', 'n']))),
                       ('signal 15k top 5', (S_, P(capital=15000.0, n=5, given=['capital', 'n']))),
                       ('сигнал 1,5 тыс', (S_, P(capital=1500.0, given=['capital']))),
                       ('сигнал 150000 риск 0,75 лимит 8 стоп 12 топ 5',
                        (S_, P(capital=150000.0, risk=0.75, total=8.0, stop=12.0, n=5, given=['capital', 'n', 'risk', 'stop', 'total']))),
                       ('сигнал риск 2', (S_, P(risk=1.0, given=['risk']))), ('сигнал лимит 20', (S_, P(total=10.0, given=['total']))),
                       ('сигнал всего 6%', (S_, P(total=6.0, given=['total']))), ('сигнал стоп 20', (S_, P(stop=14.0, given=['stop']))),
                       ('сигнал стоп 1', (S_, P(stop=2.0, given=['stop']))), ('сигнал лимит 0,1', (S_, P(total=0.5, given=['total']))),
                       ('сигнал 50', (S_, P(risk=1.0, given=['risk']))), ('signal 200000000', (S_, P(capital=10_000_000.0, given=['capital']))),
                       ('сигнал 12000 0.01', (S_, P(capital=12000.0, risk=0.05, given=['capital', 'risk']))),
                       ('/signal@adv3_bot 5000 top 2', (S_, P(capital=5000.0, n=2, given=['capital', 'n']))),
                       ('топ 3 на 10000', (S_, P(capital=10000.0, n=3, given=['capital', 'n']))),
                       ('сигнал 100 топ 3', (S_, P(capital=100.0, n=3, given=['capital', 'n']))),
                       ('реестр', R_), ('Реестр', R_), ('/registry', R_), ('рейтинг', ('ranking', 7)), ('Рейтинг 15', ('ranking', 15)),
                       ('рейтинг 99', ('ranking', 42)), ('рейтинг 0', ('ranking', 1)), ('/ranking', ('ranking', 7)),
                       ('оценка', A_), ('Оценка', A_), ('/rating', A_), ('помощь', H_), ('Помощь', H_), ('/start', H_), ('help', H_), ('меню', H_),
                       ('привет', None), ('сигнализация', None), ('', None), ('12345', None), ('eth', None), ('оценочный', None)):
        chk(f'route {text!r}', route(text) == want)
    chk('HELP: the commands, the defaults, the overrides and their ceilings, the checks at 04:10 and 19:07 and the quiet rule, in one part',
        all(k in HELP for k in ('«Сигнал»', '«Реестр»', '«Рейтинг»', '«Оценка»', '200 000 USDT', 'не ваш баланс', '0,5%', '10%', '14%',
                                'до 7 новых', '«сигнал 50000 риск 0,75 лимит 8 стоп 12 топ 3»', 'только ужесточить', '04:10', '19:07',
                                'одной строкой')) and len(chunks(HELP)) == 1)
    chk('the keyboard: Сигнал and Реестр, then Рейтинг, Оценка and Помощь, each a command route reads; five menu commands',
        [[b['text'] for b in row] for row in KEYBOARD['keyboard']] == [['Сигнал', 'Реестр'], ['Рейтинг', 'Оценка', 'Помощь']]
        and [route(b['text'])[0] for row in KEYBOARD['keyboard'] for b in row] == ['signal', 'registry', 'ranking', 'assess', 'help']
        and [route('/' + c['command'])[0] for c in COMMANDS] == ['signal', 'registry', 'ranking', 'assess', 'help'])
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

    # ---- Telegram -----------------------------------------------------------------------------------------------------
    slept, real_sleep = [], time.sleep
    time.sleep = slept.append       # the self-test never waits: each pause is recorded instead, and time.sleep restored at its end

    class Fake(Telegram):
        def __init__(self, busy=0, wait=7):
            super().__init__('123456:SECRET', 777)
            self.calls, self.busy, self.wait = [], busy, wait

        def call(self, method, http_timeout=30, **params):
            self.calls.append(params)
            if self.busy:
                self.busy -= 1
                raise TooMany(f'telegram sendMessage: 429 Too Many Requests: retry after {self.wait}', self.wait)
            if params.get('parse_mode') == 'HTML' and '<b>bad' in params.get('text', ''):
                raise RuntimeError("telegram sendMessage: 400 Bad Request: can't parse entities")
            return {'message_id': len(self.calls)}

    fk = Fake()
    chk('HTML sent as HTML, with a notification and no keyboard', fk.send('<b>ok</b>') == [1] and fk.calls[0]['parse_mode'] == 'HTML'
        and 'disable_notification' not in fk.calls[0] and 'reply_markup' not in fk.calls[0])
    chk('unparseable HTML resent as plain text', fk.send('<b>bad &amp; x</b>') == [3]
        and 'parse_mode' not in fk.calls[2] and fk.calls[2]['text'] == 'bad & x')
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000]), quiet=True)
    fk.send('<b>bad quiet</b>', quiet=True)
    chk('quiet: every part, the plain fallback among them, without a notification',
        len(fk.calls) == n0 + 4 and all(c.get('disable_notification') is True for c in fk.calls[n0:]))
    n0 = len(fk.calls)
    fk.send('\n'.join(['q' * 3000, 'r' * 3000, 's' * 3000]), keyboard=True)
    fk.send('<b>bad kb</b>', keyboard=True)
    chk('keyboard: on the last part alone, the plain fallback keeping it (TZ-42)',
        ['reply_markup' in c for c in fk.calls[n0:]] == [False, False, True, True, True] and fk.calls[-1]['reply_markup'] == KEYBOARD)
    del slept[:]
    fk.send('\n'.join(['q' * 3000, 'r' * 3000, 's' * 3000]))
    chk('pace: the parts of one message 1.1 s apart, none before the first (TZ-40)', slept == [1.1, 1.1] and PACE == 1.1)
    busy = Fake(busy=2)
    del slept[:]
    ids = busy.send('<b>one</b>', quiet=True)
    chk('429: a part refused as too many requests waits the retry_after named and a second more, and goes again, quiet still',
        ids == [3] and slept == [8, 8] and len(busy.calls) == 3 and all(c['text'] == '<b>one</b>' and c.get('disable_notification') is True
                                                                     for c in busy.calls))
    stuck, raised = Fake(busy=3), False
    try:
        stuck.send('x\n' + 'y' * 4000)
    except TooMany:
        raised = True
    chk('429: a part refused three times raises, and no later part is sent', raised and len(stuck.calls) == 3
        and all(c['text'] == 'x' for c in stuck.calls))
    del slept[:]
    Fake(busy=1, wait=600).send('z')
    chk('429: a retry_after above 60 s waits 61 s', slept == [61])
    real_open = urllib.request.urlopen

    def refuse(body):
        def opener(req, timeout=None):
            raise urllib.error.HTTPError(req.full_url, 429, 'x', {}, io.BytesIO(json.dumps(body).encode()))
        return opener
    got = []
    try:
        for body in ({'ok': False, 'error_code': 429, 'description': 'Too Many Requests: retry after 9', 'parameters': {'retry_after': 9}},
                     {'ok': False, 'error_code': 429, 'description': 'Too Many Requests'},
                     {'ok': False, 'error_code': 400, 'description': 'Bad Request'}):
            urllib.request.urlopen = refuse(body)
            try:
                Telegram('123456:SECRET', 777).call('sendMessage', text='x')
            except TooMany as e:
                got.append(('429', e.retry_after))
            except RuntimeError as e:
                got.append(('other', str(e)))
    finally:
        urllib.request.urlopen = real_open
    chk('call: a 429 raises TooMany with the retry_after named, 5 s where none is; another refusal a RuntimeError of its own',
        got == [('429', 9), ('429', 5), ('other', 'telegram sendMessage: 400 Bad Request')])
    SECRETS.append('123456:SECRET')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        log('url https://api.telegram.org/bot123456:SECRET/getMe failed')
    SECRETS.remove('123456:SECRET')
    chk('the token never reaches the log', 'SECRET' not in buf.getvalue() and '<token>' in buf.getvalue())

    # ---- the schedule: 00:10 and 15:07 UTC --------------------------------------------------------------------------------
    X = dt.date(2026, 11, 5)
    at = lambda d, h, m, s=0: dt.datetime.combine(d, dt.time(h, m, s), tzinfo=dt.timezone.utc)
    sig, fac = (X, 'signal'), (X, 'fact')
    chk('the slots are 00:10 and 15:07 UTC, 04:10 and 19:07 in Batumi', SLOTS == (('signal', dt.time(0, 10)), ('fact', dt.time(15, 7)))
        and hhmm(at(X, 0, 10)) == '04:10' and hhmm(at(X, 15, 7)) == '19:07')
    chk('latest_slot: 00:09:59 is the day before\'s fact, 00:10 the signal, 15:06:59 still the signal, 15:07 the fact',
        [latest_slot(at(X, 0, 9, 59)), latest_slot(at(X, 0, 10)), latest_slot(at(X, 15, 6, 59)), latest_slot(at(X, 15, 7)),
         latest_slot(at(X, 23, 59, 59))] == [(X - adv3.DAY, 'fact'), sig, sig, fac, fac])
    chk('due: nothing done runs the day\'s signal, at 00:10 and at 16:00 alike (15:07 repeats 00:10)',
        due(at(X, 0, 10), None) == sig and due(at(X, 16, 0), None) == sig)
    chk('due: the signal done, nothing before 15:07, the fact at 15:07; the fact done, nothing until 00:10',
        due(at(X, 15, 6), sig) is None and due(at(X, 15, 7), sig) == fac and due(at(X, 23, 0), fac) is None
        and due(at(X + adv3.DAY, 0, 10), fac) == (X + adv3.DAY, 'signal'))
    chk('done_after: a signal ended before 15:07 is itself; at or after 15:07 it covers the fact; a fact is itself',
        done_after(sig, at(X, 0, 10, 30)) == sig and done_after(sig, at(X, 15, 7)) == fac and done_after(fac, at(X, 16, 0)) == fac)
    chk('next_at: 00:10, then 15:07, then 00:10 of the next day',
        [next_at(at(X, 0, 9)), next_at(at(X, 0, 10)), next_at(at(X, 15, 7)), next_at(at(X, 23, 0))]
        == [at(X, 0, 10), at(X, 15, 7), at(X + adv3.DAY, 0, 10), at(X + adv3.DAY, 0, 10)])
    chk('slot_text and slot_parse: a round trip, and nothing else parsed', slot_parse(slot_text(fac)) == fac
        and slot_parse('2026-11-05 daily') is None and slot_parse('garbage') is None and slot_parse('') is None)
    runs, d_, t = [], None, at(X, 13, 0)
    while t < at(X + 3 * adv3.DAY, 23, 59):
        s = due(t, d_)
        fail = s == (X + adv3.DAY, 'signal') and t < at(X + adv3.DAY, 15, 30)
        if s and not fail:
            runs.append((slot_text(s), t.strftime('%d %H:%M')))
            d_ = done_after(s, t)
        t += dt.timedelta(minutes=1)
    chk('three days minute by minute from a first start at 13:00: each slot once, a signal failing until 15:30 covering its fact',
        runs == [('2026-11-05 signal', '05 13:00'), ('2026-11-05 fact', '05 15:07'), ('2026-11-06 signal', '06 15:30'),
                 ('2026-11-07 signal', '07 00:10'), ('2026-11-07 fact', '07 15:07'), ('2026-11-08 signal', '08 00:10'),
                 ('2026-11-08 fact', '08 15:07')])

    # ---- the registry's chain ---------------------------------------------------------------------------------------------
    state = tempfile.mkdtemp(prefix='.selftest-', dir=os.path.dirname(os.path.abspath(__file__)))
    saved = (globals()['STATE'], adv3.fapi)
    try:
        when = at(X, 0, 10)
        rg = Registry(state)
        chk('an empty registry: no event, the genesis head, nothing announced', rg.events == [] and rg.head == '0' * 64 and rg.announced == 0
            and rg.next_id() == 1 and rg.live() == [])
        o1 = {'type': 'open', 'id': 1, 'utc': '2026-11-05T00:10:00+00:00', 'coin': 'ETH', 'side': 1, 'close_of': '2026-11-04', 'mode': 'limit',
              'entry': 100.0, 'stop': 90.0, 'targets': [110.0, 120.0, 130.0], 'valid': '2026-11-06T00:00:00+00:00', 'risk_pct': 0.5, 'qty': 10.0}
        rg.append({'type': 'seed', 'utc': '2026-11-05T00:10:00+00:00', 'cards': 0}, when)
        rg.append(o1, when)
        rg.append({'type': 'fill', 'id': 1, 'utc': '2026-11-05T01:00:00+00:00', 'price': 100.0}, when)
        raw = open(os.path.join(state, REG_FILE), 'rb').read().split(b'\n')
        hs = [hashlib.sha256(x).hexdigest() for x in raw[:3]]
        lines3 = [json.loads(x) for x in raw[:3]]
        chk('append: one line an event, numbered 1 to 3, each prev the SHA-256 of the line before, the first the genesis; the head the last\'s',
            raw[3] == b'' and [x['n'] for x in lines3] == [1, 2, 3] and [x['prev'] for x in lines3] == ['0' * 64, hs[0], hs[1]]
            and rg.head == hs[2] and all(x['at'] == '2026-11-05T00:10:00+00:00' for x in lines3)
            and raw[1] == json.dumps(lines3[1], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
        chk('apply: the limit\'s signal waits, then its fill opens it', rg.sig[1]['status'] == 'open' and rg.sig[1]['fill'] == 100.0
            and status_of(rg.sig[1]) == 'ACTIVE' and [s['id'] for s in rg.live()] == [1] and rg.next_id() == 2)
        rg.cursor[1] = {'t': 5, 'b': 4, 'mfe': 0.5}
        rg.announced = 2
        rg.save_state()
        rb = Registry(state)
        chk('read back: the same events, signals, head, places and announced; no break, nothing torn',
            rb.events == rg.events and rb.sig == rg.sig and rb.head == rg.head and rb.cursor == {1: {'t': 5, 'b': 4, 'mfe': 0.5}}
            and rb.announced == 2 and rb.broken is None and rb.torn == 0)
        path = os.path.join(state, REG_FILE)
        good = open(path, 'rb').read()
        open(path, 'wb').write(good.replace(b'"entry":100.0', b'"entry":101.0', 1))
        chk('an edited line breaks the chain at the line after it', Registry(state).broken == 3)
        lines_ = good.split(b'\n')
        open(path, 'wb').write(b'\n'.join([lines_[0], lines_[2], b'']))
        chk('a removed line breaks the chain where it was', Registry(state).broken == 2)
        open(path, 'wb').write(b'\n'.join([lines_[0], b'not json', lines_[1], lines_[2], b'']))
        chk('a line that does not parse breaks the chain there', Registry(state).broken == 2)
        open(path, 'wb').write(good + b'{"type":"targ')
        rt = Registry(state)
        chk('a torn last line - a write cut short - is cut at load, its bytes counted, the chain whole',
            rt.torn == 13 and open(path, 'rb').read() == good and rt.broken is None and len(rt.events) == 3)
        os.remove(os.path.join(state, REG_STATE))
        chk('the state lost: the places rebuilt from each issue, every event counted announced', Registry(state).announced == 3
            and Registry(state).cursor_of(rg.sig[1]) == {'t': ceil1(from_iso('2026-11-05T00:10:00+00:00')), 'b': from_iso('2026-11-05T00:10:00+00:00'),
                                                          'mfe': 0.0})
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- a signal's walk on 5-minute candles: cases by hand ------------------------------------------------------------
        d0 = dt.date(2026, 6, 1)
        rise = [100 * 1.01 ** i for i in range(150)]

        def daily(closes, start=d0):
            out, prev = {}, closes[0]
            for i, cl in enumerate(closes):
                out[start + i * adv3.DAY] = (prev, max(prev, cl) * 1.001, min(prev, cl) * 0.999, cl)
                prev = cl
            return out

        DD = d0 + 149 * adv3.DAY           # the card's close
        issue = day_ms(DD + adv3.DAY) + 600_000          # 00:10 of the day after it
        c_up = daily(rise + [rise[-1] * 1.01 ** k for k in range(1, 30)])

        def S(side=1, mode='market', E=100.0, stop=None, T=None, hit=0, status=None, fill=None, fill_utc=None, i=7, qty=10.0):
            stop = E - side * 10 if stop is None else stop
            T = [E + side * k * 10 for k in (1, 2, 3)] if T is None else T
            return {'id': i, 'coin': 'ETH', 'side': side, 'close_of': str(DD), 'utc': iso(issue), 'mode': mode, 'entry': E, 'stop': stop,
                    'targets': T, 'valid': iso(day_ms(DD + 2 * adv3.DAY)), 'qty': qty, 'hit': hit,
                    'status': status or ('open' if mode == 'market' else 'pending'), 'fill': fill if fill is not None else (E if mode == 'market' else None),
                    'fill_utc': fill_utc or (iso(issue) if mode == 'market' else None)}

        def K(*rows, start=None, closed=True):
            t0 = ceil5(issue) if start is None else start
            return [(t0 + k * K5_MS, *r, closed) for k, r in enumerate(rows)]

        cur0 = {'t': ceil5(issue), 'b': issue, 'mfe': 0.0}
        zero = lambda d: 0.0
        kinds = lambda evs: [(e['type'], e.get('k'), e.get('price')) for e in evs]
        k1 = K((100, 105, 98, 104), (104, 111, 103, 110), (110, 121, 108, 120), (120, 121, 89, 95))
        ev1, cur1 = walk(S(), cur0, c_up, zero, k1)
        chk('walk: a long reaches its first target, then its second, then its stop: two targets and a stop at 90, -1.019 R, -101.9 USDT',
            kinds(ev1) == [('target', 1, 110), ('target', 2, 120), ('stop', None, 90)] and [e['utc'] for e in ev1] == [iso(k1[i][0]) for i in (1, 2, 3)]
            and abs(ev1[2]['R'] - (-10 - 0.001 * 190) / 10) < 1e-12 and abs(ev1[2]['pnl'] - (-10.19 * 10)) < 1e-9)
        ev2, _c = walk(S(), cur0, c_up, zero, K((100, 111, 89, 95)))
        chk('walk: a candle reaching a target and the stop is the stop alone', kinds(ev2) == [('stop', None, 90)])
        ev3, _c = walk(S(), cur0, c_up, zero, K((85, 86, 80, 82)))
        chk('walk: a candle opening beyond the stop ends at its open: 85, -1.5185 R',
            kinds(ev3) == [('stop', None, 85)] and abs(ev3[0]['R'] - (-15 - 0.001 * 185) / 10) < 1e-12)
        ev4, _c = walk(S(), cur0, c_up, zero, K((112, 113, 89, 95)))
        chk('walk: a candle opening past a target credits it, then reaches the stop', kinds(ev4) == [('target', 1, 110), ('stop', None, 90)])
        ev5, _c = walk(S(side=-1), cur0, c_up, zero, K((100, 102, 95, 96), (96, 97, 89, 90), (90, 92, 79, 80), (80, 111, 79, 105)))
        chk('walk: a short mirrored - two targets, then its stop at 110', kinds(ev5) == [('target', 1, 90), ('target', 2, 80), ('stop', None, 110)])
        k6 = K((105, 106, 101, 102), (102, 103, 99, 100), (100, 109, 99, 108))
        ev6, cur6 = walk(S(mode='limit'), cur0, c_up, zero, k6)
        chk('walk: a waiting limit fills on the candle that reaches it, at the limit; the place after the last closed candle',
            kinds(ev6) == [('fill', None, 100.0)] and ev6[0]['utc'] == iso(k6[1][0]) and cur6['t'] == k6[2][0] + K5_MS)
        ev7, _c = walk(S(mode='limit'), cur0, c_up, zero, K((98, 99, 97, 98)))
        chk('walk: a candle opening past the limit fills it at its open, 98', kinds(ev7) == [('fill', None, 98)])
        ev8, _c = walk(S(mode='limit'), cur0, c_up, zero, K((101, 101, 89, 90)))
        chk('walk: the candle that fills a limit and reaches the stop ends it at the stop - R on the planned risk',
            kinds(ev8) == [('fill', None, 100.0), ('stop', None, 90)] and abs(ev8[1]['R'] - (-10 - 0.001 * 190) / 10) < 1e-12)
        flat = K(*[(105, 105.5, 104.5, 105)] * 300)
        ev9, cur9 = walk(S(mode='limit'), cur0, {}, zero, flat)
        chk('walk: a limit not reached by its validity, the close after the card\'s, expires there - daily candles or not',
            kinds(ev9) == [('expire', None, None)] and ev9[0]['utc'] == iso(day_ms(DD + 2 * adv3.DAY)))
        # the rule's exit at a close: the sum of signs of the daily closes, written here
        fall = rise + [rise[-1] * 0.98 ** k for k in range(1, 40)]
        c_fall = daily(fall)

        def sum_signs(closes, i):
            return sum((closes[i] > closes[i - L]) - (closes[i] < closes[i - L]) for L in (14, 28, 56, 112))
        x_i = next(i for i in range(150, len(fall)) if sum_signs(fall, i) < 2)
        E_ = fall[149]
        n_c = (x_i - 149 + 2) * 288
        kx = K(*[(E_, E_ * 1.0001, E_ * 0.9999, E_)] * n_c)
        sx = S(E=E_, stop=E_ * 0.5, T=[E_ * 2, E_ * 3, E_ * 4])
        evx, curx = walk(sx, cur0, c_fall, lambda d: 0.0003, kx)
        fund_ = sum(0.0003 * fall[i] for i in range(150, x_i + 1))
        Rx = ((fall[x_i] - E_) - 0.001 * (E_ + fall[x_i]) - fund_) / (E_ * 0.5)
        chk('walk: a long ends at the first close whose sum of signs is below +2, at that close, the funding of every close held paid',
            kinds(evx) == [('exit', None, fall[x_i])] and evx[0]['utc'] == iso(day_ms(d0 + x_i * adv3.DAY) + DAY_MS)
            and abs(evx[0]['R'] - Rx) < 1e-12 and curx['b'] == day_ms(d0 + x_i * adv3.DAY) + DAY_MS)
        k10 = K((100, 105, 98, 104)) + K((104, 111, 103, 110), start=ceil5(issue) + K5_MS, closed=False)
        ev10, cur10 = walk(S(), cur0, c_up, zero, k10)
        k10b = K((100, 105, 98, 104), (104, 112, 103, 111))
        ev10b, cur10b = walk(S(hit=1), cur10, c_up, zero, k10b)
        chk('walk: a candle not yet closed is read - its target credited - and not walked past; walked again closed, nothing twice',
            kinds(ev10) == [('target', 1, 110)] and cur10['t'] == k10[1][0] and ev10b == [] and cur10b['t'] == k10b[1][0] + K5_MS)
        ev11, cur11 = walk(S(mode='limit'), cur0, c_up, zero, k6, until=k6[1][0] + K5_MS - 1)
        chk('walk: until stops it before the candle that closes after it', ev11 == [] and cur11['t'] == k6[1][0])
        # the first minutes: a signal issued at 00:10:20 is walked on 1-minute candles from 00:11 to 00:15, then on 5-minute ones
        issue2 = issue + 20_000
        cur2 = {'t': ceil1(issue2), 'b': issue2, 'mfe': 0.0}
        M = lambda *rows, closed=True: [(ceil1(issue2) + k * K1_MS, *r, closed) for k, r in enumerate(rows)]
        S2 = lambda **kw: dict(S(**kw), utc=iso(issue2), fill_utc=iso(issue2) if kw.get('mode', 'market') == 'market' else None)
        k5b = K((100, 111, 99, 110), start=ceil5(issue2))
        ev12, cur12 = walk(S2(), cur2, c_up, zero, k5b, k1=M((100, 101, 99, 100), (100, 100, 89, 91)))
        chk('walk: the first minutes on 1-minute candles - the stop in the minute 00:12, the 5-minute candle of 00:15 never read',
            kinds(ev12) == [('stop', None, 90)] and ev12[0]['utc'] == iso(ceil1(issue2) + K1_MS) and ceil5(issue2) == issue + K5_MS)
        ev13, cur13 = walk(S2(), cur2, c_up, zero, k5b, k1=M(*[(100, 101, 99, 100)] * 4))
        chk('walk: four quiet minutes to the boundary, then the 5-minute candle of 00:15 reaching target 1; the place after it',
            kinds(ev13) == [('target', 1, 110)] and ev13[0]['utc'] == iso(ceil5(issue2)) and cur13['t'] == ceil5(issue2) + K5_MS)
        k14 = M((100, 100.5, 99.8, 100), (100, 100, 99.4, 99.6)) + [(ceil1(issue2) + 2 * K1_MS, 99.6, 100, 99.5, 99.9, False)]
        ev14, cur14 = walk(S2(mode='limit', E=99.5), cur2, c_up, zero, [], k1=k14)
        chk('walk: a limit filled in its first minutes, at the minute that reached it; the place at the minute not yet closed',
            kinds(ev14) == [('fill', None, 99.5)] and ev14[0]['utc'] == iso(ceil1(issue2) + K1_MS) and cur14['t'] == ceil1(issue2) + 2 * K1_MS)
        ev15, cur15 = walk(S2(), cur2, c_up, zero, k5b, until=ceil1(issue2) + 2 * K1_MS + 1, k1=M(*[(100, 101, 99, 100)] * 4))
        chk('walk: until inside the first minutes stops at the minute closing after it', ev15 == [] and cur15['t'] == ceil1(issue2) + 2 * K1_MS)
        rgw, asked = Registry(state), []

        def fake_r(path, **p_):
            step = K1_MS if p_['interval'] == '1m' else K5_MS
            asked.append((p_['symbol'][:-4], step, int(p_['startTime']), int(p_['limit'])))
            t_, out = int(p_['startTime']), []
            while len(out) < int(p_['limit']) and t_ <= issue + 30 * K1_MS:
                out.append([t_, '100', '100.1', '99.9', '100', '0', t_ + step - 1, '0'])
                t_ += step
            return out
        adv3.fapi = fake_r
        for i_, coin_, at_ in ((1, 'ETH', issue), (2, 'SOL', issue2)):
            rgw.append(dict(S(i=i_, qty=1.0), type='open', coin=coin_, utc=iso(at_)), dt.datetime.now(dt.timezone.utc))
            rgw.append({'type': 'fill', 'id': i_, 'utc': iso(at_), 'price': 100.0}, dt.datetime.now(dt.timezone.utc))
            rgw.cursor[i_] = {'t': ceil1(at_), 'b': at_, 'mfe': 0.0}
        reconcile(rgw, {}, {}, issue + 30 * K1_MS + 1, dt.datetime.now(dt.timezone.utc))
        first_asked = list(asked)
        reconcile(rgw, {}, {}, issue + 30 * K1_MS + 1, dt.datetime.now(dt.timezone.utc))
        chk('reconcile: the signal issued at 00:10:20 asks its four minutes, 00:11 to 00:15, once, beside its coin\'s 5-minute candles from '
            '00:15; the one issued at 00:10 asks none; coins in the rule\'s order; walked, both places at the candle not yet closed, 00:40',
            first_asked == [('SOL', K5_MS, ceil5(issue2), K5_PAGE), ('SOL', K1_MS, ceil1(issue2), 4), ('ETH', K5_MS, issue, K5_PAGE)]
            and asked[3:] == [('SOL', K5_MS, issue + 6 * K5_MS, K5_PAGE), ('ETH', K5_MS, issue + 6 * K5_MS, K5_PAGE)]
            and rgw.cursor[1]['t'] == rgw.cursor[2]['t'] == issue + 6 * K5_MS)
        asked.clear()
        none_ = klines('ETH', issue + 31 * K1_MS, issue + 30 * K1_MS + 1) + klines('ETH', issue + 31 * K1_MS, issue + 30 * K1_MS + 1, K1_MS, 4)
        chk('klines: a start after the moment asks nothing - a signal issued this minute waits for its first candle, no request made', none_ == [] and asked == [])
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- the position, the shares, the plans -------------------------------------------------------------------------
        card8 = {'stop_pct': 8.0, 'leverage': 7, 'entry': 100.0}
        p8, _w = position(card8, 0.5, 200000.0, None)
        chk('position: 0.5 % at an 8 % stop is 12,195 USDT at the rule\'s 7x, margin 1,743, loss 999.99 with both sides\' costs',
            (p8['notional'], p8['leverage'], p8['margin']) == (12195, 7, 1743) and abs(p8['loss'] - 12195 * 0.082) < 1e-9
            and abs(p8['qty'] - 121.95) < 1e-12 and not p8['capped'] and not p8['over'] and not p8['cut'])
        p12, _w = position({'stop_pct': 12.0, 'leverage': 5, 'entry': 50.0}, 0.25, 200000.0, None)
        chk('position: 0.25 % at a 12 % stop is 4,098 USDT; the leverage lowered from 5x to 4x so the margin, 1,025, stays above 1,000',
            (p12['notional'], p12['leverage'], p12['lmax'], p12['margin']) == (4098, 4, 5, 1025))
        p05, w05 = position({'stop_pct': 12.0, 'leverage': 5, 'entry': 50.0}, 0.05, 200000.0, None)
        chk('position: 819 USDT is under the margin\'s floor and no position - the risk is never raised to meet it',
            p05 is None and w05 == 'позиция меньше минимальной маржи 1 000 USDT')
        pl, _w = position(card8, 0.5, 200000.0, 1_000_000.0)
        pv, wv = position(card8, 0.5, 200000.0, 100_000.0)
        chk('position: at most 0.5 % of the coin\'s daily volume - 5,000 USDT of 1,000,000 - at 5x for a margin of 1,000, and says so; '
            '500 USDT of 100,000 is under the margin\'s floor, by the liquidity',
            (pl['notional'], pl['leverage'], pl['margin'], pl['capped']) == (5000, 5, 1000, True) and abs(pl['loss'] - 410) < 1e-9
            and pv is None and wv == 'позиция меньше минимальной маржи 1 000 USDT — по ликвидности')
        pc, _w = position({'stop_pct': 5.0, 'leverage': 1, 'entry': 10.0}, 1.0, 200000.0, None)
        pc2, _w = position({'stop_pct': 5.0, 'leverage': 1, 'entry': 10.0}, 1.0, 12345.67, None)
        chk('position: a margin above 4 % of the capital is cut to 8,000 USDT, beyond the 3.5 % of 7,000 an exception; at 12,345.67 USDT '
            'to 493, the whole USDT within 4 %',
            (pc['notional'], pc['margin'], pc['cut'], pc['over']) == (8000, 8000, True, True)
            and (pc2['notional'], pc2['margin'], pc2['leverage'], pc2['cut']) == (493, 493, 1, True))
        chk('position: a rule leverage under 1x is no position', position({'stop_pct': 70.0, 'leverage': 0, 'entry': 1.0}, 0.5, 200000.0, None)[0] is None)

        def card_z(z, stop_pct=8.0, lev=7):
            return {'z': z, 'stop_pct': stop_pct, 'leverage': lev, 'entry': 100.0}
        its = [{'coin': c, 'side': 1, 'rank': k, 'card': card_z(z), 'sig': None, 'why': None} for k, (c, z) in enumerate((('ETH', 3.5), ('SOL', 2.0), ('XRP', 1.0)), 1)]
        allocate(its, DEFAULTS, 10.0, {})
        want = [3 * 0.5 * q / 6 for q in (3, 2, 1)]
        chk('allocate: shares min(|z|, 3) of 6 - a half, a third, a sixth - of three times 0.5 %: 0.75, 0.5 and 0.25 %, the strongest the most',
            [round(it['pos']['want'], 12) for it in its] == [round(x, 12) for x in want]
            and [it['pos']['notional'] for it in its] == [math.floor(w / 100 * 200000 / 0.082) for w in want])
        its2 = [{'coin': c, 'side': 1, 'rank': k, 'card': card_z(z), 'sig': None, 'why': None} for k, (c, z) in enumerate((('ETH', 3.5), ('SOL', 2.0), ('XRP', 1.0)), 1)]
        allocate(its2, DEFAULTS, 1.0, {})
        first_r = math.floor(0.75 / 100 * 200000 / 0.082) * 0.082 / 2000
        chk('allocate: a room of 1 % - the first its 0.75 %, the second the rest and marked short, the third the room\'s reason',
            abs(its2[0]['pos']['risk_pct'] - first_r) < 1e-12 and its2[1]['pos']['short'] is True
            and its2[1]['pos']['notional'] == math.floor((1.0 - first_r) / 100 * 200000 / 0.082)
            and its2[2].get('pos') is None and its2[2]['code'] == 'room' and its2[2]['why'] == 'лимит общего риска 10% исчерпан')
        its3 = [{'coin': adv3.COINS[k], 'side': 1, 'rank': k + 1, 'card': card_z(z), 'sig': None, 'why': None} for k, z in enumerate((3, 1, 1, 1, 1, 1, 1))]
        allocate(its3, DEFAULTS, 10.0, {})
        chk('allocate: seven trades, one of strength 3 and six of 1 - the first 7 x 0.5 % x 3/9, capped at the rule\'s 1 %, the others 0.39 %',
            its3[0]['pos']['want'] == 1.0 and all(abs(it['pos']['want'] - 7 * 0.5 / 9) < 1e-12 for it in its3[1:]))
        rnd, bad = random.Random(42), []
        for trial in range(300):
            k = rnd.randint(1, 9)
            zs = sorted((rnd.uniform(1.0, 5.0) for _ in range(k)), reverse=True)
            prm = dict(DEFAULTS, capital=rnd.choice((10000.0, 12345.67, 50000.0, 200000.0, 1e6)), risk=rnd.choice((0.05, 0.25, 0.5, 1.0)))
            room = rnd.choice((10.0, 3.0, 0.7, 0.01))
            vol = {adv3.COINS[i]: rnd.choice((None, 2e5, 5e6, 1e9)) for i in range(k)}
            items_ = []
            for i, z in enumerate(zs):
                sp = rnd.uniform(1.0, 14.0)
                items_.append({'coin': adv3.COINS[i], 'side': 1, 'rank': i + 1, 'sig': None, 'why': None,
                               'card': {'z': z, 'stop_pct': sp, 'leverage': min(20, math.floor(1 / (1.5 * sp / 100 + 0.01))), 'entry': 3.0}})
            allocate(items_, prm, room, vol)
            placed = [it for it in items_ if it.get('pos')]
            wants = [it['pos']['want'] for it in placed]
            cap_ = prm['capital']
            ok = (all(a >= b - 1e-12 for a, b in zip(wants, wants[1:])) and sum(it['pos']['risk_pct'] for it in placed) <= room + 1e-9
                  and all(it['pos']['risk_pct'] <= 1.0 + 1e-9 for it in placed)
                  and all(MARGIN_MIN / 100 * cap_ - 1e-9 <= it['pos']['margin'] <= MARGIN_EXC / 100 * cap_
                          and 1 <= it['pos']['leverage'] <= it['card']['leverage'] and it['pos']['margin'] * it['pos']['leverage'] >= it['pos']['notional']
                          and float(it['pos']['notional']).is_integer() for it in placed)
                  and all((not vol.get(it['coin'])) or it['pos']['notional'] <= LIQ_FRAC * vol[it['coin']] + 1e-9 for it in placed)
                  and all(abs(it['pos']['loss'] - it['pos']['notional'] * (it['card']['stop_pct'] / 100 + 0.002)) < 1e-6 for it in placed)
                  and all(it.get('code') in ('room', 'margin') for it in items_ if not it.get('pos')))
            if not ok:
                bad.append(trial)
        chk('allocate over 300 random scenarios: wanted risk never rising with rank, each within 1 %, all within the room; margin within 0.5 '
            'and 4 % of the capital and covering the position, leverage 1 to the rule\'s, whole USDT, the liquidity cap; a reason for each left out',
            not bad)

        # a report of synthetic rows: the plans
        CL = '2026-11-04'
        base_rows = {c: {'signal': None} for c in adv3.COINS}

        def row(side, z, ssum=None, U=8.0, mark=100.0):
            return {'signal': side, 'z': z * side, 'sum': (4 if ssum is None else ssum) * side, 'U': U, 'close': 100.0, 'prev': side,
                    'since': '2026-10-20', 'stop': 100.0 - side * U, 'mark': mark, 'funding': 0.0001, 'funding_h': 8}
        spec = {'ETH': row(1, 3.2), 'SOL': row(1, 2.6), 'XRP': row(-1, 2.4, U=16.0), 'ADA': row(1, 2.2, mark=92.5), 'BNB': row(1, 2.05, ssum=2),
                'AVAX': row(1, 1.9), 'LINK': row(1, 1.8), 'XMR': row(1, 1.7), 'NEAR': row(1, 1.6), 'HBAR': row(1, 1.5), 'ENA': row(1, 1.4),
                'UNI': row(1, 1.3), 'ARB': row(1, 1.25), 'ZEC': row(1, 1.2), 'HYPE': row(1, 1.1), 'SUI': row(1, 1.05), 'LTC': row(1, 0.8)}
        rep = {'rule': adv3.RULE, 'close_of': CL, 'deposit': CAPITAL, 'risk_pct': 0.5, 'marks_ok': True, 'made_at_ms': 0,
               'rows': dict(base_rows, **spec), 'top': ['ETH', 'SOL', 'XRP'], 'strong': ['ETH', 'SOL', 'XRP'], 'cards': [], 'trust': {}}
        order_hand = ['ETH', 'SOL', 'XRP', 'ADA', 'BNB', 'AVAX', 'LINK', 'XMR', 'NEAR', 'HBAR', 'ENA', 'UNI', 'ARB', 'ZEC', 'HYPE', 'SUI', 'LTC']
        chk('the synthetic report: the rule\'s order by |z|, STRONG at every rank all but BNB (sum 2) and LTC (|z| 0.8)',
            ranked(rep) == order_hand and strong_all(rep) == [c for c in order_hand if c not in ('BNB', 'LTC')])
        rg = Registry(state)
        mk = lambda i, coin, close_of, risk=0.5: {'type': 'open', 'id': i, 'utc': '2026-11-01T00:10:00+00:00', 'coin': coin, 'side': 1,
                                                 'close_of': close_of, 'mode': 'market', 'entry': 100.0, 'stop': 92.0, 'targets': [108.0, 116.0, 124.0],
                                                 'valid': '2026-11-06T00:00:00+00:00', 'risk_pct': risk, 'qty': 1.0}
        rg.append(mk(1, 'XMR', '2026-10-31'), when)
        rg.append({'type': 'fill', 'id': 1, 'utc': '2026-11-01T00:10:00+00:00', 'price': 100.0}, when)
        rg.append(mk(2, 'LINK', CL), when)
        rg.append({'type': 'fill', 'id': 2, 'utc': '2026-11-05T00:10:00+00:00', 'price': 100.0}, when)
        rg.append(mk(3, 'NEAR', CL), when)
        rg.append({'type': 'fill', 'id': 3, 'utc': '2026-11-05T00:10:00+00:00', 'price': 100.0}, when)
        rg.append({'type': 'stop', 'id': 3, 'utc': '2026-11-05T02:00:00+00:00', 'price': 92.0, 'R': -1.02, 'pnl': -8.16}, when)
        mine, new, excl = candidates(rep, rg, DEFAULTS)
        chk('candidates: this close\'s open LINK is the registry\'s; XMR, open from an earlier close, is the open list\'s; NEAR ended this close; '
            'XRP\'s stop 16 % and ADA at its stop are named; the rest new, in the rule\'s order',
            [it['coin'] for it in mine] == ['LINK'] and mine[0]['sig']['id'] == 2
            and [it['coin'] for it in new] == ['ETH', 'SOL', 'AVAX', 'HBAR', 'ENA', 'UNI', 'ARB', 'ZEC', 'HYPE', 'SUI']
            and [(c, code) for c, _s, code, _w, _d in excl] == [('XRP', 'stop'), ('ADA', 'near'), ('NEAR', 'ended')]
            and excl[0][3:] == ('стоп дальше 14%', '16,0%') and excl[2][4] == '#3 стоп')
        vols = {c: 1e12 for c in adv3.COINS}
        m = model_plan(rep, rg, vols)
        qs = [3.0, 2.6, 1.9, 1.5, 1.4]
        wants = [min(1.0, 5 * 0.5 * q / sum(qs)) for q in qs]
        chk('model_plan: two signals of this close leave five places of seven - ETH, SOL, AVAX, HBAR and ENA - their risk 5 x 0.5 % shared by '
            'min(|z|, 3); the other five named, beyond seven new a close',
            [it['coin'] for it in m['new']] == ['ETH', 'SOL', 'AVAX', 'HBAR', 'ENA']
            and all(abs(it['pos']['want'] - w) < 1e-12 for it, w in zip(m['new'], wants))
            and [(c, code) for c, _s, code, _w, _d in m['excluded'][3:]] == [(c, 'count') for c in ('UNI', 'ARB', 'ZEC', 'HYPE', 'SUI')]
            and m['risk'] == {1: 1.0, -1: 0.0})
        rg_full = Registry(state)
        rg_full.sig[1]['risk_pct'] = 9.5
        mf = model_plan(rep, rg_full, vols)
        chk('model_plan: the room spent - 9.5 % and 0.5 % open - every candidate named for the room, those beyond seven too',
            mf['new'] == [] and [code for _c, _s, code, _w, _d in mf['excluded'][3:]] == ['room'] * 10)
        v = view_plan(rep, rg, vols, dict(DEFAULTS, n=2, set=['n']), m)
        chk('view_plan: «топ 2» - ETH and SOL; LINK, this close\'s, and AVAX, HBAR and ENA named beyond the request\'s top',
            [it['coin'] for it in v['items']] == ['ETH', 'SOL'] and [c for c, _s, code, _w, _d in v['excluded'] if code == 'top'] == ['AVAX', 'LINK', 'HBAR', 'ENA'])
        rows_tight = dict(rep['rows'], SOL=row(1, 2.6, U=12.0))
        rep_t = dict(rep, rows=rows_tight)
        m_t = model_plan(rep_t, rg, vols)
        v2 = view_plan(rep_t, rg, vols, dict(DEFAULTS, stop=10.0, set=['stop']), m_t)
        chk('view_plan: «стоп 10» names SOL for its 12 % stop at 10 %; a coin the model left out keeps the model\'s reason; LINK, the '
            'registry\'s, stays sized', ('SOL', 'stop', 'стоп дальше 10%', '12,0%') in [(c, code, w, d) for c, _s, code, w, d in v2['excluded']]
            and ('UNI', 'count') in [(c, code) for c, _s, code, _w, _d in v2['excluded']]
            and 'LINK' in [it['coin'] for it in v2['items']] and all(it.get('pos') for it in v2['items']))
        ids_ = register(rg, rep, m['new'], when, 'check:test')
        reg_ev = [e for e in rg.events if e['type'] in ('open', 'fill') and e['id'] >= 4]
        chk('register: ids 4 to 8 in the rule\'s order, each open then filled at its market entry at the instant written; places from it',
            ids_ == [4, 5, 6, 7, 8] and [(e['type'], e['id']) for e in reg_ev] == [(t_, i) for i in range(4, 9) for t_ in ('open', 'fill')]
            and all(e['utc'] == when.isoformat(timespec='seconds') for e in reg_ev)
            and all(rg.sig[i]['valid'] == '2026-11-06T00:00:00+00:00' and rg.sig[i]['capital'] == CAPITAL and rg.sig[i]['btc'] is None
                    and rg.sig[i]['breadth'] == 15 for i in ids_)
            and rg.cursor[4] == {'t': ceil1(ms_at(when)), 'b': ms_at(when), 'mfe': 0.0})
        later = when + dt.timedelta(seconds=20, microseconds=500_000)
        ids_l = register(rg, rep, [dict(m['new'][0], rank=1)], later, 'request')
        sl = rg.sig[ids_l[0]]
        chk('register: an instant inside a minute - 00:10:20.5 - written to its second, the place from the next minute, 00:11',
            sl['utc'] == '2026-11-05T00:10:20+00:00' and sl['fill_utc'] == sl['utc']
            and rg.cursor[ids_l[0]] == {'t': ms_at(when) + K1_MS, 'b': ms_at(when) + 20_000, 'mfe': 0.0})
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- the seed: a journal of the old records ------------------------------------------------------------------------
        globals()['STATE'] = state
        T0 = dt.datetime(2026, 10, 29, 14, 40, tzinfo=dt.timezone.utc)
        tz_ = lambda h: (T0 + dt.timedelta(hours=h)).isoformat(timespec='seconds')
        cardj = lambda coin, mode='market', E=100.0, strong=True, side=1: {'coin': coin, 'side': side, 'strong': strong, 'mode': mode, 'entry': E,
                                                                         'stop': 90.0, 'targets': [110.0, 120.0, 130.0], 'close': 100.0, 'U': 10.0,
                                                                         'since': '2026-10-20', 'rank': 1}
        recs = [{'utc': tz_(0), 'kind': 'daily', 'close_of': '2026-10-28', 'cards': [cardj('ETH'), cardj('BTC', strong=False), cardj('SOL', mode='none', E=None), {'coin': 'ETH'}],
                 'signals': {'BTC': 1}},
                {'utc': tz_(15), 'kind': 'alloc', 'close_of': '2026-10-29', 'alloc': {'items': [{'coin': 'SOL'}], 'more': []},
                 'cards': [cardj('SOL'), cardj('AVAX')]},
                {'utc': tz_(16), 'kind': 'request', 'close_of': '2026-10-29', 'cards': [cardj('ETH', E=101.0), cardj('SOL', mode='limit')]},
                {'utc': tz_(40), 'kind': 'check', 'close_of': '2026-10-30', 'cards': [cardj('ETH', E=95.0)], 'state': {'ETH': {'z': 2.5, 'sum': 4}}},
                {'utc': tz_(41), 'kind': 'assess', 'close_of': '2026-10-30', 'cards': [cardj('XRP')]}]
        with open(os.path.join(state, 'journal.jsonl'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(json.dumps(r) for r in recs[:2]) + '\nnot json\n' + '\n'.join(json.dumps(r) for r in recs[2:]) + '\n')
        t_open = ms_at(T0)

        def fake5(path, **p_):
            coin, start = p_['symbol'][:-4], int(p_['startTime'])
            out = []
            t_ = max(start, ceil5(t_open))
            while len(out) < int(p_['limit']) and t_ <= t_open + 60 * 3600_000:
                px = 100.0 if not (coin == 'ETH' and t_open + 20 * 3600_000 <= t_ < t_open + 21 * 3600_000) else 89.0
                out.append([t_, str(px), str(px + 0.5), str(px - 0.5), str(px), '0', t_ + K5_MS - 1, '0'])
                t_ += K5_MS
            return out
        adv3.fapi = fake5
        rs = Registry(state)
        opened = seed(rs, {}, {}, t_open + 60 * 3600_000, when)
        sigs = [rs.sig[i] for i in sorted(rs.sig)]
        jsha = hashlib.sha256(open(os.path.join(state, 'journal.jsonl'), 'rb').read()).hexdigest()
        def legacy_pos(E, S):
            d_ = abs(E - S) / E
            rate = d_ + 0.002
            notional = math.floor(0.005 * CAPITAL / rate)
            lev = min(min(20, math.floor(1 / (1.5 * d_ + 0.01))), math.floor(notional / 1000))
            return notional, math.ceil(notional / lev)
        chk('seed: its first event names the journal by SHA-256, its 5 records that parse and the 5 STRONG cards with an entry of the kinds '
            'it reads; the signals ETH of 29.10, SOL of the allocation\'s placed coin and ETH again after its stop - a card repeated within a '
            'signal\'s life is that signal shown again',
            rs.events[0]['type'] == 'seed' and rs.events[0]['journal_sha'] == jsha and rs.events[0]['records'] == 5 and rs.events[0]['cards'] == 5
            and opened == 3 and [(s['coin'], s['close_of'], s['source']) for s in sigs]
            == [('ETH', '2026-10-28', 'journal:daily'), ('SOL', '2026-10-29', 'journal:alloc'), ('ETH', '2026-10-30', 'journal:check')]
            and sigs[0]['status'] == 'closed' and sigs[0]['why'] == 'stop' and sigs[2]['entry'] == 95.0 and sigs[2]['z'] == 2.5 and sigs[0]['btc'] == 1
            and all(s['legacy'] and (s['notional'], s['margin']) == legacy_pos(s['entry'], s['stop']) for s in sigs)
            and [legacy_pos(100.0, 90.0), legacy_pos(95.0, 90.0)] == [(9803, 1634), (18304, 1664)])
        chk('seed: ETH\'s stop walked to the instant of the next card - the candle opening at 89, beyond the stop at 90 - before ETH of '
            '30.10 is written', [e['type'] for e in rs.events] == ['seed', 'open', 'fill', 'open', 'fill', 'stop', 'open', 'fill']
            and rs.events[5]['utc'] == iso(t_open + 20 * 3600_000) and rs.events[5]['price'] == 89.0)
        for name in os.listdir(state):
            os.remove(os.path.join(state, name))

        # ---- the stats, by hand -------------------------------------------------------------------------------------------
        w1, w2 = wilson(5, 10), wilson(0, 1)
        chk('wilson: 5 of 10 is 23.66 to 76.34 %, 0 of 1 is 0 to 79.35 %', abs(w1[0] - 23.66) < 0.01 and abs(w1[1] - 76.34) < 0.01
            and abs(w2[0]) < 1e-9 and abs(w2[1] - 79.35) < 0.01)
        chk('t975: the table to 30 - 12.706 at 1, 2.042 at 30 - then the expansion: 2.0395 at 31, 2.0003 at 60, 1.9799 at 120',
            t975(1) == 12.706 and t975(30) == 2.042 and abs(t975(31) - 2.0395) < 2e-4 and abs(t975(60) - 2.0003) < 2e-4 and abs(t975(120) - 1.9799) < 2e-4)
        mc = mean_ci([1.0, 2.0, 3.0, 4.0])
        chk('mean_ci: 1, 2, 3, 4 - mean 2.5, 95 % from 0.446 to 4.554; one value, no interval',
            mc[0] == 2.5 and abs(mc[1] - (2.5 - 3.182 * math.sqrt(5 / 3) / 2)) < 1e-12 and mean_ci([1.0])[1:] == (None, None))

        # ---- checks and requests end to end: Binance and Telegram stood in for ------------------------------------------------
        class Cap(Telegram):
            def __init__(self, down=False):
                super().__init__('123456:SECRET', 777)
                self.sent, self.down = [], down

            def call(self, method, http_timeout=30, **params):
                if self.down:
                    raise RuntimeError('telegram sendMessage: 502 Bad Gateway')
                self.sent.append((params['text'], params.get('disable_notification', False), 'reply_markup' in params))
                return {'message_id': len(self.sent)}

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
        T1 = at(last + adv3.DAY, 0, 10)
        clock = {'now': T1}
        path5, calls1 = {}, []

        def fake(path, **p_):
            now_ms = ms_at(clock['now'])
            if path == '/fapi/v1/premiumIndex':
                return [{'symbol': c + 'USDT', 'markPrice': str(cs[c][last][3]), 'lastFundingRate': '0.0001'} for c in cs]
            if path == '/fapi/v1/fundingInfo':
                return []
            coin = p_['symbol'][:-4]
            if p_['interval'] == '1d':
                return [[day_ms(last - k * adv3.DAY), '1', '1', '1', '1', '0', day_ms(last - k * adv3.DAY) + DAY_MS - 1, '1e12'] for k in range(8)]
            step = K1_MS if p_['interval'] == '1m' else K5_MS
            calls1.append(step == K1_MS)
            out, t_ = [], max(int(p_['startTime']), ms_at(T1) - 2 * K5_MS)
            base_ = cs[coin][last][3]
            while len(out) < int(p_['limit']) and t_ <= now_ms:
                px = path5.get(coin, {}).get(t_ - t_ % K5_MS, base_)
                out.append([t_, str(px), str(px * 1.0001), str(px * 0.9999), str(px), '0', t_ + step - 1, '0'])
                t_ += step
            return out

        class Stub:
            def __init__(self):
                self.cs, self.funds, self.missing = cs, funds, []

            def fresh(self):
                return self.cs, self.funds

        adv3.fapi = fake
        stub, cap, rg = Stub(), Cap(), Registry(state)

        def run(fn, *a):
            with contextlib.redirect_stdout(io.StringIO()):
                return fn(*a)
        rep0 = adv3.report(cs, funds, {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}, CAPITAL, 0.5, ms_at(T1))
        strong0 = strong_all(rep0)
        e1 = run(check, cap, stub, rg, (T1.date(), 'signal'), T1)
        append(e1)
        n_new = len(e1['opened'])
        chk('end to end, the first signal check: the registry seeded from an empty journal, the STRONG candidates written after the message '
            'went - seven at most - loud, one full message; its record the 42 coins, the cards with their numbers and positions, the registry',
            rg.events[0]['type'] == 'seed' and rg.events[0]['cards'] == 0 and 1 <= n_new <= NEW_MAX and e1['opened'] == list(range(1, n_new + 1))
            and e1['quiet'] is False and e1['one_line'] is False and len(cap.sent) == 1 and '🆕 <b>Новые STRONG</b>' in cap.sent[0][0]
            and len(e1['state']) == 42 and [c['id'] for c in e1['cards']] == e1['opened'] and all(c['position'] for c in e1['cards'])
            and e1['strong_all'] == strong0 and e1['registry']['seeded'] == 0 and rg.announced == len(rg.events)
            and all(f'#{i}' in cap.sent[0][0] for i in e1['opened']) and cap.sent[0][2] is False)
        e1b = run(check, cap, stub, rg, (T1.date(), 'signal'), T1 + dt.timedelta(minutes=1))
        append(e1b)
        chk('end to end, the same check again: nothing new, nothing ended, the coins not taken as before - one quiet line, no signal written twice',
            e1b['one_line'] is True and e1b['quiet'] is True and e1b['opened'] == [] and '\n' not in cap.sent[-1][0]
            and cap.sent[-1][0].startswith('✓ 04:11 по Батуми · закрытие') and len([s for s in rg.sig.values()]) == n_new)
        coin_a, coin_b = rg.sig[1]['coin'], rg.sig[min(2, n_new)]['coin']
        sa = rg.sig[1]
        Tt = ms_at(T1) + 10 * K5_MS
        path5[coin_a] = {Tt: sa['targets'][0] + sa['side'] * 0.0}
        clock['now'] = T1 + dt.timedelta(hours=15)
        Tf = at(T1.date(), 15, 7)
        e2 = run(check, cap, stub, rg, (T1.date(), 'fact'), Tf)
        append(e2)
        chk('end to end, the fact check: the first signal\'s target 1, walked on its 5-minute candles, a quiet event - no new signal, no end',
            [(rg.events[n - 1]['type'], rg.events[n - 1]['id']) for n in e2['events']] == [('target', 1)] and e2['quiet'] is True
            and e2['one_line'] is False and '🎯 #1' in cap.sent[-1][0] and rg.sig[1]['hit'] == 1)
        if n_new >= 2:
            sb = rg.sig[2]
            path5[coin_b] = {ceil5(ms_at(Tf)) + 6 * K5_MS: sb['stop'] - sb['side'] * sb['entry'] * 0.01}
        clock['now'] = T1 + dt.timedelta(hours=16)
        down = Cap(down=True)
        failed = False
        try:
            run(check, down, stub, rg, (T1.date(), 'fact'), T1 + dt.timedelta(hours=16))
        except RuntimeError:
            failed = True
        stopped = [e for e in rg.events if e['type'] == 'stop']
        chk('end to end, Telegram down: the check raises, the stop it found is written and stays unannounced',
            failed and (n_new < 2 or (len(stopped) == 1 and stopped[0]['n'] > rg.announced)))
        e3 = run(check, cap, stub, rg, (T1.date(), 'fact'), T1 + dt.timedelta(hours=16, minutes=5))
        append(e3)
        chk('end to end, the retry: the stop announced once, loud', n_new < 2 or (e3['quiet'] is False and '⛔ #2' in cap.sent[-1][0]
                                                                           and [rg.events[n - 1]['type'] for n in e3['events']] == ['stop']))
        e4 = run(check, cap, stub, rg, (T1.date(), 'fact'), T1 + dt.timedelta(hours=16, minutes=10))
        chk('end to end, the fact check again: one quiet line naming the next check', e4['one_line'] is True and e4['quiet'] is True
            and 'следующая проверка 04:10' in cap.sent[-1][0])
        rr = Registry(state)
        chk('the registry read back after the checks: the same signals, head and announced, the chain whole',
            rr.sig == rg.sig and rr.head == rg.head and rr.announced == rg.announced and rr.broken is None)
        cap2, per = Cap(), []
        for text in ('сигнал', 'сигнал 50000 риск 1 топ 2', 'реестр', 'рейтинг', 'оценка', 'помощь', 'привет'):
            n0 = len(cap2.sent)
            run(handle, cap2, stub, rg, text)
            per.append(cap2.sent[n0:])
        texts = ['\n'.join(t for t, _q, _k in p_) for p_ in per]
        chk('handle: «сигнал» the close\'s STRONG with their positions and the risk, «сигнал 50000…» at the request\'s parameters, «реестр» the '
            'signals and the chain, «рейтинг» the order, «оценка» the assessment and the registry\'s figures, «помощь» and an unknown text HELP; '
            'every reply its keyboard and a notification',
            texts[0].startswith('📊 <b>ADV-3 · STRONG</b>') and 'Риск модели' in texts[0] and 'Капитал 50 000 USDT · риск 1,0%' in texts[1]
            and 'по запросу: капитал, топ, риск' in texts[1] and texts[2].startswith('📒') and '🔐 Реестр:' in texts[2]
            and texts[3].startswith('🏆') and '1. ' in texts[3] and 'Оценка доверия' in texts[4] and 'Реестр сигналов бота' in texts[4]
            and texts[5] == HELP and texts[6] == HELP and all(p_[-1][2] for p_ in per) and all(not q for p_ in per for _t, q, _k in p_))
        kinds_ = [r['kind'] for r in journal_records()]
        chk('handle: the journal holds check, check, check, check, then request, request, registry, ranking, assess - HELP no record',
            kinds_ == ['check'] * 4 + ['request', 'request', 'registry', 'ranking', 'assess'])
        saved_lr = globals()['live_report']
        globals()['live_report'] = lambda *a_: (_ for _ in ()).throw(RuntimeError('fapi.binance.com served no candles'))
        try:
            run(handle, cap2, stub, rg, 'сигнал')
            run(handle, Cap(down=True), stub, rg, 'сигнал')
        finally:
            globals()['live_report'] = saved_lr
        chk('handle: Binance down gets the apology, Telegram down raises nothing', cap2.sent[-1][0].startswith('Binance или Telegram не ответили'))
        allt = [t for t, _q, _k in cap.sent + cap2.sent]
        chk('every part of every message balances its markup', all(t.count('<b>') == t.count('</b>') and t.count('<i>') == t.count('</i>')
                                                                   for t in allt))
        chk('no message calls the bot the Boss\'s account or asks to check his positions', not any(
            k in t for t in allt for k in ('ваши позиции', 'проверьте позиции', 'ваш аккаунт', 'видит ваш счёт')))
    finally:
        globals()['STATE'], adv3.fapi = saved
        shutil.rmtree(state)
    chk('glibc takes its two settings', malloc_tune())
    time.sleep = real_sleep
    chk('the self-test restored time.sleep and paused nowhere: every pause recorded', time.sleep is real_sleep and all(x in (1.1, 8, 61) for x in slept))
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
