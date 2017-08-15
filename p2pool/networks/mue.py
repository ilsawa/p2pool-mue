from p2pool.mue import networks

PARENT = networks.nets['mue']
SHARE_PERIOD = 7
CHAIN_LENGTH = 24*60*60//7
REAL_CHAIN_LENGTH = 24*60*60//7
TARGET_LOOKBEHIND = 100
SPREAD = 10
IDENTIFIER = '1bfe0c098e49c8c3'.decode('hex')
PREFIX = '1bfe0c098ee25f44'.decode('hex')
COINBASEEXT = '2f5032506f6f6c2d4d55452f'.decode('hex')
P2P_PORT = 29963
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8963
BOOTSTRAP_ADDRS = 'crypto.office-on-the.net p2p-spb.xyz'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-mue'
VERSION_CHECK = lambda v: v >= 120100
