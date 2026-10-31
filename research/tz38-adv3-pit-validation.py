#!/usr/bin/env python3
# tz38-adv3-pit-validation.py - TZ-38's instrument: ADV-3's frozen rule run, unchanged, on every Binance USD-M USDT perpetual
# that traded - the Boss's 42 coins, the delisted ones and the rest - with an entry allowed only where the contract was liquid
# before the day. Standard library only. It fetches Binance's public archive (data.binance.vision) into a store, builds each
# contract's point-in-time admissibility, runs the advisor's own functions (advisor/adv3.py, loaded by its hash, never copied
# and never written), and writes the tables. The reading of the rule on the contracts outside the Boss's 42 is an exploration
# that moves no rung (CANON PART VII). It starts no unit, signals no process, reads nothing under /etc/adv3-bot and nothing of
# the Boss's account. Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import bisect, contextlib, datetime as dt, hashlib, http.client, importlib.util, io, json, math, os, re, resource, shutil, \
    statistics, subprocess, sys, threading, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from array import array
from concurrent.futures import ThreadPoolExecutor

WORK = os.environ.get('TZ38_WORK', '/root/tz38-work')
PRIMARY = os.environ.get('TZ38_PRIMARY', '/root/btc-5m-twap')
FORENSICS = '/root/btc-forensics'
STORE = WORK + '/archive'
OUT = WORK + '/out'
NUMBER = 'TZ-38-'
TZ_FILE = 'CryptoTZ/TZ-38-adv3-pit-validation.md'
MAP_REV = '2026-10-31-b'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
ROWS, FROZEN = 57, 54
ADV3_SHA = 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8'
RULE_SHA = 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169'
MEM_FLOOR, DISK_FLOOR = 122_462_208, 7_700_000_000   # TZ section 0.4: twice the largest anonymous set of any mode, and the reward book's floor plus this TZ's bytes

S3 = 'https://s3-ap-northeast-1.amazonaws.com/data.binance.vision'
CDN = 'https://data.binance.vision/'
UA = 'btc-5m-twap-tz38'
KL = 'data/futures/um/monthly/klines/'
FU = 'data/futures/um/monthly/fundingRate/'
KD = 'data/futures/um/daily/klines/'

# ---- the declarations of the gate, fixed before any contract outside the Boss's 42 was read ----------------------------
V_MIN = 10_000_000.0       # admissibility: the median daily quote volume of the 28 candles before the day, in USDT
V_SENS = (30_000_000.0,)
WINDOW, SPAN = 28, 42      # candles in the median; the days they must lie within
MIN_COINS = 10             # a month counts where its mean number of admissible coins is at least this
ALPHA = 0.05               # G-PIT's one-sided level for each tail, for the t-test and for the bootstrap alike
BOOT_B, BOOT_L, SEED = 100_000, 3, 0x3A38
RANDOM_LISTS, LIST_SIZE = 500, 42
M64 = (1 << 64) - 1


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


def verdict(name, checks):
    n = sum(1 for v in checks.values() if v)
    for k, v in checks.items():
        out(('ok   ' if v else 'FAIL ') + k)
    out('READING %s: %s - %d of %d' % (name, 'PASS' if n == len(checks) else 'FAIL', n, len(checks)))
    if n != len(checks):
        raise Failed(name)


# ---- the advisor, loaded by hash ---------------------------------------------------------------------------------------

def load_adv3():
    path = PRIMARY + '/advisor/adv3.py'
    assert sha256_file(path) == ADV3_SHA, 'advisor/adv3.py is not the frozen file'
    spec = importlib.util.spec_from_file_location('adv3', path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['adv3'] = mod
    spec.loader.exec_module(mod)
    return mod


# ---- the archive: listing, plan, fetch, manifest -------------------------------------------------------------------------

def request(url, tries=4):
    """The body of url, or None where the server answers 404; a network error, 418, 429 or 5xx is tried again after 1, 3 and
    5 s; any other answer raises at once. Every request names UA."""
    err = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (418, 429) and e.code < 500:
                raise RuntimeError('FETCH REFUSED %s: HTTP %d' % (url, e.code)) from None
            err = e
        except (OSError, http.client.HTTPException) as e:
            err = e
        if k + 1 < tries:
            time.sleep(1 + 2 * k)
    raise RuntimeError('FETCH FAILED %s: %r' % (url, err))


def s3_list(prefix, delimiter='/'):
    """([common prefixes], [keys]) under prefix, page after page of 1,000."""
    prefixes, keys, marker = [], [], ''
    while True:
        q = {'prefix': prefix, 'max-keys': '1000'}
        if delimiter:
            q['delimiter'] = delimiter
        if marker:
            q['marker'] = marker
        body = request(S3 + '?' + urllib.parse.urlencode(q))
        assert body is not None, 'listing %s' % prefix
        root = ET.fromstring(body)
        ns = {'s': root.tag.split('}')[0][1:]}
        prefixes += [e.find('s:Prefix', ns).text for e in root.findall('s:CommonPrefixes', ns)]
        keys += [e.find('s:Key', ns).text for e in root.findall('s:Contents', ns)]
        if root.find('s:IsTruncated', ns).text != 'true':
            return prefixes, keys
        nxt = root.find('s:NextMarker', ns)
        marker = nxt.text if nxt is not None else (prefixes[-1] if delimiter and prefixes else keys[-1])


def month_of(key):
    m = re.search(r'-(\d{4})-(\d{2})\.zip$', key)
    return (int(m.group(1)), int(m.group(2))) if m else None


def plan_symbol(sym, hist_to, funding_to):
    """The keys one contract needs, by the listing: every monthly kline file, the daily files of each month up to hist_to's that
    has no monthly file, and every monthly funding file up to funding_to. Returns (keys, listing calls made)."""
    _, k1 = s3_list(KL + '%s/1d/' % sym)
    monthly = sorted(k for k in k1 if k.endswith('.zip'))
    have = {month_of(k) for k in monthly}
    _, f1 = s3_list(FU + '%s/' % sym)
    funding = sorted(k for k in f1 if k.endswith('.zip') and month_of(k) <= funding_to)
    first = min(have) if have else None
    daily, calls = [], 2
    todo = []
    y, m = (first if first else (2019, 9))
    while (y, m) <= (hist_to.year, hist_to.month):
        if (y, m) not in have:
            todo.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    for ym in todo:
        _, kd = s3_list(KD + '%s/1d/%s-1d-%04d-%02d' % (sym, sym, ym[0], ym[1]), delimiter='')
        calls += 1
        daily += [k for k in kd if k.endswith('.zip')
                  and dt.date.fromisoformat(k[-14:-4]) <= hist_to]
    return monthly + sorted(daily) + funding, calls


def fetch_one(key):
    """key into STORE, verbatim, by one rename; (key, size, sha256) or (key, None, None) where the server has no such file."""
    path = os.path.join(STORE, key)
    if os.path.exists(path):
        b = read(path, 'rb')
        return key, len(b), sha256_bytes(b)
    b = request(CDN + key)
    if b is None:
        return key, None, None
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'wb') as f:
        f.write(b)
    os.replace(tmp, path)
    return key, len(b), sha256_bytes(b)


def universe_symbols():
    """Every plain USDT perpetual of the archive's klines listing, sorted: BASEUSDT with no delivery suffix."""
    prefixes, _ = s3_list(KL)
    return sorted(s for s in (p.split('/')[-2] for p in prefixes) if re.fullmatch(r'[A-Z0-9]+USDT', s))


# ---- the local store through adv3's own readers; the series in arrays -----------------------------------------------------

class SerialPool:
    """The one method of a pool adv3.archive_funding calls, run in order."""

    @staticmethod
    def map(fn, it):
        return [fn(x) for x in it]


def local_get_for(adv3):
    def local_get(url, tries=4):
        assert url.startswith(adv3.ARCH), url
        path = STORE + '/data/futures/um/' + url[len(adv3.ARCH):]
        return read(path, 'rb') if os.path.exists(path) else None
    return local_get


def candle_rows(adv3, sym, last_day):
    """{day: (open, high, low, close, quote volume)} of one perpetual from the store, the files selected as
    adv3.archive_candles selects them - every monthly file, then the daily files of the months with no monthly file from the
    first month with data on - the quote volume (field 7) read beside the four prices."""
    ms = list(adv3.months(adv3.ARCHIVE_FROM, last_day))
    url_m = lambda ym: '%smonthly/klines/%s/1d/%s-1d-%04d-%02d.zip' % (adv3.ARCH, sym, sym, ym[0], ym[1])
    got = {ym: adv3.get(url_m(ym)) for ym in ms}
    out_ = {}
    for ym, body in got.items():
        if body is not None:
            for p in adv3.zip_rows(body):
                out_[adv3.ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[7]))
    first_seen = min(out_) if out_ else None
    missing = [ym for ym, body in got.items() if body is None and (first_seen is None or ym >= (first_seen.year, first_seen.month))]
    days = [d for ym in missing for d in (dt.date(ym[0], ym[1], k) for k in range(1, 32) if adv3._valid(ym, k)) if d <= last_day]
    for d in days:
        body = adv3.get('%sdaily/klines/%s/1d/%s-1d-%s.zip' % (adv3.ARCH, sym, sym, d.isoformat()))
        if body is not None:
            for p in adv3.zip_rows(body):
                out_[adv3.ms_day(p[0])] = (float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[7]))
    return {d: v for d, v in out_.items() if d <= last_day}


NONE_I, NONE_F = 9, float('nan')


class Series:
    """One contract: ordinals and prices in arrays, then the states adv3.states derives from them."""
    __slots__ = ('sym', 'ords', 'o', 'h', 'l', 'c', 'qv', 'sig', 'z', 'sm', 'U', 'ended')

    def __init__(self, sym, rows):
        days = sorted(rows)
        self.sym = sym
        self.ords = array('i', [d.toordinal() for d in days])
        self.o, self.h, self.l, self.c, self.qv = (array('d', [rows[d][k] for d in days]) for k in range(5))
        self.sig = self.sm = self.z = self.U = None
        self.ended = False

    def index(self, d):
        o = d.toordinal()
        i = bisect.bisect_left(self.ords, o)
        return i if i < len(self.ords) and self.ords[i] == o else -1


class Candles:
    """The mapping adv3.simulate, adv3.states and adv3.unit read: {day: (open, high, low, close)}."""

    def __init__(self, s):
        self.s = s

    def __iter__(self):
        return (dt.date.fromordinal(x) for x in self.s.ords)

    def __len__(self):
        return len(self.s.ords)

    def __contains__(self, d):
        return self.s.index(d) >= 0

    def __getitem__(self, d):
        i = self.s.index(d)
        if i < 0:
            raise KeyError(d)
        s = self.s
        return (s.o[i], s.h[i], s.l[i], s.c[i])


class States:
    """{day: (signal, z, sum of signs, U, close)} as adv3.states returns it, over arrays; mask, where given, lifts U to None
    on the days the contract is not admissible, which no ranking admits; a contract whose data ends before the cut is flat
    on its last day, which closes a position there."""

    def __init__(self, s, mask=None):
        self.s, self.mask = s, mask

    def __iter__(self):
        return (dt.date.fromordinal(x) for x in self.s.ords)

    def __contains__(self, d):
        return self.s.index(d) >= 0

    def __getitem__(self, d):
        s = self.s
        i = s.index(d)
        if i < 0:
            raise KeyError(d)
        u = s.U[i]
        if u != u or (self.mask is not None and not self.mask[i]):
            u = None
        z = s.z[i]
        sg = 0 if (s.ended and i == len(s.ords) - 1) else s.sig[i]
        return (None if sg == NONE_I else sg, None if z != z else z, None if s.sm[i] == NONE_I else s.sm[i], u, s.c[i])


def fill_states(adv3, s, last_day):
    """The states of s, from adv3.states over the series' own candles, into arrays."""
    st = adv3.states(Candles(s), last_day)
    n = len(s.ords)
    s.sig, s.sm = array('b', [NONE_I] * n), array('b', [NONE_I] * n)
    s.z, s.U = array('d', [NONE_F] * n), array('d', [NONE_F] * n)
    for i, o in enumerate(s.ords):
        sg, z, sm, u, _ = st[dt.date.fromordinal(o)]
        if sg is not None:
            s.sig[i] = sg
        if z is not None:
            s.z[i] = z
        if sm is not None:
            s.sm[i] = sm
        if u is not None:
            s.U[i] = u


class FundingDays:
    """The {day: sum of the day's settlements} that adv3.funding_of reads through .get, in two arrays."""

    def __init__(self, per_day):
        days = sorted(per_day)
        self.ords = array('i', [d.toordinal() for d in days])
        self.vals = array('d', [per_day[d] for d in days])

    def get(self, d, default=0.0):
        o = d.toordinal()
        i = bisect.bisect_left(self.ords, o)
        return self.vals[i] if i < len(self.ords) and self.ords[i] == o else default


def funding_for(adv3, sym, s, hist_to):
    """The rule's funding of one contract, built as adv3.history() builds it, over the store: (the function, its FundingDays)."""
    first = dt.date.fromordinal(s.ords[0])
    per_day, covered = adv3.archive_funding(sym, first, hist_to, SerialPool)
    covered = {ym for ym in covered if ym <= adv3.FUNDING_TO}
    per_day = {d: x for d, x in per_day.items() if (d.year, d.month) in covered}
    first_settle = min(per_day) if per_day else None
    fd = FundingDays(per_day)
    return adv3.funding_of(fd, lambda d, fs=first_settle, cv=covered: fs is not None and d >= fs and (d.year, d.month) in cv), fd


class Arena:
    """One file holding the arrays of every contract, written as the contracts are built and mapped read-only once it is
    sealed: the arrays are then views into the map, pages the system can take back, and the process's own memory holds the
    objects and not the prices."""
    SIZE = {'d': 8, 'i': 4, 'b': 1}

    def __init__(self, path):
        self.path, self.index, self.pos, self.view, self.mm = path, {}, 0, None, None
        self.f = open(path, 'xb')

    def add(self, key, arr):
        pad = (-self.pos) % 8
        self.f.write(b'\0' * pad)
        self.pos += pad
        self.index[key] = (self.pos, len(arr), arr.typecode)
        b = arr.tobytes()
        self.f.write(b)
        self.pos += len(b)

    def seal(self):
        import mmap
        self.f.close()
        fd = os.open(self.path, os.O_RDONLY)
        self.mm = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
        os.close(fd)
        os.unlink(self.path)               # the map keeps the file's pages; nothing is left on disk
        self.view = memoryview(self.mm)

    def get(self, key):
        off, n, tc = self.index[key]
        return self.view[off:off + n * self.SIZE[tc]].cast(tc)


# ---- the admissibility, a pure function of what the contract had traded before the day -------------------------------------

def admissible(ords, qv, v_min, window=WINDOW, span=SPAN):
    """flags[i]: True where the median quote volume of the `window` candles before ords[i] is at least v_min and the
    earliest of those lies within `span` days of ords[i]. It reads qv[i - window : i] and ords[i - window : i + 1] alone; a
    v_min of 0 admits every day."""
    n = len(ords)
    flags = array('b', bytes(n))
    if v_min <= 0:
        return array('b', [1] * n)
    for i in range(window, n):
        if ords[i] - ords[i - window] <= span and statistics.median(qv[i - window:i]) >= v_min:
            flags[i] = 1
    return flags


# ---- the statistics: pure functions ---------------------------------------------------------------------------------------

def betacf(a, b, x):
    """The continued fraction of the regularized incomplete beta function, by the modified Lentz method."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 1000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-16:
            return h
    raise ArithmeticError('betacf did not converge')


def betai(a, b, x):
    """The regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbeta) * betacf(a, b, x) / a
    return 1.0 - math.exp(lbeta) * betacf(b, a, 1.0 - x) / b


def t_sf(t, df):
    """P(T >= t) for Student's t with df degrees of freedom."""
    p = 0.5 * betai(df / 2.0, 0.5, df / (df + t * t))
    return p if t >= 0 else 1.0 - p


def splitmix64(state):
    """(next state, output) of SplitMix64."""
    state = (state + 0x9E3779B97F4A7C15) & M64
    z = state
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & M64
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & M64
    return state, z ^ (z >> 31)


def boot_p(x, B=BOOT_B, L=BOOT_L, seed=SEED):
    """(p up, p down) of the circular block bootstrap of the mean of x: the series is centred, B resamples of ceil(n / L)
    blocks of L consecutive values (wrapping round), each block's start u = floor(r * n / 2^64) for r the next SplitMix64 output,
    the last block cut to the n values; p up = (1 + #{resampled mean >= the observed mean}) / (B + 1), p down alike with <=."""
    n = len(x)
    mean = sum(x) / n
    pre = [0.0]
    for v in [v - mean for v in x] * 2:
        pre.append(pre[-1] + v)
    nb = -(-n // L)
    last = n - L * (nb - 1)
    state, up, down = seed & M64, 0, 0
    for _ in range(B):
        tot = 0.0
        for j in range(nb):
            state, r = splitmix64(state)
            u = (r * n) >> 64
            tot += pre[u + (L if j < nb - 1 else last)] - pre[u]
        m = tot / n
        up += m >= mean
        down += m <= mean
    return (1 + up) / (B + 1), (1 + down) / (B + 1)


def mean_sd(x):
    n = len(x)
    m = sum(x) / n
    return m, math.sqrt(sum((v - m) ** 2 for v in x) / (n - 1))


def phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


def probit(p):
    """The z with phi(z) = p, by bisection to 1e-15."""
    lo, hi = -40.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if phi(mid) < p else (lo, mid)
    return 0.5 * (lo + hi)


def read_series(x):
    """G-PIT's statistic on a monthly series: n, mean, sd, t, the Student p up and down, the bootstrap's, the word."""
    n = len(x)
    m, sd = mean_sd(x)
    if not sd > 0:
        return {'n': n, 'mean': m, 'sd': sd, 'word': 'UNDECIDABLE', 'why': 'a series with no spread'}
    t = m / (sd / math.sqrt(n))
    pu, pd = t_sf(t, n - 1), 1.0 - t_sf(t, n - 1)
    bu, bd = boot_p(x)
    word = ('REPLICATED' if pu <= ALPHA and bu <= ALPHA else 'CONTRADICTED' if pd <= ALPHA and bd <= ALPHA
            else 'UNDECIDABLE')
    return {'n': n, 'mean': m, 'sd': sd, 'sharpe_month': m / sd, 't': t, 'p_t_up': pu, 'p_t_down': pd,
            'p_boot_up': bu, 'p_boot_down': bd, 'word': word}


def power(sharpe, n, alpha=ALPHA):
    """The normal approximation of the power of the one-sided test of a mean at the level alpha, n months of Sharpe ratio
    `sharpe` a month: phi(sharpe * sqrt(n) - z(1 - alpha))."""
    return phi(sharpe * math.sqrt(n) - probit(1.0 - alpha))


def monthly(S, N, hist_to, min_coins=MIN_COINS):
    """[(year, month, x, mean N)] of the calendar months whose last day is hist_to or before and whose mean number of admissible
    coins a day is min_coins or more; x is the month's sum of S[day] / N[day] over the days with N[day] > 0. S and N are
    keyed by ordinal."""
    import calendar
    rows = []
    if not N:
        return rows
    first = dt.date.fromordinal(min(N))
    y, m = first.year, first.month
    while (y, m) <= (hist_to.year, hist_to.month):
        nd = calendar.monthrange(y, m)[1]
        d0 = dt.date(y, m, 1).toordinal()
        if dt.date(y, m, nd) <= hist_to:
            days = range(d0, d0 + nd)
            mean_n = sum(N.get(o, 0) for o in days) / nd
            if mean_n >= min_coins:
                rows.append((y, m, sum(S.get(o, 0.0) / N[o] for o in days if N.get(o, 0) > 0), mean_n))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return rows


def monthly_sum(R, rows):
    """The month sums of R (keyed by ordinal) over the months of rows, in rows' order."""
    import calendar
    return [sum(R.get(o, 0.0) for o in range(dt.date(y, m, 1).toordinal(), dt.date(y, m, 1).toordinal() + calendar.monthrange(y, m)[1]))
            for y, m, _x, _n in rows]


# ---- the advisor's functions over the series -------------------------------------------------------------------------------

@contextlib.contextmanager
def patched(mod, **attrs):
    """Module attributes replaced for the block and restored after it, whatever happens."""
    old = {k: getattr(mod, k) for k in attrs}
    for k, v in attrs.items():
        setattr(mod, k, v)
    try:
        yield
    finally:
        for k, v in old.items():
            setattr(mod, k, v)


@contextlib.contextmanager
def gated(adv3, s, mask):
    """adv3.unit lifted to None on the days of s that mask does not admit: no entry opens there and no ranking admits the
    contract. adv3.states and adv3.simulate call unit by its module name, so the block reaches both. A mask of None changes
    nothing."""
    if mask is None:
        yield
        return
    orig = adv3.unit

    def unit(c, days, i):
        j = s.index(days[i])
        return orig(c, days, i) if j >= 0 and mask[j] else None
    with patched(adv3, unit=unit):
        yield


@contextlib.contextmanager
def recording(adv3):
    """adv3.hold wrapped so that each position keeps, in an array, the pairs (ordinal, R after the day) of its days held."""
    orig = adv3.hold

    def hold(pos, candle, pc, fund_d, day):
        r, stopped = orig(pos, candle, pc, fund_d, day)
        path = pos.get('path')
        if path is None:
            path = pos['path'] = array('d')
        path.extend((float(day.toordinal()), pos['R']))
        return r, stopped
    with patched(adv3, hold=hold):
        yield


def end_trade(adv3, s, pos, why):
    """A position open at the end of a contract's data, closed at its last close with one exit cost, as adv3.history() closes
    one at the cut; the trade and the cost in R."""
    cost = adv3.COST * s.c[-1] / pos['U']
    return dict(pos, R=pos['R'] - cost, why=why, end=dt.date.fromordinal(s.ords[-1])), cost


def rule_pass(adv3, series, funds, masks, hist_to, order=None, record=False):
    """The rule on each series of `order`, sorted by default. Returns trades (each with its coin), the daily R summed over the contracts
    as adv3.history() sums it ('facts'), the same with the exit cost of each position closed at the end of data on its last
    day ('gate'), and N, the number of contracts a day that are admissible and have a signal."""
    trades, facts, gate, N = [], {}, {}, {}
    for sym in (sorted(series) if order is None else order):
        s = series[sym]
        mask = masks.get(sym)
        with gated(adv3, s, mask), (recording(adv3) if record else contextlib.nullcontext()):
            th, dh, ph = adv3.simulate(Candles(s), funds[sym], dt.date.fromordinal(s.ords[0]), hist_to)
        why = 'delisted' if s.ended else 'open at the history cut'
        extra = None
        if ph:
            t, cost = end_trade(adv3, s, ph, why)
            th = th + [t]
            extra = (s.ords[-1], cost)
        for t in th:
            t['coin'] = sym
        trades += th
        for d, x in dh.items():
            o = d.toordinal()
            facts[o] = facts.get(o, 0.0) + x
            gate[o] = gate.get(o, 0.0) + x
        if extra:
            gate[extra[0]] = gate.get(extra[0], 0.0) - extra[1]
        for i, o in enumerate(s.ords):
            if s.sig[i] != NONE_I and (mask is None or mask[i]):
                N[o] = N.get(o, 0) + 1
    return {'trades': trades, 'facts': facts, 'gate': gate, 'N': N}


def strong_pass(adv3, series, funds, masks, syms, hist_to, top_n=3, strong_max=3, record=False):
    """The STRONG strategy over syms (their order is the ranking's tie order): trades, daily R, and the positions the data
    ends on, closed as adv3.history() closes them at the cut. A contract whose data ends before the cut is flat on its last day,
    which closes a position there."""
    cs = {k: Candles(series[k]) for k in syms}
    st = {k: States(series[k], masks.get(k)) for k in syms}
    first = dt.date.fromordinal(min(series[k].ords[0] for k in syms))
    with patched(adv3, COINS=tuple(syms), TOP_N=top_n, STRONG_MAX=strong_max), \
            (recording(adv3) if record else contextlib.nullcontext()):
        trades, daily, open_ = adv3.simulate_strong(cs, st, funds, first, hist_to)
    for coin, t in open_.items():
        tr, _cost = end_trade(adv3, series[coin], t, 'open at the history cut')
        trades.append(tr)
    return {'trades': trades, 'daily': {d.toordinal(): x for d, x in daily.items()}}


# ---- the tables: pure readings of trades and series ----------------------------------------------------------------------------

def stat_block(adv3, trades, daily):
    """adv3.stats of one strategy, with the history's own additions: the share of the five best trades in the total, the
    mean R without the best 1 % of the trades, the long and short parts, the stops hit."""
    x = adv3.stats(trades, daily)
    R = sorted((t['R'] for t in trades), reverse=True)
    x['top5_share'] = sum(R[:5]) / x['total_R'] if x['total_R'] > 0 else None
    cut = max(1, math.ceil(0.01 * len(R))) if R else 0
    x['mean_R_ex_top1pct'] = sum(R[cut:]) / (len(R) - cut) if len(R) > cut else None
    for name, side in (('long', 1), ('short', -1)):
        part = [t['R'] for t in trades if t['d'] == side]
        x[name] = {'trades': len(part), 'total_R': sum(part), 'mean_R': sum(part) / len(part) if part else None}
    x['stops'] = sum(t.get('why') == 'stop' for t in trades)
    return x


def exit_of(t):
    """The day a trade ended: its exit, or the last day of the data for a position closed there."""
    return t['exit'] if 'exit' in t else t['end']


def by_year(trades):
    out_ = {}
    for t in trades:
        y = exit_of(t).year
        a = out_.setdefault(y, [0, 0.0])
        a[0] += 1
        a[1] += t['R']
    return {str(y): {'trades': n, 'total_R': r} for y, (n, r) in sorted(out_.items())}


def bucket_table(trades, key, edges, labels):
    """Trades grouped by key(trade) into the buckets edges cut: [(label, n, mean R, total R, share in profit)]."""
    rows = [[lab, 0, 0.0, 0] for lab in labels]
    for t in trades:
        k = bisect.bisect_left(edges, key(t))
        rows[k][1] += 1
        rows[k][2] += t['R']
        rows[k][3] += t['R'] > 0
    return [{'bucket': lab, 'trades': n, 'total_R': r, 'mean_R': r / n if n else None, 'wins': w}
            for lab, n, r, w in rows]


def stop_pct(t):
    return 100.0 * t['U'] / t['E']


def rank_at(series, syms, masks, day, coin):
    """The coin's place in the day's ranking by |z| among the contracts that are active, admissible and have a signal, ties by
    syms' order, as adv3.ranking orders them."""
    act = []
    for k in syms:
        s = series[k]
        i = s.index(day)
        if i < 0:
            continue
        z, u = s.z[i], s.U[i]
        if s.sig[i] in (1, -1) and z == z and u == u and (masks.get(k) is None or masks[k][i]):
            act.append((-abs(z), k))
    act.sort(key=lambda a: a[0])
    return [k for _z, k in act].index(coin) + 1


def weakening(adv3, trades, series):
    """Of the trades entered with all four signs agreeing, those whose sum of signs fell to +/-2 while the signal held: the R
    they made after that close, against the R of leaving at it. delta = R_final - (R at the close - the exit cost in R)."""
    n4, rows, never = 0, [], []
    for t in trades:
        path = t.get('path')
        if path is None:
            continue
        s = series[t['coin']]
        j0 = s.index(t['entry'])
        if j0 < 0 or s.sm[j0] == NONE_I or abs(s.sm[j0]) != 4:
            continue
        n4 += 1
        stop_day = t['exit'].toordinal() if t.get('why') == 'stop' else None
        hit = None
        for k in range(0, len(path), 2):
            o = int(path[k])
            j = s.index(dt.date.fromordinal(o))
            if o == stop_day:
                break
            if j >= 0 and s.sig[j] == t['d'] and s.sm[j] != NONE_I and abs(s.sm[j]) == 2:
                hit = (path[k + 1], s.c[j])
                break
        if hit is None:
            never.append(t['R'])
            continue
        r_at, close = hit
        rows.append((t['R'] - (r_at - adv3.COST * close / t['U']), t['R'] - r_at))
    d = sorted(x for x, _ in rows)
    return {'entered_with_four_signs': n4, 'weakened': len(rows), 'never_weakened': len(never),
            'mean_R_never_weakened': sum(never) / len(never) if never else None,
            'mean_R_after': sum(a for _, a in rows) / len(rows) if rows else None,
            'mean_hold_minus_exit': sum(d) / len(d) if d else None,
            'median_hold_minus_exit': d[len(d) // 2] if d else None,
            'share_hold_better': sum(x > 0 for x in d) / len(d) if d else None}


def trade_csv(trades, rank=None):
    """The trades as CSV text, sorted by entry then coin: forensic reconstruction of any row without re-running."""
    head = 'coin,side,entry,exit,why,R,mfe_R,stop_pct' + (',rank' if rank else '') + '\n'
    rows = []
    for t in sorted(trades, key=lambda t: (t['entry'], t['coin'])):
        rows.append('%s,%d,%s,%s,%s,%r,%r,%r%s\n' % (t['coin'], t['d'], t['entry'], exit_of(t), t.get('why', ''), t['R'],
                                                    t['mfe'], stop_pct(t), (',%d' % rank[(t['coin'], t['entry'])]) if rank else ''))
    return head + ''.join(rows)


def series_csv(rows, extra=None):
    head = 'year,month,x,mean_coins' + (',strong_R' if extra else '') + '\n'
    return head + ''.join('%d,%d,%r,%r%s\n' % (y, m, x, n, (',%r' % extra[i]) if extra else '') for i, (y, m, x, n) in enumerate(rows))


# ---- the plan, the fetch and the probe -------------------------------------------------------------------------------------

def mode_probe():
    """G-PATH: one request to each endpoint through request(), each asserted served and parsed, before the bulk begins."""
    import zipfile
    _, keys = s3_list(KL + 'BTCUSDT/1d/')
    assert len([k for k in keys if k.endswith('.zip')]) >= 80, 'klines listing'
    out('P-LIST served: %d keys under %sBTCUSDT/1d/' % (len(keys), KL))
    for name, key in (('P-MONTHLY', KL + 'BTCUSDT/1d/BTCUSDT-1d-2024-01.zip'), ('P-DAILY', KD + 'BTCUSDT/1d/BTCUSDT-1d-2024-01-15.zip'),
                      ('P-FUNDING', FU + 'BTCUSDT/BTCUSDT-fundingRate-2024-01.zip')):
        body = request(CDN + key)
        assert body is not None, name
        z = zipfile.ZipFile(io.BytesIO(body))
        rows = [l.split(',') for l in z.read(z.namelist()[0]).decode().splitlines() if l[:1].isdigit()]
        assert rows, name
        out('%s served: %s, %d bytes, %d rows' % (name, key, len(body), len(rows)))
    out('READING P-START: served - 4 of 4 endpoints')


def mode_plan(hist_to):
    os.makedirs(WORK, exist_ok=True)
    syms = universe_symbols()
    with ThreadPoolExecutor(12) as pool:
        res = list(pool.map(lambda s: plan_symbol(s, hist_to, (2026, 9)), syms))
    plan = {'hist_to': str(hist_to), 'symbols': syms, 'keys': {s: r[0] for s, r in zip(syms, res)},
            'listing_calls': sum(r[1] for r in res)}
    text = json.dumps(plan, sort_keys=True, indent=0) + '\n'
    with open(WORK + '/plan.json', 'x', encoding='utf-8') as f:
        f.write(text)
    out('PLAN: %d symbols, %d keys, %d listing calls; plan.json %d bytes SHA-256 %s' % (
        len(syms), sum(len(v) for v in plan['keys'].values()), plan['listing_calls'], len(text.encode()), sha256_bytes(text.encode())))


def mode_fetch():
    plan = json.loads(read(WORK + '/plan.json'))
    keys = sorted({k for v in plan['keys'].values() for k in v})
    del plan
    t0, done, absent, total = time.time(), 0, [], 0
    h = hashlib.sha256()
    with ThreadPoolExecutor(16) as pool, open(WORK + '/manifest.tsv', 'x', encoding='utf-8') as mf:
        for text in ('key\tbytes\tsha256\n',):
            mf.write(text)
            h.update(text.encode())
        for lo in range(0, len(keys), 2000):
            lines = []
            for key, size, sha in pool.map(fetch_one, keys[lo:lo + 2000]):
                done += 1
                if size is None:
                    absent.append(key)
                else:
                    lines.append('%s\t%d\t%s\n' % (key, size, sha))
                    total += size
            text = ''.join(lines)
            mf.write(text)
            h.update(text.encode())
            if done % 10000 == 0:
                out('fetched %d of %d in %.0f s' % (done, len(keys), time.time() - t0))
    assert not absent, 'planned keys the server does not serve: %r' % absent[:5]
    out('FETCH PASS: %d files, %d bytes in %.0f s; manifest.tsv %d bytes SHA-256 %s' % (
        done, total, time.time() - t0, os.path.getsize(WORK + '/manifest.tsv'), h.hexdigest()))


# ---- the run ------------------------------------------------------------------------------------------------------------------

LISTED_TO = dt.date(2025, 11, 30)    # the universe L: contracts whose first candle is on or before this day
EXCLUDED_BASES = ('USDC',)            # a contract pegged to the dollar has no trend to follow
MIN_MONTHS = 24


def load_all(adv3, plan, hist_to, arena=None):
    """{symbol: Series}, {symbol: funding}, {V: {symbol: flags}} of every contract of the plan that has candles, was listed by
    LISTED_TO and is admissible on some day at the lowest V of the run - or is the Boss's. The quote volumes are dropped once
    the flags are made; with an arena the arrays go to its file and come back as views once it is sealed."""
    vs = (V_MIN,) + V_SENS
    lowest = min(vs)
    boss = {c + 'USDT' for c in adv3.COINS}
    series, funds, masks, fds = {}, {}, {v: {} for v in vs}, {}
    names = ('ords', 'o', 'h', 'l', 'c', 'sig', 'z', 'sm', 'U')
    for sym in plan['symbols']:
        rows = candle_rows(adv3, sym, hist_to)
        if not rows:
            continue
        s = Series(sym, rows)
        del rows
        s.ended = dt.date.fromordinal(s.ords[-1]) < hist_to
        if not (sym in boss or (sym[:-4] not in EXCLUDED_BASES and dt.date.fromordinal(s.ords[0]) <= LISTED_TO
                                and any(admissible(s.ords, s.qv, lowest)))):
            continue
        fill_states(adv3, s, hist_to)
        for v in vs:
            masks[v][sym] = admissible(s.ords, s.qv, v)
        s.qv = None
        funds[sym], fds[sym] = funding_for(adv3, sym, s, hist_to)
        series[sym] = s
        if arena is not None:
            for nm in names:
                arena.add((sym, nm), getattr(s, nm))
                setattr(s, nm, None)
            for v in vs:
                arena.add((sym, 'mask', v), masks[v][sym])
                masks[v][sym] = None
            arena.add((sym, 'f_ords'), fds[sym].ords)
            arena.add((sym, 'f_vals'), fds[sym].vals)
            fds[sym].ords = fds[sym].vals = None
    if arena is not None:
        arena.seal()
        for sym, s in series.items():
            for nm in names:
                setattr(s, nm, arena.get((sym, nm)))
            for v in vs:
                masks[v][sym] = arena.get((sym, 'mask', v))
            fds[sym].ords, fds[sym].vals = arena.get((sym, 'f_ords')), arena.get((sym, 'f_vals'))
    return series, funds, masks


def facts_shape(adv3, rule, strong):
    """adv3.history()'s h, from the passes of the Boss's 42 with no admissibility."""
    to_date = lambda d: {dt.date.fromordinal(o): x for o, x in d.items()}
    base, st = adv3.stats(rule['trades'], to_date(rule['facts'])), adv3.stats(strong['trades'], to_date(strong['daily']))
    for x, tr in ((base, rule['trades']), (st, strong['trades'])):
        x['top5_share'] = sum(sorted((t['R'] for t in tr), reverse=True)[:5]) / x['total_R'] if x['total_R'] > 0 else None
    base['gate_H'] = 'NOT DISQUALIFIED' if base['total_R'] > 0 else 'DISQUALIFIED'
    st['gate_S'] = 'NOT DISQUALIFIED' if st['total_R'] > 0 and st['mean_R'] > base['mean_R'] else 'DISQUALIFIED'
    return {'base': base, 'strong': st}


PEAK_ANON = [0]


def proc_mem():
    """The process's memory now, from /proc/self/status: resident, of it anonymous (its own heap) and file-backed (the map's
    pages, which the system can take back), and the high-water mark of the resident set; the largest anonymous figure read so far
    is kept in PEAK_ANON."""
    d = {}
    for line in read('/proc/self/status').splitlines():
        if line.split(':')[0] in ('VmRSS', 'RssAnon', 'RssFile', 'VmHWM'):
            d[line.split(':')[0]] = int(line.split()[1]) * 1024
    PEAK_ANON[0] = max(PEAK_ANON[0], d.get('RssAnon', 0))
    return 'resident %(VmRSS)d (anon %(RssAnon)d, file %(RssFile)d), high-water %(VmHWM)d' % d


def start_sampler(interval=0.05):
    """A thread that reads proc_mem() every `interval` s, so that PEAK_ANON is the largest anonymous set of the whole run and not of
    the instants the phases happen to log. Returns the event that stops it."""
    stop = threading.Event()

    def loop():
        while not stop.is_set():
            try:
                proc_mem()
            except (OSError, KeyError, ValueError):
                pass
            stop.wait(interval)
    threading.Thread(target=loop, daemon=True).start()
    return stop


def malloc_tune():
    """glibc's mmap threshold at 128 KiB and its arenas at two, as the project's long-lived units fix them; True if glibc took both."""
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


def g_data(adv3, boss, hist_to, log):
    """G-DATA: the store's candles, read by candle_rows and read by adv3.archive_candles, equal day for day for the Boss's 42."""
    same = 0
    for sym in boss:
        mine = candle_rows(adv3, sym, hist_to)
        theirs = adv3.archive_candles(sym, hist_to, SerialPool)
        same += bool(mine) and {d: v[:4] for d, v in mine.items()} == theirs
    log('READING G-DATA: %s - %d of %d' % ('PASS' if same == len(boss) else 'FAIL', same, len(boss)))
    assert same == len(boss), 'G-DATA'


def g_equal(adv3, series, funds, boss, hist_to, log, exact):
    """G-EQUAL: the pipeline over the Boss's 42, no admissibility, read against the frozen FACTS (20 checks) and, where `exact`,
    against adv3.history() on the same store, block for block (2 checks). Returns (the passes, h)."""
    rule_a = rule_pass(adv3, series, funds, {}, hist_to, order=boss)
    strong_a = strong_pass(adv3, series, funds, {}, boss, hist_to)
    mine = facts_shape(adv3, rule_a, strong_a)
    checks = adv3.facts_checks(mine)
    if exact:
        ref = adv3.history()
        checks['base block equals history()'] = mine['base'] == ref['base']
        checks['strong block equals history()'] = mine['strong'] == ref['strong']
    n_ok = sum(1 for v in checks.values() if (v[0] if isinstance(v, tuple) else v))
    log('READING G-EQUAL: %s - %d of %d%s' % ('PASS' if n_ok == len(checks) else 'FAIL', n_ok, len(checks),
                                              '' if exact else ' (FACTS alone)'))
    assert n_ok == len(checks), 'G-EQUAL'
    return rule_a, mine


def run_prepare(adv3, plan, hist_to, log=out):
    t0 = time.time()
    stamp = lambda: '%.0f s, %s' % (time.time() - t0, proc_mem())
    adv3.get = local_get_for(adv3)
    boss = [c + 'USDT' for c in adv3.COINS]
    g_data(adv3, boss, hist_to, log)
    series, funds, masks = load_all(adv3, plan, hist_to, Arena(WORK + '/arena.bin'))
    trim()
    log('loaded %d contracts: %s' % (len(series), stamp()))
    assert all(boss_sym in series and not series[boss_sym].ended for boss_sym in boss), 'a contract of the Boss\'s 42 is absent or ended'
    listed = [k for k, s in series.items() if k[:-4] not in EXCLUDED_BASES and dt.date.fromordinal(s.ords[0]) <= LISTED_TO]
    L = sorted(k for k in listed if any(masks[V_MIN][k]))
    G = [k for k in L if k not in set(boss)]
    log('sets: Boss %d, universe L %d, gate set G %d: %s' % (len(boss), len(L), len(G), stamp()))
    res = {'sets': {'boss': len(boss), 'L': len(L), 'G': len(G), 'ended_in_L': sum(series[k].ended for k in L), 'loaded': len(series)}}
    rule_a, mine = g_equal(adv3, series, funds, boss, hist_to, log, exact=False)
    res['facts_42'] = {k: dict(v) for k, v in mine.items()}
    return {'res': res, 'series': series, 'funds': funds, 'masks': masks, 'boss': boss, 'L': L, 'G': G, 'listed': listed,
            'rule_a': rule_a, 'stamp': stamp, 'hist_to': hist_to, 'log': log}


def mode_equal():
    """G-EQUAL's exact reading, in a process of its own: the Boss's 42 alone, the pipeline against FACTS and against history()."""
    adv3 = load_adv3()
    plan = json.loads(read(WORK + '/plan.json'))
    hist_to = dt.date.fromisoformat(plan['hist_to'])
    adv3.get = local_get_for(adv3)
    boss = [c + 'USDT' for c in adv3.COINS]
    g_data(adv3, boss, hist_to, out)
    series, funds = {}, {}
    for sym in boss:
        series[sym] = Series(sym, candle_rows(adv3, sym, hist_to))
        fill_states(adv3, series[sym], hist_to)
        funds[sym] = funding_for(adv3, sym, series[sym], hist_to)[0]
    g_equal(adv3, series, funds, boss, hist_to, out, exact=True)
    out('EQUAL PASS: peak resident %d bytes' % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))


def trim():
    """Free pages glibc holds back: the memory a finished phase released goes to the system before the next one starts."""
    import ctypes, gc
    gc.collect()
    try:
        ctypes.CDLL('libc.so.6').malloc_trim(0)
    except OSError:
        pass


def word_or_short(x):
    if len(x) < MIN_MONTHS:
        return {'n': len(x), 'word': 'UNDECIDABLE', 'why': 'fewer than %d months' % MIN_MONTHS}
    return read_series(x)


def run_measure(adv3, ctx):
    """The readings over the prepared series. Returns the result dictionary and the files to write. Nothing here is a gate of
    this TZ: the reading of the rule on G is the Architect's exploration, re-derived (TZ section 4.2), and moves no rung."""
    res, series, funds, masks, boss, L, G = (ctx[k] for k in ('res', 'series', 'funds', 'masks', 'boss', 'L', 'G'))
    hist_to, log, stamp, listed = ctx['hist_to'], ctx['log'], ctx['stamp'], ctx['listed']
    Mv = masks[V_MIN]
    to_date = lambda d: {dt.date.fromordinal(o): x for o, x in d.items()}
    files = {}
    bset = set(boss)
    # -- the rule, then STRONG, on G: the contracts outside the Boss's 42
    rule_g = rule_pass(adv3, series, funds, Mv, hist_to, order=G)
    rows_g = monthly(rule_g['gate'], rule_g['N'], hist_to)
    gp = word_or_short([r[2] for r in rows_g])
    gp['trades'] = len(rule_g['trades'])
    gp['by_year'] = by_year(rule_g['trades'])
    gp['block'] = stat_block(adv3, rule_g['trades'], to_date(rule_g['facts']))
    del rule_g
    trim()
    strong_g = strong_pass(adv3, series, funds, Mv, G, hist_to)
    gs = word_or_short(monthly_sum(strong_g['daily'], rows_g))
    gs['trades'] = len(strong_g['trades'])
    gs['block'] = stat_block(adv3, strong_g['trades'], to_date(strong_g['daily']))
    xs_g = monthly_sum(strong_g['daily'], rows_g)
    del strong_g
    trim()
    log('phase G done: %s' % stamp())
    rows_a = monthly(ctx['rule_a']['gate'], ctx['rule_a']['N'], hist_to)
    xa = [r[2] for r in rows_a]
    ma, sa = mean_sd(xa)
    gp['alternative'] = {'boss_42_months': len(xa), 'boss_42_mean': ma, 'boss_42_sharpe_month': ma / sa,
                         'power_at_boss_42_sharpe': power(ma / sa, len(rows_g)), 'power_at_half': power(ma / sa / 2, len(rows_g)),
                         'power_at_own_sharpe': power(gp['sharpe_month'], len(rows_g)) if 'sharpe_month' in gp else None}
    gp['months'] = '%d-%02d to %d-%02d' % (rows_g[0][:2] + rows_g[-1][:2]) if rows_g else None
    gp['mean_coins'] = [min(r[3] for r in rows_g), max(r[3] for r in rows_g)] if rows_g else None
    res['pit_rule'], res['pit_strong'] = gp, gs
    log('PIT rule on G (exploratory, moves no rung): the procedure reads %s - %d months, mean %.6f R a coin-month, t %.3f, p(t) up %.5f, '
        'p(boot) up %.5f; %d trades on %d contracts: %s' % (gp['word'], gp['n'], gp.get('mean', float('nan')), gp.get('t', float('nan')),
                                                          gp.get('p_t_up', float('nan')), gp.get('p_boot_up', float('nan')), gp['trades'], len(G), stamp()))
    log('PIT STRONG on G (exploratory): the procedure reads %s - %d months, mean %.4f R a month, t %.3f, p(t) up %.5f, p(boot) up %.5f; %d trades'
        % (gs['word'], gs['n'], gs.get('mean', float('nan')), gs.get('t', float('nan')), gs.get('p_t_up', float('nan')),
           gs.get('p_boot_up', float('nan')), gs['trades']))
    files['monthly-G.csv'] = series_csv(rows_g, xs_g)
    files['monthly-A.csv'] = series_csv(rows_a)
    # -- sensitivity of the rule's reading to V
    sens = []
    for v in V_SENS:
        Gv = sorted(k for k in listed if k not in bset and any(masks[v][k]))
        rv = rule_pass(adv3, series, funds, masks[v], hist_to, order=Gv)
        rr = monthly(rv['gate'], rv['N'], hist_to)
        sens.append(dict(word_or_short([r[2] for r in rr]), V=v, contracts=len(Gv), trades=len(rv['trades'])))
        del rv
    res['sensitivity'] = sens
    for s_ in sens:
        log('sensitivity V %.0f: %s - %d contracts, %d trades, n %d, mean %s, p(t) up %s' % (
            s_['V'], s_['word'], s_['contracts'], s_['trades'], s_['n'], s_.get('mean'), s_.get('p_t_up')))
    log('phase sensitivity done: %s' % stamp())
    # -- P: every admissible contract of L, the Boss's included
    rule_p = rule_pass(adv3, series, funds, Mv, hist_to, order=L)
    res['P_rule'] = stat_block(adv3, rule_p['trades'], to_date(rule_p['facts']))
    res['P_rule']['by_year'] = by_year(rule_p['trades'])
    files['trades-P-rule.csv'] = trade_csv(rule_p['trades'])
    del rule_p
    trim()
    log('phase P rule done: %s' % stamp())
    variants = {}
    for n in (3, 5, 7):
        sp = strong_pass(adv3, series, funds, Mv, L, hist_to, top_n=n, strong_max=n, record=(n == 3))
        blk = stat_block(adv3, sp['trades'], to_date(sp['daily']))
        blk['by_year'] = by_year(sp['trades'])
        blk['stop_buckets'] = bucket_table(sp['trades'], stop_pct, [11.1, 14.0], ['<=11.1%', '11.1-14%', '>14%'])
        ranks = {(t['coin'], t['entry']): rank_at(series, L, Mv, t['entry'], t['coin']) for t in sp['trades']}
        blk['rank_buckets'] = bucket_table(sp['trades'], lambda t, r=ranks: r[(t['coin'], t['entry'])], [3, 5], ['1-3', '4-5', '6-7'])
        if n == 3:
            blk['weakening'] = weakening(adv3, sp['trades'], series)
        variants['top%d' % n] = blk
        files['trades-P-strong-%d.csv' % n] = trade_csv(sp['trades'], ranks)
        del sp, ranks
        trim()
    res['P_strong'] = variants
    log('phase P strong done: %s' % stamp())
    # -- the Boss's 42 with the same admissibility, and the random lists
    rule_a2 = rule_pass(adv3, series, funds, Mv, hist_to, order=boss)
    strong_a2 = strong_pass(adv3, series, funds, Mv, boss, hist_to)
    res['A_admissible'] = {'rule': stat_block(adv3, rule_a2['trades'], to_date(rule_a2['facts'])),
                           'strong': stat_block(adv3, strong_a2['trades'], to_date(strong_a2['daily']))}
    del rule_a2, strong_a2
    state, draws = (SEED * 2 + 1) & M64, []
    for k in range(RANDOM_LISTS):
        idx = list(range(len(L)))
        for i in range(LIST_SIZE):
            state, r = splitmix64(state)
            j = i + ((r * (len(idx) - i)) >> 64)
            idx[i], idx[j] = idx[j], idx[i]
        syms = sorted(L[t] for t in idx[:LIST_SIZE])
        sp = strong_pass(adv3, series, funds, Mv, syms, hist_to)
        R = [t['R'] for t in sp['trades']]
        longs = [t['R'] for t in sp['trades'] if t['d'] > 0]
        draws.append((k, len(R), sum(R), sum(R) / len(R) if R else 0.0, len(longs), sum(longs)))
        del sp
        if k % 50 == 0:
            stamp()
    tot = sorted(d[2] for d in draws)
    ref_total = res['A_admissible']['strong']['total_R']
    q = lambda p: tot[min(len(tot) - 1, int(p * len(tot)))]
    res['random_lists'] = {'lists': RANDOM_LISTS, 'size': LIST_SIZE, 'pool': len(L),
                           'total_R_quantiles': {str(p): q(p) for p in (0.05, 0.25, 0.5, 0.75, 0.95)},
                           'share_total_positive': sum(x > 0 for x in tot) / len(tot),
                           'boss_42_total_R': ref_total,
                           'share_of_lists_below_boss_42': sum(x < ref_total for x in tot) / len(tot),
                           'mean_R_trade_quantiles': {str(p): sorted(d[3] for d in draws)[min(len(draws) - 1, int(p * len(draws)))]
                                                      for p in (0.05, 0.25, 0.5, 0.75, 0.95)},
                           'share_mean_R_positive': sum(d[3] > 0 for d in draws) / len(draws),
                           'trades_median': sorted(d[1] for d in draws)[len(draws) // 2]}
    files['random-lists.csv'] = 'list,trades,total_R,mean_R,long_trades,long_total_R\n' + ''.join('%d,%d,%r,%r,%d,%r\n' % d for d in draws)
    log('random lists: %s' % json.dumps(res['random_lists'], sort_keys=True))
    log('finished: %s' % stamp())
    return res, files


# ---- the checker: the map, the host, the number, the marks and the keep ------------------------------------------------------------

CAPTURES = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
BOT = 'adv3-bot.service'
PY = '/root/tz04a-env/venv/bin/python'
STATE = WORK + '/state.json'


def show(unit, *props):
    rc, so, se = sh(['systemctl', 'show', unit] + [a for p in props for a in ('-p', p)], env=dict(os.environ, TZ='UTC'))
    assert rc == 0, se
    return dict(line.split('=', 1) for line in so.splitlines() if '=' in line)


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
    checks['advisor/adv3.py hashes to the SHA-256 the instrument loads it by, ' + ADV3_SHA[:8]] = sha256_file(PRIMARY + '/advisor/adv3.py') == ADV3_SHA
    verdict('FINGERPRINT', checks)


def meminfo():
    return {k: int(v.split()[0]) * 1024 for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}


def memory_gate(first, second):
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', '/var/lib/btc-recorder', '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json', '-print', '-quit'])
    checks["H1 the recorder's manifest.json is found"] = rc == 0 and len(so.split()) == 1
    rc, so, _ = sh(['df', '-B1', '--output=source,size,avail', '/var/lib/btc-recorder'])
    src, size, avail = so.splitlines()[1].split()
    checks['H2 /dev/vda2 of 31612203008 bytes'] = (src, size) == ('/dev/vda2', '31612203008')
    rc, so, _ = sh(['grep', '-c', 'e3975b5da44c5328adf3bf3914634cd878842c73', '/var/lib/btc-recorder/runtime.jsonl'])
    checks["H2 the recorder's runtime record names e3975b5"] = rc == 0 and int(so) >= 1
    rc, so, _ = sh([PY, '-c', 'import sys; print(sys.version.split()[0])'])
    checks['H3 the venv interpreter is Python 3.12'] = rc == 0 and so.startswith('3.12.')
    units = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState') for u in CAPTURES + (BOT,)}
    for u in CAPTURES:
        checks['H4 %s active and enabled' % u] = (units[u]['ActiveState'], units[u]['UnitFileState']) == ('active', 'enabled')
    checks['H5 adv3-bot.service active, running and enabled'] = (
        (units[BOT]['ActiveState'], units[BOT]['SubState'], units[BOT]['UnitFileState']) == ('active', 'running', 'enabled'))
    checks['H6 the work tree holds nothing but logs/ and stage/'] = not os.path.exists(WORK) or set(os.listdir(WORK)) <= {'logs', 'stage'}
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
    out('MemAvailable first %d bytes, second %s, deciding %d; /dev/vda2 free %s bytes' % (
        first, 'not read' if second is None else second, final, avail))
    verdict('HOST', checks)


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


def mode_number():
    rc, so, se = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', 'CryptoTZ/', 'CryptoReports/'])
    assert rc == 0, se
    names = so.split('\n')
    for n in names:
        if n.startswith('CryptoTZ/' + NUMBER) or n.startswith('CryptoReports/' + NUMBER):
            out(n)
    verdict('NUMBER', number_reading(names))


def snapshot():
    return {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'UnitFileState') for u in CAPTURES + (BOT,)}


def mode_mark():
    os.makedirs(WORK, exist_ok=True)
    snap = snapshot()
    with open(STATE, 'x', encoding='utf-8') as f:
        f.write(json.dumps({'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'units': snap}, indent=1, sort_keys=True) + '\n')
    out('MARK', json.dumps(snap, sort_keys=True))


def still_reading(before, now):
    checks = {}
    for u in CAPTURES + (BOT,):
        checks['%s unchanged: MainPID, NRestarts, ActiveState, UnitFileState' % u] = before.get(u) == now.get(u) and now[u]['ActiveState'] == 'active'
    return checks


def mode_still():
    verdict('STILL', still_reading(json.loads(read(STATE))['units'], snapshot()))


def mode_same(a, b):
    """DETERMINISM: every file of two output directories equal by SHA-256, the same names in both."""
    fa, fb = sorted(os.listdir(a)), sorted(os.listdir(b))
    checks = {'the same %d file names' % len(fa): fa == fb}
    for f in fa:
        ha, hb = sha256_file(a + '/' + f), sha256_file(b + '/' + f) if f in fb else None
        out('%s %s %s' % (ha, hb, f))
        checks['equal ' + f] = ha == hb
    verdict('DETERMINISM', checks)


def kept_files():
    names = ['state.json', 'plan.json', 'manifest.tsv']
    for sub in ('logs', 'out-A', 'out-B'):
        for d, _s, fs in os.walk(WORK + '/' + sub):
            names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz38-work--<path with - for />, by exclusive create and
    verified whole; the branch worktree must hold nothing but its pushed HEAD."""
    wt = WORK + '/wt'
    rc, so, _ = sh(['git', '-C', wt, 'status', '--porcelain', '--ignored'])
    assert rc == 0 and so == '', 'keep: %s holds %r' % (wt, so[:400])
    head = sh(['git', '-C', wt, 'rev-parse', 'HEAD'])[1].strip()
    up = sh(['git', '-C', wt, 'rev-parse', '@{u}'])[1].strip()
    assert head and up == head, 'keep: %s at %s, upstream %r' % (wt, head, up)
    count = lambda: sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    before, copied, held = count(), 0, 0
    for rel in kept_files():
        path = WORK + '/' + rel
        h = sha256_file(path)
        dest = FORENSICS + '/tz38-work--' + rel.replace('/', '--')
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


def mode_run(name):
    """The measurement, offline: the store -> out-<name>/ . Peak memory and wall time are printed."""
    assert malloc_tune(), 'glibc refused its two settings'
    stop = start_sampler()
    adv3 = load_adv3()
    plan = json.loads(read(WORK + '/plan.json'))
    plan = {'hist_to': plan['hist_to'], 'symbols': plan['symbols']}      # the keys are the fetch's, not the run's
    hist_to = dt.date.fromisoformat(plan['hist_to'])
    assert hist_to == adv3.HISTORY_TO, 'the plan was made for another cut'
    ctx = run_prepare(adv3, plan, hist_to)
    res, files = run_measure(adv3, ctx)
    files['result.json'] = json.dumps(res, sort_keys=True, indent=1, default=str) + '\n'
    files['inputs.json'] = json.dumps({'plan_sha256': sha256_file(WORK + '/plan.json'), 'manifest_sha256': sha256_file(WORK + '/manifest.tsv'),
                                       'adv3_sha256': ADV3_SHA, 'cut': plan['hist_to'], 'declarations': {
                                           'V_MIN': V_MIN, 'V_SENS': V_SENS, 'WINDOW': WINDOW, 'SPAN': SPAN, 'MIN_COINS': MIN_COINS,
                                           'MIN_MONTHS': MIN_MONTHS, 'ALPHA': ALPHA, 'BOOT_B': BOOT_B, 'BOOT_L': BOOT_L, 'SEED': SEED,
                                           'RANDOM_LISTS': RANDOM_LISTS, 'LIST_SIZE': LIST_SIZE, 'LISTED_TO': str(LISTED_TO),
                                           'EXCLUDED_BASES': EXCLUDED_BASES}}, sort_keys=True, indent=1) + '\n'
    odir = WORK + '/out-' + name
    os.makedirs(odir)
    for fname, text in sorted(files.items()):
        with open(odir + '/' + fname, 'x', encoding='utf-8') as f:
            f.write(text)
        b = text.encode()
        out('OUT %s %d bytes %s' % (fname, len(b), sha256_bytes(b)))
    stop.set()
    out('RUN PASS: %s; the largest anonymous set sampled every 0.05 s: %d bytes' % (proc_mem(), PEAK_ANON[0]))


# ---- the self-test: the pure readings and the pipeline on synthetic contracts, each with a negative control ------------------------

def synth_rows(seed, n, start, drift=0.0, vol=0.03, volume=2.0e7):
    """n daily candles from start, a random walk of the given drift and volatility, prices to four decimals, a quote volume
    within a factor of three of `volume`; {day: (open, high, low, close, quote volume)}."""
    import random
    r = random.Random(seed)
    x, rows = 100.0, {}
    for i in range(n):
        o = x
        x *= math.exp(drift + vol * r.gauss(0, 1))
        h = max(o, x) * (1 + abs(r.gauss(0, 0.01)))
        l = min(o, x) * (1 - abs(r.gauss(0, 0.01)))
        rows[start + dt.timedelta(days=i)] = (round(o, 4), round(h, 4), round(l, 4), round(x, 4), volume * (0.5 + 2.5 * r.random()))
    return rows


def write_store(root, sym, rows, rate=0.0001, missing_months=(), funding_months=None):
    """sym's candles as the archive holds them under root: a monthly zip for each month but missing_months, whose days are
    written as daily zips instead, and a monthly funding file for each month with three settlements a day."""
    import zipfile
    base = root + '/data/futures/um/'
    head = 'open_time,open,high,low,close,volume,close_time,quote_volume,count,taker_buy_volume,taker_buy_quote_volume,ignore\n'
    line = lambda d, v: '%d,%s,%s,%s,%s,1.0,%d,%r,1,1.0,1.0,0\n' % (
        int(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc).timestamp() * 1000), v[0], v[1], v[2], v[3],
        int(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc).timestamp() * 1000) + 86399999, v[4])
    bymonth = {}
    for d, v in rows.items():
        bymonth.setdefault((d.year, d.month), []).append((d, v))

    def put(path, name, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with zipfile.ZipFile(path, 'w') as z:
            z.writestr(name, text)
    for (y, m), items in bymonth.items():
        if (y, m) in missing_months:
            for d, v in items:
                n = '%s-1d-%s' % (sym, d.isoformat())
                put('%sdaily/klines/%s/1d/%s.zip' % (base, sym, n), n + '.csv', head + line(d, v))
        else:
            n = '%s-1d-%04d-%02d' % (sym, y, m)
            put('%smonthly/klines/%s/1d/%s.zip' % (base, sym, n), n + '.csv', head + ''.join(line(d, v) for d, v in items))
        if funding_months is None or (y, m) in funding_months:
            n = '%s-fundingRate-%04d-%02d' % (sym, y, m)
            fl = ''.join('%d,8,%r\n' % (int(dt.datetime(d.year, d.month, d.day, h, tzinfo=dt.timezone.utc).timestamp() * 1000), rate)
                         for d, _v in items for h in (0, 8, 16))
            put('%smonthly/fundingRate/%s/%s.zip' % (base, sym, n), n + '.csv', 'calc_time,funding_interval_hours,last_funding_rate\n' + fl)


def mode_selftest():
    import random, tempfile, unittest.mock as mock
    adv3 = load_adv3()
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    # -- the statistics, against values computed by scipy 1.18.1 at 16 digits
    gold = [(1.7, 60, 0.04715490953428684), (-2.3, 64, 0.9876402584275776), (0.0, 30, 0.5), (3.1, 12, 0.004594998189195668),
            (2.0, 400, 0.023087972586784064)]
    ok(all(abs(t_sf(t, df) - p) <= 1e-11 * max(p, 1e-3) for t, df, p in gold), 't_sf equals scipy.stats.t.sf at five points to 1e-11')
    ok(abs(t_sf(2.2, 50) + t_sf(-2.2, 50) - 1.0) < 1e-14 and t_sf(1.0, 20) > t_sf(1.5, 20) > t_sf(3.0, 20), 't_sf is symmetric and decreasing')
    st = 0
    vec = []
    for _ in range(3):
        st, o = splitmix64(st)
        vec.append(o)
    ok(vec == [0xE220A8397B1DCDAF, 0x6E789E6AA1B965F4, 0x06C45D188009454F], "splitmix64 from state 0 gives the published outputs")
    ok(abs(probit(0.95) - 1.6448536269514722) < 1e-12 and abs(phi(1.0) - 0.8413447460685429) < 1e-14, 'probit and phi')
    ok(abs(power(0.3, 70) - 0.8065153063880648) < 1e-9 and abs(power(0.0, 70) - ALPHA) < 1e-12, 'power: the normal approximation, and alpha at no edge')
    rnd = random.Random(7)
    base = [rnd.gauss(0.0, 1.0) for _ in range(60)]
    b1, b2 = boot_p(base, B=2000), boot_p(base, B=2000)
    ok(b1 == b2 and b1 == (0.63968015992004, 0.36081959020489757), 'boot_p: deterministic, equal to an independent numpy implementation of its specification')
    pos = [x + 1.2 for x in base]
    neg = [x - 1.2 for x in base]
    rp, rn, rz = read_series(pos), read_series(neg), read_series([x - sum(base) / 60 for x in base])
    ok((rp['word'], rn['word'], rz['word']) == ('REPLICATED', 'CONTRADICTED', 'UNDECIDABLE'),
       'read_series: a clearly positive series REPLICATED, a negative CONTRADICTED, a centred one UNDECIDABLE')
    m, sd = mean_sd([1.0, 2.0, 4.0])
    ok(abs(m - 7 / 3) < 1e-15 and abs(sd - math.sqrt(7 / 3)) < 1e-12, 'mean_sd')
    # -- the months
    d0 = dt.date(2024, 1, 1).toordinal()
    S = {d0 + i: 1.0 for i in range(0, 91)}
    N = {d0 + i: 20 for i in range(0, 91)}
    rows = monthly(S, N, dt.date(2024, 3, 31))
    ok([(r[0], r[1]) for r in rows] == [(2024, 1), (2024, 2), (2024, 3)] and abs(rows[0][2] - 31 * 0.05) < 1e-12 and rows[1][3] == 20,
       'monthly: three complete months, x the sum of S / N')
    ok(len(monthly(S, N, dt.date(2024, 3, 30))) == 2, 'monthly: a month whose last day is after the cut is not counted (negative control)')
    ok(len(monthly(S, {o: 9 for o in N}, dt.date(2024, 3, 31))) == 0, 'monthly: a month with fewer than 10 coins a day on average is not counted')
    ok(monthly_sum({d0: 2.0, d0 + 40: 3.0}, rows) == [2.0, 3.0, 0.0], 'monthly_sum')
    # -- the admissibility
    ords = array('i', range(1000, 1100))
    qv = array('d', [20e6] * 100)
    f = admissible(ords, qv, 10e6)
    ok(list(f[:28]) == [0] * 28 and all(f[28:]), 'admissible: nothing before 28 candles exist, everything after at 20M against 10M')
    qv2 = array('d', qv)
    qv2[40] = 1.0
    ok(all(admissible(ords, qv2, 10e6)[28:]), 'admissible: one bad day among 28 does not move the median')
    for i in range(30, 50):
        qv2[i] = 1.0
    ok(not admissible(ords, qv2, 10e6)[55] and admissible(ords, qv2, 10e6)[85], 'admissible: a median below the floor excludes the day and recovers once the window has passed')
    ords2 = array('i', list(range(1000, 1050)) + list(range(1100, 1150)))
    ok(admissible(ords2, array('d', [20e6] * 100), 10e6)[50] == 0 and admissible(ords2, array('d', [20e6] * 100), 10e6)[80] == 1,
       'admissible: a gap in the days leaves the window too wide, so the day is not admitted')
    ok(all(admissible(ords, qv2, 0.0)), 'admissible: a v_min of 0 admits every day')
    big = array('d', [20e6 + 1000.0 * i for i in range(100)])
    base_f = admissible(ords, big, 20.5e6)
    pert = array('d', big)
    for i in range(60, 100):
        pert[i] *= 1000.0
    pf = admissible(ords, pert, 20.5e6)
    ok(list(pf[:61]) == list(base_f[:61]), 'CAUSALITY: multiplying every volume from index 60 on leaves the flags up to index 60 bit-identical')
    ok(any(pf[i] != base_f[i] for i in range(61, 100)), 'CAUSALITY negative control: the flags after index 60 do change')
    # -- the series over adv3: states, simulate and the strategy equal adv3's own on dicts
    start = dt.date(2024, 1, 1)
    syms = ['AAAUSDT', 'BBBUSDT', 'CCCUSDT', 'DDDUSDT', 'EEEUSDT', 'FFFUSDT']
    data = {s: synth_rows(11 + k, 420, start, drift=(0.004 if k % 2 == 0 else -0.004), vol=0.025) for k, s in enumerate(syms)}
    cut = start + dt.timedelta(days=419)
    series = {}
    for s_, rows_ in data.items():
        series[s_] = Series(s_, rows_)
        fill_states(adv3, series[s_], cut)
    ok(all(adv3.states({d: v[:4] for d, v in data[k].items()}, cut)[d] == States(series[k])[d] for k in syms for d in list(data[k])[::17]),
       'States over arrays equal adv3.states over a dict, on every 17th day of 6 contracts')
    ok(all(adv3.simulate({d: v[:4] for d, v in data[k].items()}, lambda d: 0.0001, start, cut)[:2] ==
           adv3.simulate(Candles(series[k]), lambda d: 0.0001, start, cut)[:2] for k in syms), 'simulate over Candles equals simulate over a dict (trades and daily R), 6 contracts')
    funds = {s_: (lambda d: 0.0001) for s_ in syms}
    cs_dict = {s_: {d: v[:4] for d, v in data[s_].items()} for s_ in syms}
    st_dict = {s_: adv3.states(cs_dict[s_], cut) for s_ in syms}
    with patched(adv3, COINS=tuple(syms)):
        ref_t, ref_d, ref_o = adv3.simulate_strong(cs_dict, st_dict, funds, start, cut)
    mine = strong_pass(adv3, series, funds, {}, syms, cut)
    ok(len(ref_t) + len(ref_o) == len(mine['trades']) and ref_d == {dt.date.fromordinal(o): x for o, x in mine['daily'].items()} and len(ref_t) > 0,
       'strong_pass equals simulate_strong over dicts: the same trades and the same daily R (%d trades)' % len(mine['trades']))
    ok(adv3.COINS == tuple(c for c in adv3.COINS) and len(adv3.COINS) == 42 and adv3.TOP_N == 3 and adv3.STRONG_MAX == 3, 'adv3 is restored after the passes: 42 coins, TOP_N 3, STRONG_MAX 3')
    try:
        with patched(adv3, TOP_N=9):
            raise RuntimeError('x')
    except RuntimeError:
        pass
    ok(adv3.TOP_N == 3, 'patched restores an attribute when the block raises')
    # -- the gate: no entry on a day the contract is not admissible, a position held across such days
    s0 = series['AAAUSDT']
    th_free, _dh, _ph = adv3.simulate(Candles(s0), funds['AAAUSDT'], start, cut)
    first = th_free[0]['entry']
    j = s0.index(first)
    closed = array('b', [1] * len(s0.ords))
    closed[j] = 0
    with gated(adv3, s0, closed):
        th_g, _dh, _ph = adv3.simulate(Candles(s0), funds['AAAUSDT'], start, cut)
    ok(all(t['entry'] != first for t in th_g) and len(th_g) >= 1, 'gated: the entry of the first trade is not made on the day the mask closes, later ones are')
    ok(th_free[0]['entry'] == first, 'gated negative control: with no mask the entry is made on that day')
    gap = array('b', [1] * len(s0.ords))
    for i in range(j + 1, min(j + 6, len(gap))):
        gap[i] = 0
    with gated(adv3, s0, gap):
        th_h, _d2, _p2 = adv3.simulate(Candles(s0), funds['AAAUSDT'], start, cut)
    ok(th_h[0]['entry'] == first and th_h[0]['R'] == th_free[0]['R'], 'gated: a position open when the mask closes is held to its ordinary exit, with the same R')
    # -- a contract whose data ends: flat on its last day, which closes the position and frees the slot
    lone = Series('TTTUSDT', synth_rows(21, 200, start, drift=0.012, vol=0.01))
    cut_t = dt.date.fromordinal(lone.ords[-1])
    fill_states(adv3, lone, cut_t)
    f_t = {'TTTUSDT': lambda d: 0.0}
    lone.ended = True
    ended_run = strong_pass(adv3, {'TTTUSDT': lone}, f_t, {}, ['TTTUSDT'], cut_t + dt.timedelta(days=30))
    lone.ended = False
    open_run = strong_pass(adv3, {'TTTUSDT': lone}, f_t, {}, ['TTTUSDT'], cut_t + dt.timedelta(days=30))
    ok(len(ended_run['trades']) >= 1 and ended_run['trades'][-1]['why'] == 'signal' and ended_run['trades'][-1]['exit'] == cut_t,
       'ended: a contract whose data ends closes its position on its last day, at the close, as a signal exit')
    ok(len(open_run['trades']) >= 1 and open_run['trades'][-1]['why'] == 'open at the history cut' and 'exit' not in open_run['trades'][-1]
       and open_run['trades'][-1]['end'] == cut_t, 'ended negative control: without the flag the position is carried to the end of the data and closed there as at the cut')
    # -- the rule pass and its day counts
    rp_ = rule_pass(adv3, series, funds, {}, cut)
    ok(rp_['N'][series['AAAUSDT'].ords[200]] == 6 and rp_['N'].get(series['AAAUSDT'].ords[50], 0) == 0, 'rule_pass: N counts the contracts that have a signal that day (6 late, 0 before the lookback)')
    mk = {s_: admissible(series[s_].ords, series[s_].qv, 1e12) for s_ in syms}
    ok(not rule_pass(adv3, series, funds, mk, cut)['trades'] and not any(rule_pass(adv3, series, funds, mk, cut)['N'].values()),
       'rule_pass with nothing admissible opens no trade and counts no coin')
    ends = [t for t in rp_['trades'] if t['why'] == 'open at the history cut']
    ok(abs(sum(rp_['facts'].values()) - sum(rp_['gate'].values()) - sum(adv3.COST * series[t['coin']].c[-1] / t['U'] for t in ends)) < 1e-9 and len(ends) >= 1,
       'rule_pass: the gate series is the facts series less the exit cost of each position closed at the end of data (%d of them)' % len(ends))
    # -- tables
    tr = [{'R': -1.0, 'U': 1.0, 'E': 20.0, 'd': 1, 'coin': 'X'}, {'R': 2.0, 'U': 2.4, 'E': 20.0, 'd': -1, 'coin': 'Y'},
          {'R': 5.0, 'U': 3.0, 'E': 20.0, 'd': 1, 'coin': 'Z'}]
    bt = bucket_table(tr, stop_pct, [11.1, 14.0], ['<=11.1%', '11.1-14%', '>14%'])
    ok([b['trades'] for b in bt] == [1, 1, 1] and bt[0]['total_R'] == -1.0 and bt[2]['mean_R'] == 5.0, 'bucket_table: stop distances 5 %, 12 %, 15 % land in three buckets')
    ok(bucket_table(tr, lambda t: 11.1, [11.1, 14.0], ['a', 'b', 'c'])[0]['trades'] == 3, 'bucket_table: an edge belongs to the lower bucket')
    day300 = dt.date.fromordinal(series['AAAUSDT'].ords[300])
    ranks = sorted(rank_at(series, syms, {}, day300, k) for k in syms if series[k].sig[300] in (1, -1) and series[k].U[300] == series[k].U[300])
    ok(ranks == list(range(1, len(ranks) + 1)) and len(ranks) >= 2, 'rank_at: the active contracts of a day take the places 1..n once each (%d active)' % len(ranks))
    # -- weakening on a constructed trade
    fake = Series('QQQUSDT', synth_rows(5, 40, start))
    n = len(fake.ords)
    fake.sig, fake.sm = array('b', [1] * n), array('b', [4] * 10 + [2] * 30)
    fake.z, fake.U = array('d', [1.5] * n), array('d', [1.0] * n)
    entry = dt.date.fromordinal(fake.ords[5])
    path = array('d')
    for k in range(6, 20):
        path.extend((float(fake.ords[k]), 0.1 * (k - 5)))
    t_ = {'coin': 'QQQUSDT', 'd': 1, 'entry': entry, 'exit': dt.date.fromordinal(fake.ords[19]), 'why': 'signal', 'R': 2.0, 'U': 1.0, 'path': path}
    w = weakening(adv3, [t_], {'QQQUSDT': fake})
    r_at = path[2 * 4 + 1]
    want = 2.0 - (r_at - adv3.COST * fake.c[10] / 1.0)
    ok(w['entered_with_four_signs'] == 1 and w['weakened'] == 1 and abs(w['mean_hold_minus_exit'] - want) < 1e-12 and w['share_hold_better'] == 1.0,
       'weakening: the first close with the sum at +/-2 is day 10; the R after it is read against the R of leaving there')
    t_['entry'] = dt.date.fromordinal(fake.ords[15])
    ok(weakening(adv3, [t_], {'QQQUSDT': fake})['entered_with_four_signs'] == 0, 'weakening negative control: a trade entered with two signs is not read')
    # -- the store: candle_rows equals adv3.archive_candles, a gap month read from daily files
    with tempfile.TemporaryDirectory() as tmp:
        rows_ = synth_rows(3, 150, dt.date(2024, 1, 1))
        write_store(tmp, 'ZZZUSDT', rows_, missing_months=((2024, 3),))
        old_store, old_get = globals()['STORE'], adv3.get
        globals()['STORE'] = tmp
        adv3.get = local_get_for(adv3)
        try:
            mine_c = candle_rows(adv3, 'ZZZUSDT', dt.date(2024, 5, 20))
            theirs_c = adv3.archive_candles('ZZZUSDT', dt.date(2024, 5, 20), SerialPool)
        finally:
            globals()['STORE'], adv3.get = old_store, old_get
        ok(len(mine_c) == 141 and {d: v[:4] for d, v in mine_c.items()} == theirs_c and all(mine_c[d][4] == rows_[d][4] for d in mine_c),
           'candle_rows equals adv3.archive_candles day for day over a store with a gap month read from daily files, and carries the quote volume')
    # -- G-EQUAL on a synthetic store: the pipeline over six contracts equals adv3.history()
    with tempfile.TemporaryDirectory() as tmp:
        for s_, rows_ in data.items():
            write_store(tmp, s_, rows_, funding_months={(2024, m) for m in range(1, 13)})
        old_store, old_get = globals()['STORE'], adv3.get
        globals()['STORE'] = tmp
        adv3.get = local_get_for(adv3)
        try:
            with patched(adv3, COINS=tuple(s_[:-4] for s_ in syms), HISTORY_TO=cut, ARCHIVE_FROM=start, FUNDING_TO=(2024, 9)):
                ref = adv3.history()
                ser2, fun2 = {}, {}
                for s_ in syms:
                    ser2[s_] = Series(s_, candle_rows(adv3, s_, cut))
                    fill_states(adv3, ser2[s_], cut)
                    fun2[s_] = funding_for(adv3, s_, ser2[s_], cut)[0]
                ra = rule_pass(adv3, ser2, fun2, {}, cut, order=syms)
                sa = strong_pass(adv3, ser2, fun2, {}, syms, cut)
                got = facts_shape(adv3, ra, sa)
        finally:
            globals()['STORE'], adv3.get = old_store, old_get
        ok(got['base'] == ref['base'] and got['strong'] == ref['strong'] and got['base']['trades'] > 0 and got['strong']['trades'] > 0,
           'G-EQUAL on a synthetic store: both blocks of the pipeline equal adv3.history() exactly (%d and %d trades)' % (got['base']['trades'], got['strong']['trades']))
        ok(got['base']['total_R'] != 0 and ref['base'] != {}, 'G-EQUAL negative control: a different cut gives a different block')
    # -- the arena: arrays written to one file and read back as views give the same trades, the file left no trace
    with tempfile.TemporaryDirectory() as tmp:
        for s_, rows_ in data.items():
            write_store(tmp, s_, rows_, funding_months={(2024, m) for m in range(1, 13)})
        old_store, old_get = globals()['STORE'], adv3.get
        globals()['STORE'] = tmp
        adv3.get = local_get_for(adv3)
        plan_ = {'symbols': syms}
        try:
            with patched(adv3, COINS=tuple(s_[:-4] for s_ in syms), HISTORY_TO=cut, ARCHIVE_FROM=start, FUNDING_TO=(2024, 9)):
                ser_a, fun_a, msk_a = load_all(adv3, plan_, cut, Arena(tmp + '/arena.bin'))
                ser_b, fun_b, msk_b = load_all(adv3, plan_, cut)
                ra, rb = rule_pass(adv3, ser_a, fun_a, msk_a[V_MIN], cut), rule_pass(adv3, ser_b, fun_b, msk_b[V_MIN], cut)
                sa_, sb_ = strong_pass(adv3, ser_a, fun_a, msk_a[V_MIN], syms, cut), strong_pass(adv3, ser_b, fun_b, msk_b[V_MIN], syms, cut)
                gone = not os.path.exists(tmp + '/arena.bin')
        finally:
            globals()['STORE'], adv3.get = old_store, old_get
        ok(isinstance(ser_a['AAAUSDT'].c, memoryview) and isinstance(ser_b['AAAUSDT'].c, array) and gone,
           'arena: the arrays are views into the map after the seal, the file is gone from the disk, the plain load keeps arrays')
        ok(ra['trades'] == rb['trades'] and ra['facts'] == rb['facts'] and ra['N'] == rb['N'] and sa_['trades'] == sb_['trades'] and sa_['daily'] == sb_['daily']
           and len(ra['trades']) > 0 and all(list(msk_a[V_MIN][k]) == list(msk_b[V_MIN][k]) for k in syms),
           'arena: the rule and the strategy over the views equal those over the arrays - trades, daily R, day counts and flags (%d and %d trades)' % (len(ra['trades']), len(sa_['trades'])))
    # -- the request function: the User-Agent, 404, a retried 429, a refusal
    class Resp:
        def __init__(self, body):
            self.body = body

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return self.body
    seen = []

    def fake_open(req, timeout=0):
        seen.append(req.get_header('User-agent'))
        step = len(seen)
        if 'gone' in req.full_url:
            raise urllib.error.HTTPError(req.full_url, 404, 'nf', {}, None)
        if 'busy' in req.full_url and step < 3:
            raise urllib.error.HTTPError(req.full_url, 429, 'busy', {}, None)
        if 'denied' in req.full_url:
            raise urllib.error.HTTPError(req.full_url, 403, 'no', {}, None)
        return Resp(b'body')
    with mock.patch('urllib.request.urlopen', fake_open), mock.patch('time.sleep', lambda s: None):
        r1, r2 = request('https://x/ok'), request('https://x/gone')
        seen.clear()
        r3 = request('https://x/busy')
        try:
            request('https://x/denied')
            refused = False
        except RuntimeError:
            refused = True
    ok(r1 == b'body' and r2 is None and r3 == b'body' and refused and set(seen) == {UA}, 'request: served, 404 as None, a 429 retried, a 403 raised, and every request names its User-Agent')
    # -- the plan: gap months get a daily listing, the funding of the cut month is left out
    calls = []

    def fake_list(prefix, delimiter='/'):
        calls.append(prefix)
        if prefix.startswith(KL):
            return [], [KL + 'XXXUSDT/1d/XXXUSDT-1d-2026-%02d.zip' % m for m in (5, 6, 8, 9)] + [KL + 'XXXUSDT/1d/XXXUSDT-1d-2026-05.zip.CHECKSUM']
        if prefix.startswith(FU):
            return [], [FU + 'XXXUSDT/XXXUSDT-fundingRate-2026-%02d.zip' % m for m in (5, 6, 8, 9, 10)]
        if prefix.endswith('2026-07'):
            return [], [KD + 'XXXUSDT/1d/XXXUSDT-1d-2026-07-%02d.zip' % d for d in (30, 31)]
        return [], [KD + 'XXXUSDT/1d/XXXUSDT-1d-2026-10-%02d.zip' % d for d in (1, 27, 28, 30)]
    old_list = globals()['s3_list']
    globals()['s3_list'] = fake_list
    try:
        keys_, n_calls = plan_symbol('XXXUSDT', dt.date(2026, 10, 27), (2026, 9))
    finally:
        globals()['s3_list'] = old_list
    ok(sum('/monthly/klines/' in k for k in keys_) == 4 and sum('/daily/klines/' in k for k in keys_) == 4 and sum('/fundingRate/' in k for k in keys_) == 4
       and not any(k.endswith('10-28.zip') or k.endswith('10-30.zip') for k in keys_) and n_calls == 4,
       'plan_symbol: 4 monthly files, the daily files of the July gap and of October up to the cut (28 and 30 left out), funding to September only, 4 listing calls')
    # -- the host gate against stand-ins for the machine, each reading with a negative control
    def host_run(mem=(200_000_000, None), avail=8_000_000_000, active='active', manifest=True, size='31612203008', tree=False):
        reads = iter(mem)

        def f_sh(args, **kw):
            if args[0] == 'find':
                return 0, ('/var/lib/btc-recorder/2026/manifest.json\n' if manifest else ''), ''
            if args[0] == 'df':
                return 0, 'Filesystem Size Avail\n/dev/vda2 %s %d\n' % (size, avail), ''
            if args[0] == 'grep':
                return 0, '2\n', ''
            return 0, '3.12.3\n', ''
        f_show = lambda unit, *p: {'MainPID': '5', 'NRestarts': '0', 'ActiveState': active, 'SubState': 'running', 'UnitFileState': 'enabled'}
        old = {k: globals()[k] for k in ('sh', 'show', 'meminfo', 'out')}
        old_exists, old_listdir, old_sleep = os.path.exists, os.listdir, time.sleep
        globals().update(sh=f_sh, show=f_show, meminfo=lambda: {'MemAvailable': next(reads)}, out=lambda *a: None)
        os.path.exists = lambda p: True if p == WORK else old_exists(p)
        os.listdir = lambda p: ['x'] if (p == WORK and tree) else ['logs', 'stage'] if p == WORK else old_listdir(p)
        time.sleep = lambda s: None
        try:
            mode_host()
            return True
        except Failed:
            return False
        finally:
            globals().update(old)
            os.path.exists, os.listdir, time.sleep = old_exists, old_listdir, old_sleep
    ok(host_run(), 'host: every reading passes on a stand-in that is the capture host with 200 MB available and 8 GB free')
    ok(host_run(mem=(100_000_000, 200_000_000)), 'host: a first memory read below the floor is read again and the second decides (pass)')
    ok(not host_run(mem=(100_000_000, 110_000_000)), 'host negative control: both memory reads below the floor fail')
    ok(not host_run(avail=7_000_000_000), 'host negative control: free space below the floor fails')
    ok(not host_run(active='failed'), 'host negative control: a capture unit that is not active fails')
    ok(not host_run(manifest=False), 'host negative control: no recorder manifest, so not the capture host, fails')
    ok(not host_run(size='1'), 'host negative control: another filesystem fails')
    ok(not host_run(tree=True), 'host negative control: a tree of an earlier run beside logs/ and stage/ fails')
    # -- the kept files and the determinism reading, on a temporary work tree
    with tempfile.TemporaryDirectory() as tmp:
        old_work = globals()['WORK']
        globals()['WORK'] = tmp
        try:
            for sub in ('logs', 'out-A', 'out-B'):
                os.makedirs(tmp + '/' + sub)
            for rel in ('state.json', 'plan.json', 'manifest.tsv', 'logs/01-selftest.log', 'out-A/result.json', 'out-B/result.json', 'arena.bin'):
                with open(tmp + '/' + rel, 'w') as f:
                    f.write('same bytes')
            kept = kept_files()
            same_ok, same_bad = True, False
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    mode_same(tmp + '/out-A', tmp + '/out-B')
            except Failed:
                same_ok = False
            with open(tmp + '/out-B/result.json', 'w') as f:
                f.write('changed')
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    mode_same(tmp + '/out-A', tmp + '/out-B')
            except Failed:
                same_bad = True
        finally:
            globals()['WORK'] = old_work
        ok(kept == ['logs/01-selftest.log', 'manifest.tsv', 'out-A/result.json', 'out-B/result.json', 'plan.json', 'state.json'],
           'kept_files: the logs, the state, the plan, the manifest and both outputs, and not the arena')
        ok(same_ok and same_bad, 'mode_same: equal directories pass, a changed file fails (negative control)')
    # -- the checker's pure readings
    mp = ('**Revision string:** `%s`\n| `A1` — x | `229a944f2d51` |\n### Fingerprint table\n| path | a |\n| `a.py` | 3 | 1,234 | frozen | `%s` |\n'
          '| `b.md` | — | — | reported | self |\n\n## 1. next\n') % (MAP_REV, 'ab' * 32)
    rv, an, rw = parse_map(mp)
    ok(rv == MAP_REV and an == {'A1': '229a944f2d51'} and rw == [('a.py', 3, 1234, 'frozen', 'ab' * 32), ('b.md', None, None, 'reported', None)], 'parse_map reads the revision, the anchors and the rows')
    ok(all(number_reading(['CryptoTZ/' + TZ_FILE.split('/')[1], 'CryptoTZ/TZ-37-x.md']).values()) and
       not all(number_reading(['CryptoTZ/' + TZ_FILE.split('/')[1], 'CryptoTZ/TZ-38-other.md']).values()) and
       not all(number_reading([TZ_FILE, 'CryptoReports/TZ-38-adv3-pit-validation-report.md']).values()), 'number_reading: one file passes, a second file or a report fails')
    global MEM_FLOOR
    old_floor, MEM_FLOOR = MEM_FLOOR, 100
    ok(memory_gate(150, None) == (True, 150) and memory_gate(50, 120) == (True, 120) and memory_gate(50, 60) == (False, 60) and memory_gate(50, None) == (False, 50),
       'memory_gate: the second read decides where the first was below the floor')
    MEM_FLOOR = old_floor
    snap = {u: {'MainPID': '1', 'NRestarts': '0', 'ActiveState': 'active', 'UnitFileState': 'enabled'} for u in CAPTURES + (BOT,)}
    moved = {u: dict(v) for u, v in snap.items()}
    moved[BOT]['MainPID'] = '2'
    ok(all(still_reading(snap, snap).values()) and not all(still_reading(snap, moved).values()), 'still_reading: equal passes, a moved MainPID fails')
    print('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz38-adv3-pit-validation.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'probe': mode_probe, 'fetch': mode_fetch,
             'mark': mode_mark, 'still': mode_still, 'keep': mode_keep, 'selftest': mode_selftest, 'equal': mode_equal}
    try:
        if mode == 'plan':
            mode_plan(load_adv3().HISTORY_TO)
        elif mode == 'run':
            assert len(rest) == 1 and re.fullmatch(r'[AB]', rest[0]), 'run A|B'
            mode_run(rest[0])
        elif mode == 'same':
            assert not rest
            mode_same(WORK + '/out-A', WORK + '/out-B')
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
