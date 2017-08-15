import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'bda3c8b1'.decode('hex')
P2P_PORT = 18683
ADDRESS_VERSION = 38
SCRIPT_ADDRESS_VERSION = 19
RPC_PORT = 29683
RPC_CHECK = defer.inlineCallbacks(lambda mued: defer.returnValue(
            'mueaddress' in (yield mued.rpc_help()) and
            (yield mued.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('mue_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('mue_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tMUE'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'MueCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/MueCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.muecore'), 'mue.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://test.explorer.mue.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://test.explorer.mue.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://test.explorer.mue.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**20 - 1)
DUST_THRESHOLD = 0.001e8
