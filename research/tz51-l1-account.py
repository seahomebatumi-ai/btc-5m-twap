#!/usr/bin/env python3
"""TZ-51 - L1's account, its session key and one order's round trip at the minimum size, from the live host in Sofia.
The bot's Deposit Wallet is the Boss's; its owner key stays in his MetaMask. This file makes a session key on the live
host, which can trade and cannot withdraw, has the Boss authorize it by his own signature through the signing page,
docs/l1-sign.html, has him approve the wallet's pUSD to the venue's two exchanges at 1 pUSD each where it is short,
and proves one order's round trip with the key through the venue's official client, polymarket-client, installed at
pinned versions and hashes into /root/l1-env. It pins the bot's Telegram chat and reports there.

TZ-50 ran the same steps and BLOCKED at the Boss's terminal: its Tty opened /dev/tty with "r+" in text mode, whose
buffered random access needs a seekable file, and a terminal is never one (map section 7 item 189). This file opens
the terminal as two streams, one to read and one to write, and its self-tests run every one of the Boss's modes that
asks him anything at a real pseudo-terminal - their /dev/tty a terminal, as sshd gives `ssh -t`, their log a pipe -
never through a stand-in alone.

On the capture host, from /root/tz51-work, under /root/tz04a-env:
    fingerprint       map section 0 against the primary checkout
    number            CANON hard rule 2: of the number TZ-51, this TZ's file alone under CryptoTZ/, no report
    refs              origin's refs by kind; no branch of this TZ yet
    room              the capture's room and its margin (map section 7 item 175); no threshold
    methods LABEL     G-SSH K6: the methods the live host's sshd offers root, read from outside
    scratch OWN       the UUID directories beside this session's own, each named live or earlier
    reclaim TREE...   section 9: the work tree's files into the forensic store
On the live host, from /root/tz51-work, under its system python3 (the standard library alone):
    host LABEL        the live host gate and the facts L1 starts from; exit 1 where the gate fails
    geoblock          G-GEO over IPv4 alone; exit 1 where blocked or unread
    sshd              G-SSH K1 to K5: TZ-49's drop-in and sshd's configuration in force; exit 4 on FAIL
    page              G-PAGE: the signing page as GitHub Pages serves it, byte for byte; exit 4 on FAIL
    wheels            G-ENV's first half: the 35 pinned wheels from PyPI, each by its size and SHA-256
    secrets           the Boss, at his terminal: the bot's Telegram token, the owner's Relayer API key and address
    bosskey           the Boss, at his terminal: his own SSH public key for root, or none
    tg-probe          G-TG's first check: the bot's getMe
    find-chat         G-TG's second: the one private chat that sent /start, pinned
    tg-report         G-TG's third: the round trip's report, sent to that chat
On the live host, from /root/tz51-work, under /root/l1-env/bin/python (the venue's client):
    env               G-ENV's second half: the 34 distributions installed, each at its pin, every installed file at
                      its RECORD's SHA-256, and the client's terms
    key               G-KEY: the session key, made once, never printed
    authorize         G-AUTH, the Boss at his terminal: the owner's signature from MetaMask, its submission and
                      the key's registration; exit 4 on FAIL
    approve           G-APPROVE, the Boss at his terminal: where the wallet's pUSD allowance to either exchange is
                      under one order's cost, the owner's signature approving 1 pUSD to each such; exit 4 on FAIL
    revoke            the Boss's stop of the order path: the same flow, revoking the key; not run by TZ-51
    ready             G-READY: the account read through the session key; exit 4 on FAIL
    roundtrip         G-RT: one post-only order at the minimum size placed, read, cancelled and read; exit 4 on FAIL
    sdk-selftest      the client's flows against loopback stand-ins of the relayer, the CLOB and gamma
On either host:
    selftest          every rule of this file that needs no client, on literals, temporary trees and loopback servers

IPv4 alone, in this process (map section 7 item 181): every network socket it opens is AF_INET, every name is
resolved in AF_INET alone, and its audit hook refuses an AF_INET6 socket and a lookup in any other family; the
client's modes resolve through a wrapper that asks AF_INET of every lookup. An AF_UNIX socket is let through in the
client's modes alone - asyncio's own self-pipe - and reaches no network. No mode prints to its log a key, a token, an
address of the bot's wallets or keys, a transaction hash or an order's id, and none reads or prints a price or size of
any book; what the Boss must check before he signs - the addresses - goes to his terminal alone.

Written for CryptoTZ/TZ-51-l1-account-round-trip-rerun.md. The TZ is the specification.
"""

import asyncio
import base64
import datetime
import getpass
import hashlib
import http.client
import http.server
import json
import os
import re
import resource
import shutil
import socket
import ssl
import struct
import subprocess
import sys
import threading
import time
import types
import urllib.parse

if not __debug__:
    sys.stderr.write("tz51: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

PYFILE = "tz51-l1-account.py"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-20-b"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "6ac6e10aeabc", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 64, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-51-"
OWN_TZ = "CryptoTZ/TZ-51-l1-account-round-trip-rerun.md"
BRANCH = "tz-51-l1-account-round-trip-rerun"

PRIMARY = "/root/btc-5m-twap"
WORK = "/root/tz51-work"
WT = WORK + "/wt"
TMP = WORK + "/selftest-tmp"
WHEELS = WORK + "/wheels"
FORENSICS = "/root/btc-forensics"
RB = "/var/lib/btc-rewardbook"
RB_ARCHIVE_SVC = "btc-rewardbook-archive.service"
ARCHIVE_READS, ARCHIVE_WAIT_S = 30, 60
CAPTURE_MARK = "/var/lib/btc-recorder"     # map section 6, host identity: on the capture host alone
PROTECTED = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook", RB,
             "/var/lib/btc-rewardbook-archive", "/var/lib/btc-pairbook-archive", "/var/lib/adv3-bot", "/etc/adv3-bot")
LIVE_HOSTNAME = "vs-2348"                  # the host name's first label; the rest is its provider's domain
LIVE_HOST_KEY = ("ssh-ed25519", "SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw")   # TZ-47 report section 2.2
EXECUTOR_KEY = ("ssh-ed25519", "SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo")   # root's key since TZ-47
LIVE_ALIAS = "live-host"                    # root's ~/.ssh/config alias on the capture host; it alone holds the address
HOST_KEY_DIR = "/etc/ssh"
CAPTURE_DISK = "/var/lib"
LIVE_DISK = "/"
IPV4 = re.compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
ADDRESS = re.compile(r"0x[0-9a-fA-F]{40}")
ZERO_ADDRESS = "0x" + "0" * 40

UA = "btc-5m-twap-tz51"
HEADERS = (("User-Agent", UA), ("Accept", "application/json"))
GEO_HOST, GEO_PATH = "polymarket.com", "/api/geoblock"
CLOB_HOST = "clob.polymarket.com"
RELAYER_HOST = "relayer-v2.polymarket.com"
GAMMA_HOST = "gamma-api.polymarket.com"
RPC_HOST = "polygon.drpc.org"            # the client's own Polygon RPC: the wallet's collateral read on chain
BALANCE_OF = "70a08231"                  # balanceOf(address)
ALLOWANCE_OF = "dd62ed3e"                # allowance(address,address)
APPROVE_SEL = "095ea7b3"                 # approve(address,uint256)
PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"                 # the client's collateral_token
EXCHANGES = (("c", "0xE111180000d2663C0091e4f400237545B87B996B"),   # standard_exchange: a CTF market's orders
             ("v", "0xe3333700cA9d93003F00f0F71f8515005F6c00Aa"))   # exchange_v3: a Protocol V2 market's orders
V2_RESERVED = ((1 << 64) - 1) << 40      # the client's _V2_RESERVED_BITS_MASK: all zero in a V2 position ID
APPROVE_METADATA = "btc-5m-twap TZ-51 approvals"
TG_HOST = "api.telegram.org"
PAGES_HOST, PAGE_PATH = "seahomebatumi-ai.github.io", "/btc-5m-twap/l1-sign.html"
PYPI_HOST = "files.pythonhosted.org"
TIMEOUT_S, READ_MAX = 15, 4194304
TRIES, TRY_GAP_S = 3, 30
PAGE_TRIES = 20                # the page read over ten minutes: GitHub Pages' first build after it is turned on

SSHD_DROPIN = "/etc/ssh/sshd_config.d/00-btc-5m-twap.conf"
SSHD_SHA256 = "94fff8f1f044b31d393eecf24700dabc5b7316c70a37d0f3984cbc5957563624"   # TZ-49's SSHD_TEXT
SSHD_IN_FORCE = (("passwordauthentication", "no"), ("kbdinteractiveauthentication", "no"),
                 ("permitrootlogin", "without-password"), ("pubkeyauthentication", "yes"))
METHODS_ONLY = ["publickey"]
AUTHORIZED_KEYS = "/root/.ssh/authorized_keys"
BOSS_KEY_TYPES = ("ssh-ed25519", "ecdsa-sha2-nistp256", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp521",
                  "sk-ssh-ed25519@openssh.com", "ssh-rsa")
RSA_MIN_BITS = 3072

# ---- L1's files: credentials under /etc/l1-bot, its record under /var/lib/l1-bot, its client under /root/l1-env --

L1_ETC = "/etc/l1-bot"
SESSION_KEY_FILE = L1_ETC + "/session-key"
RELAYER_FILE = L1_ETC + "/relayer-key"
TG_TOKEN_FILE = L1_ETC + "/telegram-token"
CHAT_FILE = L1_ETC + "/chat-id"
L1_VAR = "/var/lib/l1-bot"
ACCOUNT_FILE = L1_VAR + "/account.json"
RT_RECORD = re.compile(r"tz51-roundtrip-([123])\.json")   # one record a run, under L1_VAR; three runs at most
L1_ENV = "/root/l1-env"
SECRETS = (SESSION_KEY_FILE, RELAYER_FILE, TG_TOKEN_FILE, CHAT_FILE)

# ---- the signing page: docs/l1-sign.html on main, served by GitHub Pages ------------------------------------

PAGE_REPO_PATH = "docs/l1-sign.html"
PAGE_SHA256 = "f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528"
PAGE_BYTES = 11846
PAGE_URL = "https://" + PAGES_HOST + PAGE_PATH

# ---- the venue's client, pinned: 34 distributions and pip itself, each by its size and SHA-256 on PyPI ---------

PIP_WHEEL = "pip-24.0-py3-none-any.whl"
WHEEL_SET = (
    ("annotated_types-0.8.0-py3-none-any.whl", 13427, "f072f4d804ea359e4eaf198b1af7a8b0943881a87f31bb764f8bf219bb9419e0",
     "/packages/99/91/8acff4f5e50511b911bbccb72b8628a49c68ce14148cd9f6431094859a90/annotated_types-0.8.0-py3-none-any.whl"),
    ("anyio-4.16.0-py3-none-any.whl", 134521, "c66ae634e0b8228396b801741beb3294326d4b6102f7bba4041c0dfb58c29026",
     "/packages/a9/16/7757fb84c819accc7d7e9af5291b261e4abb8627ee040f99e7d35ef2457a/anyio-4.16.0-py3-none-any.whl"),
    ("bitarray-3.12.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 404906, "8a32e10bd3c7e287df1e4c3da73efda5585a56ec59337b1467245f53dd469a99",
     "/packages/c0/8a/c9d2e34decc080374ea3dcca6d46c86907c1eb2ea5c47a13c7d0cf28e084/bitarray-3.12.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("certifi-2026.10.23-py3-none-any.whl", 135082, "e9b54de76e530bb6cf0ccd036787103acb58fd42ba930ea8bf948ddbaa2f61d1",
     "/packages/32/d1/a3652fe2c19134d0d15922177821d863cbd7e842d53a21bbe7e8e3a1b5ac/certifi-2026.10.23-py3-none-any.whl"),
    ("ckzg-2.1.8-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 176775, "10339d23e36b8a0a4e6fda7f6c72d6b2fd4e1506f7b64a661ba8c706ee33f335",
     "/packages/43/af/d0ed7c7b2babfa76e91190a90e8e1f93729d63370493c2c79acfe9002abe/ckzg-2.1.8-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("cytoolz-1.2.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 3153531, "f99e8e1f1e84522257c4c762ed194106b6b40eeca5a5d181b180fdeb3e927ef5",
     "/packages/8a/25/d782900308fff1872ec5df44b2a2ec36eee97e442657038a2b7e9f25c58c/cytoolz-1.2.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("eth_abi-5.2.0-py3-none-any.whl", 28511, "17abe47560ad753f18054f5b3089fcb588f3e3a092136a416b6c1502cb7e8877",
     "/packages/7a/b4/2f3982c4cbcbf5eeb6aec62df1533c0e63c653b3021ff338d44944405676/eth_abi-5.2.0-py3-none-any.whl"),
    ("eth_account-0.13.7-py3-none-any.whl", 587452, "39727de8c94d004ff61d10da7587509c04d2dc7eac71e04830135300bdfc6d24",
     "/packages/46/18/088fb250018cbe665bc2111974301b2d59f294a565aff7564c4df6878da2/eth_account-0.13.7-py3-none-any.whl"),
    ("eth_hash-0.8.0-py3-none-any.whl", 7965, "523718a51b369ab89866b929a5c93c52978cd866ea309192ad980dd8271f9fac",
     "/packages/87/87/b36792150ca0b28e4df683a34be15a61461ca0e349e5b5cf3ec8f694edb9/eth_hash-0.8.0-py3-none-any.whl"),
    ("eth_keyfile-0.8.1-py3-none-any.whl", 7510, "65387378b82fe7e86d7cb9f8d98e6d639142661b2f6f490629da09fddbef6d64",
     "/packages/88/fc/48a586175f847dd9e05e5b8994d2fe8336098781ec2e9836a2ad94280281/eth_keyfile-0.8.1-py3-none-any.whl"),
    ("eth_keys-0.8.0-py3-none-any.whl", 20461, "a7b94222638cccbdf2b5dae5c365d883a96826d82bb0faeb56baa65375f514ae",
     "/packages/f9/f5/24806598664a2fbc65d5ed4f0e9e986e7f9061e3b43738412c8df7ba1cbd/eth_keys-0.8.0-py3-none-any.whl"),
    ("eth_rlp-3.0.0-py3-none-any.whl", 15221, "32f355261c36ad2c369db098170f873123795667e50d496b034f369e2c9d2346",
     "/packages/ab/35/a3071f2a7ee701f99c8562865edbc426991d0964543d2947901b4135f259/eth_rlp-3.0.0-py3-none-any.whl"),
    ("eth_typing-6.0.0-py3-none-any.whl", 19191, "ee74fb641eb36dd885e1c42c2a3055314efa532b3e71480816df70a94d35cfb9",
     "/packages/aa/0d/e756622fab29f404d846d7464f929d642a7ee6eff5b38bcc79e7c64ac630/eth_typing-6.0.0-py3-none-any.whl"),
    ("eth_utils-5.3.1-py3-none-any.whl", 102529, "1f5476d8f29588d25b8ae4987e1ffdfae6d4c09026e476c4aad13b32dda3ead0",
     "/packages/bf/4d/257cdc01ada430b8e84b9f2385c2553f33218f5b47da9adf0a616308d4b7/eth_utils-5.3.1-py3-none-any.whl"),
    ("h11-0.16.0-py3-none-any.whl", 37515, "63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86",
     "/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl"),
    ("h2-4.4.1-py3-none-any.whl", 62636, "0e25f1462b23c9cb82d9eb02e28bc706dac2a68cb457c6a0d74d63c8a2a5d0e6",
     "/packages/7e/22/e85faf23bd72a92d1921e37d674ca56eb298a3c8be31fdecef0ff2b3aaac/h2-4.4.1-py3-none-any.whl"),
    ("hexbytes-2.0.0-py3-none-any.whl", 18866, "5425bd7ac83cdd9791c13a5bf97cfe9b9609a304b1ef3ab146adfd50de06cf0e",
     "/packages/e8/72/c7049aabd9e05efebc29b10208b11e5ae5cf819f48685ffced6abf871d10/hexbytes-2.0.0-py3-none-any.whl"),
    ("hpack-4.2.0-py3-none-any.whl", 34246, "858ac0b02280fa582b5080d68db0899c62a80375e0e5413a74970c5e518b6986",
     "/packages/71/b4/4a9fcfb2aef6ba44d9073ecd301443aa00b3dac95de5619f2a7de7ec8a91/hpack-4.2.0-py3-none-any.whl"),
    ("httpcore-1.0.9-py3-none-any.whl", 78784, "2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55",
     "/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl"),
    ("httpx-0.28.1-py3-none-any.whl", 73517, "d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad",
     "/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl"),
    ("hyperframe-6.1.0-py3-none-any.whl", 13007, "b03380493a519fce58ea5af42e4a42317bf9bd425596f7a0835ffce80f1a42e5",
     "/packages/48/30/47d0bf6072f7252e6521f3447ccfa40b421b6824517f82854703d0f5a98b/hyperframe-6.1.0-py3-none-any.whl"),
    ("idna-3.20-py3-none-any.whl", 69583, "ab7ae7122974553370f0bdb919e1a960b2cd1bc1ef0276416d896db81c14582c",
     "/packages/58/a2/bb081bab032533a855d44de1d56f8e8426114ff1ba5d1f07a438a0a654f8/idna-3.20-py3-none-any.whl"),
    ("msgpack-1.2.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 475652, "c4d5bbdbea8f5669b3a734d6c226772804fb120848f99cbe63a0ddee63b049c9",
     "/packages/1e/d9/f59bd841fc2fd2b74dc50ce85860a6a25f58e588dd48946aeaf2862cf990/msgpack-1.2.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("parsimonious-0.10.0-py3-none-any.whl", 48427, "982ab435fabe86519b57f6b35610aa4e4e977e9f02a14353edf4bbc75369fc0f",
     "/packages/aa/0f/c8b64d9b54ea631fcad4e9e3c8dbe8c11bb32a623be94f22974c88e71eaf/parsimonious-0.10.0-py3-none-any.whl"),
    ("polymarket_client-0.20.0-py3-none-any.whl", 428375, "677e074364bc051e330b1430e22b634ddf308e95c7ba6ca85645cd82741625c6",
     "/packages/25/91/e0d5814619fbab8ed9614f3791624834580fb619bb39f76792824baa3970/polymarket_client-0.20.0-py3-none-any.whl"),
    ("pycryptodome-3.24.1-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", 2276644, "93619c3117a8f14ea1267b427e465d152a66c89c3d3c643262070c05b2855aae",
     "/packages/a0/3f/e6a6b5d261746378a9267af50463d6aa01f88f88c98bedfd404c94eb7ec6/pycryptodome-3.24.1-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl"),
    ("pydantic-2.14.3-py3-none-any.whl", 494071, "3f7b347782ab7e4cf4c798496ae3a82787d9f21ec12676a9c564355eeef8daa8",
     "/packages/72/b8/b864503789ef5c58597d2a7b4adbee62c26440ab1e682581fc6838df8947/pydantic-2.14.3-py3-none-any.whl"),
    ("pydantic_core-2.50.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", 2261727, "c81d98e27d9d9261909dcccab1ba5d6ea1c98b0bb9470e368604614fd1d36ddd",
     "/packages/91/23/e0c6e3cd09a0ac809953fea698c816b9f03bf0b35b6820c9553e4f5d85a8/pydantic_core-2.50.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl"),
    ("regex-2026.11.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 808826, "ab4a0c5cd3df4b93841ba4a419a5438b2a4c78a4e418682fc674e3f50d56b857",
     "/packages/46/c2/59c5b6cf4b762d80de04cf60f2d0deba1da2f4172a91c41eaee8933080a8/regex-2026.11.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("rlp-5.0.0-py3-none-any.whl", 19832, "9525fb895d3a6540b7401eadd11c1b64740a5eccb82e543ac7e9735d319b0977",
     "/packages/a7/35/26ea7adca149e506bb03c50ade0c4d96cf269e6fc13a2b3f726d65905ffb/rlp-5.0.0-py3-none-any.whl"),
    ("toolz-1.2.0-py3-none-any.whl", 60789, "890f820b1cb8152785aaf9386d8707770110809035800985ca65cb24ce1120ef",
     "/packages/db/17/4c8beb6c8c4176c6bf143bfd7e1e4dd6719b00ced90738c7ac471b71c1df/toolz-1.2.0-py3-none-any.whl"),
    ("typing_extensions-4.16.0-py3-none-any.whl", 45571, "481caa481374e813c1b176ada14e97f1f67a4539ce9cfeb3f350d78d6370c2e8",
     "/packages/49/d3/b8441a820a491ddfc024b0b0cf0393375b75ea13866d9c66727e54c2fc80/typing_extensions-4.16.0-py3-none-any.whl"),
    ("typing_inspection-0.4.5-py3-none-any.whl", 14874, "bc210535442b39e1bf2805e0c7a17dfd6a4ace760c84c7f7d16245d23a6b1c39",
     "/packages/de/0c/ea2544850a7c135e15033a5c7a8e7211136184b7ae63e2239d557c2b3019/typing_inspection-0.4.5-py3-none-any.whl"),
    ("websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", 182523, "64dee438fed052b52e4f98f76c5790513235efaa1ef7f3f2192c392cd7c91b65",
     "/packages/14/8f/aa61f528fba38578ec553c145857a181384c72b98156f858ca5c8e82d9d3/websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl"),
    ("pip-24.0-py3-none-any.whl", 2110226, "ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc",
     "/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl"),
)
SDK_DIST, SDK_VERSION = "polymarket-client", "0.20.0"

# ---- the venue's terms, read on 2026-11-19 from the client's own source and docs.polymarket.com -----------------

CHAIN_ID = 137
SCOPES = ("CLOB",)
LIFETIME_S = 15534000          # 4,315 h: the client's _SESSION_KEY_LIFETIME_SECONDS; the venue's 180 days less 5 h
DEADLINE_S = 600               # the client's _DEPOSIT_WALLET_DEADLINE_S: a signed batch's validity
SELECTORS = {"authorize": "24017fae", "revoke": "e63f952f"}   # authorizeSessionSigner(address,uint256), revoke...(address)
LINKS, SIGNATURE_TRIES = 3, 3  # fresh signing links, and signatures asked of one link
READY_TRIES, READY_GAP_S = 30, 10

# ---- the round trip ---------------------------------------------------------------------------------------------

RT_FAMILY = "btc-updown-5m-"
RT_WINDOW_S = 300
RT_MIN_LEFT_S = 150            # the window open at placement keeps at least this long; else the next is waited for
RT_PRICE = "0.01"              # the lowest price on either tick the family uses, 0.01 or 0.001 (map section 6)
RT_SIZE = "5"                  # the family's minimum order size (map section 6, venue constants)
RT_MAX_PLACEMENTS = 2         # its Up token, and its Down token where the first crosses the book
RT_COST_UNITS = 50000          # 5 shares at 0.01, in the collateral's six-decimal units: what one fill can cost
RT_LOSS_MAX_UNITS = RT_COST_UNITS * RT_MAX_PLACEMENTS            # 0.10 pUSD: this TZ's whole loss, at most
APPROVE_UNITS = 1000000        # 1 pUSD to each exchange whose allowance is short, never the maximum: what a key can
                               # spend through that exchange until another TZ approves more
RT_SIDES = ("Up", "Down")

# ---- Telegram ---------------------------------------------------------------------------------------------------

TG_WAIT_S = 1800
TOKEN_RE = re.compile(r"[0-9]{5,12}:[A-Za-z0-9_-]{30,64}")
RELAYER_KEY_RE = re.compile(r"[A-Za-z0-9._:-]{16,256}")

# ---- floors -----------------------------------------------------------------------------------------------------

STREAM_FLOOR = 7300000000    # research/tz33-reward-book-capture.py line 190
PEAK = 445535636             # fourteen slots of 31,823,974 bytes (TZ-46; map section 6)
MARGIN_WATCH = 1000000000    # map section 7 item 175
SESSION_WRITES = 50000000    # this session's writes on the capture host, at most
CAPTURE_FLOOR = STREAM_FLOOR + PEAK + SESSION_WRITES                       # 7,795,535,636
JOURNAL_KEEP_FREE = 2147483648                                             # TZ-49's SystemKeepFree=2G
L1_ENV_MAX = 200000000       # the client's tree, 47,855,239 bytes installed by the Architect, with room
LIVE_WORK_MAX = 100000000    # the live work tree: the wheels, 14,422,773 bytes, and the logs
LIVE_FLOOR = JOURNAL_KEEP_FREE + L1_ENV_MAX + LIVE_WORK_MAX                 # 2,447,483,648
RECLAIM_FLOOR = STREAM_FLOOR + 100000000
MEM_FLOOR = 86426834          # twice 43,213,417: selftest's 36,040,704 at TZ-37's ratio, 58,953,728 / 49,168,384
MEM_FLOOR_SDK = 274917678     # twice 137,458,839: sdk-selftest's 114,642,944 at the same ratio (map item 156)
MEM_READS, MEM_WAIT_S = 5, 60

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
DAY_RE = re.compile(r"[0-9]{10}")
RB_STREAM_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz")
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
LIVE_S = 60

# ---- the audit hook: TZ-51 section 2 as a pure function, and the hook that applies it -------------------------

MODE = [None]
REFUSED = []
RESOLVED = set()
COUNTS = {"lookups": 0, "requests": 0}
CLIENT_MODES = ("env", "key", "authorize", "approve", "revoke", "ready", "roundtrip", "sdk-selftest")
TTY_MODES = ("secrets", "bosskey", "authorize", "approve", "revoke")
NET = {"geoblock": (GEO_HOST,), "page": (PAGES_HOST,), "wheels": (PYPI_HOST,),
       "tg-probe": (TG_HOST,), "find-chat": (TG_HOST,), "tg-report": (TG_HOST,),
       "authorize": (RELAYER_HOST, CLOB_HOST), "revoke": (RELAYER_HOST, CLOB_HOST), "approve": (RELAYER_HOST, RPC_HOST),
       "ready": (RELAYER_HOST, CLOB_HOST, RPC_HOST), "roundtrip": (RELAYER_HOST, CLOB_HOST, GAMMA_HOST, RPC_HOST),
       "selftest": ("127.0.0.1",), "sdk-selftest": ("127.0.0.1",)}
EXECS = {"number": ("git",), "refs": ("git",), "room": ("systemctl",), "scratch": ("stat",), "reclaim": ("git", "stat"),
         "methods": ("ssh",), "host": ("systemctl", "timedatectl", "locale"), "sshd": ("sshd",)}
for _m in CLIENT_MODES:      # pycryptodome's import runs platform.architecture(), which runs `file` on the interpreter
    EXECS[_m] = ("file", "timedatectl") if _m == "roundtrip" else ("file",)
READS = {SESSION_KEY_FILE: ("key", "authorize", "revoke", "ready", "roundtrip"),
         RELAYER_FILE: ("secrets", "authorize", "approve", "revoke"),
         TG_TOKEN_FILE: ("secrets", "tg-probe", "find-chat", "tg-report"),
         CHAT_FILE: ("find-chat", "tg-report")}
WRITES = {SESSION_KEY_FILE: ("key",), RELAYER_FILE: ("secrets",), TG_TOKEN_FILE: ("secrets",),
          CHAT_FILE: ("find-chat",), AUTHORIZED_KEYS: ("bosskey",),
          ACCOUNT_FILE: ("secrets", "authorize", "approve", "revoke"),
          ACCOUNT_FILE + ".tmp": ("secrets", "authorize", "approve", "revoke")}
EXCLUSIVE = (SESSION_KEY_FILE, RELAYER_FILE, TG_TOKEN_FILE, CHAT_FILE)
MKDIRS = {L1_ETC: ("secrets", "key"), L1_VAR: ("secrets", "authorize", "approve", "revoke", "roundtrip")}
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.copyfile")
HOOKED = ("open", "os.listdir", "os.scandir", "socket.__new__", "socket.getaddrinfo", "socket.connect",
          "subprocess.Popen") + CHANGE_EVENTS


class GuardError(RuntimeError):
    pass


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def _appending(wmode, flags):
    if isinstance(wmode, str):
        return wmode in ("a", "ab")
    return isinstance(flags, int) and bool(flags & os.O_APPEND) and not flags & os.O_TRUNC


def policy(mode, event, args):
    """None where TZ-51 section 2 allows the event in this mode; otherwise why it is refused. Pure but for the
    addresses this process resolved from an allowed name. IPv4 alone (map section 7 item 181): a network socket of
    any family but AF_INET, a lookup in any family but AF_INET and a connection to anything but an IPv4 address are
    refused in every mode; an AF_UNIX socket is let through in the client's modes alone, asyncio's self-pipe."""
    if event == "socket.__new__":
        fam = args[1] if len(args) > 1 else None
        if fam == socket.AF_INET or (fam == socket.AF_UNIX and mode in CLIENT_MODES):
            return None
        return "a socket of family %r: IPv4 alone" % (fam,)
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        fam = args[2] if len(args) > 2 else None
        if fam != socket.AF_INET:
            return "a lookup of %r in family %r: IPv4 alone" % (host, fam)
        return None if host in RESOLVED or host in NET.get(mode, ()) else "a lookup of %r" % (host,)
    if event == "socket.connect":
        addr = args[1] if len(args) > 1 else None
        if isinstance(addr, (str, bytes)) and mode in CLIENT_MODES:
            return None                     # an AF_UNIX path: asyncio's self-pipe never connects one, but nothing else may
        ok = isinstance(addr, tuple) and len(addr) == 2 and isinstance(addr[0], str) \
            and IPV4.fullmatch(addr[0]) is not None and (addr[0] in RESOLVED or addr[0] in NET.get(mode, ()))
        return None if ok else "a connection to %r" % (addr,)
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else None)
        name = os.path.basename(os.fsdecode(exe)) if exe is not None else None
        return None if name in EXECS.get(mode, ()) else "running %r" % (name,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        if any(_under(p, r) for r in PROTECTED):
            return "an open under a capture's store or the advisor's credentials"
        if p == "/dev/tty":
            return None if mode in TTY_MODES else "the terminal outside the Boss's modes"
        if p == "/dev/null":
            return None
        if p in READS and mode not in READS[p] and not _writing(wm, fl):
            return "a read of %s in mode %s" % (p, mode)
        if _writing(wm, fl):
            if _under(p, FORENSICS):
                return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
            if os.path.dirname(p) == L1_VAR and RT_RECORD.fullmatch(os.path.basename(p)):
                return None if mode == "roundtrip" and _exclusive(wm, fl) else "a round trip's record in mode %s" % mode
            if p in WRITES:
                if mode not in WRITES[p]:
                    return "a write of %s in mode %s" % (p, mode)
                if p in EXCLUSIVE and not _exclusive(wm, fl):
                    return "a write of %s that is not an exclusive create" % p
                if p == AUTHORIZED_KEYS and not _appending(wm, fl):
                    return "a write of %s that is not an append" % p
                return None
            if not _under(p, WORK):
                return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        if _under(p, RB):
            return None if mode == "room" else "a listing of the reward book's store"
        return "a listing under a capture's store" if any(_under(p, r) for r in PROTECTED) else None
    paths = [p]
    if event in ("os.rename", "os.link", "os.symlink", "shutil.copyfile") and len(args) > 1:
        paths.append(_path(args[1]))
    for q in paths:
        if q is None or _under(q, WORK):
            continue
        if event == "os.mkdir" and q in MKDIRS and mode in MKDIRS[q]:
            continue
        if event == "os.chmod" and q in WRITES and mode in WRITES[q]:
            continue
        if event == "os.rename" and q in (ACCOUNT_FILE, ACCOUNT_FILE + ".tmp") and mode in WRITES[ACCOUNT_FILE]:
            continue
        return "a change outside the work tree"
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, MODE[0]))
        raise GuardError("%s refused in mode %s: %s" % (event, MODE[0], why))


sys.addaudithook(_audit)
_GAI = socket.getaddrinfo


def gai4(host, port, family=0, type=0, proto=0, flags=0):
    """socket.getaddrinfo with AF_INET asked of every lookup that asks for no family, and any other family refused:
    the client's modes resolve through it, so httpx and asyncio open IPv4 sockets alone (map section 7 item 181)."""
    if family in (0, socket.AF_UNSPEC):
        family = socket.AF_INET
    if family != socket.AF_INET:
        raise GuardError("a lookup of %r in family %r: IPv4 alone" % (host, family))
    infos = _GAI(host, port, family, type, proto, flags)
    RESOLVED.update(ai[4][0] for ai in infos if ai[0] == socket.AF_INET)
    COUNTS["lookups"] += 1
    return infos

# ---- small helpers ------------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path, chunk=1 << 20):
    """The SHA-256 and the byte count of a file read as bytes."""
    h, n = hashlib.sha256(), 0
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def read_text(path, default=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return default


def meminfo(text):
    """The fields of /proc/meminfo in bytes. Pure."""
    found = {}
    for line in text.split("\n"):
        f = line.split()
        if len(f) >= 2 and f[0].endswith(":") and f[1].isdigit():
            found[f[0][:-1]] = int(f[1]) * (1024 if len(f) > 2 and f[2] == "kB" else 1)
    return found


def mem_available():
    return meminfo(read_text("/proc/meminfo", ""))["MemAvailable"]


def fs_bytes(path):
    """Total, available and free bytes of the file system holding `path`."""
    st = os.statvfs(path)
    return st.f_blocks * st.f_frsize, st.f_bavail * st.f_frsize, st.f_bfree * st.f_frsize


def floors(disk, disk_floor, mem_floor=None, read=mem_available, sleep=time.sleep, statf=fs_bytes):
    """At a mode's start: MemAvailable read up to five times 60 s apart, the first at or above the memory floor
    passing - the client's modes' own where they run; the available bytes of `disk` at or above disk_floor."""
    mem_floor = mem_floor or (MEM_FLOOR_SDK if MODE[0] in CLIENT_MODES else MEM_FLOOR)
    for k in range(1, MEM_READS + 1):
        m = read()
        out("MemAvailable read %d: %d bytes, floor %d" % (k, m, mem_floor))
        if m >= mem_floor:
            break
        assert k < MEM_READS, "BLOCKED: MemAvailable below %d at %d reads" % (mem_floor, MEM_READS)
        sleep(MEM_WAIT_S)
    avail = statf(disk)[1]
    out("available on %s: %d bytes, floor %d" % (disk, avail, disk_floor))
    assert avail >= disk_floor, "BLOCKED: %d bytes available on %s, below %d" % (avail, disk, disk_floor)
    return avail


def run(argv, timeout=20, env=None):
    """A command under TZ=UTC and the C locale, or under `env` where given: (exit, stdout, stderr)."""
    cp = subprocess.run(argv, capture_output=True, text=True, timeout=timeout,
                        env=env if env is not None else dict(os.environ, **SHOW_ENV))
    return cp.returncode, cp.stdout, cp.stderr


def show(unit, props):
    """systemctl show: {property: value}."""
    args = ["systemctl", "show", unit]
    for p in props:
        args += ["-p", p]
    rc, so, se = run(args)
    assert rc == 0, "systemctl show %s: %s" % (unit, se.strip())
    kv = {}
    for line in so.split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            kv[k] = v
    return kv


def git(*args, tree=PRIMARY):
    rc, so, se = run(["git", "-C", tree] + list(args), timeout=120)
    assert rc == 0, "git %s: %s" % (" ".join(args), se.strip()[:300])
    return so.strip()


def record(kind, obj):
    out("RECORD %s %s" % (kind, json.dumps(obj, sort_keys=True, separators=(",", ":"))))


def is_capture_host():
    return os.path.isdir(CAPTURE_MARK)


def first_label(name):
    """A host name to its first dot. Pure."""
    return name.split(".", 1)[0]


def short_hostname():
    return first_label(socket.gethostname())


def key_fingerprints(text):
    """The type and SHA256 fingerprint of each key line of an authorized_keys or .pub text, in ssh-keygen's form;
    never a key's comment. Pure."""
    found = []
    for ln in text.split("\n"):
        f = ln.split()
        for i, w in enumerate(f[:-1]):
            if w.startswith("ssh-") or w.startswith("ecdsa-") or w.startswith("sk-"):
                try:
                    blob = base64.b64decode(f[i + 1], validate=True)
                except ValueError:
                    break
                found.append((w, "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")))
                break
    return found


def host_keys():
    names = sorted(os.listdir(HOST_KEY_DIR)) if os.path.isdir(HOST_KEY_DIR) else []
    found = []
    for n in names:
        if n.startswith("ssh_host_") and n.endswith("_key.pub"):
            found += key_fingerprints(read_text(os.path.join(HOST_KEY_DIR, n), "") or "")
    return sorted(found)


def is_live_host():
    return (short_hostname() == LIVE_HOSTNAME and LIVE_HOST_KEY in host_keys()
            and not os.path.exists(CAPTURE_MARK))


def assert_live():
    assert is_live_host(), "BLOCKED: this mode runs on the live host %s and nowhere else" % LIVE_HOSTNAME


def file_state(path):
    """A path's kind, mode, owner and size - never its content: what may be printed of a credential."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent"
    kind = "dir" if os.path.isdir(path) and not os.path.islink(path) else (
        "file" if os.path.isfile(path) and not os.path.islink(path) else "other")
    return "%s mode %04o uid %d bytes %d" % (kind, st.st_mode & 0o7777, st.st_uid, st.st_size)


def private_file_ok(path, mode=0o600):
    """A regular file, not a link, root's, of `mode`, and not empty."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return (os.path.isfile(path) and not os.path.islink(path) and st.st_uid == 0
            and st.st_mode & 0o7777 == mode and st.st_size > 0)


def write_private(path, data, dir_mode=0o700):
    """`data` to `path` by exclusive create, 0600 from its first byte; its directory made 0700 where absent.
    Returns the bytes written."""
    d = os.path.dirname(path)
    if not os.path.isdir(d):
        os.mkdir(d, dir_mode)
    st = os.lstat(d)
    assert st.st_uid == 0 and st.st_mode & 0o7777 == dir_mode and not os.path.islink(d), \
        "%s: %s" % (d, file_state(d))
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    assert private_file_ok(path), "%s: %s" % (path, file_state(path))
    return len(data)


def write_json_atomic(path, obj, dir_mode=0o700):
    """`obj` as JSON to `path` through `path`.tmp and a rename, 0600."""
    d = os.path.dirname(path)
    if not os.path.isdir(d):
        os.mkdir(d, dir_mode)
    tmp = path + ".tmp"
    data = (json.dumps(obj, sort_keys=True, indent=1) + "\n").encode()
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.rename(tmp, path)
    return len(data)

# ---- the network, standard library: IPv4 alone, every request with this TZ's agent --------------------------


def resolve(host, port=443):
    """The IPv4 addresses of `host`, sorted; each is the only address a later connection may use. An address
    literal is its own."""
    if IPV4.fullmatch(host):
        return [host]
    infos = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    addrs = sorted({ai[4][0] for ai in infos})
    RESOLVED.update(addrs)
    COUNTS["lookups"] += 1
    return addrs


def connect4(addr, port, timeout):
    """A TCP connection to the IPv4 address `addr`: its socket AF_INET by construction, and no lookup made."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(timeout)
        s.connect((addr, port))
    except BaseException:
        s.close()
        raise
    return s


def err_of(exc):
    """An error as printed: its type, errno and the C library's message - never an address. Pure."""
    no, msg = getattr(exc, "errno", None), getattr(exc, "strerror", None)
    return "%s errno %s: %s" % (type(exc).__name__, no, msg) if no is not None else type(exc).__name__


def http_call(base, method, path, body=None, timeout=TIMEOUT_S, max_bytes=READ_MAX):
    """One request over a fresh IPv4 connection to base = (scheme, host, port), every header this TZ's: (status,
    headers, body, the connection's own source address). A body over max_bytes is refused."""
    scheme, host, port = base
    addr = resolve(host, port)[0]
    if scheme == "https":
        c = http.client.HTTPSConnection(host, port, timeout=timeout, context=ssl.create_default_context())
    else:
        c = http.client.HTTPConnection(host, port, timeout=timeout)
    c._create_connection = lambda address, timeout=None, source_address=None: connect4(addr, port, timeout)
    hdrs = dict(HEADERS)
    data = None
    if body is not None:
        data = json.dumps(body, separators=(",", ":")).encode()
        hdrs["Content-Type"] = "application/json"
    try:
        c.request(method, path, body=data, headers=hdrs)
        src = c.sock.getsockname()[0]
        r = c.getresponse()
        blob = r.read(max_bytes + 1)
        assert len(blob) <= max_bytes, "a reply over %d bytes" % max_bytes
        COUNTS["requests"] += 1
        return r.status, {k.lower(): v for k, v in r.getheaders()}, blob, src
    finally:
        c.close()


def json_of(blob):
    try:
        return json.loads(blob.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None

# ---- the readings: pure -------------------------------------------------------------------------------------


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def refs_reading(text):
    """origin's refs counted by kind, and whether this TZ's branch is among them. Pure."""
    kinds, branch = {}, False
    for ln in text.split("\n"):
        if "\t" not in ln:
            continue
        ref = ln.split("\t", 1)[1].strip()
        branch = branch or ref == "refs/heads/" + BRANCH
        if ref in ("HEAD", "refs/heads/main"):
            k = ref
        elif ref.startswith("refs/heads/tz-"):
            k = "refs/heads/tz-*"
        elif ref.startswith("refs/pull/"):
            k = "refs/pull/*/" + ref.rsplit("/", 1)[1]
        elif ref.startswith("refs/tags/pairbook-streams-") or ref.startswith("refs/tags/rewardbook-streams-"):
            k = ref.split("-streams-", 1)[0] + "-streams-*" + ("^{}" if ref.endswith("^{}") else "")
        else:
            k = ref
        kinds[k] = kinds.get(k, 0) + 1
    return kinds, branch


def room_reading(avail, streams):
    """The room and its margin over the stream floor and PEAK (map section 7 item 175). Pure."""
    room = avail + streams
    return room, room - STREAM_FLOOR - PEAK


def geo_fields(doc):
    """What may be printed of the venue's reply: blocked, country and region, and its keys' names - never the
    address it carries. Pure."""
    if not isinstance(doc, dict):
        return None
    return {"blocked": doc.get("blocked"), "country": doc.get("country"), "region": doc.get("region"),
            "keys": sorted(str(k) for k in doc)}


def geo_reading(status, doc):
    """One geoblock read: UNREAD unless status 200 and a reply whose blocked is a boolean and whose country is two
    capital letters; else BLOCKED where blocked is true, PASS where it is false. Pure."""
    f = geo_fields(doc)
    if status != 200 or f is None or not isinstance(f["blocked"], bool) \
            or not (isinstance(f["country"], str) and re.fullmatch(r"[A-Z]{2}", f["country"])):
        return "UNREAD"
    return "BLOCKED" if f["blocked"] else "PASS"


def os_release(text):
    found = {}
    for ln in text.split("\n"):
        if "=" in ln and not ln.startswith("#"):
            k, v = ln.split("=", 1)
            found[k.strip()] = v.strip().strip('"')
    return found


def live_gate(hostname, osrel, pyver, capture_paths, keys):
    """The live host gate's five checks, TZ-49's: `hostname` the first label of the host's name, `keys` its SSH host
    keys by type and fingerprint. Pure."""
    checks = {"LH1 hostname %s" % LIVE_HOSTNAME: hostname == LIVE_HOSTNAME,
              "LH2 Ubuntu 24.04": osrel.get("ID") == "ubuntu" and osrel.get("VERSION_ID") == "24.04",
              "LH3 Python 3.12": tuple(pyver[:2]) == (3, 12),
              "LH4 not the capture host": not capture_paths,
              "LH5 the host key pinned at TZ-47's first connection": LIVE_HOST_KEY in keys}
    return all(checks.values()), checks


def sshd_effective(text):
    """`sshd -T` text: each keyword and its value, the last line of a keyword kept. Pure."""
    found = {}
    for ln in text.split("\n"):
        f = ln.strip().split(None, 1)
        if len(f) == 2:
            found[f[0].lower()] = f[1].strip()
    return found


def ssh_reading(dropin, effective):
    """G-SSH's K1 to K5: `dropin` TZ-49's sshd drop-in's (SHA-256, mode) or None; `effective` sshd_effective's
    reading of `sshd -T`. Pure."""
    checks = {"K1 TZ-49's sshd drop-in, byte for byte": dropin == (SSHD_SHA256, 0o644)}
    for i, (k, v) in enumerate(SSHD_IN_FORCE, 2):
        checks["K%d %s %s" % (i, k, v)] = effective.get(k) == v
    return all(checks.values()), checks


METHODS_RE = re.compile(r"Authentications that can continue: ([A-Za-z0-9@.,_-]+)")


def methods_of(text):
    """The lists of authentication methods an sshd offered, from `ssh -v` text: each list once, sorted - nothing
    else of the text, which carries the address. Pure."""
    return sorted(set(METHODS_RE.findall(text)))


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def _ssh_string(blob, i):
    assert i + 4 <= len(blob), "a truncated key"
    n = struct.unpack(">I", blob[i:i + 4])[0]
    assert i + 4 + n <= len(blob), "a truncated key"
    return blob[i + 4:i + 4 + n], i + 4 + n


def pubkey_line(text):
    """The Boss's SSH public key as one line of authorized_keys: (the line, its type, its fingerprint, its bits for
    RSA). Refuses a private key, options, two lines, an unknown type, a blob whose own type differs from its line's,
    and RSA under RSA_MIN_BITS. Pure."""
    line = text.strip()
    if not line:
        raise ValueError("empty")
    if "PRIVATE" in line.upper() or "\n" in line or "\r" in line:
        raise ValueError("not one public key line")
    f = line.split()
    if len(f) < 2 or f[0] not in BOSS_KEY_TYPES:
        raise ValueError("not a public key of a known type at the line's start")
    try:
        blob = base64.b64decode(f[1], validate=True)
    except ValueError:
        raise ValueError("the key is not base64")
    try:
        kind, i = _ssh_string(blob, 0)
        assert kind.decode("ascii") == f[0], "the key's own type differs"
        bits = None
        if f[0] == "ssh-rsa":
            _e, i = _ssh_string(blob, i)
            n, i = _ssh_string(blob, i)
            bits = int.from_bytes(n, "big").bit_length()
            assert bits >= RSA_MIN_BITS, "RSA of %d bits" % bits
        elif f[0] == "ssh-ed25519":
            pk, i = _ssh_string(blob, i)
            assert len(pk) == 32, "an ed25519 key of %d bytes" % len(pk)
        assert i <= len(blob)
    except (AssertionError, UnicodeDecodeError) as exc:
        raise ValueError(str(exc) or "a malformed key")
    fp = "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")
    return " ".join(f), f[0], fp, bits


def valid_address(text):
    """An EVM address as typed: its lowercase form, or None. Pure."""
    t = (text or "").strip()
    if not ADDRESS.fullmatch(t) or t.lower() == ZERO_ADDRESS:
        return None
    return t.lower()


def token_ok(text):
    return isinstance(text, str) and TOKEN_RE.fullmatch(text) is not None


def relayer_key_ok(text):
    return isinstance(text, str) and RELAYER_KEY_RE.fullmatch(text) is not None


def sign_link(op, owner, wallet, key, nonce, deadline, valid_until=None, url=PAGE_URL, exchanges=None):
    """The signing page's link: every field in the fragment, which no request carries. An approval names its
    exchanges by letter - c, v or cv - and the page alone holds their addresses and the amount. Pure."""
    assert op in ("authorize", "revoke", "approve")
    f = [("v", "1"), ("op", op), ("o", owner), ("w", wallet)]
    if op == "approve":
        assert exchanges in ("c", "v", "cv"), exchanges
        f.append(("x", exchanges))
    else:
        f.append(("k", key))
    if op == "authorize":
        f.append(("u", str(int(valid_until))))
    f += [("n", str(int(nonce))), ("d", str(int(deadline)))]
    return url + "#" + "&".join("%s=%s" % (k, v) for k, v in f)


def wheel_name(filename):
    """A wheel file's distribution name, normalized as pip normalizes it, and its version. Pure."""
    m = re.fullmatch(r"([A-Za-z0-9_.]+?)-([0-9][^-]*)-.+\.whl", filename)
    assert m, filename
    return re.sub(r"[-_.]+", "-", m.group(1)).lower(), m.group(2)


def requirements_text(wheel_set=None):
    """The hash-pinned requirements of the client's 34 distributions: every wheel of the set but pip's. Pure."""
    rows = []
    for fn, _size, sha, _url in (wheel_set or WHEEL_SET):
        if fn == PIP_WHEEL:
            continue
        name, ver = wheel_name(fn)
        rows.append("%s==%s --hash=sha256:%s" % (name, ver, sha))
    return "\n".join(sorted(rows)) + "\n"


def pins(wheel_set=None):
    return dict(wheel_name(fn) for fn, _s, _h, _u in (wheel_set or WHEEL_SET) if fn != PIP_WHEEL)


def installed_reading(found, want):
    """G-ENV's second half: the distributions installed against the pins - none missing, none extra, none at another
    version. Pure."""
    missing = sorted(set(want) - set(found))
    extra = sorted(set(found) - set(want))
    wrong = sorted(k for k in set(want) & set(found) if found[k] != want[k])
    return not (missing or extra or wrong), missing, extra, wrong


def record_reading(claims, actual):
    """G-ENV's files: every file a distribution's RECORD lists with a SHA-256, against the file as it is. `claims` is
    [(distribution, path, the RECORD's hash)], `actual` {path: the file's hash in the RECORD's form, or None where it
    is absent}. A path two distributions list - eth-rlp's and hexbytes' docs/ files - holds the bytes of the one pip
    installed last, so it passes where it equals one of its claims. Returns (ok, entries, paths, paths listed twice or
    more, missing, another hash). Pure."""
    count, by_path = {}, {}
    for _dist, path, h in claims:
        by_path.setdefault(path, set()).add(h)
        count[path] = count.get(path, 0) + 1
    missing = sorted(p for p in by_path if actual.get(p) is None)
    wrong = sorted(p for p in by_path if actual.get(p) is not None and actual[p] not in by_path[p])
    multi = sum(1 for p in count if count[p] > 1)
    return not (missing or wrong), len(claims), len(by_path), multi, missing, wrong


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


def window_of(now):
    """The five-minute window open at `now`: (its open, the seconds left in it). Pure."""
    t0 = int(now) // RT_WINDOW_S * RT_WINDOW_S
    return t0, t0 + RT_WINDOW_S - now


def market_reading(doc, t0):
    """A five-minute market's gamma document read for the round trip: (ok, why, its Up and Down trading IDs, its
    condition, its exchange's letter). A CTF market - version v1 or none - trades its clobTokenIds on the CTF
    exchange, a Protocol V2 market its positionIds on the V2 exchange, each ID checked to be of its own kind by the
    client's reserved bits; a negative-risk market is refused. Its IDs are read from its outcomes, never by position;
    no price of it is read. Pure."""
    no = (False, None, {}, None, None)
    if isinstance(doc, list):
        doc = doc[0] if len(doc) == 1 else None
    if not isinstance(doc, dict):
        return (False, "no document") + no[2:]
    if doc.get("slug") != RT_FAMILY + str(t0):
        return (False, "another market's document") + no[2:]
    for k, v in (("active", True), ("closed", False), ("acceptingOrders", True), ("enableOrderBook", True)):
        if doc.get(k) is not v:
            return (False, "%s is %r" % (k, doc.get(k))) + no[2:]
    version = doc.get("version")
    if version not in (None, "v1", "v2"):
        return (False, "version is %r" % (version,)) + no[2:]
    if doc.get("negRisk") not in (None, False):
        return (False, "negRisk is %r" % (doc.get("negRisk"),)) + no[2:]
    try:
        mins = float(doc.get("orderMinSize"))
    except (TypeError, ValueError):
        mins = None
    if mins != float(RT_SIZE):
        return (False, "orderMinSize is %r" % (doc.get("orderMinSize"),)) + no[2:]
    field = "positionIds" if version == "v2" else "clobTokenIds"
    try:
        outcomes, ids = doc.get("outcomes"), doc.get(field)
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
        ids = json.loads(ids) if isinstance(ids, str) else ids
    except ValueError:
        return (False, "outcomes or %s is not JSON" % field) + no[2:]
    if not (isinstance(outcomes, list) and isinstance(ids, list) and len(outcomes) == 2 and len(ids) == 2
            and sorted(outcomes) == sorted(RT_SIDES) and all(isinstance(t, str) and t.isdigit() and 0 < int(t) < 1 << 256
                                                             for t in ids)):
        return (False, "outcomes is not a two-element Up/Down array of %s" % field) + no[2:]
    if any((int(t) & V2_RESERVED == 0) != (version == "v2") for t in ids):
        return (False, "an ID of %s is not of its version's kind" % field) + no[2:]
    cid = doc.get("conditionId")
    if not (isinstance(cid, str) and re.fullmatch(r"0x[0-9a-fA-F]{64}", cid)):
        return (False, "no condition id") + no[2:]
    return True, "eligible, %s" % ("Protocol V2" if version == "v2" else "CTF"), \
        {outcomes[i]: ids[i] for i in range(2)}, cid, ("v" if version == "v2" else "c")


def rt_reading(rt):
    """G-RT, from the round trip's own record. Pure. PASS: one placement accepted live, at most RT_MAX_PLACEMENTS
    made, every earlier one refused as post-only crossing the book; the order read back live at this TZ's price,
    size, side and type with nothing matched; cancelled by its own request; read back cancelled with nothing matched;
    no open order of the key, of the wallet by the key, after it; the balance after equal to the balance before."""
    pl = rt.get("placements", [])
    live = [p for p in pl if p.get("result") == "live"]
    checks = {
        "a placement accepted live": len(live) == 1 and pl[-1].get("result") == "live",
        "placements at most %d" % RT_MAX_PLACEMENTS: 0 < len(pl) <= RT_MAX_PLACEMENTS,
        "every earlier placement refused as crossing the book": all(
            p.get("result") == "post_only_would_cross" for p in pl[:-1]),
        "read back LIVE at 0.01, 5, BUY, GTC, nothing matched": rt.get("read_live") == {
            "status": "LIVE", "price": RT_PRICE, "size": RT_SIZE, "side": "BUY", "type": "GTC", "matched": "0",
            "maker is the wallet": True, "asset is the token": True},
        "cancelled by its own request": rt.get("cancel") == {"canceled": True, "not_canceled": 0},
        "read back cancelled, nothing matched": (isinstance(rt.get("read_after"), dict)
                                                 and str(rt["read_after"].get("status", "")).startswith("CANCELED")
                                                 and rt["read_after"].get("matched") == "0"),
        "no open order of the key after it": rt.get("open_after") == 0,
        "no open order of the wallet by the key after it": rt.get("wallet_open_after") == 0,
        "the balance after equal to the balance before": (isinstance(rt.get("balance_before"), int)
                                                          and rt.get("balance_before") == rt.get("balance_after")),
    }
    return all(checks.values()), checks

# ---- the capture host's modes -------------------------------------------------------------------------------


def mode_fingerprint():
    assert is_capture_host(), "BLOCKED: fingerprint runs on the capture host"
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "BLOCKED: map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "BLOCKED: anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[0][:12]
        assert h == ANCHORS[k], "BLOCKED: re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "BLOCKED: rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "BLOCKED: frozen row %s: %r, the map %r" % (path, got, want)
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    with open(os.path.join(PRIMARY, PAGE_REPO_PATH), "rb") as fh:
        page = fh.read()
    pg = (len(page), sha256_bytes(page))
    out("%s %d bytes sha256 %s, TZ-50's Appendix B's %d and %s: %s" % (PAGE_REPO_PATH, pg[0], pg[1], PAGE_BYTES, PAGE_SHA256,
                                                            "equal" if pg == (PAGE_BYTES, PAGE_SHA256) else "DIFFER"))
    assert pg == (PAGE_BYTES, PAGE_SHA256), "BLOCKED: %s on main is not TZ-50's Appendix B" % PAGE_REPO_PATH
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; the signing page on main equal to TZ-50's Appendix B" % (
            MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"], states["reported"]))
    return 0


def mode_number():
    assert is_capture_host(), "BLOCKED: number runs on the capture host"
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/").split("\n")
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        git("rev-parse", "origin/main"), len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)
    return 0


def mode_refs():
    assert is_capture_host(), "BLOCKED: refs runs on the capture host"
    text = git("ls-remote", "origin")
    kinds, branch = refs_reading(text)
    for ln in text.split("\n"):
        if ln.endswith("\tHEAD") or ln.endswith("\trefs/heads/main"):
            out("REF %s" % ln)
    for k in sorted(kinds):
        out("REFS %-40s %d" % (k, kinds[k]))
    out("REFS %d lines; refs/heads/%s %s" % (sum(kinds.values()), BRANCH, "PRESENT" if branch else "absent"))
    assert not branch, "BLOCKED: refs/heads/%s exists on origin already" % BRANCH
    return 0


def rb_streams(root=RB):
    """The reward book's stream files by their directory entries alone: (bytes, files, day directories)."""
    total = files = 0
    with os.scandir(root) as it:
        days = sorted(e.name for e in it if e.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(e.name))
    for d in days:
        with os.scandir(os.path.join(root, d)) as it:
            for e in it:
                if e.is_file(follow_symlinks=False) and RB_STREAM_RE.fullmatch(e.name):
                    total += e.stat(follow_symlinks=False).st_size
                    files += 1
    return total, files, len(days)


def mode_room(sleep=time.sleep):
    """The room, read while the reward book's archive is not running (map section 3, the units)."""
    assert is_capture_host(), "BLOCKED: room runs on the capture host"
    for k in range(1, ARCHIVE_READS + 1):
        state = show(RB_ARCHIVE_SVC, ["ActiveState"]).get("ActiveState")
        out("%s read %d: %s" % (RB_ARCHIVE_SVC, k, state))
        if state == "inactive":
            break
        if k == ARCHIVE_READS:
            out("ROOM not read: the reward book's archive was running at %d reads" % ARCHIVE_READS)
            return 0
        sleep(ARCHIVE_WAIT_S)
    avail = floors(CAPTURE_DISK, CAPTURE_FLOOR)
    streams, files, days = rb_streams()
    room, margin = room_reading(avail, streams)
    out("ROOM: %d bytes available on %s; the reward book's stream files %d bytes in %d files under %d day "
        "directories; the room %d; its margin over STREAM_FLOOR %d and PEAK %d: %d bytes%s" % (
            avail, CAPTURE_DISK, streams, files, days, room, STREAM_FLOOR, PEAK, margin,
            "" if margin >= MARGIN_WATCH else " - BELOW %d (map section 7 item 175)" % MARGIN_WATCH))
    return 0


def mode_methods(label):
    """G-SSH K6: the methods the live host's sshd offers root, read from outside by one connection that offers no
    key and can answer no prompt. Of ssh's text, which carries the address, nothing is printed but the methods."""
    assert label in ("gate", "after"), "methods takes gate or after"
    assert is_capture_host(), "BLOCKED: methods runs on the capture host"
    try:
        rc, so, se = run(["ssh", "-T", "-v", "-o", "BatchMode=yes", "-o", "ConnectTimeout=20", "-o",
                          "PubkeyAuthentication=no", "-o", "PreferredAuthentications=password,keyboard-interactive",
                          "-o", "NumberOfPasswordPrompts=0", LIVE_ALIAS, "true"], timeout=60)
    except subprocess.TimeoutExpired:
        rc, so, se = None, "", ""
    found = methods_of(so + "\n" + se)
    ok = found == METHODS_ONLY
    out("METHODS %s: the methods the live host's sshd offers root, from outside: %s; ssh exit %s" % (
        label, found, "none, past 60 s" if rc is None else rc))
    out("G-SSH K6 %s alone, from outside: %s" % (",".join(METHODS_ONLY), "PASS" if ok else "FAIL"))
    return 0 if ok else 4


def proc_start_times():
    """The start instant of every running process whose argv[0] is `claude` or ends in `/claude.exe`."""
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    hz = os.sysconf("SC_CLK_TCK")
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                argv = fh.read().split(b"\0")
            with open("/proc/%s/stat" % pid, encoding="utf-8") as fh:
                fields = fh.read().rsplit(")", 1)[1].split()
        except OSError:
            continue
        a0 = argv[0].decode("utf-8", "replace") if argv else ""
        if a0 == "claude" or a0.endswith("/claude.exe"):
            found.append((int(pid), btime + int(fields[19]) / hz, a0))
    return found


def birth(path):
    rc, so, se = run(["stat", "-c", "%W", path])
    assert rc == 0, se
    return int(so.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
    assert is_capture_host(), "BLOCKED: scratch runs on the capture host"
    parent = os.path.dirname(own)
    procs = proc_start_times()
    for pid, t, a0 in procs:
        out("running %d started %s %s" % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        b = birth(path)
        owner = [pid for pid, t, _a in procs if t - 1 <= b <= t + LIVE_S]
        out("%s born %s: %s" % (name, utc(b), ("live, process %s" % owner) if owner else "earlier"))
    return 0


def pristine(tree):
    rc, so, _se = run(["git", "-C", tree, "status", "--porcelain", "--ignored"])
    assert rc == 0 and so == "", "reclaim: %s holds %r" % (tree, so[:400])
    head = git("rev-parse", "HEAD", tree=tree)
    up = git("rev-parse", "@{u}", tree=tree)
    assert up == head, "reclaim: %s is at %s, its upstream at %s" % (tree, head, up)
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def tree_count(root):
    n = 0
    for _d, _s, files in os.walk(root):
        n += len(files)
    return n


def mode_reclaim(trees):
    """The work tree's every file but the worktree's and the wheels into the forensic store, each by exclusive
    create and its SHA-256 checked; an earlier session's directory checked reclaimable and not live."""
    assert is_capture_host(), "BLOCKED: reclaim runs on the capture host"
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
    before = tree_count(FORENSICS)
    considered = copied = held = 0
    for tree in trees:
        if tree != WORK:
            n = sum(len(f) for _d, _s, f in os.walk(tree))
            out("reclaim: %s, an earlier session's directory of %d files: nothing of it is kept" % (tree, n))
            continue
        if os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) not in (WT, TMP, WHEELS))
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)[0]
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    assert sha256_file(dest)[0] == h, "reclaim: %s exists with another sha256" % dest
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, avail = os.path.getsize(path), fs_bytes(FORENSICS)[1]
                assert avail - size >= RECLAIM_FLOOR, "BLOCKED: reclaim: %d bytes available, %s is %d" % (
                    avail, path, size)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = tree_count(FORENSICS)
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d copied, %d already held; the forensic store %d -> %d files" % (
        considered, copied, held, before, after))
    return 0

# ---- the live host's modes, standard library ----------------------------------------------------------------


def mode_host(label):
    """The live host gate, TZ-49's five checks, and the facts L1 starts from: its locale (map section 7 item 185),
    its clock, root's keys by fingerprint and L1's paths by kind, mode, owner and size - never a file's content."""
    assert label in ("before", "after"), "host takes before or after"
    osrel = os_release(read_text("/etc/os-release", "") or "")
    ok, checks = live_gate(short_hostname(), osrel, sys.version_info,
                           [p for p in (CAPTURE_MARK, PRIMARY) if os.path.exists(p)], host_keys())
    for k, v in checks.items():
        out("%s: %s" % (k, "PASS" if v else "FAIL"))
    out("LIVE HOST GATE %s: %d of 5" % ("PASS" if ok else "FAIL", sum(checks.values())))
    if not ok:
        return 1
    floors(LIVE_DISK, LIVE_FLOOR)
    mem = meminfo(read_text("/proc/meminfo", ""))
    total, avail, _free = fs_bytes(LIVE_DISK)
    out("HOST %s: kernel %s; Python %s; %s; MemTotal %d MemAvailable %d SwapTotal %d SwapFree %d; / %d bytes, "
        "%d available" % (label, os.uname().release, sys.version.split()[0], osrel.get("PRETTY_NAME"),
                          mem.get("MemTotal", -1), mem.get("MemAvailable", -1), mem.get("SwapTotal", -1),
                          mem.get("SwapFree", -1), total, avail))
    for ln in (read_text("/etc/default/locale", "") or "").split("\n"):
        if ln.strip() and not ln.lstrip().startswith("#"):
            out("LOCALE /etc/default/locale: %s" % ln.strip())
    rc, so, _se = run(["locale"], env=dict(os.environ))
    out("LOCALE `locale` in this session, exit %d: %s" % (rc, "; ".join(x for x in so.split("\n") if x)))
    rc, so, _se = run(["timedatectl", "show", "-p", "NTP", "-p", "NTPSynchronized", "-p", "TimeUSec"])
    out("CLOCK exit %d: %s" % (rc, "; ".join(x for x in so.split("\n") if x)))
    keys = key_fingerprints(read_text(AUTHORIZED_KEYS, "") or "")
    out("SSHD authorized keys of root: %s; the Executor's among them: %s" % (keys, EXECUTOR_KEY in keys))
    for p in (L1_ETC,) + SECRETS + (L1_VAR, ACCOUNT_FILE) + tuple(rt_paths()) + (L1_ENV, WHEELS):
        out("PATH %s: %s" % (p, file_state(p)))
    return 0


def geo_read(base=("https", GEO_HOST, 443), sleep=time.sleep):
    """G-GEO: up to TRIES reads TRY_GAP_S apart while a reply is unread, over IPv4 alone; printed of each its status,
    its fields and whether the address the venue saw is the connection's own - a comparison, never the address."""
    for k in range(1, TRIES + 1):
        try:
            status, _h, blob, src = http_call(base, "GET", GEO_PATH)
            doc = json_of(blob)
            reading, f = geo_reading(status, doc), geo_fields(doc) or {}
            same = isinstance(doc, dict) and doc.get("ip") == src
            out("G-GEO read %d over IPv4: status %s, %d bytes, blocked %r, country %r, region %r, keys %s; the address "
                "the venue saw is the connection's own: %s -> %s" % (k, status, len(blob), f.get("blocked"),
                                                                     f.get("country"), f.get("region"), f.get("keys"),
                                                                     same, reading))
        except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
            reading = "UNREAD"
            out("G-GEO read %d over IPv4: %s -> UNREAD" % (k, err_of(exc)))
        if reading != "UNREAD":
            return reading
        if k < TRIES:
            sleep(TRY_GAP_S)
    return "UNREAD"


def mode_geoblock():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    r = geo_read()
    out("G-GEO %s" % r)
    return 0 if r == "PASS" else 1


def mode_sshd():
    """G-SSH K1 to K5 on the live host: TZ-49's drop-in, byte for byte, and sshd's configuration in force."""
    assert_live()
    st = None
    if os.path.isfile(SSHD_DROPIN) and not os.path.islink(SSHD_DROPIN):
        st = (sha256_file(SSHD_DROPIN)[0], os.stat(SSHD_DROPIN).st_mode & 0o7777)
    rc, so, se = run(["sshd", "-T"])
    assert rc == 0, "sshd -T: %s" % se.strip()[:300]
    ok, checks = ssh_reading(st, sshd_effective(so))
    for k, v in checks.items():
        out("%s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-SSH K1 to K5 %s: %d of 5" % ("PASS" if ok else "FAIL", sum(checks.values())))
    return 0 if ok else 4


def page_read(base=("https", PAGES_HOST, 443), path=PAGE_PATH, want=None, sleep=time.sleep, tries=PAGE_TRIES):
    """G-PAGE: the signing page as GitHub Pages serves it, read up to `tries` times TRY_GAP_S apart until its bytes
    are TZ-50's Appendix B's - its length and SHA-256 - printed with its status and type."""
    want = want or (PAGE_BYTES, PAGE_SHA256)
    for k in range(1, tries + 1):
        try:
            status, h, blob, _src = http_call(base, "GET", path)
            got = (len(blob), sha256_bytes(blob))
            out("G-PAGE read %d: status %s, content-type %r, %d bytes, sha256 %s: %s" % (
                k, status, h.get("content-type"), got[0], got[1], "equal" if status == 200 and got == want else
                "not TZ-50's page"))
            if status == 200 and got == want:
                return True
        except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
            out("G-PAGE read %d: %s" % (k, err_of(exc)))
        if k < tries:
            sleep(TRY_GAP_S)
    return False


def mode_page():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    ok = page_read()
    out("G-PAGE %s: %s" % ("PASS" if ok else "FAIL", PAGE_URL))
    return 0 if ok else 4


def fetch_wheels(base=("https", PYPI_HOST, 443), dest=WHEELS, wheel_set=None, sleep=time.sleep):
    """G-ENV's first half: every wheel of the set into `dest`, kept where its bytes are the set's, else fetched from
    PyPI over IPv4 and kept where its size and SHA-256 are - the first not served so ending it; then requirements."""
    wheel_set = wheel_set or WHEEL_SET
    if not os.path.isdir(dest):
        os.mkdir(dest, 0o755)
    good = 0
    for fn, size, sha, urlpath in wheel_set:
        path = os.path.join(dest, fn)
        if os.path.isfile(path) and sha256_file(path) == (sha, size):
            good += 1
            out("WHEEL kept       %-64s %9d %s" % (fn[:64], size, sha))
            continue
        blob = None
        for k in range(1, TRIES + 1):
            try:
                status, _h, b, _src = http_call(base, "GET", urlpath, timeout=60)
                if status == 200 and len(b) == size and sha256_bytes(b) == sha:
                    blob = b
                    break
                out("WHEEL %s read %d: status %s, %d bytes, sha256 %s: not the set's" % (
                    fn, k, status, len(b), sha256_bytes(b)))
            except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
                out("WHEEL %s read %d: %s" % (fn, k, err_of(exc)))
            if k < TRIES:
                sleep(TRY_GAP_S)
        if blob is None:
            break                   # one wheel PyPI did not serve whole in three reads ends the fetch: G-ENV FAIL
        with open(path + ".part", "wb") as fh:
            fh.write(blob)
        os.rename(path + ".part", path)
        assert sha256_file(path) == (sha, size), path
        good += 1
        out("WHEEL downloaded %-64s %9d %s" % (fn[:64], size, sha))
    req = requirements_text(wheel_set).encode()
    with open(os.path.join(dest, "requirements.txt"), "wb") as fh:
        fh.write(req)
    out("WHEELS requirements.txt: %d lines, %d bytes, sha256 %s" % (req.count(b"\n"), len(req), sha256_bytes(req)))
    out("G-ENV wheels %s: %d of %d, %d bytes in all" % ("PASS" if good == len(wheel_set) else "FAIL", good,
                                                       len(wheel_set), sum(w[1] for w in wheel_set)))
    return good == len(wheel_set)


def mode_wheels():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    return 0 if fetch_wheels() else 4


class Tty:
    """The Boss's terminal: what he is asked and shown goes there, and to no log. A terminal is never seekable, so it
    is opened as two streams - "r" for his answers, "w" for what he is shown - and never "r+", whose buffered random
    access raised io.UnsupportedOperation at TZ-50's every run (map section 7 item 189). A hidden answer is read by
    getpass, which opens the same terminal itself and turns its echo off while he types. What was typed before a
    question is asked - a pasted line's own newline among it - is discarded when it is asked, as getpass discards it
    before a hidden one, so that no stray line answers the next question."""

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


def ask_until(tty, prompt, ok, hidden=False, tries=3, refusal="Не подходит — попробуйте ещё раз."):
    """An answer the predicate accepts, asked at most `tries` times; None where none was."""
    for _k in range(tries):
        a = tty.ask(prompt, hidden=hidden).strip()
        if ok(a):
            return a
        tty.say(refusal)
    return None


def mode_secrets(tty=None, token_file=TG_TOKEN_FILE, relayer_file=RELAYER_FILE, account_file=ACCOUNT_FILE):
    """The Boss's credentials onto the live host, typed by him at his terminal: the bot's Telegram token and the
    owner's Relayer API key hidden, the key's signer address - the owner - shown. Each written once, by exclusive
    create, 0600, root's; one that is already in place is kept. Printed: written or kept, and the bytes - never a
    value."""
    if tty is None:
        assert_live()
        floors(LIVE_DISK, LIVE_FLOOR)
        tty = Tty()
    tty.say("L1 · ТЗ-51: учётные данные бота. Ввод токенов скрыт; ничего из введённого не попадает в журнал.")
    done = {}
    t = read_text(token_file) if os.path.exists(token_file) else None
    if t is not None and token_ok(t.strip()) and private_file_ok(token_file):
        done["telegram-token"] = "kept"
    else:
        assert t is None, "BLOCKED: %s holds something that is not a bot token: %s" % (token_file, file_state(token_file))
        v = ask_until(tty, "Токен Telegram-бота L1 от BotFather (ввод скрыт): ", token_ok, hidden=True,
                      refusal="Это не токен бота (вида 123456789:AA…). Ещё раз.")
        if v is None:
            out("SECRETS telegram-token: no token in 3 tries")
            return 4
        done["telegram-token"] = "written, %d bytes" % write_private(token_file, (v + "\n").encode())
    r = read_text(relayer_file) if os.path.exists(relayer_file) else None
    if r is not None:
        doc = json_of(r.encode())
        assert isinstance(doc, dict) and relayer_key_ok(doc.get("key")) and valid_address(doc.get("address")) \
            and private_file_ok(relayer_file), "BLOCKED: %s is not a relayer key: %s" % (relayer_file,
                                                                                       file_state(relayer_file))
        owner = valid_address(doc["address"])
        done["relayer-key"] = "kept"
    else:
        key = ask_until(tty, "Ключ API релеера (Relayer API key) — polymarket.com, вкладка «API-ключи» (ввод скрыт): ",
                        relayer_key_ok, hidden=True, refusal="Это не похоже на ключ. Ещё раз.")
        owner = ask_until(tty, "Адрес подписанта (Signer Address) того же ключа — 0x…, адрес аккаунта MetaMask бота: ",
                          valid_address, refusal="Нужен адрес вида 0x и 40 шестнадцатеричных знаков. Ещё раз.")
        if key is None or owner is None:
            out("SECRETS relayer-key: no key or no address in 3 tries")
            return 4
        owner = valid_address(owner)
        body = (json.dumps({"key": key, "address": owner}, sort_keys=True) + "\n").encode()
        done["relayer-key"] = "written, %d bytes" % write_private(relayer_file, body)
    acct = json_of((read_text(account_file) or "").encode()) if os.path.exists(account_file) else None
    if acct is None:
        done["account"] = "written, %d bytes" % write_json_atomic(account_file, {"owner": owner})
    else:
        assert isinstance(acct, dict) and acct.get("owner") == owner, \
            "BLOCKED: %s names another owner than the relayer key's" % account_file
        done["account"] = "kept"
    for k in ("telegram-token", "relayer-key", "account"):
        out("SECRETS %s: %s" % (k, done[k]))
    for p in (token_file, relayer_file, account_file):
        out("PATH %s: %s" % (p, file_state(p)))
    tty.say("Готово: токен бота и ключ Relayer записаны на сервер.")
    return 0


def mode_bosskey(tty=None, path=AUTHORIZED_KEYS):
    """The Boss's own SSH public key appended to root's authorized_keys - one line, a public key of a known type -
    or none where he gives none. Printed: its type and fingerprint, and root's keys by fingerprint."""
    if tty is None:
        assert_live()
        tty = Tty()
    before = key_fingerprints(read_text(path, "") or "")
    got = None
    for _k in range(3):
        line = tty.ask("Публичный ключ из Termius (одна строка ssh-ed25519 …) — или просто Enter, чтобы пропустить: ")
        if not line.strip():
            out("BOSSKEY skipped: no key given; root's keys by fingerprint: %s" % before)
            tty.say("Пропущено: вход на этот сервер остаётся через «ssh live-host» с сервера в Варшаве.")
            return 0
        try:
            got = pubkey_line(line)
            break
        except ValueError as exc:
            tty.say("Это не публичный ключ (%s). В Termius: Keychain → ключ → Copy public key." % exc)
            out("BOSSKEY refused a line: %s" % exc)
    if got is None:
        return 4
    full, kind, fp, bits = got
    if (kind, fp) in before:
        out("BOSSKEY present already: %s %s; root's keys by fingerprint: %s" % (kind, fp, before))
        tty.say("Этот ключ уже стоит на сервере: %s" % fp)
        return 0
    text = read_text(path, "") or ""
    with open(path, "a", encoding="utf-8") as fh:
        if text and not text.endswith("\n"):
            fh.write("\n")
        fh.write(full + "\n")
    after = key_fingerprints(read_text(path, "") or "")
    assert (kind, fp) in after and len(after) == len(before) + 1, "BOSSKEY: %r" % (after,)
    out("BOSSKEY added: %s %s%s; root's keys by fingerprint: %s" % (kind, fp, "" if bits is None else ", %d bits" % bits,
                                                                    after))
    tty.say("Ключ добавлен: %s. Вход в Termius напрямую теперь работает этим ключом." % fp)
    return 0

# ---- Telegram: the Bot API through one request function -------------------------------------------------------


class Telegram:
    """Every call a JSON POST with this TZ's agent; the token is in the path and in no printed line."""

    def __init__(self, token, base=("https", TG_HOST, 443)):
        self.token, self.base = token, base

    def call(self, method, http_timeout=30, **params):
        status, _h, blob, _src = http_call(self.base, "POST", "/bot%s/%s" % (self.token, method), body=params,
                                           timeout=http_timeout)
        doc = json_of(blob)
        if not (isinstance(doc, dict) and doc.get("ok") is True):
            code = doc.get("error_code") if isinstance(doc, dict) else status
            desc = doc.get("description") if isinstance(doc, dict) else None
            raise RuntimeError("telegram %s: %s %s" % (method, code, desc))
        return doc["result"]


def read_token(path=TG_TOKEN_FILE):
    assert private_file_ok(path), "BLOCKED: %s: %s" % (path, file_state(path))
    t = (read_text(path) or "").strip()
    assert token_ok(t), "BLOCKED: %s holds no bot token" % path
    return t


def mode_tg_probe(tg=None):
    """G-TG's first check: getMe answers is_bot and a username, getMyCommands a list; the name is not printed."""
    if tg is None:
        assert_live()
        tg = Telegram(read_token())
    me = tg.call("getMe")
    cmds = tg.call("getMyCommands")
    ok = isinstance(me, dict) and me.get("is_bot") is True and bool(me.get("username")) and isinstance(cmds, list)
    out("G-TG getMe: a bot with a username - its name withheld, as a public report would publish it - %d commands in "
        "its menu: %s" % (len(cmds) if isinstance(cmds, list) else -1, "PASS" if ok else "FAIL"))
    return 0 if ok else 4


def mode_find_chat(tg=None, chat_file=CHAT_FILE, wait_s=TG_WAIT_S):
    """G-TG's second check: the one private chat that sent /start to the bot, pinned to chat_file, 0600, by exclusive
    create; a chat already pinned is kept. Waits up to wait_s for a /start. Prints counts only, never a chat id."""
    if tg is None:
        assert_live()
        tg = Telegram(read_token())
    if os.path.exists(chat_file):
        c = (read_text(chat_file) or "").strip()
        assert re.fullmatch(r"-?[0-9]+", c) and private_file_ok(chat_file), "BLOCKED: %s: %s" % (
            chat_file, file_state(chat_file))
        out("G-TG chat: pinned already, kept")
        return 0
    deadline, said, offset = time.time() + wait_s, False, {}
    while True:
        ups = tg.call("getUpdates", http_timeout=80, timeout=min(50, max(1, int(deadline - time.time()))),
                      allowed_updates=["message"], **offset)
        private = private_starts(ups)
        if len(private) == 1:
            break
        if len(private) > 1 or time.time() >= deadline:
            out("G-TG chat: updates %d, private chats that sent /start: %d - FAIL" % (len(ups), len(private)))
            return 1
        if ups:
            offset = {"offset": ups[-1]["update_id"] + 1}
        if not said:
            out("G-TG chat: no /start among %d pending updates; waiting up to %d s for the Boss's /start" % (
                len(ups), wait_s))
            said = True
    write_private(chat_file, ("%d\n" % private[0]).encode())
    out("G-TG chat: updates %d, private chats that sent /start: 1, pinned to %s" % (len(ups), chat_file))
    return 0


def report_text(rt, acct):
    """The round trip's report to the Boss's chat, in Russian, from its record: no address, id or hash. Pure."""
    ok, _checks = rt_reading(rt)
    live = [p for p in rt.get("placements", []) if p.get("result") == "live"]
    until = acct.get("valid_until")
    lines = ["L1 · ТЗ-51 · счёт бота и первый ордер",
             "• Сессионный ключ разрешён владельцем: только ордера CLOB, вывод средств ему недоступен%s." % (
                 ", до %s UTC" % utc(until)[:10] if isinstance(until, int) else ""),
             "• Ордер: покупка %s %s по %s (post-only) на %s — %s." % (
                 RT_SIZE, live[0]["side"] if live else "—", RT_PRICE, rt.get("market", "—"),
                 "выставлен за %s мс, отменён за %s мс" % (live[0].get("ms"), rt.get("cancel_ms")) if live
                 else "не выставлен"),
             "• Баланс: %s pUSD до и %s pUSD после; открытых ордеров нет: %s." % (
                 units(rt.get("balance_before")), units(rt.get("balance_after")),
                 "да" if rt.get("open_after") == 0 and rt.get("wallet_open_after") == 0 else "нет"),
             "• Итог: %s." % ("ордер туда и обратно прошёл" if ok else "проверка не пройдена — смотрите отчёт ТЗ-51"),
             "Кнопка «Стоп» и отчёты работающего бота появятся вместе с ним — в следующем ТЗ."]
    return "\n".join(lines)


def units(v):
    """Six-decimal collateral units as pUSD. Pure."""
    return "%d.%06d" % divmod(v, 1000000) if isinstance(v, int) and v >= 0 else "—"


def rt_paths(root=L1_VAR):
    """The round trip's records under `root`, in run order."""
    if not os.path.isdir(root):
        return []
    found = sorted((int(m.group(1)), n) for n in os.listdir(root) for m in [RT_RECORD.fullmatch(n)] if m)
    return [os.path.join(root, n) for _i, n in found]


def mode_tg_report(tg=None, root=L1_VAR, account_file=ACCOUNT_FILE, chat_file=CHAT_FILE):
    """G-TG's third check: the last round trip's report sent to the pinned chat; the text printed, its message id."""
    if tg is None:
        assert_live()
        tg = Telegram(read_token())
    paths = rt_paths(root)
    assert paths, "BLOCKED: no round trip recorded under %s" % root
    rt = json_of((read_text(paths[-1]) or "").encode())
    acct = json_of((read_text(account_file) or "").encode())
    assert isinstance(rt, dict) and isinstance(acct, dict), "BLOCKED: no round trip or no account record"
    assert private_file_ok(chat_file), "BLOCKED: %s: %s" % (chat_file, file_state(chat_file))
    chat = int((read_text(chat_file) or "").strip())
    text = report_text(rt, acct)
    msg = tg.call("sendMessage", chat_id=chat, text=text, disable_web_page_preview=True)
    ok = isinstance(msg, dict) and isinstance(msg.get("message_id"), int)
    for ln in text.split("\n"):
        out("G-TG report | %s" % ln)
    out("G-TG report sent: %s" % ("PASS, message %d" % msg["message_id"] if ok else "FAIL"))
    return 0 if ok else 4

# ---- the venue's client: /root/l1-env, polymarket-client 0.20.0 ----------------------------------------------


def client():
    """The venue's client, made ready in this process: every lookup through gai4, every request with this TZ's
    agent; its pinned version and the terms this file relies on asserted. Returns the names the modes use."""
    import dataclasses
    import importlib.metadata as md
    socket.getaddrinfo = gai4
    import httpx
    import httpx._client
    httpx._client.USER_AGENT = UA
    from eth_account import Account
    from eth_account.messages import encode_typed_data
    from eth_utils import to_checksum_address
    from polymarket import AsyncSecureClient, RelayerApiKey
    from polymarket.clients._transport import AsyncTransport
    from polymarket.environments import PRODUCTION, _create_environment
    from polymarket.errors import RequestRejectedError
    from polymarket.models.clob.relayer import RelayerTransactionType
    from polymarket.transactions import GaslessTransactionHandle
    from polymarket._internal import protocol as P
    from polymarket._internal import wallet as W
    from polymarket._internal.actions import account as A
    from polymarket._internal.actions import session_keys as S
    from polymarket._internal.actions.orders.context import resolve_order_exchange_address
    from polymarket._internal.actions.relayer import calls as C
    from polymarket._internal.actions.relayer import gasless as G
    from polymarket._internal.actions.relayer.auth import make_relayer_header_resolver
    from polymarket._internal.actions.relayer.deployed import fetch_deployed
    from polymarket._internal.actions.relayer.nonce import fetch_execute_params
    from polymarket._internal.actions.relayer.submit import submit_gasless
    from polymarket._internal.actions.relayer.signing.deposit_wallet import build_deposit_wallet_typed_data
    assert md.version(SDK_DIST) == SDK_VERSION, "the client is %s, not %s" % (md.version(SDK_DIST), SDK_VERSION)
    assert S._SESSION_KEY_LIFETIME_SECONDS == LIFETIME_S and G._DEPOSIT_WALLET_DEADLINE_S == DEADLINE_S
    assert C._DEPOSIT_WALLET_AUTHORIZE_SESSION_SIGNER_SELECTOR.hex() == SELECTORS["authorize"]
    assert C._DEPOSIT_WALLET_REVOKE_SESSION_SIGNER_SELECTOR.hex() == SELECTORS["revoke"]
    assert (C._ERC20_APPROVE_SELECTOR.hex(), C._ERC20_ALLOWANCE_SELECTOR.hex()) == (APPROVE_SEL, ALLOWANCE_OF)
    assert P._V2_RESERVED_BITS_MASK == V2_RESERVED, "the client's V2 position IDs"
    cfg = PRODUCTION._config
    assert (cfg.collateral_token, cfg.standard_exchange, cfg.exchange_v3) == (PUSD,) + tuple(a for _x, a in EXCHANGES), \
        "the client's collateral and exchanges"
    assert (cfg.chain_id, cfg.clob_url, cfg.relayer_url, cfg.gamma_url, cfg.rpc_url) == (
        CHAIN_ID, "https://" + CLOB_HOST, "https://" + RELAYER_HOST, "https://" + GAMMA_HOST, "https://" + RPC_HOST), \
        "the client's hosts"
    return types.SimpleNamespace(**{k: v for k, v in locals().items() if k != "md"})


def test_env(k, base_url):
    """An environment of the client whose CLOB, relayer and gamma are the self-test's loopback stand-in."""
    cfg = k.dataclasses.replace(k.PRODUCTION._config, clob_url=base_url + "/clob", relayer_url=base_url + "/relayer",
                                gamma_url=base_url + "/gamma", rpc_url=base_url + "/rpc", relayer_poll_frequency_ms=50,
                                relayer_max_polls=40)
    return k._create_environment(name="tz51-selftest", config=cfg)


def load_session_key(path=SESSION_KEY_FILE):
    assert private_file_ok(path), "BLOCKED: %s: %s" % (path, file_state(path))
    v = (read_text(path) or "").strip()
    assert re.fullmatch(r"0x[0-9a-f]{64}", v), "BLOCKED: %s holds no key" % path
    return v


def load_relayer(path=RELAYER_FILE):
    assert private_file_ok(path), "BLOCKED: %s: %s" % (path, file_state(path))
    doc = json_of((read_text(path) or "").encode())
    assert isinstance(doc, dict) and relayer_key_ok(doc.get("key")) and valid_address(doc.get("address")), \
        "BLOCKED: %s holds no relayer key" % path
    return doc["key"], valid_address(doc["address"])


def load_account(path=ACCOUNT_FILE):
    doc = json_of((read_text(path) or "").encode())
    assert isinstance(doc, dict) and valid_address(doc.get("owner")), "BLOCKED: %s holds no account" % path
    return doc


async def first_items(paginator):
    page = await paginator.first_page()
    return list(page.items)


async def resolve_wallet(k, owner, rt, cfg):
    """The owner's Deposit Wallet, as the client resolves a default one: the legacy derivation where the relayer
    reads it deployed, else the beacon derivation, which must read deployed."""
    uups = k.W.derive_uups_deposit_wallet_address(owner, cfg.wallet_derivation)
    if await k.fetch_deployed(rt, address=uups, type=k.RelayerTransactionType.WALLET):
        return uups, "legacy"
    beacon = k.W.derive_beacon_deposit_wallet_address(owner, cfg.wallet_derivation)
    assert await k.fetch_deployed(rt, address=beacon, type=k.RelayerTransactionType.WALLET), \
        "BLOCKED: the owner's Deposit Wallet is not deployed"
    return beacon, "beacon"


async def registered(k, env, key_hex, wallet, session, want, tries=READY_TRIES, gap=READY_GAP_S, sleep=None):
    """Whether the session key acts for the wallet - its client made and the wallet's orders listed by it - read
    up to `tries` times `gap` apart until the reading is `want`. Returns the last reading."""
    sleep = sleep or asyncio.sleep
    state = None
    for i in range(1, tries + 1):
        try:
            c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=wallet, environment=env)
            try:
                assert c.wallet_type == "DEPOSIT_WALLET" and c._ctx.signer_type == "SESSION_KEY", "not a session key"
                items = await first_items(c.list_wallet_open_orders(signer_addresses=[session]))
                state = True
                out("KEY read %d: the session key lists the wallet's orders - %d on the first page" % (i, len(items)))
            finally:
                await c.close()
        except k.RequestRejectedError as exc:
            state = False
            out("KEY read %d: refused, status %s" % (i, exc.status))
        if state is want:
            return state
        if i < tries:
            await sleep(gap)
    return state


async def authorize_kept(k, env, key_hex, acct):
    """Whether an earlier run's authorization of this key stands - the account records it for this key, unrevoked,
    and the key acts for the wallet at one read - so that a second run of the Boss's paste asks for no signature."""
    session = k.Account.from_key(key_hex).address
    if not (acct.get("authorized_at") and acct.get("session_key") == session.lower() and acct.get("wallet")
            and not acct.get("revoked_at")):
        return False
    return (await registered(k, env, key_hex, acct["wallet"], session, want=True, tries=1)) is True


def ask_signature(k, op, tty, td, owner_cs, deadline, link, now):
    """One link's answers at the terminal: the owner's signature of the typed data `td`, recovered to the owner by
    the client's own encoding; None where none came in SIGNATURE_TRIES answers, an empty answer asks for a new
    link, or it came within ten seconds of the link's deadline."""
    for t in range(1, SIGNATURE_TRIES + 1):
        ans = tty.ask("Подпись из MetaMask (0x…), или просто Enter — новая ссылка: ").strip()
        if not ans:
            break
        if not re.fullmatch(r"0x[0-9a-fA-F]{130}", ans):
            tty.say("Это не подпись: нужно 0x и 130 шестнадцатеричных знаков.")
            out("OWNER %s link %d answer %d: not a signature" % (op, link, t))
            continue
        try:
            rec = k.Account.recover_message(k.encode_typed_data(full_message=td), signature=ans)
        except Exception:   # an unrecoverable signature is the same answer as another signer's
            rec = None
        if rec != owner_cs:
            tty.say("Подпись не владельца для этой ссылки: подпишите ссылку выше аккаунтом владельца.")
            out("OWNER %s link %d answer %d: a signature, not the owner's for this batch" % (op, link, t))
            continue
        if int(now()) > int(deadline) - 10:
            tty.say("Срок этой ссылки истёк — вот новая.")
            out("OWNER %s link %d: the owner's signature, past its deadline" % (op, link))
            return None
        out("OWNER %s link %d: the owner's signature, recovered to the owner under the client's own typed data" % (
            op, link))
        return ans
    out("OWNER %s link %d: no owner's signature" % (op, link))
    return None


async def owner_flow(k, op, env, tty, key_hex, relayer_key, owner, page_url=PAGE_URL, now=time.time):
    """authorize or revoke: the owner's signature of one Deposit Wallet batch, made in MetaMask on the Boss's device
    from the signing page's link, checked to recover to the owner, submitted to the relayer with his Relayer API key
    and its transaction confirmed. Every part but the signature is the client's own code. Returns (wallet, session,
    valid_until) or None where no signature came."""
    cfg = env._config
    owner_cs = k.to_checksum_address(owner)
    rt = k.AsyncTransport(base_url=cfg.relayer_url, header_resolver=k.make_relayer_header_resolver(
        k.RelayerApiKey(key=relayer_key, address=owner_cs)))
    try:
        wallet, how = await resolve_wallet(k, owner_cs, rt, cfg)
        session = k.Account.from_key(key_hex).address
        out("OWNER %s: the owner's Deposit Wallet derived (%s) and deployed; the addresses withheld" % (op, how))
        for link in range(1, LINKS + 1):
            if op == "authorize":
                req = k.S._parse_authorize_session_key_request(address=session, scopes=list(SCOPES), idempotency_key=None)
                call = k.C.authorize_session_signer_call(wallet_address=wallet, session_signer=req.address,
                                                         valid_until=req.valid_until_epoch)
                until = req.valid_until_epoch
            else:
                req = k.S._parse_revoke_session_key_request(address=session, idempotency_key=None)
                call = k.C.revoke_session_signer_call(wallet_address=wallet, session_signer=req.address)
                until = None
            nonce = (await k.fetch_execute_params(rt, address=owner_cs, type=k.RelayerTransactionType.WALLET)).nonce
            deadline = str(int(now()) + DEADLINE_S)
            td = k.build_deposit_wallet_typed_data(wallet=wallet, calls=[call], nonce=nonce, deadline=deadline,
                                                   chain_id=cfg.chain_id)
            url = sign_link(op, owner_cs, wallet, session, nonce, deadline, until, url=page_url)
            tty.say("")
            tty.say("%s сессионного ключа бота. Владелец: %s" % ("Разрешение" if op == "authorize" else "Отзыв", owner_cs))
            tty.say("Кошелёк бота (Deposit Wallet): %s" % wallet)
            tty.say("Сессионный ключ: %s%s" % (session, ", только ордера CLOB, до %s UTC" % utc(until) if until else ""))
            tty.say("Откройте эту ссылку во встроенном браузере MetaMask (аккаунт бота), проверьте ключ и подпишите;"
                    " ссылка действует до %s UTC:" % utc(int(deadline))[11:19])
            tty.say(url)
            sig = ask_signature(k, op, tty, td, owner_cs, deadline, link, now)
            if sig is None:
                continue
            batch = k.G.SignedDepositWalletBatch(nonce=nonce, deadline=deadline, signature=sig)
            ctx = types.SimpleNamespace(wallet=wallet, relayer=rt, environment_config=cfg)
            if op == "authorize":
                payload = k.S._build_authorization_payload(ctx, request=req, batch=batch)
                path, parse = k.S._AUTHORIZATIONS_PATH, k.S._AuthorizeSessionKeyResponse.parse_response
            else:
                payload = k.S._build_revocation_payload(ctx, request=req, batch=batch)
                path, parse = k.S._REVOCATIONS_PATH, k.S._RevokeSessionKeyResponse.parse_response
            resp = await k.S._post_session_key_operation(ctx, path=path, payload=payload,
                                                          idempotency_key=req.idempotency_key, parse=parse)
            (k.S._assert_authorization_accepted if op == "authorize" else k.S._assert_revocation_accepted)(resp.status)
            out("OWNER %s: the relayer accepted the request, status %s" % (op, resp.status))
            await k.GaslessTransactionHandle(transaction_id=resp.transaction_id,
                                             transaction_hash=getattr(resp, "transaction_hash", None), _relayer=rt,
                                             _max_polls=cfg.relayer_max_polls,
                                             _poll_delay_s=cfg.relayer_poll_frequency_ms / 1000).wait()
            out("OWNER %s: the relayer's transaction confirmed" % op)
            return wallet, session, until
        return None
    finally:
        await rt.close()


async def approve_flow(k, env, tty, relayer_key, owner, page_url=PAGE_URL, now=time.time, sleep=None):
    """approve: where the wallet's pUSD allowance on chain to either exchange is under one order's cost or above
    APPROVE_UNITS - the maximum polymarket.com may have set among it - the owner's signature of one Deposit Wallet
    batch of approve(exchange, APPROVE_UNITS) on pUSD for each such exchange, which sets its allowance to 1 pUSD,
    never more: what a stolen session key could spend through it (CANON PART IV). Made in MetaMask from the signing
    page's link, recovered to the owner, submitted to the relayer with his Relayer API key and confirmed, and the
    allowances read on chain again. Every part but the signature is the client's own code. Returns (wallet, before,
    after): after is before where every allowance was in bounds, None where no signature came."""
    sleep = sleep or asyncio.sleep
    cfg = env._config
    owner_cs = k.to_checksum_address(owner)
    rt = k.AsyncTransport(base_url=cfg.relayer_url, header_resolver=k.make_relayer_header_resolver(
        k.RelayerApiKey(key=relayer_key, address=owner_cs)))
    try:
        wallet, how = await resolve_wallet(k, owner_cs, rt, cfg)
        before = await chain_allowances(k, env, wallet)
        out("OWNER approve: the owner's Deposit Wallet derived (%s) and deployed; its pUSD allowances on chain %s" % (
            how, shown(before)))
        short = [(x, a) for x, a in EXCHANGES if not bounded(before[x])]
        if not short:
            out("OWNER approve: every allowance between one order's cost and 1 pUSD - kept, nothing to sign")
            return wallet, before, before
        calls = [k.C.erc20_approval_call(token_address=PUSD, spender=a, amount=APPROVE_UNITS) for _x, a in short]
        letters = "".join(x for x, _a in short)
        for link in range(1, LINKS + 1):
            nonce = (await k.fetch_execute_params(rt, address=owner_cs, type=k.RelayerTransactionType.WALLET)).nonce
            deadline = str(int(now()) + DEADLINE_S)
            td = k.build_deposit_wallet_typed_data(wallet=wallet, calls=calls, nonce=nonce, deadline=deadline,
                                                   chain_id=cfg.chain_id)
            url = sign_link("approve", owner_cs, wallet, None, nonce, deadline, url=page_url, exchanges=letters)
            tty.say("")
            tty.say("Разрешение %s Polymarket списывать pUSD кошелька бота для исполнения его ордеров — %s %s pUSD. "
                    "Владелец: %s" % ("двум биржам" if len(short) == 2 else "бирже", "каждой не больше" if len(short) == 2
                                      else "не больше", units(APPROVE_UNITS).rstrip("0").rstrip("."), owner_cs))
            tty.say("Кошелёк бота (Deposit Wallet): %s" % wallet)
            for x, a in short:
                tty.say("Биржа для рынков %s: %s — сейчас разрешено %s" % (
                    "протокола V2" if x == "v" else "CTF", a,
                    "без ограничения" if shown(before)[x] == "max" else "%s pUSD" % shown(before)[x]))
            tty.say("Откройте эту ссылку во встроенном браузере MetaMask (аккаунт бота), проверьте биржи и подпишите;"
                    " ссылка действует до %s UTC:" % utc(int(deadline))[11:19])
            tty.say(url)
            sig = ask_signature(k, "approve", tty, td, owner_cs, deadline, link, now)
            if sig is None:
                continue
            payload = k.G.build_deposit_wallet_payload(
                signer_address=owner_cs, deposit_wallet_factory=cfg.wallet_derivation.deposit_wallet_factory,
                wallet=wallet, calls=calls, nonce=nonce, deadline=deadline, signature=sig, metadata=APPROVE_METADATA)
            try:
                resp = await k.submit_gasless(rt, payload=payload)
            except k.RequestRejectedError as exc:
                tty.say("Релейер не принял эту подпись — вот новая ссылка.")
                out("OWNER approve link %d: the relayer refused the batch, status %s" % (link, exc.status))
                continue
            out("OWNER approve: the relayer accepted the batch of %d, state %s" % (len(calls), resp.state))
            await k.GaslessTransactionHandle(transaction_id=resp.transaction_id, transaction_hash=resp.transaction_hash,
                                             _relayer=rt, _max_polls=cfg.relayer_max_polls,
                                             _poll_delay_s=cfg.relayer_poll_frequency_ms / 1000).wait()
            out("OWNER approve: the relayer's transaction confirmed")
            after = None
            for i in range(1, READY_TRIES + 1):
                after = await chain_allowances(k, env, wallet)
                out("OWNER approve read %d: allowances on chain %s" % (i, shown(after)))
                if all(bounded(v) for v in after.values()):
                    break
                if i < READY_TRIES:
                    await sleep(READY_GAP_S)
            return wallet, before, after
        return wallet, before, None
    finally:
        await rt.close()


def record_claims(md):
    """Every installed file a distribution's RECORD lists with a hash, and each such file's own hash in the RECORD's
    form - urlsafe base64 of its SHA-256, no padding: (claims, actual) for record_reading."""
    claims, actual = [], {}
    for d in md.distributions():
        name = re.sub(r"[-_.]+", "-", d.metadata["Name"]).lower()
        for f in d.files or ():
            if f.hash is None:
                continue
            assert f.hash.mode == "sha256", "%s: a RECORD hash of %s" % (name, f.hash.mode)
            p = os.path.realpath(str(f.locate()))
            claims.append((name, p, f.hash.value))
            if p not in actual:
                try:
                    with open(p, "rb") as fh:
                        actual[p] = base64.urlsafe_b64encode(hashlib.sha256(fh.read()).digest()).rstrip(b"=").decode()
                except FileNotFoundError:
                    actual[p] = None
    return claims, actual


def mode_env():
    """G-ENV's second half, in /root/l1-env: the distributions installed are the pins, none missing, extra or at
    another version; every file their RECORDs list with a hash is at that hash; the interpreter is this venv's; the
    client's terms are this file's."""
    import importlib.metadata as md
    ok_prefix = os.path.realpath(sys.prefix) == L1_ENV
    found = {}
    for d in md.distributions():
        found[re.sub(r"[-_.]+", "-", d.metadata["Name"]).lower()] = d.version
    ok, missing, extra, wrong = installed_reading(found, pins())
    rec_ok, entries, paths, multi, absent, other = record_reading(*record_claims(md))
    k = client()
    out("ENV interpreter %s, prefix %s: %s" % (sys.version.split()[0], sys.prefix, "PASS" if ok_prefix else "FAIL"))
    out("ENV distributions: %d installed, %d pinned; missing %s, extra %s, another version %s" % (
        len(found), len(pins()), missing, extra, wrong))
    out("ENV files: %d RECORD entries with a SHA-256 over %d paths, %d of them listed by two distributions; absent %s, "
        "another hash %s" % (entries, paths, multi, absent, other))
    out("ENV the client %s %s; session keys %d s, a batch %d s; selectors %s; hosts %s, %s, %s" % (
        SDK_DIST, SDK_VERSION, LIFETIME_S, DEADLINE_S, SELECTORS, k.cfg.clob_url, k.cfg.relayer_url, k.cfg.gamma_url))
    good = ok and ok_prefix and rec_ok
    out("G-ENV installed %s" % ("PASS" if good else "FAIL"))
    return 0 if good else 4


def mode_key(path=SESSION_KEY_FILE):
    """G-KEY: the session key made once on this host - a fresh secp256k1 key from os.urandom by eth_account - into
    its own file by exclusive create, 0600, root's; read back and its address re-derived. Never printed, hashed or
    copied; a key already in place is kept."""
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    k = client()
    if os.path.exists(path):
        load_session_key(path)
        out("G-KEY %s: present, kept; %s" % (path, file_state(path)))
        return 0
    acct = k.Account.create()
    write_private(path, ("0x%s\n" % acct.key.hex().removeprefix("0x")).encode())
    back = load_session_key(path)
    assert k.Account.from_key(back).address == acct.address, "the key read back is not the key made"
    del acct, back
    out("G-KEY %s: made; %s; read back and its address re-derived equal; address withheld" % (path, file_state(path)))
    return 0


def mode_owner(op):
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    k = client()
    tty = Tty()
    acct = load_account()
    relayer_key, owner = load_relayer()
    assert acct["owner"] == owner, "BLOCKED: the account's owner is not the relayer key's"
    if op == "approve":
        wallet, before, after = asyncio.run(approve_flow(k, k.PRODUCTION, tty, relayer_key, owner))
        assert acct.get("wallet") in (None, wallet.lower()), "BLOCKED: the account's wallet is another"
        good = after is not None and all(bounded(v) for v in after.values())
        acct.update({"wallet": wallet.lower(), "allowances": shown(after if after is not None else before)})
        if good and after is not before:
            acct["approved_at"] = int(time.time())
        write_json_atomic(ACCOUNT_FILE, acct)
        out("G-APPROVE %s: allowances on chain %s, each between one order's cost and 1 pUSD: %s" % (
            "PASS" if good else "FAIL", acct["allowances"], good))
        tty.say("Готово: биржи могут исполнять ордера бота." if good else
                "Не получилось — исполнитель увидит причину в журнале.")
        return 0 if good else 4
    key_hex = load_session_key()
    if op == "authorize" and asyncio.run(authorize_kept(k, k.PRODUCTION, key_hex, acct)):
        out("G-AUTH authorize PASS: kept - the key authorized at %s acts for the wallet; nothing signed" % (
            utc(acct["authorized_at"])))
        tty.say("Ключ уже разрешён и работает — подписывать ничего не нужно.")
        return 0
    got = asyncio.run(owner_flow(k, op, k.PRODUCTION, tty, key_hex, relayer_key, owner))
    if got is None:
        out("G-AUTH %s FAIL: no owner's signature in %d links" % (op, LINKS))
        return 4
    wallet, session, until = got
    state = asyncio.run(registered(k, k.PRODUCTION, key_hex, wallet, session, want=(op == "authorize")))
    good = state is (op == "authorize")
    acct.update({"wallet": wallet.lower(), "session_key": session.lower(), "scopes": list(SCOPES)})
    if op == "authorize" and good:
        acct.update({"valid_until": until, "authorized_at": int(time.time())})
    if op == "revoke" and good:
        acct["revoked_at"] = int(time.time())
    write_json_atomic(ACCOUNT_FILE, acct)
    out("G-AUTH %s %s: the key %s for the wallet" % (op, "PASS" if good else "FAIL",
                                                      "acts" if state else "does not act"))
    tty.say("Готово: ключ %s." % ("разрешён и работает" if op == "authorize" else "отозван") if good else
            "Не получилось — исполнитель увидит причину в журнале.")
    return 0 if good else 4


def _word(address):
    return address.lower().removeprefix("0x").rjust(64, "0")


async def chain_call(k, env, data):
    """One eth_call on the collateral token through the client's own RPC with this TZ's agent: the 32-byte result
    as a number, None where the reply is not one."""
    cfg = env._config
    body = {"jsonrpc": "2.0", "id": 1, "method": "eth_call",
            "params": [{"to": cfg.collateral_token, "data": data}, "latest"]}
    async with k.httpx.AsyncClient(timeout=TIMEOUT_S) as h:
        r = await h.post(cfg.rpc_url, json=body)
        COUNTS["requests"] += 1
    try:
        res = r.json().get("result")
        return int(res, 16) if r.status_code == 200 and isinstance(res, str) and re.fullmatch(r"0x[0-9a-fA-F]{1,64}", res) \
            else None
    except ValueError:
        return None


async def chain_balance(k, env, wallet):
    """The wallet's pUSD on chain: balanceOf(wallet)."""
    return await chain_call(k, env, "0x" + BALANCE_OF + _word(wallet))


async def chain_allowances(k, env, wallet):
    """The wallet's pUSD allowance on chain to each exchange, by its letter: allowance(wallet, exchange)."""
    return {x: await chain_call(k, env, "0x" + ALLOWANCE_OF + _word(wallet) + _word(a)) for x, a in EXCHANGES}


def enough(v):
    return isinstance(v, int) and v >= RT_COST_UNITS


def bounded(v):
    """An allowance G-APPROVE keeps: at least one order's cost and at most APPROVE_UNITS. Pure."""
    return enough(v) and v <= APPROVE_UNITS


def shown(allowances):
    """Allowances as printed: pUSD, or max at 2^255 and above. Pure."""
    return {x: ("max" if isinstance(v, int) and v >= 1 << 255 else units(v)) for x, v in (allowances or {}).items()}


async def clob_refresh(k, c):
    """The CLOB's view of the wallet's pUSD and allowances re-read from chain: /balance-allowance/update, as the
    client's own allowance recovery calls it."""
    path, params = k.A.build_update_balance_allowance_request(
        asset_type="COLLATERAL", signature_type=k.W.signature_type_for(c._ctx.wallet_type))
    await c._ctx.secure_clob.get_bytes(path, params=params)
    COUNTS["requests"] += 1


async def ready_flow(k, env, key_hex, acct):
    """G-READY: the account read through the session key - a Deposit Wallet signed for by a session key, not in
    closed-only mode, its pUSD on chain at least one order's cost, its pUSD allowance on chain to each exchange at
    least that and at most 1 pUSD, and no open order of the key. The CLOB's own view, refreshed first, is printed
    beside, no threshold."""
    c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=acct["wallet"], environment=env)
    try:
        session = k.Account.from_key(key_hex).address
        await clob_refresh(k, c)
        ba = await c.get_balance_allowance(asset_type="COLLATERAL")
        onchain = await chain_balance(k, env, acct["wallet"])
        allow = await chain_allowances(k, env, acct["wallet"])
        checks = {
            "a Deposit Wallet signed for by a session key": c.wallet_type == "DEPOSIT_WALLET"
            and c._ctx.signer_type == "SESSION_KEY",
            "not in closed-only mode": (await c.get_closed_only_mode()) is False,
            "its pUSD on chain at least one order's cost": enough(onchain),
            "its allowance on chain to the CTF exchange between one order's cost and 1 pUSD": bounded(allow["c"]),
            "its allowance on chain to the V2 exchange between one order's cost and 1 pUSD": bounded(allow["v"]),
            "no open order of the key": len(await first_items(c.list_open_orders())) == 0,
            "no open order of the wallet by the key": len(await first_items(
                c.list_wallet_open_orders(signer_addresses=[session]))) == 0}
        out("READY pUSD on chain %s, allowances on chain %s; the CLOB's view %s pUSD, allowances %d, at least one "
            "order's cost %d" % (units(onchain), shown(allow), units(ba.balance), len(ba.allowances),
                                 sum(1 for v in ba.allowances.values() if v >= RT_COST_UNITS)))
        return checks
    finally:
        await c.close()


def mode_ready():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    k = client()
    checks = asyncio.run(ready_flow(k, k.PRODUCTION, load_session_key(), load_account()))
    for name, v in checks.items():
        out("G-READY %s: %s" % (name, "PASS" if v else "FAIL"))
    ok = all(checks.values())
    out("G-READY %s: %d of %d" % ("PASS" if ok else "FAIL", sum(checks.values()), len(checks)))
    return 0 if ok else 4


def dec(v):
    """A decimal as the venue would print it, normalized: 0.01, 5, 0. Pure."""
    import decimal
    d = decimal.Decimal(str(v)).normalize()
    return format(d, "f") if d != 0 else "0"


async def gamma_market(k, env, t0):
    """The five-minute market of window t0, its gamma document read with this TZ's agent - its tokens and condition
    taken, no price read."""
    async with k.httpx.AsyncClient(base_url=env._config.gamma_url, timeout=TIMEOUT_S) as h:
        r = await h.get("/markets/slug/%s%d" % (RT_FAMILY, t0))
        COUNTS["requests"] += 1
        return r.status_code, (r.json() if r.status_code == 200 else None)


async def roundtrip_flow(k, env, key_hex, acct, now=time.time, sleep=None, perf=time.perf_counter_ns):
    """G-RT's record: one post-only BUY of RT_SIZE at RT_PRICE, GTC, in the five-minute market open at placement -
    its Up token, its Down token where the first crosses the book - read back, cancelled by its id, read back, and
    the key's and the wallet's open orders and the balance read after. The market's own close is the venue's net
    under a resting order; cancel_all is this flow's last act whatever happened."""
    sleep = sleep or asyncio.sleep
    rt = {"placements": []}
    c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=acct["wallet"], environment=env)
    try:
        session = k.Account.from_key(key_hex).address
        assert c.wallet_type == "DEPOSIT_WALLET" and c._ctx.signer_type == "SESSION_KEY", "not a session key"
        rt["closed_only"] = await c.get_closed_only_mode()
        rt["balance_before"] = await chain_balance(k, env, acct["wallet"])
        rt["clob_balance_before"] = (await c.get_balance_allowance(asset_type="COLLATERAL")).balance
        rt["open_before"] = len(await first_items(c.list_open_orders()))
        if rt["closed_only"] is not False or not isinstance(rt["balance_before"], int) \
                or rt["balance_before"] < RT_COST_UNITS or rt["open_before"]:
            rt["stopped"] = "before any placement: closed-only, balance or an open order"
            return rt
        t0, left = window_of(now())
        if left < RT_MIN_LEFT_S:
            out("RT window %d has %d s left, under %d: waiting %d s for the next" % (t0, left, RT_MIN_LEFT_S, left + 2))
            await sleep(left + 2)
            t0, left = window_of(now())
        status, doc = await gamma_market(k, env, t0)
        ok, why, tokens, cid, ex = market_reading(doc, t0)
        rt.update(market=RT_FAMILY + str(t0), market_status=status, market_reading=why, left_s=int(left), exchange=ex)
        out("RT market %s%d: gamma status %s, %s; %d s left in its window" % (RT_FAMILY, t0, status, why, left))
        if not ok:
            rt["stopped"] = "the market is not eligible"
            return rt
        spender = dict(EXCHANGES)[ex]
        rt["client_exchange"] = all(
            str(k.resolve_order_exchange_address(env._config, asset_id=t, neg_risk=False)).lower() == spender.lower()
            for t in tokens.values())
        rt["allowance"] = (await chain_allowances(k, env, acct["wallet"]))[ex]
        out("RT the client signs for the %s exchange: %s; the wallet's allowance on chain to it %s pUSD" % (
            "V2" if ex == "v" else "CTF", rt["client_exchange"], shown({ex: rt["allowance"]})[ex]))
        if not (rt["client_exchange"] and enough(rt["allowance"])):
            rt["stopped"] = "the client's exchange is not the market's, or its allowance is short"
            return rt
        await clob_refresh(k, c)
        oid = token = None
        for side in RT_SIDES[:RT_MAX_PLACEMENTS]:
            token = tokens[side]
            signed = await c.create_limit_order(asset_id=token, price=RT_PRICE, size=RT_SIZE, side="BUY",
                                                post_only=True)
            t_a = perf()
            try:
                resp = await c.post_order(signed)
                if resp.ok:
                    result = "live" if resp.status == "live" else "filled or pending: %s" % resp.status
                else:
                    result = resp.code if resp.code == "post_only_would_cross" else "refused: %s" % resp.code
            except k.RequestRejectedError as exc:
                resp = None
                result = "post_only_would_cross" if "crosses book" in str(exc) else "refused: status %s" % exc.status
            ms = (perf() - t_a) // 1000000
            rt["placements"].append({"side": side, "result": result, "ms": int(ms)})
            out("RT placement %d: BUY %s %s at %s, post-only, GTC: %s in %d ms" % (
                len(rt["placements"]), RT_SIZE, side, RT_PRICE, result, ms))
            if result == "live":
                oid = resp.order_id
                break
            if result != "post_only_would_cross":
                break
        if oid is None:
            rt["stopped"] = "no placement live"
            return rt
        o1 = await c.get_order(order_id=oid)
        rt["read_live"] = {"status": o1.status, "price": dec(o1.price), "size": dec(o1.original_size),
                           "side": o1.side, "type": o1.order_type, "matched": dec(o1.size_matched),
                           "maker is the wallet": o1.maker_address.lower() == acct["wallet"].lower(),
                           "asset is the token": str(o1.asset_id) == token}
        t_c = perf()
        cr = await c.cancel_order(order_id=oid)
        rt["cancel_ms"] = int((perf() - t_c) // 1000000)
        rt["cancel"] = {"canceled": oid in cr.canceled, "not_canceled": len(cr.not_canceled)}
        try:
            o2 = await c.get_order(order_id=oid)
            rt["read_after"] = {"status": o2.status, "matched": dec(o2.size_matched)}
        except k.RequestRejectedError as exc:
            rt["read_after"] = {"status": "not served, status %s" % exc.status, "matched": None}
        rt["open_after"] = len(await first_items(c.list_open_orders()))
        rt["wallet_open_after"] = len(await first_items(c.list_wallet_open_orders(signer_addresses=[session])))
        rt["balance_after"] = await chain_balance(k, env, acct["wallet"])
        rt["clob_balance_after"] = (await c.get_balance_allowance(asset_type="COLLATERAL")).balance
        out("RT read live %s; cancel %s in %d ms; read after %s; open after: the key's %d, the wallet's by the key %d; "
            "collateral on chain %s -> %s pUSD, the CLOB's view %s -> %s" % (
                rt["read_live"], rt["cancel"], rt["cancel_ms"], rt["read_after"], rt["open_after"],
                rt["wallet_open_after"], units(rt["balance_before"]), units(rt["balance_after"]),
                units(rt["clob_balance_before"]), units(rt["clob_balance_after"])))
        return rt
    finally:
        try:
            ca = await c.cancel_all()
            rt["final_cancel_all"] = {"canceled": len(ca.canceled), "not_canceled": len(ca.not_canceled)}
        except Exception as exc:   # the record says what the last act met; the gate reads the open orders
            rt["final_cancel_all"] = "error %s" % type(exc).__name__
        out("RT the last act, cancel_all of the key: %s" % (rt["final_cancel_all"],))
        await c.close()


def mode_roundtrip():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    rc, so, _se = run(["timedatectl", "show", "-p", "NTPSynchronized", "--value"])
    synced = rc == 0 and so.strip() == "yes"
    out("RT clock NTP-synchronized: %s" % synced)
    if not synced:
        out("G-RT FAIL: the clock is not NTP-synchronized; no order placed")
        return 4
    k = client()
    acct = load_account()
    assert acct.get("wallet") and acct.get("session_key") and acct.get("authorized_at"), \
        "BLOCKED: the account record names no authorized session key"
    earlier = rt_paths()
    for p in earlier:
        prior = json_of((read_text(p) or "").encode()) or {}
        assert not prior.get("placements"), "BLOCKED: %s placed an order already; a round trip runs once" % p
    assert len(earlier) < 3, "BLOCKED: three round trips are recorded already"
    rt = asyncio.run(roundtrip_flow(k, k.PRODUCTION, load_session_key(), acct))
    rt["at"] = int(time.time())
    path = os.path.join(L1_VAR, "tz51-roundtrip-%d.json" % (len(earlier) + 1))
    n = write_private(path, (json.dumps(rt, sort_keys=True, indent=1) + "\n").encode())
    out("RT record %s: %d bytes, 0600" % (path, n))
    ok, checks = rt_reading(rt)
    for name, v in checks.items():
        out("G-RT %s: %s" % (name, "PASS" if v else "FAIL"))
    out("G-RT %s: %d of %d; this TZ's whole loss at most %s pUSD" % ("PASS" if ok else "FAIL", sum(checks.values()),
                                                                  len(checks), units(RT_LOSS_MAX_UNITS)))
    return 0 if ok else 4

# ---- the self-tests -----------------------------------------------------------------------------------------


class FakeTty:
    """The Boss's terminal, scripted: each answer a string, or a function of everything said so far."""

    def __init__(self, answers):
        self.answers, self.said = list(answers), []

    def say(self, text):
        self.said.append(text)

    def ask(self, prompt, hidden=False):
        self.said.append(prompt)
        a = self.answers.pop(0)
        return a(self.said) if callable(a) else a


def on_terminal(child, script, timeout=60):
    """child() run in a child process whose controlling terminal is a new pseudo-terminal - its /dev/tty that
    terminal, as sshd gives the Boss's paste under `ssh -t` - and whose standard output and error are a pipe, its log.
    `script` is the Boss: (what the screen shows, the line he types or a function of the screen that returns it), each
    line typed once the screen shows its text after the last line typed. Returns (the child's exit status, the screen,
    the log, the lines left untyped). Called while this process runs one thread: a fork copies the calling thread
    alone (map section 7 item 189)."""
    import codecs
    import fcntl
    import select
    import signal
    import termios
    assert threading.active_count() == 1, "on_terminal: %d threads in this process" % threading.active_count()
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
                except OSError:          # EIO on the master once every holder of the terminal is gone
                    data = b""
                if not data:
                    fds.remove(fd)
                elif fd == master:
                    screen += dec.decode(data)
                else:
                    log += data
            if pending and pending[0][0] in screen[mark:]:
                mark = screen.index(pending[0][0], mark) + len(pending[0][0])
                answer = pending.pop(0)[1]
                os.write(master, ((answer(screen) if callable(answer) else answer) + "\n").encode())
    finally:
        os.close(master)
        os.close(rlog)
        status = os.waitpid(pid, 0)[1]
    return os.waitstatus_to_exitcode(status), screen, log.decode("utf-8", "replace"), pending


class _Fake(http.server.BaseHTTPRequestHandler):
    """The self-tests' loopback stand-in of the relayer, the CLOB, gamma, GitHub Pages, PyPI, the geoblock and
    Telegram, under one port, each by its path's first segment. It records every request's agent."""
    protocol_version = "HTTP/1.1"

    def log_message(self, *_a):
        pass

    def _send(self, code, obj=None, raw=None, ctype="application/json"):
        body = raw if raw is not None else json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._route("GET")

    def do_POST(self):
        self._route("POST")

    def do_DELETE(self):
        self._route("DELETE")

    def _route(self, method):
        st = self.server.st
        u = urllib.parse.urlsplit(self.path)
        q = {a: b[0] for a, b in urllib.parse.parse_qs(u.query).items()}
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        body = json.loads(raw) if raw else None
        st["seen"].append((method, u.path, self.headers.get("User-Agent")))
        seg, rest = (u.path.split("/", 2)[1:] + [""])[:2]
        try:
            code, obj = (st["handlers"].get(seg) or st["handlers"]["*"])(st, method, "/" + rest, q, body, self.headers)
        except Exception as exc:     # a stand-in's own fault is a 500 the test sees
            code, obj = 500, {"error": "%s: %s" % (type(exc).__name__, exc)}
        if isinstance(obj, (bytes, bytearray)):
            self._send(code, raw=bytes(obj), ctype="application/octet-stream")
        else:
            self._send(code, obj)


def fake_server(handlers):
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Fake)
    srv.daemon_threads = True
    srv.st = {"seen": [], "handlers": handlers}
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def _tx_handler(st, txid):
    st["polls"][txid] = st["polls"].get(txid, 0) + 1
    state = "STATE_CONFIRMED" if st["polls"][txid] >= 2 else "STATE_NEW"
    return 200, {"transaction_id": txid, "transaction_hash": "0x" + "ab" * 32, "state": state, "error_msg": None}


def _relayer(k):
    def handler(st, method, path, q, body, h):
        if method == "GET" and path == "/deployed":
            return 200, {"deployed": q.get("address", "").lower() == st["wallet"].lower()}
        if method == "GET" and path == "/v1/account/transactions/params":
            assert q.get("type") == "WALLET" and q.get("address", "").lower() == st["owner"].lower()
            return 200, {"address": "0x" + "11" * 20, "nonce": str(st["nonce"])}
        if method == "GET" and path.startswith("/v1/account/transactions/"):
            return _tx_handler(st, path.rsplit("/", 1)[1])
        if method == "POST" and path in ("/v1/session-signers/authorizations", "/v1/session-signers/revocations"):
            assert h.get("RELAYER_API_KEY") == st["relayer_key"], "the relayer key"
            assert h.get("RELAYER_API_KEY_ADDRESS") == st["owner"], "the relayer key's address"
            assert h.get("Idempotency-Key"), "an idempotency key"
            auth = path.endswith("authorizations")
            want = {"deadline", "nonce", "sessionSignerAddress", "signature", "walletAddress"} | (
                {"scopes", "validUntil"} if auth else set())
            assert set(body) == want, sorted(body)
            assert body["walletAddress"] == st["wallet"] and body["nonce"] == str(st["nonce"])
            assert int(body["deadline"]) >= int(time.time()) + 10, "the deadline"
            if auth:
                assert body["scopes"] == list(SCOPES)
                assert abs(int(body["validUntil"]) - int(time.time()) - LIFETIME_S) < 120, "validUntil"
                call = k.C.authorize_session_signer_call(wallet_address=st["wallet"],
                                                         session_signer=body["sessionSignerAddress"],
                                                         valid_until=int(body["validUntil"]))
            else:
                call = k.C.revoke_session_signer_call(wallet_address=st["wallet"],
                                                      session_signer=body["sessionSignerAddress"])
            td = k.build_deposit_wallet_typed_data(wallet=st["wallet"], calls=[call], nonce=body["nonce"],
                                                   deadline=body["deadline"], chain_id=CHAIN_ID)
            rec = k.Account.recover_message(k.encode_typed_data(full_message=td), signature=body["signature"])
            assert rec == st["owner"], "the owner's signature"
            st["nonce"] += 1
            if st.get("refuse"):
                return 200, {"operationId": "op", "status": "FAILED", "transactionHash": "", "transactionId": "txf"}
            if auth:
                st["authorized"].add(body["sessionSignerAddress"].lower())
                return 200, {"operationId": "op", "status": "SUBMITTED", "transactionHash": "0x" + "cd" * 32,
                             "transactionId": "txa%d" % st["nonce"]}
            st["authorized"].discard(body["sessionSignerAddress"].lower())
            return 200, {"fenced": True, "operationId": "op", "status": "PENDING", "transactionId": "txr%d" % st["nonce"]}
        if method == "POST" and path == "/submit":
            assert h.get("RELAYER_API_KEY") == st["relayer_key"], "the relayer key"
            assert h.get("RELAYER_API_KEY_ADDRESS") == st["owner"], "the relayer key's address"
            dw = body["depositWalletParams"]
            assert (body["type"], body["from"], body["to"], body["nonce"], body["metadata"], dw["depositWallet"]) == (
                "WALLET", st["owner"], k.PRODUCTION._config.wallet_derivation.deposit_wallet_factory, str(st["nonce"]),
                APPROVE_METADATA, st["wallet"]), body
            spenders = ["0x" + c["data"][34:74] for c in dw["calls"]]
            calls = [k.C.erc20_approval_call(token_address=PUSD, spender=k.to_checksum_address(a), amount=APPROVE_UNITS)
                     for a in spenders]
            assert [(c["target"], c["value"], c["data"]) for c in dw["calls"]] == [
                (str(c.to), "0", str(c.data)) for c in calls], dw["calls"]
            td = k.build_deposit_wallet_typed_data(wallet=st["wallet"], calls=calls, nonce=body["nonce"],
                                                   deadline=dw["deadline"], chain_id=CHAIN_ID)
            rec = k.Account.recover_message(k.encode_typed_data(full_message=td), signature=body["signature"])
            assert rec == st["owner"], "the owner's signature"
            st["nonce"] += 1
            st["batches"].append(spenders)
            for a in spenders:
                st["allowances"][a] = APPROVE_UNITS
            return 200, {"transactionID": "txp%d" % st["nonce"], "transactionHash": "", "state": "STATE_NEW"}
        return 404, {"error": "no such path %s %s" % (method, path)}
    return handler


def _order_wire(o, st):
    return {"id": o["id"], "market": st["cid"], "asset_id": o["token"], "owner": o["owner"],
            "maker_address": st["wallet"], "side": "BUY", "price": o["price"], "original_size": o["size"],
            "size_matched": "0", "outcome": "Up" if o["token"] == st["tokens"]["Up"] else "Down", "order_type": "GTC",
            "status": o["status"], "associate_trades": [], "created_at": 1795000000, "expiration": "0"}


def _clob(st, method, path, q, body, h):
    addr = (h.get("POLY_ADDRESS") or "").lower()
    if path in ("/auth/api-key", "/auth/derive-api-key"):
        assert h.get("POLY_SIGNATURE") and h.get("POLY_TIMESTAMP") and h.get("POLY_NONCE") == "0", "L1 headers"
        if method == "POST" and addr in st["creds"]:
            return 400, {"error": "Could not create api key"}
        st["creds"].setdefault(addr, {"apiKey": "k-%d" % len(st["creds"]),
                                      "secret": base64.urlsafe_b64encode(os.urandom(32)).decode(), "passphrase": "pp"})
        return 200, st["creds"][addr]
    if path.startswith("/markets-by-token/"):
        return 200, {"condition_id": st["cid"]}
    if path.startswith("/clob-markets/"):
        return 200, {"nr": False, "mts": "0.01", "fd": {"r": 0.07, "e": 1},
                     "t": [{"t": st["tokens"]["Up"]}, {"t": st["tokens"]["Down"]}]}
    cred = st["creds"].get(addr)
    if not (cred and h.get("POLY_API_KEY") == cred["apiKey"] and h.get("POLY_SIGNATURE") and h.get("POLY_TIMESTAMP")):
        return 401, {"error": "Unauthorized/Invalid api key"}
    if path == "/auth/api-keys":
        return 200, {"apiKeys": [cred["apiKey"]]}
    if addr not in st["authorized"]:
        return 401, {"error": "the signer is not authorized for the wallet"}
    mine = [o for o in st["orders"].values() if o["owner"] == cred["apiKey"]]
    if path == "/auth/ban-status/closed-only":
        return 200, {"closed_only": False}
    if path == "/balance-allowance/update":
        assert q.get("asset_type") == "COLLATERAL" and q.get("signature_type") == "3", q
        st["refreshed"] = st.get("refreshed", 0) + 1
        return 200, {}
    if path == "/balance-allowance":
        assert q.get("asset_type") == "COLLATERAL" and q.get("signature_type") == "3", q
        return 200, {"balance": str(st["balance"]), "allowances": {"0x" + "e1" * 20: "115792089237316195423570985008687"}}
    if path == "/order" and method == "POST":
        o = body["order"]
        assert body.get("postOnly") is True and body.get("orderType") == "GTC" and body.get("owner") == cred["apiKey"]
        assert (o["side"], o["signatureType"], o["maker"], o["signer"], o["makerAmount"], o["takerAmount"]) == (
            "BUY", 3, st["wallet"], st["wallet"], "50000", "5000000"), o
        st["posted"].append(o["tokenId"])
        if o["tokenId"] == st.get("cross"):
            msg = "invalid post-only order: order crosses book"
            if st.get("cross_http"):
                return 400, {"error": msg}
            return 200, {"success": False, "errorMsg": msg, "orderID": "", "status": "", "makingAmount": "",
                         "takingAmount": ""}
        oid = "0x%064x" % (len(st["orders"]) + 1)
        st["orders"][oid] = {"id": oid, "token": o["tokenId"], "owner": cred["apiKey"], "price": "0.01", "size": "5",
                             "status": "LIVE"}
        status = st.get("post_status", "live")
        return 200, {"success": True, "errorMsg": "", "orderID": oid, "status": status, "makingAmount": "",
                     "takingAmount": "", "tradeIDs": [], "transactionsHashes": []}
    if path.startswith("/data/order/"):
        o = st["orders"].get(path.rsplit("/", 1)[1])
        return (200, _order_wire(o, st)) if o else (404, {"error": "order not found"})
    if path == "/order" and method == "DELETE":
        o = st["orders"].get(body["orderID"])
        if o and o["status"] == "LIVE":
            o["status"] = "CANCELED"
            return 200, {"canceled": [o["id"]], "not_canceled": {}}
        return 200, {"canceled": [], "not_canceled": {body["orderID"]: "order not found"}}
    if path == "/cancel-all" and method == "DELETE":
        ids = [o["id"] for o in mine if o["status"] == "LIVE"]
        for i in ids:
            st["orders"][i]["status"] = "CANCELED"
        return 200, {"canceled": ids, "not_canceled": {}}
    if path == "/data/orders":
        return 200, {"data": [_order_wire(o, st) for o in mine if o["status"] == "LIVE"], "next_cursor": "LTE="}
    if path == "/data/wallet-open-orders":
        live = [o for o in st["orders"].values() if o["status"] == "LIVE"]
        return 200, {"data": [dict(_order_wire(o, st), signer_address=addr) for o in live], "next_cursor": ""}
    return 404, {"error": "no such path %s %s" % (method, path)}


def _rpc(st, method, path, q, body, h):
    assert method == "POST" and body["method"] == "eth_call" and body["params"][1] == "latest", body
    call = body["params"][0]
    d = call["data"]
    assert call["to"] == PUSD and d[34:74] == st["wallet"].lower()[2:], call
    if d[:10] == "0x" + BALANCE_OF and len(d) == 74:
        v = st["balance"]
    else:
        assert d[:10] == "0x" + ALLOWANCE_OF and len(d) == 138, call
        v = st["allowances"].get("0x" + d[98:138], 0)
    return 200, {"jsonrpc": "2.0", "id": body["id"], "result": "0x%064x" % v}


def _gamma(st, method, path, q, body, h):
    if path == "/markets/slug/%s%d" % (RT_FAMILY, st["t0"]):
        doc = {"slug": RT_FAMILY + str(st["t0"]), "active": True, "closed": False, "acceptingOrders": True,
               "enableOrderBook": True, "orderMinSize": 5, "conditionId": st["cid"], "negRisk": False,
               "outcomes": json.dumps(["Up", "Down"]), "outcomePrices": json.dumps(["0.5", "0.5"]),
               "clobTokenIds": json.dumps([st["ctf"]["Up"], st["ctf"]["Down"]])}
        if st.get("version") == "v2":
            doc.update(version="v2", positionIds=json.dumps([st["v2"]["Up"], st["v2"]["Down"]]))
        return 200, doc
    return 404, {"error": "not found"}


def withheld(text):
    """No EVM address and no 32-byte hex - an order's id, a transaction's hash - in `text`. Pure."""
    return re.search(r"0x[0-9a-fA-F]{40}", text) is None


def quiet(fn):
    """fn's result and every line it printed; the lines printed again after."""
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        got = fn()
    sys.stdout.write(buf.getvalue())
    return got, buf.getvalue()


def mode_sdk_selftest():
    """The client's flows, in /root/l1-env, against the loopback stand-in: the owner's authorization and approval at a
    real terminal; the owner's authorization from a link signed as the page signs, wrong answers refused; the key's
    registration; G-READY; the round trip in its four shapes; the revocation; a relayer's refusal; every request with
    this TZ's agent; the hook's IPv4 rules live."""
    k = client()
    passed = []

    def ok(cond, what):
        assert cond, "SDK SELFTEST FAIL: " + what
        passed.append(what)
        out("ok   " + what)

    ok(k.httpx._client.USER_AGENT == UA and socket.getaddrinfo is gai4, "the client's agent and lookups are this TZ's")
    for fam, bad in ((socket.AF_INET6, True), (socket.AF_UNIX, False)):
        try:
            s = socket.socket(fam, socket.SOCK_STREAM)
            s.close()
            refused = False
        except GuardError:
            refused = True
        ok(refused == bad, "the hook: a socket of family %s %s" % (fam.name, "refused" if bad else "let through"))
    try:
        socket.getaddrinfo("localhost", 80, socket.AF_INET6)
        ok(False, "an AF_INET6 lookup")
    except GuardError:
        ok(True, "the hook: an AF_INET6 lookup refused by gai4")
    try:
        socket.getaddrinfo("example.com", 443)
        ok(False, "a lookup of an unlisted host")
    except GuardError:
        ok(True, "the hook: a lookup of a host this mode does not name refused")
    a, b = socket.socketpair()
    a.close()
    b.close()
    ok(True, "the hook: asyncio's self-pipe, an AF_UNIX socketpair, let through")

    owner, other = k.Account.create(), k.Account.create()
    sess_key = "0x" + os.urandom(32).hex()
    session = k.Account.from_key(sess_key).address
    cfg0 = k.PRODUCTION._config
    wallet = k.W.derive_beacon_deposit_wallet_address(owner.address, cfg0.wallet_derivation)
    h1, h2 = (int.from_bytes(hashlib.sha256(b).digest(), "big") for b in (b"tz51 up", b"tz51 down"))
    ctf = {"Up": str(h1), "Down": str(h2)}                                    # reserved bits set: CTF token IDs
    v2 = {"Up": str((h1 >> 104 << 104) | 1), "Down": str((h1 >> 104 << 104) | 2)}   # reserved bits zero: V2 IDs
    assert all(int(t) & V2_RESERVED for t in ctf.values()) and not any(int(t) & V2_RESERVED for t in v2.values())
    st_extra = {"owner": owner.address, "wallet": wallet, "relayer_key": "rk-0123456789abcdef", "nonce": 7,
                "authorized": set(), "polls": {}, "creds": {}, "orders": {}, "balance": 10000000,
                "cid": "0x" + "ab" * 32, "ctf": ctf, "v2": v2, "tokens": ctf, "allowances": {}, "batches": [],
                "posted": []}
    ctf_x, v2_x = (a.lower() for _x, a in EXCHANGES)

    def sign_from(said, key=owner):
        url = [s for s in said if s.startswith("https://x.test/l1-sign.html#")][-1]
        f = dict(p.split("=", 1) for p in url.split("#", 1)[1].split("&"))
        if f["op"] == "authorize":
            calls = [k.C.authorize_session_signer_call(wallet_address=f["w"], session_signer=f["k"],
                                                       valid_until=int(f["u"]))]
        elif f["op"] == "revoke":
            calls = [k.C.revoke_session_signer_call(wallet_address=f["w"], session_signer=f["k"])]
        else:
            calls = [k.C.erc20_approval_call(token_address=PUSD, spender=dict(EXCHANGES)[x], amount=APPROVE_UNITS)
                     for x in f["x"]]
        td = k.build_deposit_wallet_typed_data(wallet=f["w"], calls=calls, nonce=f["n"], deadline=f["d"],
                                               chain_id=CHAIN_ID)
        return "0x" + key.sign_message(k.encode_typed_data(full_message=td)).signature.hex().removeprefix("0x")

    # -- the owner's flows at a real terminal (map section 7 item 189), before any thread of this process starts:
    # the child opens its terminal under authorize's rule, as mode_owner does, and reaches its own stand-in on
    # loopback under this mode's; the Boss signs each link the screen shows and types the signature back
    def owner_child():
        import copy
        MODE[0] = "authorize"
        tty = Tty()
        MODE[0] = "sdk-selftest"
        srv1 = fake_server({"relayer": _relayer(k), "clob": _clob, "gamma": _gamma, "rpc": _rpc})
        srv1.st.update(copy.deepcopy(st_extra))
        env1 = test_env(k, "http://127.0.0.1:%d" % srv1.server_address[1])
        got1 = asyncio.run(owner_flow(k, "authorize", env1, tty, sess_key, srv1.st["relayer_key"], owner.address.lower(),
                                      page_url="https://x.test/l1-sign.html"))
        a_ok = got1 is not None and got1[:2] == (wallet, session) and session.lower() in srv1.st["authorized"]
        got2 = asyncio.run(approve_flow(k, env1, tty, srv1.st["relayer_key"], owner.address.lower(),
                                        page_url="https://x.test/l1-sign.html", sleep=lambda s: None))
        p_ok = got2[2] == {"c": APPROVE_UNITS, "v": APPROVE_UNITS} and srv1.st["batches"] == [[ctf_x, v2_x]]
        out("TERMINAL authorize %s, approve %s" % (a_ok, p_ok))
        srv1.shutdown()
        return 0 if a_ok and p_ok else 4

    def sign_screen(screen):
        return sign_from(re.findall(r"https://x\.test/l1-sign\.html#[^\s]+", screen))

    rc, screen, log, left = on_terminal(owner_child, [("Подпись из MetaMask", lambda sc: sign_screen(sc) + "\n"),
                                                      ("Подпись из MetaMask", sign_screen)], timeout=120)
    sys.stdout.write(log)
    ok(rc == 0 and not left and "TERMINAL authorize True, approve True" in log and withheld(log) and wallet in screen
       and session in screen and len(re.findall(r"https://x\.test/l1-sign\.html#", screen)) == 2,
       "authorize and approve at a real terminal: two links shown with the addresses, two signatures typed back, the "
       "stray line typed after the first discarded; the log carries no address")

    srv = fake_server({"relayer": _relayer(k), "clob": _clob, "gamma": _gamma, "rpc": _rpc})
    srv.st.update(st_extra)
    st = srv.st
    env = test_env(k, "http://127.0.0.1:%d" % srv.server_address[1])

    tty = FakeTty(["not a signature", lambda said: sign_from(said, other), sign_from])
    got, printed = quiet(lambda: asyncio.run(owner_flow(k, "authorize", env, tty, sess_key, st["relayer_key"],
                                                        owner.address.lower(), page_url="https://x.test/l1-sign.html")))
    ok(got is not None and got[0] == wallet and got[1] == session and session.lower() in st["authorized"],
       "authorize: a link signed as the page signs, after a non-signature and another key's signature refused")
    ok(sum(1 for s in tty.said if "Подпись не владельца" in s) == 1 and sum(1 for s in tty.said if "Это не подпись" in s)
       == 1, "authorize: the two wrong answers each refused once, at the terminal")
    ok(st["nonce"] == 8, "authorize: the relayer took one request, its nonce moved once")
    ok(withheld(printed) and not withheld("\n".join(tty.said)),
       "authorize: the printed lines carry no address and no hash; the terminal shows them to the Boss")
    ok(asyncio.run(registered(k, env, sess_key, wallet, session, want=True, tries=2, gap=0)) is True,
       "the key's registration: it lists the wallet's orders")
    other_key = "0x" + os.urandom(32).hex()
    ok(asyncio.run(registered(k, env, other_key, wallet, k.Account.from_key(other_key).address, want=True, tries=2,
                              gap=0)) is False, "a key never authorized: refused at each of two reads")
    acct = {"owner": owner.address.lower(), "wallet": wallet.lower(), "session_key": session.lower(),
            "authorized_at": 1}
    fresh = "0x" + hashlib.sha256(b"tz51 another session key").hexdigest()
    ok(quiet(lambda: asyncio.run(authorize_kept(k, env, sess_key, acct)))[0] is True and
       quiet(lambda: asyncio.run(authorize_kept(k, env, sess_key, dict(acct, revoked_at=2))))[0] is False and
       quiet(lambda: asyncio.run(authorize_kept(k, env, fresh, acct)))[0] is False,
       "authorize kept on a second run: this key, unrevoked, acting; a revoked record or another key is not")
    checks = asyncio.run(ready_flow(k, env, sess_key, acct))
    ok(sum(checks.values()) == 5 and not checks["its allowance on chain to the CTF exchange between one order's cost "
                                                  "and 1 pUSD"]
       and not checks["its allowance on chain to the V2 exchange between one order's cost and 1 pUSD"],
       "G-READY before any approval: 5 of 7, both allowances short")
    st["allowances"] = {ctf_x: 2 ** 256 - 1}
    tty = FakeTty([sign_from])
    got, printed = quiet(lambda: asyncio.run(approve_flow(k, env, tty, st["relayer_key"], owner.address.lower(),
                                                          page_url="https://x.test/l1-sign.html", sleep=lambda s: None)))
    link = [x for x in tty.said if x.startswith("https://x.test/l1-sign.html#")]
    ok(got[2] == {"c": APPROVE_UNITS, "v": APPROVE_UNITS} and st["batches"] == [[ctf_x, v2_x]] and len(link) == 1 and
       "&x=cv&" in link[0] and st["nonce"] == 9 and withheld(printed) and
       sum(1 for x in tty.said if "без ограничения" in x) == 1,
       "approve, the CTF exchange at the maximum and the V2 exchange short: one link of x=cv, each set to 1 pUSD")
    st["allowances"] = {ctf_x: APPROVE_UNITS}
    tty = FakeTty(["", sign_from])
    got, printed = quiet(lambda: asyncio.run(approve_flow(k, env, tty, st["relayer_key"], owner.address.lower(),
                                                          page_url="https://x.test/l1-sign.html", sleep=lambda s: None)))
    links = [x for x in tty.said if x.startswith("https://x.test/l1-sign.html#")]
    ok(got[2] == {"c": APPROVE_UNITS, "v": APPROVE_UNITS} and st["batches"][-1] == [v2_x] and len(links) == 2
       and all("&x=v&" in x for x in links) and st["nonce"] == 10,
       "approve, the V2 exchange short alone: an empty answer gives a second link, one call of 1 pUSD, the CTF "
       "exchange's 1 pUSD kept")
    got, printed = quiet(lambda: asyncio.run(approve_flow(k, env, FakeTty([]), st["relayer_key"],
                                                          owner.address.lower(), page_url="https://x.test/l1-sign.html")))
    ok(got[1] is got[2] and len(st["batches"]) == 2 and st["nonce"] == 10,
       "approve, both at 1 pUSD: kept, nothing asked, nothing sent")
    checks = asyncio.run(ready_flow(k, env, sess_key, acct))
    ok(all(checks.values()) and len(checks) == 7 and st["refreshed"] >= 2,
       "G-READY: 7 of 7 against the stand-in, the CLOB's view refreshed first")

    def trip(now, cross=None, cross_http=False, post_status="live"):
        st.update(cross=cross, cross_http=cross_http, post_status=post_status, t0=window_of(now)[0])
        slept = []

        async def nap(s):
            slept.append(s)
            st["t0"] = window_of(now + s)[0]

        clock = [now]

        def fake_now():
            return clock[0] + sum(slept)
        rt, printed = quiet(lambda: asyncio.run(roundtrip_flow(k, env, sess_key, acct, now=fake_now, sleep=nap)))
        assert withheld(printed), "the round trip printed an address, an id or a hash"
        return rt, slept

    base = 1795000020.0
    for label, kw, sides in (("Up crossing, as a 400", dict(cross=ctf["Up"], cross_http=True), ["Up", "Down"]),
                             ("Up crossing, as a refusal", dict(cross=ctf["Up"]), ["Up", "Down"]),
                             ("no crossing", {}, ["Up"])):
        rt, slept = trip(base, **kw)
        good, chk = rt_reading(rt)
        ok(good and [p["side"] for p in rt["placements"]] == sides and slept == [] and rt["read_after"]["status"] ==
           "CANCELED" and rt["final_cancel_all"] == {"canceled": 0, "not_canceled": 0},
           "the round trip, %s: G-RT PASS, %d of %d, placements %s" % (label, sum(chk.values()), len(chk), sides))
    rt, slept = trip(base + 80)
    ok(rt_reading(rt)[0] and slept == [102.0] and rt["market"] == RT_FAMILY + str(int(base) // 300 * 300 + 300),
       "the round trip with 100 s left: waits 102 s for the next window, and PASS there")
    st.update(version="v2", tokens=v2)
    rt, slept = trip(base, cross=v2["Up"])
    ok(rt_reading(rt)[0] and rt["exchange"] == "v" and rt["client_exchange"] is True and
       [p["side"] for p in rt["placements"]] == ["Up", "Down"] and st["posted"][-2:] == [v2["Up"], v2["Down"]] and
       all(t in ctf.values() for t in st["posted"][:-2]),
       "the round trip on a Protocol V2 market: its positionIds traded through the V2 exchange, G-RT PASS")
    st["allowances"][v2_x] = 10
    rt, slept = trip(base)
    ok(not rt_reading(rt)[0] and rt["placements"] == [] and rt["exchange"] == "v" and "allowance" in rt["stopped"],
       "the round trip with the V2 exchange's allowance short: nothing placed, G-RT FAIL")
    st.update(version=None, tokens=ctf)
    st["allowances"][v2_x] = APPROVE_UNITS
    rt, slept = trip(base, post_status="matched")
    good, chk = rt_reading(rt)
    ok(not good and rt["placements"][0]["result"] == "filled or pending: matched" and
       rt["final_cancel_all"]["canceled"] == 1,
       "the round trip with a placement matched: G-RT FAIL, and the last act cancels what stands")
    st["balance"] = 10
    rt, _s = trip(base)
    ok(not rt_reading(rt)[0] and rt["placements"] == [] and "before any placement" in rt.get("stopped", ""),
       "the round trip under one order's cost: nothing placed, G-RT FAIL")
    st["balance"] = 10000000
    ok(all(o["status"] != "LIVE" for o in st["orders"].values()), "no order of the stand-in left live by any trip")

    tty = FakeTty([sign_from])
    got = asyncio.run(owner_flow(k, "revoke", env, tty, sess_key, st["relayer_key"], owner.address.lower(),
                                 page_url="https://x.test/l1-sign.html"))
    ok(got is not None and session.lower() not in st["authorized"], "revoke: one link signed, the key removed")
    ok(asyncio.run(registered(k, env, sess_key, wallet, session, want=False, tries=2, gap=0)) is False,
       "after revoke: the key refused")
    st["refuse"] = True
    try:
        asyncio.run(owner_flow(k, "authorize", env, FakeTty([sign_from]), sess_key, st["relayer_key"],
                               owner.address.lower(), page_url="https://x.test/l1-sign.html"))
        ok(False, "a relayer's FAILED")
    except Exception as exc:
        ok(type(exc).__name__ == "TransactionFailedError", "authorize: the relayer's FAILED raises %s" %
           type(exc).__name__)
    st["refuse"] = False
    agents = sorted({ua for _m, _p, ua in st["seen"]})
    ok(agents == [UA], "every one of %d requests carried the agent %s" % (len(st["seen"]), UA))
    srv.shutdown()
    out("SDK SELFTEST PASS: %d checks, %d passed; refused by the hook: %d, each a check's own" % (
        len(passed), len(passed), len(REFUSED)))
    return 0


def _ssh_str(b):
    return struct.pack(">I", len(b)) + b


def _pub(kind, *parts):
    return "%s %s tz51-selftest" % (kind, base64.b64encode(_ssh_str(kind.encode()) + b"".join(
        _ssh_str(p) for p in parts)).decode())


def mode_selftest():
    """Every rule of this file that needs no client: the readings on literals; the hook's decisions and its live
    refusals; the credentials' files and the Boss's key under a temporary tree, through a stand-in of his terminal and
    at a real one; the geoblock, the page, the wheels and Telegram against a loopback stand-in, each request with this
    TZ's agent."""
    passed = []

    def ok(cond, what):
        assert cond, "SELFTEST FAIL: " + what
        passed.append(what)
        out("ok   " + what)

    def refused(fn):
        try:
            fn()
        except GuardError:
            return True
        return False

    if os.path.exists(TMP):
        shutil.rmtree(TMP)
    os.mkdir(TMP, 0o700)
    # -- the readings, pure
    ok(number_reading([OWN_TZ, "CryptoTZ/TZ-50-x.md"], OWN_TZ)[0] and not number_reading(
        [OWN_TZ, "CryptoTZ/TZ-51-other.md"], OWN_TZ)[0] and not number_reading(
        [OWN_TZ, "CryptoReports/TZ-51-l1-account-round-trip-rerun-report.md"], OWN_TZ)[0], "NUMBER: own file alone, no report")
    kinds, br = refs_reading("a\tHEAD\nb\trefs/heads/main\nc\trefs/heads/tz-49-x\nd\trefs/tags/rewardbook-streams-1\n"
                             "e\trefs/heads/" + BRANCH + "\n")
    ok(br and kinds == {"HEAD": 1, "refs/heads/main": 1, "refs/heads/tz-*": 2, "refs/tags/rewardbook-streams-*": 1},
       "refs by kind, this TZ's branch seen")
    ok(room_reading(8000000000, 100) == (8000000100, 8000000100 - STREAM_FLOOR - PEAK), "the room and its margin")
    for status, doc, want in ((200, {"blocked": False, "country": "BG", "ip": "x"}, "PASS"),
                              (200, {"blocked": True, "country": "PL"}, "BLOCKED"),
                              (200, {"blocked": "false", "country": "BG"}, "UNREAD"),
                              (200, {"blocked": False, "country": "bg"}, "UNREAD"), (403, None, "UNREAD")):
        ok(geo_reading(status, doc) == want, "G-GEO %s on %r" % (want, doc))
    ok("198.51.100.7" not in str(geo_fields({"blocked": False, "country": "BG", "ip": "198.51.100.7"})),
       "G-GEO prints the reply's keys and fields, never its address")
    good = ("vs-2348", {"ID": "ubuntu", "VERSION_ID": "24.04"}, (3, 12, 3), [], [LIVE_HOST_KEY])
    ok(live_gate(*good)[0], "the live host gate: 5 of 5")
    for i, bad in enumerate((("vs-2348.example",), ({"ID": "debian", "VERSION_ID": "12"},), ((3, 13, 0),),
                             (["/var/lib/btc-recorder"],), ([("ssh-ed25519", "SHA256:x")],))):
        args = list(good)
        args[i] = bad[0]
        ok(not live_gate(*args)[0], "the live host gate fails on LH%d alone" % (i + 1))
    eff = sshd_effective("port 22\npasswordauthentication no\nkbdinteractiveauthentication no\npermitrootlogin "
                         "without-password\npubkeyauthentication yes\n")
    ok(ssh_reading((SSHD_SHA256, 0o644), eff)[0], "G-SSH K1 to K5: 5 of 5")
    ok(not ssh_reading((SSHD_SHA256, 0o600), eff)[0] and not ssh_reading(None, eff)[0], "G-SSH K1 fails alone")
    for kw, v in SSHD_IN_FORCE:
        ok(not ssh_reading((SSHD_SHA256, 0o644), dict(eff, **{kw: "yes" if v != "yes" else "no"}))[0],
           "G-SSH fails on %s alone" % kw)
    ok(methods_of("debug1: Authentications that can continue: publickey\nfoo 192.0.2.1\n"
                  "debug1: Authentications that can continue: publickey\n") == ["publickey"], "methods, the address never")
    ok(reclaimable(WORK) and not reclaimable("/root") and not reclaimable("/tmp/x/y"), "reclaim's trees")
    ed = _pub("ssh-ed25519", b"\x01" * 32)
    rsa4k = _pub("ssh-rsa", b"\x01\x00\x01", b"\x00" + b"\xff" * 512)
    rsa2k = _pub("ssh-rsa", b"\x01\x00\x01", b"\x00" + b"\xff" * 256)
    ok(pubkey_line(ed)[1:3] == ("ssh-ed25519", key_fingerprints(ed)[0][1]), "the Boss's key: ed25519, its fingerprint")
    ok(pubkey_line(rsa4k)[3] == 4096, "the Boss's key: RSA of 4096 bits")
    for bad, why in ((rsa2k, "RSA of 2048 bits"), ("-----BEGIN OPENSSH PRIVATE KEY-----", "a private key"),
                     ('from="10.0.0.1" ' + ed, "options before the key"), ("ssh-ed25519 %%%", "not base64"),
                     (ed + "\n" + ed, "two lines"), ("ssh-dss AAAA", "an unknown type"),
                     (_pub("ssh-ed25519", b"\x01" * 31), "a short ed25519 key"),
                     ("ssh-rsa " + ed.split()[1], "a blob of another type")):
        try:
            pubkey_line(bad)
            ok(False, "the Boss's key refuses " + why)
        except ValueError:
            ok(True, "the Boss's key refuses " + why)
    ok(valid_address("0x" + "aB" * 20) == "0x" + "ab" * 20 and valid_address(ZERO_ADDRESS) is None and
       valid_address("0x12") is None, "an address as typed")
    ok(token_ok("123456789:" + "A" * 35) and not token_ok("123:abc") and relayer_key_ok("019a2b3c-4d5e-6f70-8192-a3b4c5d6e7f8")
       and not relayer_key_ok("short") and not relayer_key_ok("has space in it here"), "a token and a relayer key")
    o, w, s_ = "0x" + "1" * 40, "0x" + "2" * 40, "0x" + "3" * 40
    ok(sign_link("authorize", o, w, s_, 7, 1800000600, 1815534000) == PAGE_URL + "#v=1&op=authorize&o=%s&w=%s&k=%s"
       "&u=1815534000&n=7&d=1800000600" % (o, w, s_) and sign_link("revoke", o, w, s_, 8, 9).endswith(
        "#v=1&op=revoke&o=%s&w=%s&k=%s&n=8&d=9" % (o, w, s_)) and sign_link("approve", o, w, None, 10, 11,
                                                                       exchanges="cv").endswith(
        "#v=1&op=approve&o=%s&w=%s&x=cv&n=10&d=11" % (o, w)), "the signing link's fields, the page's order")
    try:
        sign_link("approve", o, w, None, 1, 2, exchanges="cvz")
        ok(False, "an approval of another exchange")
    except AssertionError:
        ok(True, "the signing link refuses an approval of a third exchange")
    req = requirements_text()
    ok(len(WHEEL_SET) == 35 and req.count("\n") == 34 and "pip==" not in req and "polymarket-client==0.20.0 --hash"
       in req and req.split("\n")[:-1] == sorted(req.split("\n")[:-1]), "the requirements: 34 pinned lines, pip's not")
    p = pins()
    ok(installed_reading(dict(p), p)[0] and installed_reading(dict(p, extra="1"), p)[2] == ["extra"] and
       installed_reading({a: b for a, b in p.items() if a != "httpx"}, p)[1] == ["httpx"] and
       installed_reading(dict(p, httpx="9"), p)[3] == ["httpx"], "G-ENV's installed reading and its three faults")
    claims = [("a", "/x/1", "h1"), ("b", "/x/2", "h2"), ("c", "/x/docs", "hc"), ("d", "/x/docs", "hd")]
    ok(record_reading(claims, {"/x/1": "h1", "/x/2": "h2", "/x/docs": "hd"}) == (True, 4, 3, 1, [], []) and
       record_reading(claims, {"/x/1": "h1", "/x/2": "hX", "/x/docs": "hc"})[5] == ["/x/2"] and
       record_reading(claims, {"/x/1": "h1", "/x/docs": "hd"})[4] == ["/x/2"] and
       record_reading(claims, {"/x/1": "h1", "/x/2": "h2", "/x/docs": "hX"})[5] == ["/x/docs"],
       "G-ENV's files: equal, another hash, absent, and a path two distributions list holding one of their bytes")
    ups = [{"update_id": 1, "message": {"text": "/start", "chat": {"id": 42, "type": "private"}}},
           {"update_id": 2, "message": {"text": "hi", "chat": {"id": 43, "type": "private"}}},
           {"update_id": 3, "message": {"text": "/start", "chat": {"id": -5, "type": "group"}}}]
    ok(private_starts(ups) == [42], "the private chats that sent /start")
    ok(window_of(1795000020) == (1794999900, 180) and window_of(1795000200) == (1795000200, 300), "the window")
    t1, t2 = str(3 << 200 | 5 << 50), str(7 << 200 | 9 << 60)            # reserved bits set: CTF token IDs
    p1, p2 = str(3 << 200 | 1), str(3 << 200 | 2)                        # reserved bits zero: V2 position IDs
    doc = {"slug": RT_FAMILY + "1794999900", "active": True, "closed": False, "acceptingOrders": True,
           "enableOrderBook": True, "orderMinSize": 5, "conditionId": "0x" + "ab" * 32, "negRisk": False,
           "outcomes": '["Down", "Up"]', "clobTokenIds": json.dumps([t2, t1])}
    ok(market_reading(doc, 1794999900) == (True, "eligible, CTF", {"Down": t2, "Up": t1}, "0x" + "ab" * 32, "c"),
       "the market: a CTF market, its token IDs by outcome, the CTF exchange")
    v2doc = dict(doc, version="v2", positionIds=json.dumps([p2, p1]))
    ok(market_reading(v2doc, 1794999900) == (True, "eligible, Protocol V2", {"Down": p2, "Up": p1}, "0x" + "ab" * 32,
                                             "v"), "the market: a Protocol V2 market, its position IDs, the V2 exchange")
    for key, val in (("slug", "x"), ("closed", True), ("acceptingOrders", False), ("orderMinSize", 15),
                     ("outcomes", '["Yes", "No"]'), ("conditionId", "0x12"), ("clobTokenIds", "not json"),
                     ("negRisk", True), ("version", "v3"), ("clobTokenIds", json.dumps([p2, p1]))):
        ok(not market_reading(dict(doc, **{key: val}), 1794999900)[0], "the market refused on %s %s" % (
            key, ("V2 position IDs" if val == json.dumps([p2, p1]) else repr(val))))
    for key, val in (("positionIds", json.dumps([t2, t1])), ("positionIds", None)):
        ok(not market_reading(dict(v2doc, **{key: val}), 1794999900)[0], "the V2 market refused on %s %s" % (
            key, "CTF token IDs" if val else "absent"))
    rt = {"placements": [{"side": "Up", "result": "post_only_would_cross", "ms": 40},
                         {"side": "Down", "result": "live", "ms": 50}],
          "read_live": {"status": "LIVE", "price": "0.01", "size": "5", "side": "BUY", "type": "GTC", "matched": "0",
                        "maker is the wallet": True, "asset is the token": True},
          "cancel": {"canceled": True, "not_canceled": 0}, "read_after": {"status": "CANCELED", "matched": "0"},
          "open_after": 0, "wallet_open_after": 0, "balance_before": 10000000, "balance_after": 10000000,
          "market": RT_FAMILY + "1794999900", "cancel_ms": 60}
    ok(rt_reading(rt)[0], "G-RT: PASS on a record of two placements")
    for key, val in (("placements", [{"side": "Up", "result": "refused: unknown"}, {"side": "Down", "result": "live"}]),
                     ("placements", []), ("read_live", dict(rt["read_live"], matched="1")),
                     ("cancel", {"canceled": False, "not_canceled": 1}), ("read_after", {"status": "LIVE"}),
                     ("open_after", 1), ("wallet_open_after", 1), ("balance_after", 9950000)):
        ok(not rt_reading(dict(rt, **{key: val}))[0], "G-RT fails on %s alone" % key)
    ok(rt_reading(dict(rt, read_after={"status": "CANCELED_MARKET_RESOLVED", "matched": "0"}))[0],
       "G-RT: a cancellation's family of statuses")
    txt = report_text(rt, {"valid_until": 1810000000})
    ok(withheld(txt) and "Down" in txt and "отменён за 60 мс" in txt and "10.000000 pUSD" in txt,
       "the report: what happened, no address or id")
    ok(units(1234567) == "1.234567" and units(None) == "—", "pUSD from units")
    ok(bounded(RT_COST_UNITS) and bounded(APPROVE_UNITS) and not bounded(RT_COST_UNITS - 1) and
       not bounded(APPROVE_UNITS + 1) and not bounded(2 ** 256 - 1) and not bounded(None),
       "an allowance in bounds: from one order's cost to 1 pUSD, the maximum out")
    # -- the hook
    MODE[0] = "selftest"
    for mode, event, args, allowed in (
            ("selftest", "socket.getaddrinfo", ("example.com", 443, socket.AF_INET), False),
            ("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, socket.AF_INET), True),
            ("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, socket.AF_UNSPEC), False),
            ("authorize", "socket.getaddrinfo", (RELAYER_HOST.encode(), 443, socket.AF_INET), True),
            ("authorize", "socket.getaddrinfo", (GAMMA_HOST, 443, socket.AF_INET), False),
            ("approve", "socket.getaddrinfo", (RPC_HOST, 443, socket.AF_INET), True),
            ("approve", "socket.getaddrinfo", (CLOB_HOST, 443, socket.AF_INET), False),
            ("approve", "open", (RELAYER_FILE, "r", 0), True), ("approve", "open", (SESSION_KEY_FILE, "r", 0), False),
            ("approve", "os.rename", (ACCOUNT_FILE + ".tmp", ACCOUNT_FILE), True),
            ("approve", "open", ("/dev/tty", "r", 0), True),
            ("roundtrip", "socket.getaddrinfo", (GAMMA_HOST, 443, socket.AF_INET), True),
            ("roundtrip", "socket.getaddrinfo", (RPC_HOST, 443, socket.AF_INET), True),
            ("roundtrip", "socket.getaddrinfo", ("data-api.polymarket.com", 443, socket.AF_INET), False),
            ("roundtrip", "socket.__new__", (None, socket.AF_UNIX, 1, 0), True),
            ("geoblock", "socket.__new__", (None, socket.AF_UNIX, 1, 0), False),
            ("roundtrip", "socket.__new__", (None, socket.AF_INET6, 1, 0), False),
            ("roundtrip", "socket.connect", (None, ("192.0.2.9", 443)), False),
            ("secrets", "open", ("/dev/tty", "w", os.O_WRONLY | os.O_CREAT | os.O_TRUNC), True),
            ("secrets", "open", ("/dev/tty", None, os.O_RDWR | os.O_NOCTTY), True),
            ("ready", "open", ("/dev/tty", "r", 0), False),
            ("ready", "open", (SESSION_KEY_FILE, "r", 0), True), ("ready", "open", (RELAYER_FILE, "r", 0), False),
            ("host", "open", (TG_TOKEN_FILE, "r", 0), False), ("tg-report", "open", (CHAT_FILE, "r", 0), True),
            ("key", "open", (SESSION_KEY_FILE, None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), True),
            ("key", "open", (SESSION_KEY_FILE, None, os.O_WRONLY | os.O_CREAT), False),
            ("secrets", "open", (SESSION_KEY_FILE, None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), False),
            ("bosskey", "open", (AUTHORIZED_KEYS, "a", None), True),
            ("bosskey", "open", (AUTHORIZED_KEYS, "w", None), False),
            ("host", "open", (AUTHORIZED_KEYS, "a", None), False),
            ("roundtrip", "open", (L1_VAR + "/tz51-roundtrip-2.json", None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), True),
            ("roundtrip", "open", (L1_VAR + "/tz51-roundtrip-4.json", None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), False),
            ("authorize", "open", (L1_VAR + "/tz51-roundtrip-1.json", None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), False),
            ("authorize", "os.rename", (ACCOUNT_FILE + ".tmp", ACCOUNT_FILE), True),
            ("ready", "os.rename", (ACCOUNT_FILE + ".tmp", ACCOUNT_FILE), False),
            ("secrets", "os.mkdir", (L1_ETC, 0o700), True), ("ready", "os.mkdir", (L1_ETC, 0o700), False),
            ("wheels", "open", (WHEELS + "/a.whl", "wb", None), True), ("wheels", "open", ("/root/x", "wb", None), False),
            ("reclaim", "open", (FORENSICS + "/x", "xb", None), True), ("selftest", "open", (FORENSICS + "/x", "xb", None),
                                                                        False),
            ("host", "open", ("/var/lib/adv3-bot/journal.jsonl", "r", 0), False),
            ("host", "subprocess.Popen", ("timedatectl", ["timedatectl"]), True),
            ("secrets", "subprocess.Popen", ("bash", ["bash"]), False)):
        got = policy(mode, event, args) is None
        ok(got == allowed, "the hook in %s: %s %s %s" % (mode, event, str(args[:2])[:70],
                                                         "allowed" if allowed else "refused"))
    ok(refused(lambda: socket.socket(socket.AF_INET6, socket.SOCK_STREAM)), "the hook refuses an AF_INET6 socket, live")
    ok(refused(lambda: socket.getaddrinfo("localhost", 80)), "the hook refuses a lookup in no family, live")
    ok(refused(lambda: open(TG_TOKEN_FILE, "r")), "the hook refuses a read of the bot's token in this mode, live")
    ok(refused(lambda: open("/root/tz51-selftest-outside", "w")), "the hook refuses a write outside the work tree, live")
    ok(refused(lambda: subprocess.run(["true"])), "the hook refuses a command this mode does not name, live")
    # -- files under the temporary tree
    tok, rel, acc = TMP + "/etc/telegram-token", TMP + "/etc/relayer-key", TMP + "/var/account.json"
    tty = FakeTty(["123:bad", "123456789:" + "B" * 35, "019a2b3c-4d5e-6f70-8192-a3b4c5d6e7f8", "0x12",
                   "0x" + "Ab" * 20])
    ok(mode_secrets(tty, tok, rel, acc) == 0 and private_file_ok(tok) and private_file_ok(rel) and
       json_of(open(acc, "rb").read()) == {"owner": "0x" + "ab" * 20} and oct(os.stat(TMP + "/etc").st_mode & 0o7777)
       == "0o700", "secrets: the token, the relayer key and its owner written 0600, refused inputs asked again")
    ok(mode_secrets(FakeTty([]), tok, rel, acc) == 0, "secrets again: every item kept, nothing asked")
    try:
        write_private(tok, b"x")
        ok(False, "an exclusive create over an existing file")
    except FileExistsError:
        ok(True, "write_private refuses an existing file")
    ak = TMP + "/authorized_keys"
    with open(ak, "w") as fh:
        fh.write("ssh-ed25519 %s executor" % base64.b64encode(_ssh_str(b"ssh-ed25519") + _ssh_str(b"\x02" * 32)).decode())
    tty = FakeTty(["-----BEGIN OPENSSH PRIVATE KEY-----", ed])
    ok(mode_bosskey(tty, ak) == 0 and len(key_fingerprints(open(ak).read())) == 2 and
       open(ak).read().count("\n") == 2, "bosskey: a private key refused, the public one appended on its own line")
    ok(mode_bosskey(FakeTty([ed]), ak) == 0 and len(key_fingerprints(open(ak).read())) == 2, "bosskey: present, kept")
    ok(mode_bosskey(FakeTty([""]), ak) == 0, "bosskey: none given, skipped")
    # -- the Boss's modes at a real terminal: a pseudo-terminal as sshd gives `ssh -t`, the log a pipe (item 189)
    tok3, rel3, acc3 = TMP + "/etc3/telegram-token", TMP + "/etc3/relayer-key", TMP + "/var3/account.json"
    token3, rkey3, owner3 = "123456789:" + "D" * 35, "019a2b3c-4d5e-6f70-8192-a3b4c5d6e7f9", "0x" + "Cd" * 20

    def secrets_child():
        MODE[0] = "secrets"
        return mode_secrets(Tty(), tok3, rel3, acc3)
    rc, screen, log, left = on_terminal(secrets_child, [
        ("Токен Telegram-бота", "123:bad\n"), ("Токен Telegram-бота", token3), ("Ключ API релеера", rkey3),
        ("Адрес подписанта", owner3)])
    sys.stdout.write(log)
    ok(rc == 0 and not left and private_file_ok(tok3) and private_file_ok(rel3) and
       json_of(open(acc3, "rb").read()) == {"owner": owner3.lower()} and screen.count("Это не токен бота") == 1 and
       owner3 in screen and token3 not in screen and rkey3 not in screen and "SECRETS telegram-token: written" in log
       and not any(s in log for s in (token3, rkey3, owner3, owner3.lower())),
       "secrets at a real terminal: the token and the key read hidden, the address shown, a bad token asked again "
       "and the stray line typed after it discarded; the log holds none of them")
    ed3 = _pub("ssh-ed25519", b"\x03" * 32)

    def bosskey_child():
        MODE[0] = "bosskey"
        return mode_bosskey(Tty(), ak)
    rc, screen, log, left = on_terminal(bosskey_child, [("Публичный ключ из Termius", ed3)])
    sys.stdout.write(log)
    ok(rc == 0 and not left and "Ключ добавлен" in screen and "BOSSKEY added: ssh-ed25519" in log and
       key_fingerprints(open(ak).read())[-1] == key_fingerprints(ed3)[0],
       "bosskey at a real terminal: the key read and appended on its own line")
    # -- the network, against the loopback stand-in
    page = b"<!DOCTYPE html><p>tz51</p>\n"
    wheel_a, wheel_b = b"wheel-a" * 100, b"wheel-b" * 50
    tg_token = "123456789:" + "C" * 35
    calls = {"bad_wheel": 1}

    def h_geo(st, method, path, q, body, h):
        return 200, {"blocked": False, "country": "BG", "region": "22", "ip": "127.0.0.1"}

    def h_page(st, method, path, q, body, h):
        return (200, page) if path == "/l1-sign.html" else (404, {})

    def h_pypi(st, method, path, q, body, h):
        if path == "/b.whl" and calls["bad_wheel"]:
            calls["bad_wheel"] -= 1
            return 200, b"truncated"
        return (200, {"/a.whl": wheel_a, "/b.whl": wheel_b}[path]) if path in ("/a.whl", "/b.whl") else (404, b"")

    sent = []

    def h_tg(st, method, path, q, body, h):
        assert path.split("/")[-1] in ("getMe", "getMyCommands", "getUpdates", "sendMessage"), path
        m = path.split("/")[-1]
        if m == "getMe":
            return 200, {"ok": True, "result": {"is_bot": True, "username": "tz51_selftest_bot"}}
        if m == "getMyCommands":
            return 200, {"ok": True, "result": []}
        if m == "getUpdates":
            return 200, {"ok": True, "result": ups}
        sent.append(body)
        return 200, {"ok": True, "result": {"message_id": 77}}

    srv = fake_server({"api": h_geo, "btc-5m-twap": h_page, "pypi": h_pypi, "*": h_tg})
    base = ("http", "127.0.0.1", srv.server_address[1])
    ok(geo_read(base, sleep=lambda s: None) == "PASS", "G-GEO against the stand-in: PASS, the address its own")
    ok(page_read(base, path="/btc-5m-twap/l1-sign.html", want=(len(page), sha256_bytes(page)), sleep=lambda s: None)
       and not page_read(base, path="/btc-5m-twap/other.html", want=(len(page), sha256_bytes(page)),
                         sleep=lambda s: None, tries=3), "G-PAGE: the page's bytes, and another path refused")
    mini = (("a-1.0-py3-none-any.whl", len(wheel_a), sha256_bytes(wheel_a), "/pypi/a.whl"),
            ("b-2.0-py3-none-any.whl", len(wheel_b), sha256_bytes(wheel_b), "/pypi/b.whl"),
            (PIP_WHEEL, len(wheel_a), sha256_bytes(wheel_a), "/pypi/a.whl"))
    ok(fetch_wheels(base, TMP + "/wheels", mini, sleep=lambda s: None) and
       open(TMP + "/wheels/requirements.txt").read() == "a==1.0 --hash=sha256:%s\nb==2.0 --hash=sha256:%s\n" % (
           sha256_bytes(wheel_a), sha256_bytes(wheel_b)), "G-ENV wheels: 3 of 3, one refused once for its bytes")
    ok(fetch_wheels(base, TMP + "/wheels", mini, sleep=lambda s: None), "G-ENV wheels again: every one kept")
    gone = mini[:1] + (("c-3.0-py3-none-any.whl", 9, "0" * 64, "/pypi/c.whl"),) + mini[1:]
    ok(not fetch_wheels(base, TMP + "/wheels2", gone, sleep=lambda s: None) and sorted(os.listdir(TMP + "/wheels2")) ==
       ["a-1.0-py3-none-any.whl", "requirements.txt"], "G-ENV wheels: the first wheel not served whole ends the fetch")
    tg = Telegram(tg_token, base)
    ok(mode_tg_probe(tg) == 0, "G-TG getMe against the stand-in")
    chat = TMP + "/etc/chat-id"
    ok(mode_find_chat(tg, chat, wait_s=5) == 0 and open(chat).read() == "42\n" and private_file_ok(chat),
       "G-TG chat: one private /start, pinned 0600")
    ok(mode_find_chat(tg, chat, wait_s=5) == 0, "G-TG chat: pinned already, kept")
    ups.append({"update_id": 4, "message": {"text": "/start", "chat": {"id": 44, "type": "private"}}})
    ok(mode_find_chat(tg, TMP + "/etc/chat-id-2", wait_s=5) == 1, "G-TG chat: two private /start, FAIL")
    os.makedirs(TMP + "/var2", 0o700)
    with open(TMP + "/var2/tz51-roundtrip-1.json", "w") as fh:
        json.dump(rt, fh)
    with open(TMP + "/var2/account.json", "w") as fh:
        json.dump({"owner": "0x" + "ab" * 20, "valid_until": 1810000000}, fh)
    ok(mode_tg_report(tg, TMP + "/var2", TMP + "/var2/account.json", chat) == 0 and sent[-1]["chat_id"] == 42 and
       sent[-1]["text"] == report_text(rt, {"valid_until": 1810000000}), "G-TG report: sent to the pinned chat")
    agents = sorted({ua for _m, _p, ua in srv.st["seen"]})
    ok(agents == [UA], "every one of %d requests carried the agent %s" % (len(srv.st["seen"]), UA))
    srv.shutdown()
    floors("/", 1, mem_floor=1, read=lambda: 2, sleep=lambda s: None, statf=lambda d: (10, 5, 5))
    try:
        floors("/", 6, mem_floor=1, read=lambda: 2, sleep=lambda s: None, statf=lambda d: (10, 5, 5))
        ok(False, "a disk floor")
    except AssertionError:
        ok(True, "the floors: a disk under its floor BLOCKS")
    shutil.rmtree(TMP)
    ok(not os.path.exists(TMP), "the temporary tree removed")
    out("SELFTEST PASS: %d checks, %d passed; refused by the hook: %d, each a check's own" % (
        len(passed), len(passed), len(REFUSED)))
    return 0

# ---- main ---------------------------------------------------------------------------------------------------


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "refs": mode_refs, "room": mode_room,
             "geoblock": mode_geoblock, "sshd": mode_sshd, "page": mode_page, "wheels": mode_wheels,
             "secrets": mode_secrets, "bosskey": mode_bosskey, "tg-probe": mode_tg_probe, "find-chat": mode_find_chat,
             "tg-report": mode_tg_report, "env": mode_env, "key": mode_key, "ready": mode_ready,
             "roundtrip": mode_roundtrip, "authorize": lambda: mode_owner("authorize"),
             "approve": lambda: mode_owner("approve"), "revoke": lambda: mode_owner("revoke"),
             "selftest": mode_selftest, "sdk-selftest": mode_sdk_selftest}
    one = {"scratch": mode_scratch, "methods": mode_methods, "host": mode_host}
    rc = 1
    try:
        if mode == "reclaim":
            rc = mode_reclaim(rest)
        elif mode in one:
            assert len(rest) == 1, "%s takes one argument" % mode
            rc = one[mode](rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            rc = table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("refused by the hook: %d; lookups %d, requests %d" % (len(REFUSED), COUNTS["lookups"], COUNTS["requests"]))
    return rc or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
