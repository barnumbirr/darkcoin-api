#!/usr/bin/env python
# -*- coding: utf-8 -*-

#      _            _             _       
#     | |          | |           (_)      
#   __| | __ _ _ __| | _____ ___  _ _ __  
#  / _` |/ _` | '__| |/ / __/ _ \| | '_ \ 
# | (_| | (_| | |  |   < (_| (_) | | | | |
#  \__,_|\__,_|_|  |_|\_\___\___/|_|_| |_|

__title__   = 'darkcoin'
__version__ = '0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/darkcoin-api'
__license__ = 'Apache v2.0 License'

import darkcoin_utils
from darkcoin_api import (
	about, difficulty, hashrate, block_count, total_coins, addressbalance,
	addresstohash, checkaddress, decode_address, getreceivedbyaddress,
	getsentbyaddress, hashpubkey, hashtoaddress, translate_address,
	generate_address, to_btc, to_ltc, to_doge, to_usd
)
