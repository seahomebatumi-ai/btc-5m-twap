#!/usr/bin/env python3
"""liq-guard.py - the liquidation guard (TZ-54, CANON PART VII): the Boss's Binance USD-M futures positions read
every five seconds through a key that can read and nothing else, each position's distance from its mark price to its
liquidation price held against three thresholds of his - a Telegram message, then Pushover's emergency alarm, then a
second one - and the guard's own loss of Binance alarmed the same way. It never trades and holds no key that can.
Standard library only; every connection IPv4, because the key is bound to the host's IPv4 address.

Modes:
    secrets     the Boss, at his terminal: the Binance key and secret, the Pushover user key and token, the Telegram
                token, the dead-man's ping address or none - each hidden, each written once, 0600, root's
    find-chat   the one private chat that sent /start to the guard's bot, pinned
    prove       every request path proved through this file's own functions, the key's permissions read, and a test
                alarm acknowledged on the Boss's phone (CANON hard rule 14); its record prove.json
    serve       the unit's loop, under systemd, Type=notify with a watchdog
    status      the guard's own state from its files - no symbol, price, size or margin is printed
    scan FILE.. G-PRINT: in each file, the occurrences of every credential, the chat id and this host's own IPv4
                addresses - counts alone; exit 4 where any is found
    selftest    every pure function and every flow against stand-ins, and `secrets` at a real pseudo-terminal
Exits: 0 done; 1 a failed assert or a BLOCK; 2 refused - a key that can do more than read, or a credential missing or
malformed - which the unit does not restart; 4 a reading's FAIL. Never printed by any mode: a key, secret, token,
user key, ping address, chat id, address of this host, or any figure of a position."""
import datetime as dt
import getpass
import hashlib
import hmac
import http.client
import json
import os
import re
import signal
import socket
import ssl
import sys
import threading
import time
import urllib.parse

if not __debug__:
    sys.stderr.write("liq-guard: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

# ---- constants: none is measured by this file -------------------------------------------------------------------

ETC = "/etc/liq-guard"
VAR = "/var/lib/liq-guard"
UA = "btc-5m-twap-liq-guard"
FAPI, SAPI, PUSHOVER, TG, HC = "fapi.binance.com", "api.binance.com", "api.pushover.net", "api.telegram.org", "hc-ping.com"
POSITION_PATHS = ("/fapi/v3/positionRisk", "/fapi/v2/positionRisk")
POLL_S = 5                    # one read of the positions; its weight 5 is 60 a minute of Binance's 2,400
TIMEOUT_S = 10                # a request's socket timeout: two reads and a send fit a watchdog interval
RECV_WINDOW = 10000           # ms; the clock is read from Binance every hour besides
BLIND_S = 120                 # no read for this long: the guard is blind and says so
BLIND_REPEAT_S = 1800
TIME_SYNC_S, BRACKETS_S, PERM_S, PERM_RETRY_S = 3600, 3600, 6 * 3600, 60
HC_S, TICK_S, STATE_S = 60, 600, 30
ERR_EVERY_S = 60             # one journal line a minute for a repeating error
KEEP_DAYS = 90               # journal files older than this are removed at the tick
BACKOFF_S = {429: 60, 418: 300}   # Binance's rate refusals: no request to it until this has passed
DEFAULT_THRESHOLDS = (5.0, 3.0, 1.5)   # percent of the mark price: Telegram, the alarm, the second alarm
REARM_PP = 1.0                # a level re-arms once the distance is this many points above its threshold
TARGET_PCT = 8.0              # the distance the margin hint aims the liquidation price at
ALARM_RETRY_S, ALARM_EXPIRE_S = 30, 3600       # Pushover's emergency priority: its minimum retry, an hour
TEST_EXPIRE_S, TEST_WAIT_S, RECEIPT_EVERY_S = 900, 900, 10
PUSH_PER_HOUR = 20
OUTBOX_TRIES = 10
OUTBOX_MAX = 100             # Telegram messages beyond this, oldest first, are dropped; alarms never
TG_PER_PASS = 5              # Telegram messages sent in one pass; the rest wait for the next
COOLDOWN_S = 15              # a host that failed at the network is not tried again for this long
HEARTBEAT_UTC = (19, 0)       # 23:00 in Batumi
FIND_CHAT_S = 1800
PROVE_GATES = ("G-CRED", "G-TIME", "G-KEY", "G-POS", "G-BRACKET", "G-PUSH", "G-TG", "G-SEE", "G-ALARM", "G-HC")
SEE_WAIT_S = 900             # the Boss's answer to what the guard sees, at prove
LONG_POLL_S = 25             # Telegram's long poll in find-chat and prove; their sockets wait 40 s
YES, NO = ("да", "yes", "совпадает"), ("нет", "no", "не совпадает")
READ_PERMS = ("enableReading", "enableFixReadOnly")
CORE_PERMS = ("enableReading", "ipRestrict", "enableWithdrawals", "enableFutures", "enableSpotAndMarginTrading")
LABEL = {"binance-key": "ключ Binance", "binance-secret": "секрет Binance", "pushover-user": "User Key Pushover",
         "pushover-token": "токен Pushover", "tg-token": "токен бота", "hc-url": "адрес пинга"}
LEVEL_NAME = {1: "предупреждение", 2: "тревога", 3: "последний звонок"}
SIDE_RU = {"LONG": "лонг", "SHORT": "шорт"}
KEYBOARD = {"keyboard": [[{"text": "Статус"}, {"text": "Тест"}], [{"text": "Пороги"}, {"text": "Помощь"}]],
            "resize_keyboard": True, "is_persistent": True}
IPV4 = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
CREDENTIALS = (   # name, form, required, the Boss's prompt
    ("binance-key", r"[A-Za-z0-9]{32,128}", True,
     "Binance — API Key ключа «только чтение» (ввод скрыт): "),
    ("binance-secret", r"[A-Za-z0-9]{32,128}", True,
     "Binance — Secret Key того же ключа (ввод скрыт): "),
    ("pushover-user", r"[A-Za-z0-9]{30}", True,
     "Pushover — ваш User Key, вверху страницы pushover.net (ввод скрыт): "),
    ("pushover-token", r"[A-Za-z0-9]{30}", True,
     "Pushover — API Token приложения «Сторож» (ввод скрыт): "),
    ("tg-token", r"[0-9]{5,12}:[A-Za-z0-9_-]{30,64}", True,
     "Telegram — токен бота «Сторож» от BotFather (ввод скрыт): "),
    ("hc-url", r"https://hc-ping\.com/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", False,
     "healthchecks.io — адрес пинга (https://hc-ping.com/…), или просто Enter — без него (ввод скрыт): "),
)
FORM = {n: re.compile(f) for n, f, _r, _p in CREDENTIALS}
FORM["tg-chat"] = re.compile(r"-?[0-9]{1,20}")


def out(*parts):
    sys.stdout.write(" ".join(str(p) for p in parts) + "\n")
    sys.stdout.flush()


def utc(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ---- files -------------------------------------------------------------------------------------------------------

def file_state(path):
    """A path's kind, mode, owner and size - never its content: all that is printed of a credential."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent"
    kind = "dir" if os.path.isdir(path) and not os.path.islink(path) else (
        "file" if os.path.isfile(path) and not os.path.islink(path) else "other")
    return "%s mode %04o uid %d bytes %d" % (kind, st.st_mode & 0o7777, st.st_uid, st.st_size)


def private_file_ok(path, mode=0o600, uid=0):
    """A regular file, not a link, of `uid`, of `mode`, not empty."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return (os.path.isfile(path) and not os.path.islink(path) and st.st_uid == uid
            and st.st_mode & 0o7777 == mode and st.st_size > 0)


def private_dir(path, uid=0):
    """`path` made 0700 where absent; asserted a directory of `uid`, 0700, not a link."""
    if not os.path.isdir(path):
        os.mkdir(path, 0o700)
    st = os.lstat(path)
    assert not os.path.islink(path) and st.st_uid == uid and st.st_mode & 0o7777 == 0o700, \
        "%s: %s" % (path, file_state(path))


def write_private(path, data, uid=0):
    """`data` to `path` by exclusive create, 0600 from its first byte. Returns the bytes written."""
    private_dir(os.path.dirname(path), uid)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    assert private_file_ok(path, uid=uid), "%s: %s" % (path, file_state(path))
    return len(data)


def replace_private(path, data, uid=0):
    """`data` to `path` through a 0600 file beside it and a rename: no reader sees half a file."""
    private_dir(os.path.dirname(path), uid)
    tmp = path + ".tmp"
    if os.path.exists(tmp):
        os.unlink(tmp)
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.replace(tmp, path)


def read_credentials(etc=ETC, uid=0):
    """{name: value} of every credential present; refused (exit 2) where a required one is absent, malformed, or
    not a 0600 file of `uid`. The dead-man's address may be absent."""
    creds, problems = {}, []
    for name in [c[0] for c in CREDENTIALS] + ["tg-chat"]:
        path = os.path.join(etc, name)
        required = name == "tg-chat" or dict((c[0], c[2]) for c in CREDENTIALS)[name]
        if not os.path.lexists(path):
            if required:
                problems.append("%s absent" % name)
            continue
        if not private_file_ok(path, uid=uid):
            problems.append("%s: %s" % (name, file_state(path)))
            continue
        with open(path, encoding="utf-8") as fh:
            v = fh.read().strip()
        if not FORM[name].fullmatch(v):
            problems.append("%s malformed, %d bytes" % (name, len(v)))
            continue
        creds[name] = v
    return creds, problems


class Scrub:
    """Every loaded secret and every IPv4 address out of a text before it is printed, journaled or sent."""

    def __init__(self, creds=None):
        self.values = sorted((v for k, v in (creds or {}).items() if k != "tg-chat" and v), key=len, reverse=True)

    def __call__(self, text):
        t = str(text)
        for v in self.values:
            t = t.replace(v, "***")
        return IPV4.sub("x.x.x.x", t)


# ---- the network: IPv4 alone, one kept connection a host ----------------------------------------------------------

class V4HTTPS(http.client.HTTPSConnection):
    """An HTTPS connection whose every (re)connect resolves the host to IPv4 alone."""

    def connect(self):
        infos = socket.getaddrinfo(self.host, self.port, socket.AF_INET, socket.SOCK_STREAM)
        assert infos, "no IPv4 address for %s" % self.host
        sock = socket.create_connection(infos[0][4], self.timeout)
        self.sock = self._context.wrap_socket(sock, server_hostname=self.host)


class Net:
    """call(host, method, path, body, headers) -> (status, bytes). A kept connection is reopened once where the
    server closed it while idle; a host that failed at the network is not tried again for COOLDOWN_S, so that one
    pass of the loop waits at most one timeout a host."""

    def __init__(self, timeout=TIMEOUT_S, clock=time.monotonic):
        self.timeout, self.clock, self.conns, self.count, self.down_until = timeout, clock, {}, {}, {}

    def call(self, host, method, path, body=None, headers=()):
        if self.clock() < self.down_until.get(host, 0.0):
            raise ConnectionError("%s not tried: it failed less than %d s ago" % (host, COOLDOWN_S))
        try:
            return self._call(host, method, path, body, headers)
        except (OSError, http.client.HTTPException):
            self.down_until[host] = self.clock() + COOLDOWN_S
            raise

    def _call(self, host, method, path, body, headers):
        hdrs = dict(headers)
        hdrs.setdefault("User-Agent", UA)
        self.count[host] = self.count.get(host, 0) + 1
        for attempt in (1, 2):
            c = self.conns.get(host)
            reused = c is not None and c.sock is not None
            if c is None:
                c = self.conns[host] = V4HTTPS(host, 443, timeout=self.timeout,
                                               context=ssl.create_default_context())
            try:
                c.request(method, path, body=body, headers=hdrs)
                r = c.getresponse()
                data = r.read()
                if r.will_close:
                    c.close()
                return r.status, data
            except (http.client.RemoteDisconnected, BrokenPipeError, ConnectionResetError):
                c.close()
                self.conns.pop(host, None)
                if attempt == 2 or not reused:
                    raise
            except Exception:
                c.close()
                self.conns.pop(host, None)
                raise


def json_of(data):
    try:
        return json.loads(data.decode("utf-8"))
    except (ValueError, UnicodeDecodeError, AttributeError):
        return None


class Refused(Exception):
    """A request the far end answered and refused: its status and its own words."""

    def __init__(self, host, status, words):
        Exception.__init__(self, "%s answered %s: %s" % (host, status, words))
        self.status, self.words = status, words


class Binance:
    def __init__(self, net, key, secret, now=time.time):
        self.net, self.key, self.secret, self.now, self.offset_ms = net, key, secret, now, 0
        self.position_path = None

    def _get(self, host, path, signed=False):
        headers = [("Accept", "application/json")] + ([("X-MBX-APIKEY", self.key)] if signed else [])
        status, data = self.net.call(host, "GET", path, None, headers)
        doc = json_of(data)
        if status != 200 or doc is None:
            words = ("%s %s" % (doc.get("code"), doc.get("msg"))) if isinstance(doc, dict) else "%d bytes" % len(data)
            raise Refused(host, status, words)
        return doc

    def signed(self, host, path, params=()):
        ts = int(self.now() * 1000) + self.offset_ms
        q = urllib.parse.urlencode(list(params) + [("recvWindow", RECV_WINDOW), ("timestamp", ts)])
        sig = hmac.new(self.secret.encode(), q.encode(), hashlib.sha256).hexdigest()
        return self._get(host, "%s?%s&signature=%s" % (path, q, sig), signed=True)

    def sync_time(self):
        t0 = self.now()
        doc = self._get(FAPI, "/fapi/v1/time")
        t1 = self.now()
        assert isinstance(doc, dict) and isinstance(doc.get("serverTime"), int), "time: %r" % (doc,)
        self.offset_ms = doc["serverTime"] - int((t0 + t1) * 500)
        return self.offset_ms

    def positions(self):
        paths = (self.position_path,) if self.position_path else POSITION_PATHS
        for k, path in enumerate(paths):
            try:
                doc = self.signed(FAPI, path)
            except Refused as e:
                if e.status == 404 and k + 1 < len(paths):
                    continue
                raise
            self.position_path = path
            return doc
        raise AssertionError("unreachable")

    def brackets(self, symbol):
        return self.signed(FAPI, "/fapi/v1/leverageBracket", [("symbol", symbol)])

    def restrictions(self):
        return self.signed(SAPI, "/sapi/v1/account/apiRestrictions")


class Pushover:
    def __init__(self, net, token, user):
        self.net, self.token, self.user = net, token, user

    def _post(self, path, fields):
        body = urllib.parse.urlencode(fields).encode()
        status, data = self.net.call(PUSHOVER, "POST", path, body,
                                     [("Content-Type", "application/x-www-form-urlencoded")])
        doc = json_of(data)
        if status != 200 or not isinstance(doc, dict) or doc.get("status") != 1:
            words = "; ".join(doc.get("errors") or []) if isinstance(doc, dict) else "%d bytes" % len(data)
            raise Refused(PUSHOVER, status, words)
        return doc

    def validate(self):
        return self._post("/1/users/validate.json", {"token": self.token, "user": self.user})

    def send(self, title, message, priority, expire=ALARM_EXPIRE_S):
        fields = {"token": self.token, "user": self.user, "title": title[:250], "message": message[:1024],
                  "priority": priority}
        if priority == 2:
            fields.update(retry=ALARM_RETRY_S, expire=expire, tags="liq-guard")
        return self._post("/1/messages.json", fields).get("receipt")

    def receipt(self, receipt):
        assert re.fullmatch(r"[A-Za-z0-9]{20,40}", receipt or ""), "receipt: malformed"
        status, data = self.net.call(PUSHOVER, "GET", "/1/receipts/%s.json?token=%s" % (receipt, self.token))
        doc = json_of(data)
        if status != 200 or not isinstance(doc, dict) or doc.get("status") != 1:
            raise Refused(PUSHOVER, status, "receipt")
        return doc

    def cancel(self, receipt):
        assert re.fullmatch(r"[A-Za-z0-9]{20,40}", receipt or ""), "receipt: malformed"
        return self._post("/1/receipts/%s/cancel.json" % receipt, {"token": self.token})


class Telegram:
    def __init__(self, net, token):
        self.net, self.token = net, token

    def call(self, method, **params):
        status, data = self.net.call(TG, "POST", "/bot%s/%s" % (self.token, method),
                                     json.dumps(params).encode(), [("Content-Type", "application/json")])
        doc = json_of(data)
        if not isinstance(doc, dict) or doc.get("ok") is not True:
            raise Refused(TG, status, doc.get("description") if isinstance(doc, dict) else "%d bytes" % len(data))
        return doc["result"]

    def send(self, chat, text, quiet=False):
        return self.call("sendMessage", chat_id=int(chat), text=text[:4000], disable_notification=bool(quiet),
                         reply_markup=KEYBOARD)


def hc_ping(net, url):
    u = urllib.parse.urlsplit(url)
    assert u.scheme == "https" and u.hostname == HC, "the dead-man's address is not hc-ping.com"
    status, data = net.call(HC, "GET", u.path)
    if status != 200 or data.strip() != b"OK":
        raise Refused(HC, status, "%d bytes" % len(data))
    return True


def sd_notify(msg):
    """systemd's notify socket, where the unit gives one: READY=1 once, WATCHDOG=1 every cycle."""
    addr = os.environ.get("NOTIFY_SOCKET")
    if not addr:
        return False
    if addr.startswith("@"):
        addr = "\0" + addr[1:]
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
        s.connect(addr)
        s.sendall(msg.encode())
    return True


# ---- the readings: pure functions ---------------------------------------------------------------------------------

def num(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if v == v and v not in (float("inf"), float("-inf")) else None


def parse_positions(doc):
    """The open positions of positionRisk's reply, v3 or v2: symbol, side, quantity, mark, liquidation price,
    notional, isolated or not. Pure."""
    assert isinstance(doc, list), "positionRisk: not a list"
    found = []
    for e in doc:
        assert isinstance(e, dict) and isinstance(e.get("symbol"), str), "positionRisk: an entry %r" % (type(e),)
        amt = num(e.get("positionAmt"))
        if not amt:
            continue
        ps = e.get("positionSide")
        side = ps if ps in ("LONG", "SHORT") else ("LONG" if amt > 0 else "SHORT")
        mark = num(e.get("markPrice"))
        notional = num(e.get("notional"))
        found.append({"symbol": e["symbol"], "side": side, "key": "%s:%s" % (e["symbol"], side), "qty": abs(amt),
                      "mark": mark, "liq": num(e.get("liquidationPrice")),
                      "notional": abs(notional) if notional is not None else abs(amt) * (mark or 0.0),
                      "isolated": (num(e.get("isolatedWallet")) or 0.0) > 0 or e.get("marginType") == "isolated"})
    return found


def distance_pct(p):
    """Percent of the mark price between it and the liquidation price, on the side that loses; None where there is
    no liquidation price. At or under 0 the mark is at or past it. Pure."""
    mark, liq = p.get("mark"), p.get("liq")
    if not mark or mark <= 0 or liq is None or liq <= 0:
        return None
    return 100.0 * ((mark - liq) / mark if p["side"] == "LONG" else (liq - mark) / mark)


def crossed(d, th):
    """The highest level whose threshold `d` is at or under: 3, 2, 1, or 0. Pure."""
    for lvl, t in ((3, th[2]), (2, th[1]), (1, th[0])):
        if d <= t:
            return lvl
    return 0


def step(fired, d, th, rearm=REARM_PP):
    """(the level to announce now, or 0; the levels announced in this descent after this read). A level re-arms once
    `d` is above its threshold by `rearm` points; a read that crosses several levels at once announces the highest
    alone and counts the lower ones announced; no liquidation price re-arms every level. Pure."""
    if d is None:
        return 0, frozenset()
    left = {lvl for lvl in fired if not d > th[lvl - 1] + rearm}
    top = crossed(d, th)
    new = top if top and top not in left else 0
    return new, frozenset(left | set(range(1, top + 1)))


def bracket_for(doc, notional):
    """(maintMarginRatio, cum) of the leverage bracket holding `notional`, or None. `doc` is leverageBracket's
    reply for one symbol - an object, or a list of one. Pure."""
    if isinstance(doc, list):
        doc = doc[0] if len(doc) == 1 else {}
    for b in sorted((doc or {}).get("brackets") or [], key=lambda b: num(b.get("notionalFloor")) or 0.0):
        lo, hi, r = num(b.get("notionalFloor")), num(b.get("notionalCap")), num(b.get("maintMarginRatio"))
        if lo is not None and hi is not None and r is not None and lo <= notional < hi:
            return r, num(b.get("cum")) or 0.0
    return None


def margin_hint(p, mmr, target=TARGET_PCT):
    """USDT of margin that moves the liquidation price to `target` percent from the mark price; 0 where it is there
    already. For an isolated position the liquidation price is linear in its margin M: dLP/dM = 1/(Q(1+mmr)) for a
    short and -1/(Q(1-mmr)) for a long, so this is exact; for a cross position, an estimate. Pure."""
    t = target / 100.0
    if p["side"] == "SHORT":
        need = (p["mark"] * (1 + t) - p["liq"]) * p["qty"] * (1 + mmr)
    else:
        need = (p["liq"] - p["mark"] * (1 - t)) * p["qty"] * (1 - mmr)
    return max(0.0, need)


def key_reading(doc):
    """(read-only and bound to an address, the problems): the key's permissions as Binance reads them. Pure."""
    if not isinstance(doc, dict):
        return False, ["no permissions object"]
    problems = ["%s absent" % k for k in CORE_PERMS if not isinstance(doc.get(k), bool)]
    if doc.get("enableReading") is not True:
        problems.append("enableReading not true")
    if doc.get("ipRestrict") is not True:
        problems.append("ipRestrict not true")
    problems += ["%s true" % k for k, v in sorted(doc.items())
                 if (k.startswith("enable") or k.startswith("permits")) and k not in READ_PERMS and v is True]
    return not problems, problems


def perms_line(doc):
    """Every permission's name and value - booleans alone. Pure."""
    return ", ".join("%s %s" % (k, v) for k, v in sorted(doc.items()) if isinstance(v, bool))


def parse_command(text):
    """(command, arguments) of a chat message: status, test, thresholds, help, or None. Pure."""
    words = (text or "").strip().lower().replace("ё", "е").split()
    if not words:
        return None, []
    w = words[0].lstrip("/").split("@")[0]
    names = {"статус": "status", "status": "status", "тест": "test", "test": "test", "пороги": "thresholds",
             "thresholds": "thresholds", "помощь": "help", "help": "help", "start": "help"}
    return names.get(w), words[1:]


def thresholds_of(args):
    """Three thresholds from a message's words, `5 3 1,5`, or None: each a number, 0 < third < second < first <= 30.
    Pure."""
    if len(args) != 3:
        return None
    try:
        w, a, c = (float(x.replace(",", ".")) for x in args)
    except ValueError:
        return None
    if not (0 < c < a < w <= 30):
        return None
    return (round(w, 2), round(a, 2), round(c, 2))


def ru(x, d):
    s = "{:,.{}f}".format(x, d)
    return s.replace(",", " ").replace(".", ",")


def price(x):
    """A price in Russian notation, to about six significant digits. Pure."""
    if x is None:
        return "—"
    a = abs(x)
    d = 1 if a >= 1000 else 2 if a >= 100 else 3 if a >= 1 else min(8, max(4, 3 - int(f"{a:e}".split("e")[1])))
    return ru(x, d)


def pct(x):
    return "—" if x is None else ru(x, 1) + "%"


def usdt(x):
    return ru(x, 0) + " USDT"


def position_line(p, d, mmr, target=TARGET_PCT):
    """One position for the Boss: its distance, prices and the margin hint. Pure."""
    line = "%s %s: до ликвидации %s (цена %s → ликвидация %s)" % (
        p["symbol"], SIDE_RU[p["side"]], pct(d), price(p["mark"]), price(p["liq"]))
    if d is None:
        return line
    need = margin_hint(p, mmr or 0.0, target)
    if need > 0:
        line += "; долить %s%s, чтобы ликвидация ушла на %s%s" % (
            "≈ " if mmr is None or not p["isolated"] else "", usdt(need), ru(target, 0) + "%",
            "" if p["isolated"] else " (кросс-маржа — оценка)")
    return line


def alarm_text(items, mmrs, target=TARGET_PCT):
    """(title, message) of one alarm: items are (level, position, distance), the highest level first. Pure."""
    items = sorted(items, key=lambda i: (-i[0], i[2] if i[2] is not None else -1e9))
    lvl, p, d = items[0]
    title = "Сторож: %s — %s %s, до ликвидации %s" % (
        LEVEL_NAME[lvl].upper() if lvl == 3 else LEVEL_NAME[lvl], p["symbol"], SIDE_RU[p["side"]], pct(d))
    body = "\n".join(position_line(q, e, mmrs.get(q["symbol"]), target) for _l, q, e in items)
    return title, body


def private_starts(updates):
    """The private chats that sent /start among Telegram updates, sorted. Pure."""
    chats = set()
    for u in updates:
        m = u.get("message") if isinstance(u, dict) else None
        if not isinstance(m, dict):
            continue
        chat = m.get("chat") or {}
        if (m.get("text") or "").startswith("/start") and chat.get("type") == "private" \
                and isinstance(chat.get("id"), int):
            chats.add(chat["id"])
    return sorted(chats)


HELP = ("Сторож следит за твоими фьючерсными позициями Binance каждые 5 секунд — по ключу «только чтение».\n"
        "• Ближе первого порога до ликвидации — сообщение здесь; ближе второго — тревога Pushover (звучит сквозь "
        "беззвучный режим и «Сон», повторяется каждые 30 с, пока не нажмёшь «Подтвердить»); ближе третьего — "
        "второй звонок. В каждой тревоге — сколько долить, чтобы ликвидация ушла на 8% от цены.\n"
        "• Потеряет Binance дольше 2 минут — тоже разбудит.\n"
        "Команды: «Статус», «Тест» (проверить звонок перед сном), «Пороги», «Пороги 5 3 1,5» — задать свои, "
        "в процентах от цены. Сторож никогда не торгует и не доливает маржу сам.")


# ---- the guard: one cycle at a time, every effect through its stand-ins in the self-test ---------------------------

class Guard:
    def __init__(self, creds, net=None, now=time.time, var=VAR, uid=0, notify=sd_notify):
        self.creds, self.now, self.var, self.uid, self.notify = creds, now, var, uid, notify
        self.net = net or Net()
        self.scrub = Scrub(creds)
        self.bn = Binance(self.net, creds["binance-key"], creds["binance-secret"], now)
        self.po = Pushover(self.net, creds["pushover-token"], creds["pushover-user"])
        self.tg = Telegram(self.net, creds["tg-token"])
        self.chat, self.hc = int(creds["tg-chat"]), creds.get("hc-url")
        t = now()
        st = self.load_state()
        th = st.get("thresholds")
        self.th = tuple(th) if isinstance(th, list) and thresholds_of([str(x) for x in th]) else DEFAULT_THRESHOLDS
        self.tg_offset = st.get("tg_offset") if isinstance(st.get("tg_offset"), int) else 0
        self.hb_day = st.get("hb_day")
        self.fired, self.positions, self.mmr, self.outbox, self.pushes = {}, [], {}, [], []
        self.started, self.last_ok, self.polls_ok, self.polls_err, self.last_error = t, t, 0, 0, None
        self.blind, self.blind_next, self.key_ok, self.key_checked = False, 0.0, None, None
        self.next_time = self.next_key = self.next_hc = 0.0
        self.next_tick, self.next_state = t + TICK_S, 0.0
        self.test = None
        self.min_seen = None
        self.bn_error, self.bn_backoff, self.err_last = None, 0.0, (None, 0.0)
        self.disk_faults = 0

    # -- record ------------------------------------------------------------------------------------------------------
    def load_state(self):
        try:
            with open(os.path.join(self.var, "state.json"), encoding="utf-8") as fh:
                doc = json.load(fh)
            return doc if isinstance(doc, dict) else {}
        except (OSError, ValueError):
            return {}

    def save_state(self):
        t = self.now()
        doc = {"at": utc(t), "started": utc(self.started), "thresholds": list(self.th), "tg_offset": self.tg_offset,
               "hb_day": self.hb_day, "last_ok": utc(self.last_ok), "polls_ok": self.polls_ok,
               "polls_err": self.polls_err, "positions": len(self.positions),
               "with_liquidation": sum(1 for p in self.positions if distance_pct(p) is not None),
               "blind": self.blind, "last_error": self.last_error, "key_ok": self.key_ok,
               "key_checked": utc(self.key_checked) if self.key_checked else None, "dead_man": bool(self.hc),
               "outbox": len(self.outbox), "disk_faults": self.disk_faults, "pid": os.getpid()}
        self.next_state = t + STATE_S
        try:
            replace_private(os.path.join(self.var, "state.json"), (json.dumps(doc, sort_keys=True) + "\n").encode(),
                            self.uid)
        except OSError:
            self.disk_faults += 1

    def journal(self, ev, **fields):
        t = self.now()
        rec = {"t": utc(t), "ev": ev}
        rec.update({k: (self.scrub(v) if isinstance(v, str) else v) for k, v in fields.items()})
        d = os.path.join(self.var, "journal")
        try:
            private_dir(self.var, self.uid)
            private_dir(d, self.uid)
            fd = os.open(os.path.join(d, utc(t)[:10] + ".jsonl"), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
            try:
                os.write(fd, (json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n").encode())
            finally:
                os.close(fd)
        except OSError:
            self.disk_faults += 1

    def err(self, where, e):
        t = self.now()
        self.last_error = self.scrub("%s: %s" % (where, e))[:300]
        if self.err_last[0] != self.last_error or t - self.err_last[1] >= ERR_EVERY_S:
            self.err_last = (self.last_error, t)
            self.journal("error", where=where, error=self.last_error)

    # -- sending -----------------------------------------------------------------------------------------------------
    def say(self, text, quiet=False):
        self.outbox.append({"to": "tg", "text": text, "quiet": quiet, "tries": 0})

    def push(self, title, message, priority, expire=ALARM_EXPIRE_S):
        t = self.now()
        self.pushes = [x for x in self.pushes if x > t - 3600]
        if len(self.pushes) >= PUSH_PER_HOUR:
            self.journal("push_capped", title=title)
            self.say("Pushover: предел %d тревог в час достигнут — эта только здесь:\n%s\n%s" % (
                PUSH_PER_HOUR, title, message))
            return None
        self.pushes.append(t)
        m = {"to": "push", "title": title, "text": message, "priority": priority, "expire": expire, "tries": 0}
        self.outbox.append(m)
        return m

    def flush(self):
        """Every waiting message tried once, in order; a channel that fails is not tried again in this pass."""
        pending, self.outbox, failed, tg_sent = self.outbox, [], set(), 0
        for m in pending:
            if m["to"] in failed or (m["to"] == "tg" and tg_sent >= TG_PER_PASS):
                self.outbox.append(m)
                continue
            try:
                if m["to"] == "tg":
                    tg_sent += 1
                    self.tg.send(self.chat, m["text"], m["quiet"])
                else:
                    r = self.po.send(m["title"], m["text"], m["priority"], m["expire"])
                    self.journal("pushed", priority=m["priority"], title=m["title"], receipt=bool(r))
                    if m.get("test") and r:
                        self.test = {"receipt": r, "sent": self.now(), "next": self.now() + RECEIPT_EVERY_S,
                                     "deadline": self.now() + TEST_WAIT_S}
            except Exception as e:
                failed.add(m["to"])
                m["tries"] += 1
                self.err("send %s" % m["to"], e)
                if m["tries"] < OUTBOX_TRIES:
                    self.outbox.append(m)
                else:
                    self.journal("dropped", to=m["to"], tries=m["tries"])
                    if m["to"] == "push":
                        self.say("Pushover не принял тревогу за %d попыток: %s\n%s" % (
                            OUTBOX_TRIES, m["title"], m["text"]))
        tg = [m for m in self.outbox if m["to"] == "tg"]
        if len(tg) > OUTBOX_MAX:
            drop = {id(m) for m in tg[:len(tg) - OUTBOX_MAX]}
            self.outbox = [m for m in self.outbox if id(m) not in drop]
            self.journal("dropped", to="tg", count=len(drop))

    # -- the cycle ---------------------------------------------------------------------------------------------------
    def check_key(self):
        t = self.now()
        try:
            doc = self.bn.restrictions()
        except Exception as e:
            self.err("key", e)
            self.next_key = t + PERM_RETRY_S
            return
        ok, problems = key_reading(doc)
        self.key_checked, self.key_ok, self.next_key = t, ok, t + PERM_S
        self.journal("key", ok=ok, perms=perms_line(doc), problems=problems)
        if not ok:
            raise KeyRefused(problems)

    def poll(self):
        t = self.now()
        if t < self.bn_backoff:
            return False
        try:
            pos = parse_positions(self.bn.positions())
        except Exception as e:
            self.polls_err += 1
            self.err("positions", e)
            self.bn_error = self.last_error
            if isinstance(e, Refused):
                self.bn_backoff = t + BACKOFF_S.get(e.status, 0)
                if "-1021" in str(e.words):
                    self.next_time = 0.0
            return False
        alarms, fired = [], {}
        for p in pos:
            d = distance_pct(p)
            lvl, fired[p["key"]] = step(self.fired.get(p["key"], frozenset()), d, self.th)
            if lvl:
                alarms.append((lvl, p, d))
        self.positions = pos
        if alarms:
            self.refresh_brackets([p["symbol"] for _l, p, _d in alarms])
            self.announce(alarms)
        self.fired = fired          # committed once the alarms are queued: a fault before this rings them again
        for lvl, p, d in alarms:
            self.journal("level", key=p["key"], level=lvl, distance=d, mark=p["mark"], liq=p["liq"])
        self.polls_ok += 1
        if self.blind:
            self.blind = False
            self.say("Сторож снова видит Binance: слеп был %d мин." % round((t - self.last_ok) / 60))
            self.journal("seen_again", blind_s=round(t - self.last_ok))
        self.last_ok = t
        ds = [d for d in (distance_pct(p) for p in pos) if d is not None]
        self.min_seen = min(ds) if ds else None
        return True

    def announce(self, alarms):
        top = max(lvl for lvl, _p, _d in alarms)
        title, body = alarm_text(alarms, self.mmr)
        if top >= 2:
            self.push(title, body + "\nПодтверди в Pushover, чтобы звонок затих.", 2)
        self.say(("🔴 " if top >= 2 else "⚠️ ") + title + "\n" + body, quiet=False)

    def check_blind(self):
        t = self.now()
        if t - self.last_ok >= BLIND_S and (not self.blind or t >= self.blind_next):
            first = not self.blind
            self.blind, self.blind_next = True, t + BLIND_REPEAT_S
            why = self.bn_error or "нет ответа"
            text = "Сторож не видит Binance %d мин: %s. Твои позиции сейчас без присмотра." % (
                round((t - self.last_ok) / 60), why)
            self.push("Сторож ослеп" if first else "Сторож всё ещё слеп", text, 1)
            self.say("🔴 " + text)
            self.journal("blind", since=utc(self.last_ok), error=why)

    def refresh_brackets(self, first=()):
        t = self.now()
        done = 0
        order = [p for s in first for p in self.positions if p["symbol"] == s]
        for p in order + [p for p in self.positions if p not in order]:
            s = p["symbol"]
            got = self.mmr.get(s)
            if got is not None and self.mmr.get(s + "@t", 0) > t - BRACKETS_S:
                continue
            if done >= 2:
                break
            done += 1
            try:
                b = bracket_for(self.bn.brackets(s), p["notional"])
            except Exception as e:
                self.err("brackets %s" % s, e)
                b = None
            self.mmr[s] = b[0] if b else None
            self.mmr[s + "@t"] = t

    def telegram(self):
        try:
            ups = self.tg.call("getUpdates", offset=self.tg_offset, timeout=0, allowed_updates=["message"])
        except Exception as e:
            self.err("telegram", e)
            return
        for u in ups:
            if isinstance(u.get("update_id"), int):
                self.tg_offset = max(self.tg_offset, u["update_id"] + 1)
            m = u.get("message") or {}
            if (m.get("chat") or {}).get("id") != self.chat:
                self.journal("foreign_chat")
                continue
            cmd, args = parse_command(m.get("text"))
            self.journal("command", cmd=cmd or "none")
            self.command(cmd, args)

    def command(self, cmd, args):
        if cmd == "status":
            self.say(self.status_text())
        elif cmd == "test":
            if self.test:
                self.say("Тест уже идёт — подтверди тревогу в Pushover.")
                return
            m = self.push("Сторож: проверка тревоги",
                          "Это тест. Нажми «Подтвердить» — и сторож напишет, что звонок дошёл.", 2, TEST_EXPIRE_S)
            if m is not None:
                m["test"] = True
                self.say("Тестовая тревога отправлена в Pushover. Подтверди её на телефоне.")
        elif cmd == "thresholds":
            if not args:
                self.say("Пороги: %s / %s / %s до ликвидации (сообщение / тревога / последний звонок). "
                         "Задать свои: «Пороги 5 3 1,5»." % tuple(pct(x) for x in self.th))
                return
            th = thresholds_of(args)
            if th is None:
                self.say("Не понял. Нужно три числа по убыванию, не больше 30: «Пороги 5 3 1,5».")
                return
            self.th = th
            self.fired = {p["key"]: frozenset(range(1, crossed(distance_pct(p), th) + 1))
                          for p in self.positions if distance_pct(p) is not None}
            self.journal("thresholds", th=list(th))
            self.save_state()
            self.say("Пороги заданы: %s / %s / %s." % tuple(pct(x) for x in th))
        else:
            self.say(HELP)

    def status_text(self):
        t = self.now()
        lines = ["Сторож: %s; последнее чтение Binance %d с назад; ключ %s; пороги %s / %s / %s; "
                 "страховка от падения сервера: %s." % (
                     "слеп" if self.blind else "на месте", round(t - self.last_ok),
                     "только чтение ✓" if self.key_ok else "не проверен" if self.key_ok is None else "НЕ только чтение",
                     pct(self.th[0]), pct(self.th[1]), pct(self.th[2]), "есть" if self.hc else "нет")]
        if not self.positions:
            lines.append("Открытых позиций нет.")
        for p in sorted(self.positions, key=lambda q: (distance_pct(q) is None, distance_pct(q) or 0)):
            lines.append("• " + position_line(p, distance_pct(p), self.mmr.get(p["symbol"])))
        return "\n".join(lines)

    def check_test(self):
        t = self.now()
        if not self.test or t < self.test["next"]:
            return
        self.test["next"] = t + RECEIPT_EVERY_S
        try:
            doc = self.po.receipt(self.test["receipt"])
        except Exception as e:
            self.err("receipt", e)
            doc = {}
        if doc.get("acknowledged") == 1:
            at = doc.get("acknowledged_at")
            self.say("Тест пройден: тревогу подтвердили%s. Звонок до тебя доходит." % (
                " в %s UTC" % utc(at)[11:19] if isinstance(at, int) else ""))
            self.journal("test", acknowledged=True, after_s=round(t - self.test["sent"]))
            self.test = None
        elif t >= self.test["deadline"]:
            try:
                self.po.cancel(self.test["receipt"])
            except Exception as e:
                self.err("cancel", e)
            self.say("Тест не подтверждён за %d мин. Проверь в Pushover: Настройки → Critical Alerts включены, "
                     "громкость не на нуле." % (TEST_WAIT_S // 60))
            self.journal("test", acknowledged=False)
            self.test = None

    def heartbeat(self):
        t = self.now()
        day = utc(t)[:10]
        h, m = HEARTBEAT_UTC
        now = dt.datetime.fromtimestamp(t, dt.timezone.utc)
        if self.hb_day != day and (now.hour, now.minute) >= (h, m):
            self.hb_day = day
            near = min(((distance_pct(p), p) for p in self.positions if distance_pct(p) is not None),
                       default=None, key=lambda x: x[0])
            self.say("Сторож на месте: позиций %d%s; ключ %s; пороги %s / %s / %s." % (
                len(self.positions),
                ", ближе всех к ликвидации %s — %s" % (near[1]["symbol"], pct(near[0])) if near else "",
                "только чтение ✓" if self.key_ok else "не проверен", pct(self.th[0]), pct(self.th[1]),
                pct(self.th[2])), quiet=True)
            self.journal("heartbeat")

    def sync(self):
        t = self.now()
        if t >= self.next_time:
            try:
                self.bn.sync_time()
                self.next_time = t + TIME_SYNC_S
            except Exception as e:
                self.err("time", e)
                self.next_time = t + PERM_RETRY_S

    def ping(self):
        t = self.now()
        if self.hc and t >= self.next_hc and t - self.last_ok < 2 * HC_S:
            self.next_hc = t + HC_S
            hc_ping(self.net, self.hc)

    def tick(self):
        t = self.now()
        if t >= self.next_tick:
            self.next_tick = t + TICK_S
            self.journal("tick", polls_ok=self.polls_ok, polls_err=self.polls_err, positions=len(self.positions),
                         min_distance=self.min_seen, blind=self.blind, outbox=len(self.outbox))
            d = os.path.join(self.var, "journal")
            cut = utc(t - KEEP_DAYS * 86400)[:10]
            for f in sorted(os.listdir(d)):
                if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}\.jsonl", f) and f[:10] < cut:
                    os.unlink(os.path.join(d, f))
                    self.journal("pruned", file=f)
        if t >= self.next_state:
            self.save_state()

    def cycle(self):
        """One pass: the clock, the key's permissions, the positions, blindness, brackets, the chat, the test, the
        heartbeat, the outbox, the dead-man, the record, the watchdog. A step's fault is journaled and stops no
        other step; a key that can do more than read stops the guard."""
        if self.now() >= self.next_key:
            self.check_key()
        for name, f in (("sync", self.sync), ("poll", self.poll), ("blind", self.check_blind),
                        ("brackets", self.refresh_brackets), ("telegram", self.telegram), ("test", self.check_test),
                        ("heartbeat", self.heartbeat), ("flush", self.flush), ("dead-man", self.ping),
                        ("tick", self.tick)):
            try:
                f()
            except KeyRefused:
                raise
            except Exception as e:
                self.err(name, e)
        self.notify("WATCHDOG=1")


class KeyRefused(Exception):
    pass


# ---- the modes ----------------------------------------------------------------------------------------------------

class Tty:
    """The Boss's terminal, as TZ-51 corrected it: two streams, never "r+" (map section 7 item 189); a hidden answer
    read by getpass, which discards what was typed before it; a visible one discards it too."""

    def __init__(self, path="/dev/tty"):
        self.rh = open(path, "r", encoding="utf-8", errors="replace")
        self.fh = open(path, "w", encoding="utf-8", errors="replace")

    def say(self, text):
        self.fh.write(text + "\n")
        self.fh.flush()

    def ask(self, prompt, hidden=False):
        if hidden:
            return getpass.getpass(prompt, stream=self.fh)
        import termios
        termios.tcflush(self.rh.fileno(), termios.TCIFLUSH)
        self.fh.write(prompt)
        self.fh.flush()
        line = self.rh.readline()
        if line == "":
            raise EOFError("the terminal closed")
        return line.rstrip("\r\n")


def mode_secrets(tty=None, etc=ETC, uid=0):
    """The Boss's credentials onto the host, typed by him: each hidden, refused and asked again where it is not of
    its form, three times at most, written once by exclusive create, 0600; one already in place and of its form is
    kept. Printed: written, kept or skipped, and the bytes - never a value."""
    tty = tty or Tty()
    tty.say("Сторож · ТЗ-54: учётные данные. Ввод скрыт; ничего из введённого не попадает ни в журнал, ни в отчёт.")
    rc = 0
    for name, _form, required, prompt in CREDENTIALS:
        path = os.path.join(etc, name)
        if os.path.lexists(path):
            with open(path, encoding="utf-8") as fh:
                ok = FORM[name].fullmatch(fh.read().strip()) is not None
            assert ok and private_file_ok(path, uid=uid), "BLOCKED: %s: %s" % (path, file_state(path))
            out("SECRETS %s: kept" % name)
            continue
        v = None
        for _k in range(3):
            a = tty.ask(prompt, hidden=True).strip()
            if not a and not required:
                break
            if FORM[name].fullmatch(a):
                v = a
                break
            tty.say("Не похоже на %s. Ещё раз." % LABEL[name])
        if v is None:
            out("SECRETS %s: %s" % (name, "skipped" if not required else "not given in 3 tries"))
            rc = rc or (4 if required else 0)
            continue
        out("SECRETS %s: written, %d bytes" % (name, write_private(path, (v + "\n").encode(), uid)))
    tty.say("Готово." if rc == 0 else "Не всё введено — запустите ту же строку ещё раз.")
    return rc


def mode_find_chat(tg=None, etc=ETC, wait_s=FIND_CHAT_S, uid=0, now=time.time, sleep=time.sleep):
    """The one private chat that sent /start to the guard's bot, pinned to tg-chat by exclusive create; one already
    pinned is kept. Waits up to wait_s. Prints counts only, never a chat id."""
    path = os.path.join(etc, "tg-chat")
    if os.path.lexists(path):
        with open(path, encoding="utf-8") as fh:
            ok = FORM["tg-chat"].fullmatch(fh.read().strip()) is not None
        assert ok and private_file_ok(path, uid=uid), "BLOCKED: %s: %s" % (path, file_state(path))
        out("FIND-CHAT pinned already, kept")
        return 0
    if tg is None:
        creds, problems = read_credentials(etc, uid)
        assert "tg-token" in creds, "BLOCKED: tg-token: %s" % problems
        tg = Telegram(Net(timeout=LONG_POLL_S + 15), creds["tg-token"])
    deadline, offset, said = now() + wait_s, 0, False
    while True:
        try:
            ups = tg.call("getUpdates", offset=offset, timeout=min(LONG_POLL_S, max(0, int(deadline - now()))),
                          allowed_updates=["message"])
        except Exception as e:
            out("FIND-CHAT a poll failed: %s" % type(e).__name__)
            if now() >= deadline:
                return 4
            sleep(5)
            continue
        found = private_starts(ups)
        if len(found) == 1:
            break
        if len(found) > 1 or now() >= deadline:
            out("FIND-CHAT updates %d, private chats that sent /start: %d - FAIL" % (len(ups), len(found)))
            return 4
        if ups:
            offset = ups[-1]["update_id"] + 1
        if not said:
            out("FIND-CHAT no /start among %d updates; waiting up to %d s" % (len(ups), wait_s))
            said = True
    write_private(path, ("%d\n" % found[0]).encode(), uid)
    tg.send(found[0], "Сторож на связи. Чат закреплён — сюда будут приходить предупреждения.", quiet=False)
    out("FIND-CHAT updates %d, private chats that sent /start: 1, pinned" % len(ups))
    return 0


def see_text(pos):
    """What the guard sees, for the Boss to hold against his Binance app. Pure."""
    if not pos:
        return "Сторож не видит ни одной открытой позиции на фьючерсах USDⓈ-M."
    lines = ["Сторож видит открытых позиций: %d" % len(pos)]
    for p in sorted(pos, key=lambda q: (q["symbol"], q["side"])):
        lines.append("• " + position_line(p, distance_pct(p), None))
    return "\n".join(lines)


def answer_of(updates, chat):
    """The first yes or no from `chat` among Telegram updates: True, False or None. Pure."""
    for u in updates:
        m = u.get("message") if isinstance(u, dict) else None
        if not isinstance(m, dict) or (m.get("chat") or {}).get("id") != chat:
            continue
        t = (m.get("text") or "").strip().lower().strip(".!")
        if t in YES:
            return True
        if t in NO:
            return False
    return None


def mode_prove(net=None, etc=ETC, var=VAR, uid=0, now=time.time, sleep=time.sleep, code=None):
    """CANON hard rule 14: every request path the unit uses, through this file's own functions, served and parsed;
    the key read able to read and nothing else, and bound to an address; what it sees confirmed by the Boss in his
    chat as every open position he has; a test alarm sent at Pushover's emergency priority and acknowledged on his
    phone. Its record, prove.json, carries this code's SHA-256."""
    creds, problems = read_credentials(etc, uid)
    gates = []

    def gate(name, ok, detail):
        gates.append({"gate": name, "pass": bool(ok), "detail": detail})
        out("%s %s - %s" % (name, "PASS" if ok else "FAIL", detail))
        return ok
    if not gate("G-CRED", not problems, "%d credentials of their form, 0600, root's; the dead-man %s%s" % (
            len(creds), "set" if "hc-url" in creds else "not set", "; " + "; ".join(problems) if problems else "")):
        return 4
    scrub = Scrub(creds)
    net = net or Net(timeout=LONG_POLL_S + 15)
    bn = Binance(net, creds["binance-key"], creds["binance-secret"], now)
    po = Pushover(net, creds["pushover-token"], creds["pushover-user"])
    tg = Telegram(net, creds["tg-token"])

    def tried(name, f):
        try:
            return f(), None
        except Exception as e:
            return None, scrub("%s: %s" % (type(e).__name__, e))[:300]
    off, e = tried("time", bn.sync_time)
    gate("G-TIME", e is None and abs(off) < 2000, "Binance's clock less this host's: %s ms" % (off if e is None else e))
    doc, e = tried("key", bn.restrictions)
    ok, why = key_reading(doc) if e is None else (False, [e])
    gate("G-KEY", ok, (perms_line(doc) if e is None else "") + ("; refused: " + "; ".join(why) if why else ""))
    raw, e = tried("positions", bn.positions)
    pos = None
    if e is None:
        try:
            pos = parse_positions(raw)
        except AssertionError as x:
            e = scrub(x)
    gate("G-POS", e is None, ("%s served; open positions %d, with a liquidation price %d" % (
        bn.position_path, len(pos), sum(1 for p in pos if distance_pct(p) is not None))) if e is None else e)
    sym = pos[0]["symbol"] if pos else "BTCUSDT"
    br, e = tried("brackets", lambda: bn.brackets(sym))
    n = len((br[0] if isinstance(br, list) and br else br or {}).get("brackets") or []) if e is None else 0
    gate("G-BRACKET", e is None and n > 0, ("leverage brackets of one held symbol: %d" % n) if e is None else e)
    _v, e = tried("pushover", po.validate)
    gate("G-PUSH", e is None, "the user key and token validated" if e is None else e)
    me, e = tried("telegram", lambda: tg.call("getMe"))
    if e is None:
        _s, e = tried("telegram", lambda: tg.send(creds["tg-chat"], "Сторож · проверка связи (ТЗ-54)."))
    gate("G-TG", e is None, "getMe and one message to the pinned chat" if e is None else e)
    if all(g["pass"] for g in gates):
        chat = int(creds["tg-chat"])
        last, e = tried("telegram", lambda: tg.call("getUpdates", offset=-1, timeout=0, allowed_updates=["message"]))
        offset = (last[-1]["update_id"] + 1) if e is None and last else 0
        if e is None:
            _s, e = tried("telegram", lambda: tg.send(chat, see_text(pos) + "\n\nСовпадает с твоими позициями в "
                                                                       "Binance? Ответь «да» или «нет»."))
        said, t0 = None, now()
        while e is None and said is None and now() - t0 < SEE_WAIT_S:
            ups, e2 = tried("telegram", lambda: tg.call("getUpdates", offset=offset, timeout=LONG_POLL_S,
                                                        allowed_updates=["message"]))
            if e2 is not None:
                sleep(5)
                continue
            if ups:
                offset = ups[-1]["update_id"] + 1
            said = answer_of(ups, chat)
        gate("G-SEE", said is True, e or ("the Boss answered yes to the list of %d positions after %d s" % (
            len(pos), round(now() - t0)) if said is True else "the Boss answered no" if said is False
            else "no answer in %d s" % SEE_WAIT_S))
    if all(g["pass"] for g in gates):
        r, e = tried("alarm", lambda: po.send("Сторож: проверка тревоги (ТЗ-54)",
                                               "Нажми «Подтвердить» — так проверяется, что тревога будит тебя.", 2,
                                               TEST_EXPIRE_S))
        acked, waited = False, 0
        if e is None:
            tried("telegram", lambda: tg.send(creds["tg-chat"], "Сейчас зазвонит Pushover — нажми «Подтвердить»."))
            t0 = now()
            while now() - t0 < TEST_WAIT_S:
                sleep(RECEIPT_EVERY_S)
                d, e2 = tried("receipt", lambda: po.receipt(r))
                if e2 is None and d.get("acknowledged") == 1:
                    acked = True
                    break
            waited = round(now() - t0)
            if not acked:
                tried("cancel", lambda: po.cancel(r))
        gate("G-ALARM", acked, ("acknowledged after %d s" % waited) if acked else (e or "not acknowledged in %d s" % TEST_WAIT_S))
    if all(g["pass"] for g in gates):
        if "hc-url" in creds:
            _h, e = tried("dead-man", lambda: hc_ping(net, creds["hc-url"]))
            gate("G-HC", e is None, "the dead-man's ping answered OK" if e is None else e)
        else:
            gate("G-HC", True, "not set - no ping")
    passed = all(g["pass"] for g in gates) and [g["gate"] for g in gates] == list(PROVE_GATES)
    code = code or sha256_file(os.path.abspath(__file__))
    rec = {"at": utc(now()), "code_sha256": code, "pass": passed, "gates": gates,
           "requests": {h: c for h, c in sorted(net.count.items())} if hasattr(net, "count") else {}}
    replace_private(os.path.join(var, "prove.json"), (json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n").encode(),
                    uid)
    out("PROVE %s: %d gates of %d passed; requests %s" % ("PASS" if passed else "FAIL",
                                                          sum(g["pass"] for g in gates), len(gates), rec["requests"]))
    return 0 if passed else 4


def mode_status(var=VAR):
    """The guard's own state from its files: counts, states and instants - no symbol, price, size or margin."""
    path = os.path.join(var, "state.json")
    if not os.path.exists(path):
        out("STATUS no state.json")
        return 4
    with open(path, encoding="utf-8") as fh:
        st = json.load(fh)
    keys = ("at", "started", "last_ok", "polls_ok", "polls_err", "positions", "with_liquidation", "blind", "key_ok",
            "key_checked", "dead_man", "outbox", "disk_faults", "thresholds", "pid")
    out("STATUS " + "; ".join("%s %s" % (k, st.get(k)) for k in keys))
    jd = os.path.join(var, "journal")
    files = sorted(os.listdir(jd)) if os.path.isdir(jd) else []
    evs = {}
    for f in files[-2:]:
        with open(os.path.join(jd, f), encoding="utf-8") as fh:
            for ln in fh:
                e = json.loads(ln).get("ev")
                evs[e] = evs.get(e, 0) + 1
    out("STATUS journal files %d; events in the last two: %s" % (len(files), dict(sorted(evs.items()))))
    return 0


def host_addresses():
    """This host's global IPv4 addresses, as `ip -4 -o addr show scope global` lists them."""
    import subprocess
    r = subprocess.run(["ip", "-4", "-o", "addr", "show", "scope", "global"], capture_output=True, text=True,
                       timeout=20)
    assert r.returncode == 0, "ip: exit %d" % r.returncode
    return sorted(set(re.findall(r"inet ((?:[0-9]{1,3}\.){3}[0-9]{1,3})/", r.stdout)))


def scan_counts(blob, needles):
    """{label: occurrences} of each needle in blob, a number matched whole. Pure."""
    found = {}
    for label, v in needles:
        pat = re.escape(v.encode())
        if v.isdigit() or IPV4.fullmatch(v):
            pat = rb"(?<![0-9.])" + pat + rb"(?![0-9])"
        found[label] = len(re.findall(pat, blob))
    return found


def mode_scan(paths, etc=ETC, uid=0, addresses=None):
    """G-PRINT: every given file read whole for every credential, the chat id and this host's own IPv4 addresses.
    Prints counts per file - never a value; exit 4 where any count is above zero."""
    creds, problems = read_credentials(etc, uid)
    needles = [(k, v) for k, v in sorted(creds.items())]
    addrs = host_addresses() if addresses is None else addresses
    needles += [("host-ipv4-%d" % i, a) for i, a in enumerate(addrs, 1)]
    assert paths, "scan takes files"
    total = 0
    for path in paths:
        with open(path, "rb") as fh:
            found = scan_counts(fh.read(), needles)
        n = sum(found.values())
        total += n
        out("SCAN %s: %d bytes, %s" % (path, os.path.getsize(path), "nothing found" if n == 0 else
                                       ", ".join("%s %d" % (k, c) for k, c in sorted(found.items()) if c)))
    out("G-PRINT %s: %d files, %d values sought - credentials %d, the host's IPv4 addresses %d; found %d" % (
        "PASS" if total == 0 else "FAIL", len(paths), len(needles), len(creds), len(addrs), total))
    return 0 if total == 0 else 4


def mode_serve(etc=ETC, var=VAR):
    creds, problems = read_credentials(etc)
    if problems:
        out("SERVE refused: %s" % "; ".join(problems))
        return 2
    g = Guard(creds, var=var)
    stop = []
    signal.signal(signal.SIGTERM, lambda *_a: stop.append(1))
    g.journal("start", code=sha256_file(os.path.abspath(__file__)), thresholds=list(g.th), dead_man=bool(g.hc))
    try:
        g.check_key()
    except KeyRefused as e:
        return refuse(g, e)
    g.poll()
    g.say("Сторож запущен: позиций %d; пороги %s / %s / %s; ключ %s." % (
        len(g.positions), pct(g.th[0]), pct(g.th[1]), pct(g.th[2]),
        "только чтение ✓" if g.key_ok else "ещё не проверен"), quiet=True)
    g.flush()
    g.save_state()
    g.notify("READY=1")
    out("SERVE start: key %s, positions read %s" % (g.key_ok, g.polls_ok))
    while not stop:
        t0 = time.monotonic()
        try:
            g.cycle()
        except KeyRefused as e:
            return refuse(g, e)
        except Exception as e:
            g.err("cycle", e)
        while not stop and time.monotonic() - t0 < POLL_S:
            time.sleep(min(1.0, max(0.0, POLL_S - (time.monotonic() - t0))))
    g.journal("stop", polls_ok=g.polls_ok, polls_err=g.polls_err)
    g.save_state()
    out("SERVE stop on SIGTERM")
    return 0


def refuse(g, e):
    text = "Сторож остановлен: ключ Binance может больше, чем читать (%s). Создай ключ только с «Enable Reading» и " \
           "привязкой к IP сервера." % "; ".join(e.args[0])
    for f in (lambda: g.po.send("Сторож остановлен", text, 1), lambda: g.tg.send(g.chat, "🔴 " + text)):
        try:
            f()
        except Exception as x:
            g.err("refuse", x)
    g.journal("refused", problems=e.args[0])
    g.save_state()
    out("SERVE refused: the key can do more than read: %s" % "; ".join(e.args[0]))
    return 2


# ---- the self-test: stand-ins for Binance, Pushover, Telegram and healthchecks ----------------------------------

class FakeNet:
    """Binance, Pushover, Telegram and healthchecks.io as dictionaries; every request recorded."""

    def __init__(self, key, secret, positions=(), perms=None):
        self.key, self.secret, self.log, self.count = key, secret, [], {}
        self.positions, self.down = list(positions), set()
        self.perms = perms if perms is not None else {"ipRestrict": True, "enableReading": True,
                                                     "enableWithdrawals": False, "enableInternalTransfer": False,
                                                     "enableMargin": False, "enableFutures": False,
                                                     "permitsUniversalTransfer": False, "enableVanillaOptions": False,
                                                     "enableFixApiTrade": False, "enableFixReadOnly": True,
                                                     "enableSpotAndMarginTrading": False,
                                                     "enablePortfolioMarginTrading": False, "createTime": 1}
        self.pushes, self.receipts, self.tg_sent, self.updates, self.v3 = [], {}, [], [], True
        self.answer = "Да"
        self.now = time.time

    def call(self, host, method, path, body=None, headers=()):
        h = dict(headers)
        self.log.append((host, method, path.split("?")[0]))
        self.count[host] = self.count.get(host, 0) + 1
        if host in self.down:
            raise ConnectionResetError("down")
        u = urllib.parse.urlsplit(path)
        q = urllib.parse.parse_qs(u.query)
        if host in (FAPI, SAPI):
            if u.path == "/fapi/v1/time":
                return 200, json.dumps({"serverTime": int(self.now() * 1000)}).encode()
            assert h.get("X-MBX-APIKEY") == self.key, "a signed request without the key"
            raw, sig = u.query.rsplit("&signature=", 1)
            want = hmac.new(self.secret.encode(), raw.encode(), hashlib.sha256).hexdigest()
            if sig != want:
                return 400, b'{"code":-1022,"msg":"Signature for this request is not valid."}'
            if host == SAPI and u.path == "/sapi/v1/account/apiRestrictions":
                return 200, json.dumps(self.perms).encode()
            if host == FAPI and u.path in POSITION_PATHS:
                if u.path.startswith("/fapi/v3") and not self.v3:
                    return 404, b"<html>404</html>"
                return 200, json.dumps(self.positions).encode()
            if host == FAPI and u.path == "/fapi/v1/leverageBracket":
                return 200, json.dumps({"symbol": q["symbol"][0], "brackets": [
                    {"bracket": 1, "notionalFloor": 0, "notionalCap": 50000, "maintMarginRatio": 0.01, "cum": 0},
                    {"bracket": 2, "notionalFloor": 50000, "notionalCap": 250000, "maintMarginRatio": 0.02,
                     "cum": 500}]}).encode()
            return 404, b"{}"
        if host == PUSHOVER:
            if method == "POST":
                f = urllib.parse.parse_qs(body.decode())
                if u.path == "/1/users/validate.json":
                    return 200, b'{"status":1,"devices":["iphone"]}'
                if u.path == "/1/messages.json":
                    r = "r%029d" % len(self.pushes) if f["priority"][0] == "2" else None
                    self.pushes.append({k: v[0] for k, v in f.items()})
                    if r:
                        self.receipts[r] = {"status": 1, "acknowledged": 0}
                    return 200, json.dumps({"status": 1, "request": "x", **({"receipt": r} if r else {})}).encode()
                m = re.fullmatch(r"/1/receipts/(\w+)/cancel\.json", u.path)
                if m:
                    self.receipts[m.group(1)]["cancelled"] = True
                    return 200, b'{"status":1}'
            m = re.fullmatch(r"/1/receipts/(\w+)\.json", u.path)
            if m and m.group(1) in self.receipts:
                return 200, json.dumps(self.receipts[m.group(1)]).encode()
            return 400, b'{"status":0,"errors":["bad"]}'
        if host == TG:
            meth = u.path.rsplit("/", 1)[1]
            p = json.loads(body.decode())
            if meth == "getMe":
                return 200, b'{"ok":true,"result":{"id":1,"is_bot":true}}'
            if meth == "sendMessage":
                self.tg_sent.append(p)
                if "Совпадает" in p["text"] and self.answer is not None:
                    n = max([x["update_id"] for x in self.updates] or [0]) + 1
                    self.updates.append({"update_id": n, "message": {"text": self.answer,
                                                                    "chat": {"id": p["chat_id"], "type": "private"}}})
                return 200, b'{"ok":true,"result":{"message_id":1}}'
            if meth == "getUpdates":
                off = p.get("offset", 0)          # as Telegram: an offset confirms, and forgets, what is before it
                self.updates = self.updates[off:] if off < 0 else [x for x in self.updates if x["update_id"] >= off]
                return 200, json.dumps({"ok": True, "result": self.updates}).encode()
            return 404, b'{"ok":false,"description":"Not Found"}'
        if host == HC:
            return 200, b"OK"
        raise AssertionError("an unknown host %s" % host)


def binance_lp(side, qty, entry, wallet, mmr, cum):
    """Binance's liquidation price of a one-way isolated position, for the self-test's arithmetic."""
    s = 1 if side == "LONG" else -1
    return (wallet + cum - s * qty * entry) / (qty * mmr - s * qty)


def on_terminal(child, script, timeout=60):
    """child() in a child process whose controlling terminal is a new pseudo-terminal, as sshd gives `ssh -t`, and
    whose standard output and error are a pipe. `script`: (what the screen shows, what is typed), each typed once the
    screen shows its text after the last line typed. Returns (exit status, screen, log, lines left untyped)."""
    import codecs
    import fcntl
    import select
    import termios
    assert threading.active_count() == 1
    sys.stdout.flush()
    sys.stderr.flush()
    master, slave = os.openpty()
    rlog, wlog = os.pipe()
    pid = os.fork()
    if pid == 0:
        rc = 70
        try:
            os.close(master)
            os.close(rlog)
            os.setsid()
            fcntl.ioctl(slave, termios.TIOCSCTTY, 0)
            os.dup2(slave, 0)
            os.dup2(wlog, 1)
            os.dup2(wlog, 2)
            os.close(slave)
            os.close(wlog)
            rc = child()
        except BaseException:
            import traceback
            traceback.print_exc()
            rc = 71
        finally:
            try:
                sys.stdout.flush()
                sys.stderr.flush()
            finally:
                os._exit(rc if isinstance(rc, int) else 72)
    os.close(slave)
    os.close(wlog)
    dec = codecs.getincrementaldecoder("utf-8")("replace")
    screen, log, pending, mark = "", b"", list(script), 0
    fds, deadline = [master, rlog], time.monotonic() + timeout
    try:
        while fds:
            if time.monotonic() > deadline:
                os.kill(pid, signal.SIGKILL)
                break
            ready, _w, _x = select.select(fds, [], [], 0.2)
            for fd in ready:
                try:
                    data = os.read(fd, 65536)
                except OSError:
                    data = b""
                if not data:
                    fds.remove(fd)
                elif fd == master:
                    screen += dec.decode(data)
                else:
                    log += data
            if pending and pending[0][0] in screen[mark:]:
                mark = screen.index(pending[0][0], mark) + len(pending[0][0])
                os.write(master, (pending.pop(0)[1] + "\n").encode())
    finally:
        os.close(master)
        os.close(rlog)
        status = os.waitpid(pid, 0)[1]
    return os.waitstatus_to_exitcode(status), screen, log.decode("utf-8", "replace"), pending


def mode_selftest():
    import shutil
    import tempfile
    n = [0]

    def check(cond, what):
        n[0] += 1
        assert cond, "SELFTEST FAIL: " + what

    root = tempfile.mkdtemp(prefix="liq-guard-selftest-")
    uid = os.getuid()
    try:
        # -- arithmetic: the margin hint against Binance's own liquidation formula --------------------------------
        for side, qty, entry, wallet, mmr, cum, mark in (("SHORT", 25.0, 1787.0, 4100.0, 0.01, 0.0, 1900.0),
                                                        ("LONG", 0.5, 97000.0, 3000.0, 0.004, 0.0, 92000.0),
                                                        ("SHORT", 1200.0, 2.31, 180.0, 0.025, 12.5, 2.40)):
            lp = binance_lp(side, qty, entry, wallet, mmr, cum)
            p = {"side": side, "qty": qty, "mark": mark, "liq": lp, "isolated": True}
            need = margin_hint(p, mmr, 8.0)
            lp2 = binance_lp(side, qty, entry, wallet + need, mmr, cum)
            d2 = distance_pct({"side": side, "mark": mark, "liq": lp2})
            check(need > 0 and abs(d2 - 8.0) < 1e-9, "the margin hint moves %s's liquidation to 8%%: %r" % (side, d2))
            check(margin_hint(dict(p, liq=binance_lp(side, qty, entry, wallet + need + 100, mmr, cum)), mmr) == 0.0,
                  "no hint where the liquidation is beyond the target")
        check(abs(distance_pct({"side": "SHORT", "mark": 100.0, "liq": 103.0}) - 3.0) < 1e-12, "a short's distance")
        check(abs(distance_pct({"side": "LONG", "mark": 100.0, "liq": 97.0}) - 3.0) < 1e-12, "a long's distance")
        check(distance_pct({"side": "LONG", "mark": 100.0, "liq": 0.0}) is None, "no liquidation price, no distance")
        # -- levels: announce once a descent, the highest of a jump, re-arm above threshold + 1 -------------------
        th, f, seq = (5.0, 3.0, 1.5), frozenset(), []
        for d in (6.0, 4.9, 4.5, 2.9, 2.8, 1.4, 1.0, 2.6, 1.4, 8.0, 0.9, None, 4.0):
            lvl, f = step(f, d, th)
            seq.append(lvl)
        check(seq == [0, 1, 0, 2, 0, 3, 0, 0, 3, 0, 3, 0, 1], "the levels announced: %r" % seq)
        check(step(frozenset({1}), 5.5, th)[1] == frozenset({1}) and step(frozenset({1}), 6.01, th)[1] == frozenset(),
              "hysteresis of one point")
        # -- positions, brackets, the key's permissions, commands ----------------------------------------------------
        raw = [{"symbol": "YFIUSDT", "positionSide": "BOTH", "positionAmt": "-25.000", "markPrice": "1596.20",
                "liquidationPrice": "1700.00", "notional": "-39905.0", "isolatedWallet": "4100.0"},
               {"symbol": "BTCUSDT", "positionSide": "LONG", "positionAmt": "0.500", "markPrice": "92000",
                "liquidationPrice": "0", "notional": "46000", "isolatedWallet": "0"},
               {"symbol": "ETHUSDT", "positionSide": "BOTH", "positionAmt": "0.000", "markPrice": "3000",
                "liquidationPrice": "0"}]
        ps = parse_positions(raw)
        check([(p["symbol"], p["side"], p["isolated"]) for p in ps] == [("YFIUSDT", "SHORT", True),
                                                                        ("BTCUSDT", "LONG", False)], "positions: %r" % ps)
        br = {"brackets": [{"notionalFloor": 50000, "notionalCap": 250000, "maintMarginRatio": 0.02, "cum": 500},
                           {"notionalFloor": 0, "notionalCap": 50000, "maintMarginRatio": 0.01, "cum": 0}]}
        check(bracket_for(br, 39905.0) == (0.01, 0.0) and bracket_for([br], 60000) == (0.02, 500.0)
              and bracket_for(br, 9e9) is None, "brackets")
        good = FakeNet("k" * 64, "s" * 64).perms
        check(key_reading(good) == (True, []), "a read-only, bound key")
        for k in ("enableFutures", "enableWithdrawals", "enableSpotAndMarginTrading", "permitsUniversalTransfer",
                  "enableSomethingNew"):
            check(key_reading(dict(good, **{k: True}))[0] is False, "refused: %s" % k)
        check(key_reading(dict(good, ipRestrict=False))[0] is False, "refused: no address")
        check(key_reading({k: v for k, v in good.items() if k != "enableFutures"})[0] is False, "refused: absent field")
        check(parse_command("/status@SomeBot") == ("status", []) and parse_command("Пороги 5 3 1,5")
              == ("thresholds", ["5", "3", "1,5"]) and parse_command("  ТЕСТ ") == ("test", []), "commands")
        check(thresholds_of(["5", "3", "1,5"]) == (5.0, 3.0, 1.5) and thresholds_of(["3", "5", "1"]) is None
              and thresholds_of(["40", "3", "1"]) is None and thresholds_of(["5", "3"]) is None, "thresholds")
        check(price(1596.2) == "1 596,2" and price(0.00012346) == "0,0001235" and pct(2.94) == "2,9%",
              "notation: %r %r" % (price(1596.2), price(0.00012346)))
        sc = Scrub({"binance-key": "A" * 64, "tg-chat": "123"})
        check(sc("key %s from 203.0.113.9" % ("A" * 64)) == "key *** from x.x.x.x", "scrub")
        # -- IPv4 alone ----------------------------------------------------------------------------------------------
        seen = []

        def fake_gai(host, port, family=0, type=0, *a):
            seen.append(family)
            raise OSError("stop")
        real_gai, socket.getaddrinfo = socket.getaddrinfo, fake_gai
        try:
            try:
                V4HTTPS("example.invalid", 443, timeout=1, context=ssl.create_default_context()).connect()
            except OSError:
                pass
        finally:
            socket.getaddrinfo = real_gai
        check(seen == [socket.AF_INET], "every connect resolves IPv4 alone: %r" % seen)
        tick = [100.0]
        net = Net(timeout=1, clock=lambda: tick[0])
        calls = []

        def timing_out(*a, **k):
            calls.append(1)
            raise TimeoutError("timed out")
        net._call = timing_out
        for _k in range(3):
            try:
                net.call(FAPI, "GET", "/x")
            except OSError:
                pass
        tick[0] += COOLDOWN_S
        try:
            net.call(FAPI, "GET", "/x")
        except OSError:
            pass
        check(len(calls) == 2, "a failed host waits out its cooldown: %d tries" % len(calls))
        # -- secrets at a real terminal ------------------------------------------------------------------------------
        etc = os.path.join(root, "etc")
        vals = {"binance-key": "K" * 64, "binance-secret": "S" * 64, "pushover-user": "u" * 30,
                "pushover-token": "a" * 30, "tg-token": "123456789:" + "T" * 35}
        script = [("API Key", "not-a-key"), ("API Key", vals["binance-key"]), ("Secret Key", vals["binance-secret"]),
                  ("User Key", vals["pushover-user"]), ("API Token", vals["pushover-token"]),
                  ("BotFather", vals["tg-token"]), ("hc-ping.com", "")]
        rc, screen, log, left = on_terminal(lambda: mode_secrets(etc=etc, uid=uid), script)
        check(rc == 0 and not left, "secrets at a real terminal: rc %s, left %d, log %r" % (rc, len(left), log[-300:]))
        check(all(v not in screen + log for v in vals.values()), "no value echoed or logged")
        check(sorted(os.listdir(etc)) == sorted(vals) and all(private_file_ok(os.path.join(etc, k), uid=uid)
                                                              for k in vals), "five files, 0600")
        check("hc-url: skipped" in log and "written, 65 bytes" in log, "the log: written and skipped")
        rc2, _s, log2, _l = on_terminal(lambda: mode_secrets(etc=etc, uid=uid), [("hc-ping.com", "")])
        check(rc2 == 0 and log2.count(": kept") == 5 and "hc-url: skipped" in log2,
              "a second run keeps them and asks for the optional one again: %r" % log2[-200:])
        # -- find-chat -----------------------------------------------------------------------------------------------
        fn = FakeNet(vals["binance-key"], vals["binance-secret"])
        fn.updates = [{"update_id": 7, "message": {"text": "/start", "chat": {"id": 4242, "type": "private"}}}]
        check(mode_find_chat(Telegram(fn, vals["tg-token"]), etc, 5, uid) == 0, "find-chat pins one chat")
        creds, problems = read_credentials(etc, uid)
        check(problems == [] and creds["tg-chat"] == "4242", "credentials read: %r" % problems)
        # -- prove ---------------------------------------------------------------------------------------------------
        clock = [1.8e9]
        var = os.path.join(root, "var")

        def ack_later(_s):
            clock[0] += _s
            for r in fn.receipts.values():
                r["acknowledged"], r["acknowledged_at"] = 1, int(clock[0])
        fn.positions, fn.now = raw, (lambda: clock[0])
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 0, "prove passes")
        rec = json.load(open(os.path.join(var, "prove.json")))
        check(rec["pass"] is True and [g["gate"] for g in rec["gates"]] == list(PROVE_GATES), "prove's ten gates")
        write_private(os.path.join(etc, "hc-url"), b"https://hc-ping.com/0f0e0d0c-0b0a-4908-8706-050403020100\n", uid)
        n_hc = fn.count.get(HC, 0)
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 0
              and json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["detail"] == "the dead-man's ping answered OK"
              and fn.count.get(HC, 0) == n_hc + 1, "the dead-man pinged once, last, after the Boss's answers")
        check(any("YFIUSDT шорт" in m["text"] and "Совпадает" in m["text"] for m in fn.tg_sent), "the list shown")
        fn.answer = "нет"
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4,
              "prove fails where the Boss answers no")
        check(json.load(open(os.path.join(var, "prove.json")))["gates"][-1]["gate"] == "G-SEE", "no alarm after a no")
        fn.answer = "да"
        check(fn.pushes[-1]["priority"] == "2" and fn.pushes[-1]["expire"] == str(TEST_EXPIRE_S), "a test alarm")
        fn.perms = dict(fn.perms, enableFutures=True)
        check(mode_prove(fn, etc, var, uid, lambda: clock[0], ack_later, code="c" * 64) == 4,
              "prove refuses a key that can trade")
        fn.perms["enableFutures"] = False
        fn.v3 = False
        bn = Binance(fn, vals["binance-key"], vals["binance-secret"], lambda: clock[0])
        check(bn.positions() == raw and bn.position_path == "/fapi/v2/positionRisk", "v2 where v3 is not served")
        fn.v3 = True
        # -- the guard's cycle -----------------------------------------------------------------------------------------
        notes = []
        g = Guard(creds, net=fn, now=lambda: clock[0], var=var, uid=uid, notify=notes.append)
        fn.positions = [dict(raw[0], liquidationPrice="1700.00")]
        n_push, n_tg = len(fn.pushes), len(fn.tg_sent)
        g.cycle()
        check(g.key_ok is True and g.polls_ok == 1 and len(fn.pushes) == n_push and len(fn.tg_sent) == n_tg + 1
              and HELP[:20] in fn.tg_sent[-1]["text"], "first cycle: 6.5%% from liquidation, nothing rings; the "
              "pending /start answered with the help")
        base_push = len(fn.pushes)
        for liq, want_push in (("1670.0", 0), ("1640.0", 1), ("1630.0", 0), ("1615.0", 1)):
            clock[0] += 5
            fn.positions = [dict(raw[0], liquidationPrice=liq)]
            g.cycle()
            check(len(fn.pushes) - base_push == want_push, "liq %s: pushes %d" % (liq, len(fn.pushes) - base_push))
            base_push = len(fn.pushes)
        alarm = fn.pushes[-1]
        check(alarm["priority"] == "2" and alarm["retry"] == "30" and "ПОСЛЕДНИЙ ЗВОНОК" in alarm["title"]
              and "долить" in alarm["message"] and "4242" not in alarm["message"], "the second alarm: %r" % alarm)
        check(any("до ликвидации" in m["text"] for m in fn.tg_sent), "Telegram carries the warning")
        # margin added: re-armed, then a new descent alarms again
        clock[0] += 5
        fn.positions = [dict(raw[0], liquidationPrice="1800.0")]
        g.cycle()
        check(g.fired.get("YFIUSDT:SHORT") == frozenset(), "re-armed after margin")
        clock[0] += 5
        fn.positions = [dict(raw[0], liquidationPrice="1640.0")]
        n0 = len(fn.pushes)
        g.cycle()
        check(len(fn.pushes) == n0 + 1, "a new descent alarms again")
        # commands: status, thresholds, test acknowledged; a foreign chat ignored
        sent0 = len(fn.tg_sent)
        fn.updates = [{"update_id": 20, "message": {"text": "Статус", "chat": {"id": 4242, "type": "private"}}},
                      {"update_id": 21, "message": {"text": "Пороги 6 4 2", "chat": {"id": 4242, "type": "private"}}},
                      {"update_id": 22, "message": {"text": "Пороги 9 8 7", "chat": {"id": 9999, "type": "private"}}},
                      {"update_id": 23, "message": {"text": "Тест", "chat": {"id": 4242, "type": "private"}}}]
        clock[0] += 5
        g.cycle()
        texts = [m["text"] for m in fn.tg_sent[sent0:]]
        check(g.th == (6.0, 4.0, 2.0) and g.tg_offset == 24 and all(m["chat_id"] == 4242 for m in fn.tg_sent),
              "commands from the pinned chat alone: %r" % (g.th,))
        check(any(t.startswith("Сторож: на месте") for t in texts) and any("Пороги заданы" in t for t in texts),
              "status and thresholds answered: %r" % texts)
        check(g.test is not None and fn.pushes[-1]["expire"] == str(TEST_EXPIRE_S), "the test alarm sent")
        rid = g.test["receipt"]
        n2 = sum(1 for x in fn.pushes if x["priority"] == "2")
        fn.receipts[rid].update(acknowledged=1, acknowledged_at=int(clock[0]))
        fn.updates = []
        clock[0] += RECEIPT_EVERY_S
        g.cycle()
        check(g.test is None and any("Тест пройден" in m["text"] for m in fn.tg_sent), "the test acknowledged")
        check(json.load(open(os.path.join(var, "state.json")))["thresholds"] == [6.0, 4.0, 2.0], "thresholds kept")
        check(sum(1 for x in fn.pushes if x["priority"] == "2") == n2
              and g.fired.get("YFIUSDT:SHORT") == frozenset({1, 2}), "new thresholds ring nothing at once")
        # Binance's rate refusal: no request until its back-off has passed
        real_call = fn.call

        def limited(host, *a, **k):
            if host == FAPI and a[1].startswith("/fapi/v3/positionRisk"):
                return 429, b'{"code":-1003,"msg":"Too many requests"}'
            return real_call(host, *a, **k)
        fn.call = limited
        clock[0] += 5
        g.cycle()
        n_req = sum(1 for h, _m, pth in fn.log if pth.startswith("/fapi/v3/positionRisk"))
        clock[0] += 5
        g.cycle()
        check(sum(1 for h, _m, pth in fn.log if pth.startswith("/fapi/v3/positionRisk")) == n_req
              and g.bn_backoff > clock[0], "a 429 holds the reads back")
        fn.call = real_call
        clock[0] += 60
        g.cycle()
        check(g.polls_ok > 0 and g.bn_backoff <= clock[0], "reads resume after the back-off")
        # blindness: two minutes without a read alarm once, then a reminder after 30 minutes, then seen again
        fn.down.add(FAPI)
        n0 = len(fn.pushes)
        g.heartbeat = lambda: 1 / 0
        for _k in range(30):
            clock[0] += 5
            g.cycle()
        check(g.blind and len(fn.pushes) == n0 + 1 and fn.pushes[-1]["priority"] == "1", "blind once")
        check("Сторож не видит Binance" in fn.pushes[-1]["message"] and "positions" in fn.pushes[-1]["message"],
              "the blind alarm names Binance's own error")
        del g.heartbeat
        check(any(json.loads(ln).get("where") == "heartbeat" for f in os.listdir(os.path.join(var, "journal"))
                  for ln in open(os.path.join(var, "journal", f), encoding="utf-8")), "the failing step journaled")
        clock[0] += BLIND_REPEAT_S
        g.cycle()
        check(len(fn.pushes) == n0 + 2, "blind, reminded")
        fn.down.discard(FAPI)
        clock[0] += 5
        g.cycle()
        check(not g.blind and any("снова видит" in m["text"] for m in fn.tg_sent), "seen again")
        # a disk that refuses every write: the alarm still goes, the fault is counted
        real_open, faults0 = os.open, g.disk_faults

        def no_room(path, *a, **k):
            if str(path).startswith(var):
                raise OSError(28, "No space left on device")
            return real_open(path, *a, **k)
        os.open = no_room
        try:
            fn.positions = [dict(raw[0], liquidationPrice="1800.0")]
            clock[0] += 5
            g.cycle()
            n0 = len(fn.pushes)
            fn.positions = [dict(raw[0], liquidationPrice="1625.0")]
            clock[0] += STATE_S
            g.cycle()
        finally:
            os.open = real_open
        check(len(fn.pushes) == n0 + 1 and g.disk_faults > faults0, "a full disk stops no alarm")
        # Pushover down: the alarm waits in the outbox, then goes
        fn.down.add(PUSHOVER)
        fn.positions = [dict(raw[0], liquidationPrice="1800.0")]
        clock[0] += 5
        g.cycle()
        fn.positions = [dict(raw[0], liquidationPrice="1620.0")]
        clock[0] += 5
        g.cycle()
        check(any(m["to"] == "push" for m in g.outbox), "an alarm kept while Pushover is down")
        fn.down.discard(PUSHOVER)
        n0 = len(fn.pushes)
        clock[0] += 5
        g.cycle()
        check(len(fn.pushes) == n0 + 1 and not any(m["to"] == "push" for m in g.outbox), "sent once it is up")
        # Telegram down: one try a pass, the alarm channel still served, the queue bounded
        fn.down.add(TG)
        tries0 = sum(1 for h, _m, _p in fn.log if h == TG)
        for k in range(OUTBOX_MAX + 5):
            g.say("m%d" % k)
        clock[0] += 5
        g.cycle()
        check(sum(1 for h, _m, _p in fn.log if h == TG) - tries0 == 2, "Telegram tried once for the outbox and once "
              "for its updates")
        check(len([m for m in g.outbox if m["to"] == "tg"]) == OUTBOX_MAX, "the queue bounded")
        fn.down.discard(TG)
        sent0 = len(fn.tg_sent)
        clock[0] += 5
        g.cycle()
        check(len(fn.tg_sent) - sent0 == TG_PER_PASS, "at most %d Telegram messages a pass" % TG_PER_PASS)
        for _k in range(30):
            clock[0] += 5
            g.cycle()
        check(not g.outbox, "the queue sent, five a pass, once Telegram is up")
        # the heartbeat at 19:00 UTC, once a day, quiet
        day0 = dt.datetime(2027, 1, 5, 18, 59, 0, tzinfo=dt.timezone.utc).timestamp()
        clock[0] = day0
        g.last_ok = clock[0]
        g.cycle()
        clock[0] = day0 + 120
        g.cycle()
        clock[0] = day0 + 600
        g.cycle()
        old = os.path.join(var, "journal", "2026-09-01.jsonl")
        open(old, "w").close()
        os.chmod(old, 0o600)
        g.next_tick = 0
        g.cycle()
        check(not os.path.exists(old), "a journal file older than %d days removed" % KEEP_DAYS)
        hb = [m for m in fn.tg_sent if m["text"].startswith("Сторож на месте")]
        check(len(hb) == 1 and hb[0]["disable_notification"] is True, "one quiet heartbeat: %d" % len(hb))
        # a key widened at a later check: refused
        fn.perms = dict(fn.perms, enableSpotAndMarginTrading=True)
        g.next_key = 0
        try:
            g.cycle()
            refused = False
        except KeyRefused:
            refused = True
        check(refused, "a key widened later is refused")
        # the record: 0600 files, no secret in any of them, no chat id
        jd = os.path.join(var, "journal")
        blob = b"".join(open(os.path.join(jd, f), "rb").read() for f in os.listdir(jd))
        blob += open(os.path.join(var, "state.json"), "rb").read() + open(os.path.join(var, "prove.json"), "rb").read()
        check(all(v.encode() not in blob for v in vals.values()) and b"4242" not in blob, "no secret in the record")
        check(all(private_file_ok(os.path.join(jd, f), uid=uid) for f in os.listdir(jd)), "journal files 0600")
        check("WATCHDOG=1" in notes, "the watchdog notified")
        check(all(h in (FAPI, SAPI, PUSHOVER, TG, HC) for h, _m, _p in fn.log), "no other host")
        clean = os.path.join(root, "clean.log")
        open(clean, "w").write("G-KEY PASS - enableReading True\nat 1795000000 from 10.0.0.2\n")
        dirty = os.path.join(root, "dirty.log")
        open(dirty, "w").write("x %s y 4242 z 203.0.113.7 w 203.0.113.70\n" % vals["pushover-token"])
        check(mode_scan([clean], etc, uid, ["203.0.113.7"]) == 0, "scan: a clean file")
        check(scan_counts(open(dirty, "rb").read(), [("t", vals["pushover-token"]), ("c", "4242"),
                                                     ("a", "203.0.113.7")]) == {"t": 1, "c": 1, "a": 1},
              "scan: a token, the chat id and an address found, a longer address not")
        check(mode_scan([clean, dirty], etc, uid, ["203.0.113.7"]) == 4, "scan: a dirty file fails G-PRINT")
    finally:
        shutil.rmtree(root, ignore_errors=True)
    check(not os.path.exists(root), "the self-test's tree removed")
    out("SELFTEST PASS: %d checks" % n[0])
    return 0


def main(argv):
    modes = {"secrets": mode_secrets, "find-chat": mode_find_chat, "prove": mode_prove, "serve": mode_serve,
             "status": mode_status, "selftest": mode_selftest}
    if len(argv) >= 3 and argv[1] == "scan":
        assert os.geteuid() == 0, "BLOCKED: scan runs as root"
        return mode_scan(argv[2:])
    if len(argv) != 2 or argv[1] not in modes:
        out("usage: liq-guard.py " + "|".join(modes) + "|scan FILE...")
        return 1
    if argv[1] != "selftest":
        assert os.geteuid() == 0, "BLOCKED: %s runs as root" % argv[1]
    return modes[argv[1]]()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
