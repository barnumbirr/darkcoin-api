#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
import darkcoin

__title__   = 'darkcoin'
__version__ = '0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/darkcoin-api'
__license__ = 'Apache v2.0 License'

class darkcointestsuite(unittest.TestCase):

	_multiprocess_can_split_ = True

	def test_difficulty(self):
		darkcoin.difficulty()
		assert type(darkcoin.difficulty()) is float
	
	def test_hashrate(self):
		darkcoin.hashrate()
		assert type(darkcoin.hashrate()) is str

	def test_block_count(self):
		darkcoin.block_count()
		assert type(darkcoin.block_count()) is float

	def test_total_coins(self):
		darkcoin.total_coins()
		assert type(darkcoin.total_coins()) is float
		
	def test_addressbalance(self):
		darkcoin.addressbalance('n194KCwPQJjti53z9gN6wh9wUChfVePEab')
		assert type(darkcoin.addressbalance('n194KCwPQJjti53z9gN6wh9wUChfVePEab')) is float
		
	def test_addresstohash(self):
		darkcoin.addresstohash('n194KCwPQJjti53z9gN6wh9wUChfVePEab')
		assert type(darkcoin.addresstohash('n194KCwPQJjti53z9gN6wh9wUChfVePEab')) is str
		
	def test_checkaddress(self):
		darkcoin.checkaddress('n194KCwPQJjti53z9gN6wh9wUChfVePEab')
		assert type(darkcoin.checkaddress('n194KCwPQJjti53z9gN6wh9wUChfVePEab')) is str
		
	def test_getreceivedbyaddress(self):
		darkcoin.getreceivedbyaddress('n194KCwPQJjti53z9gN6wh9wUChfVePEab')
		assert type(darkcoin.getreceivedbyaddress('n194KCwPQJjti53z9gN6wh9wUChfVePEab')) is str
		
	def test_getsentbyaddress(self):
		darkcoin.getsentbyaddress('n194KCwPQJjti53z9gN6wh9wUChfVePEab')
		assert type(darkcoin.getsentbyaddress('n194KCwPQJjti53z9gN6wh9wUChfVePEab')) is str
		
	def test_hashpubkey(self):
		darkcoin.hashpubkey('D73E63C04A6CBAD8D5DC94FDBEF5175D2364E32F')
		assert type(darkcoin.hashpubkey('D73E63C04A6CBAD8D5DC94FDBEF5175D2364E32F')) is str
		
	def test_hashtoaddress(self):
		darkcoin.hashtoaddress('D73E63C04A6CBAD8D5DC94FDBEF5175D2364E32F')
		assert type(darkcoin.hashtoaddress('D73E63C04A6CBAD8D5DC94FDBEF5175D2364E32F')) is str
		
	def test_translate_address(self):
		darkcoin.translate_address('n194KCwPQJjti53z9gN6wh9wUChfVePEab')
		assert type(darkcoin.translate_address('n194KCwPQJjti53z9gN6wh9wUChfVePEab')) is str
		
	def test_generate_address(self):
		darkcoin.generate_address()
		assert type(darkcoin.generate_address()) is str
		
	def test_to_btc(self):
		darkcoin.to_btc()
		assert type(darkcoin.to_btc()) is dict

	def test_to_ltc(self):
		darkcoin.to_ltc()
		assert type(darkcoin.to_ltc()) is dict

	def test_to_doge(self):
		darkcoin.to_doge()
		assert type(darkcoin.to_doge()) is dict

	def test_to_usd(self):
		darkcoin.to_usd()
		assert type(darkcoin.to_usd()) is dict

if __name__ == '__main__':
    unittest.main()
