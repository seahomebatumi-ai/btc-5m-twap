"""TZ-04a shared constants, extended by TZ-05a.

Every value here is fixed by CryptoTZ/TZ-04a-market-recorder-corrected.md or, for the Tier C
and SNTP rows, by CryptoTZ/TZ-05a-quote-capture-deploy.md. Nothing in this file is a tuning
knob: the two resource floors are the exact byte counts from TZ-04a section 4, the window is
the exact span from that same section, and the Tier C checkpoints are the exact seven values
from TZ-05a section 3.
"""

# Capture root. Outside the repository by design (TZ-04a section 4), so no capture can reach
# git history.
ROOT = "/var/lib/btc-recorder"
SERIES = "btc-updown-5m"

# Interval geometry. For an interval opening at T0 the window is [T0 - 90, T0 + 330].
INTERVAL_S = 300
PRE_S = 90
POST_S = 330

# TZ-04a section 4, "Resource floors. Two independent stops, whichever is reached first."
FREE_SPACE_FLOOR_BYTES = 2_000_000_000
SELF_CAP_BYTES = 4_000_000_000

# TZ-04a section 6, V6. The venue's crypto taker delay is 50 ms.
CLOCK_OFFSET_LIMIT_MS = 50.0

# TZ-05a section 5, R-b. An SNTP reply whose transmit timestamp sits further than this from
# the host clock is rejected at reception and never becomes an offset.
SNTP_MAX_SKEW_S = 86_400

# Endpoints. The CLOB websocket URL and the resolution endpoint are read from the current
# Polymarket documentation at implementation time (TZ-04a section 3) and are reported verbatim.
RTDS_URL = "wss://ws-live-data.polymarket.com"
CLOB_WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
GAMMA_MARKET_BY_SLUG = "https://gamma-api.polymarket.com/markets/slug/{slug}"
# TZ-05a section 3. The CLOB REST order-book endpoint, read on 2026-09-12 from
# https://docs.polymarket.com/api-reference/market-data/get-order-book, which gives the method
# and path as `GET /book`, the production host as `https://clob.polymarket.com`, and `token_id`
# as the one required query parameter. Public and unauthenticated: this is a read, and the
# recorder sends no header beyond its User-Agent.
CLOB_BOOK_BY_TOKEN = "https://clob.polymarket.com/book?token_id={token_id}"

USER_AGENT = "btc-5m-twap-recorder/TZ-04a"

# RTDS application-level heartbeat: the text frame PING every 5 seconds.
RTDS_PING_S = 5
# CLOB application-level heartbeat: the text frame PING every 10 seconds.
CLOB_PING_S = 10

# Tier A subscriptions. topic -> (filters, stream name). `filters` is the exact compact JSON
# form with one lowercase symbol and no spaces, as TZ-04a section 3 requires.
TIER_A = {
    "crypto_prices_twap_sixty":  ('{"symbol":"btc/usd"}',  "twap60"),
    "crypto_prices_twap_thirty": ('{"symbol":"btc/usd"}',  "twap30"),
    "crypto_prices_chainlink":   ('{"symbol":"btc/usd"}',  "chainlink"),
    "crypto_prices":             ('{"symbol":"btcusdt"}',  "binance"),
}

# Tier C subscriptions are not subscriptions: TZ-05a section 3 fixes seven checkpoints, given
# as seconds remaining in the interval, and one order-book read per token id at each of them.
QUOTE_TAUS = (240, 180, 120, 90, 60, 30, 10)
TOKENS_PER_MARKET = 2
QUOTE_READS_PER_INTERVAL = len(QUOTE_TAUS) * TOKENS_PER_MARKET
QUOTES_STEM = "quotes"

# The TZ names S1 and S3 as the streams whose continuity decides `complete`.
S1_STREAM = "twap60"
S3_STREAM = "chainlink"

STREAM_FILES = ["twap60", "twap30", "chainlink", "binance"]

# NTP servers sampled for V6. The first is the host's own configured server.
NTP_SERVERS = ["108.61.73.243", "pool.ntp.org"]
NTP_SAMPLE_S = 60


def intervals_for(ts):
    """Every interval whose window [T0-90, T0+330] contains wall-clock second `ts`.

    The window is 420 s long on a 300 s grid, so a frame lands in at most two intervals.
    """
    base = int(ts // INTERVAL_S) * INTERVAL_S
    return [t0 for t0 in (base - INTERVAL_S, base, base + INTERVAL_S)
            if t0 - PRE_S <= ts <= t0 + POST_S]


def quote_checkpoint_epoch(t0, tau):
    """The wall-clock second at which the `tau`-seconds-remaining checkpoint of `t0` is read.

    TZ-05a section 3 states both forms: tau in {240, 180, 120, 90, 60, 30, 10} is t in
    {60, 120, 180, 210, 240, 270, 290}. Only one of them is implemented, here.
    """
    return t0 + INTERVAL_S - tau


def quote_checkpoints_ahead(t0, now):
    """The checkpoints of `t0` still ahead of `now`, in the order they are read.

    A process that starts mid-interval cannot read a checkpoint whose instant has already
    passed. That checkpoint is skipped: TZ-05a section 3 forbids a read being issued into
    another checkpoint's slot, and a checkpoint that did not happen is never filled.
    """
    return [(tau, quote_checkpoint_epoch(t0, tau))
            for tau in QUOTE_TAUS if now <= quote_checkpoint_epoch(t0, tau)]


def interval_dir(t0):
    return "%s/%s/%d" % (ROOT, SERIES, t0)


def slug_for(t0):
    return "%s-%d" % (SERIES, t0)
