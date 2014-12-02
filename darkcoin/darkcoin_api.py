#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
from darkcoin_utils import get_addr
from darkcoin_utils import exchange
from darkcoin_utils import gen_eckey
from darkcoin_utils import blockexplorer

__title__   = 'darkcoin'
__version__ = '0.2'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/darkcoin-api'
__license__ = 'Apache v2.0 License'


BROWSER_HEADER = {'User-Agent' : 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/36.0'}


def about():
	"""Returns some information about the darkcoin module."""

	return '{} v.{} is maintained by {} and available at {}.'.format(__title__, __version__, __author__, __repo__)


def difficulty():
	"""Returns the current network difficulty."""

	d = urllib2.urlopen(blockexplorer('getdifficulty'))
	return float(d.read())


def hashrate():
	"""Returns the current network hashrate."""

	c = block_count()
	blocks = "%.0f" %c
	d = urllib2.urlopen(blockexplorer('nethash') + '/' + str(blocks))
	last_line = d.readlines()[-1]
	e = last_line.split(',')
	return e[-1]


def block_count():
	"""Returns the number of blocks in the longest block chain.
	   Equivalent to Bitcoin's getblockcount.
	"""

	d = urllib2.urlopen(blockexplorer('getblockcount'))
	return float(d.read())


def total_coins():
	"""Returns the number of Darkcoin mined."""
	
	d = urllib2.urlopen(blockexplorer('totalbc'))
	return float(d.read())


def addressbalance(PARAMETER):
	"""Returns the address balance.
	   [PARAMETER] is required and should be a DRK address.
	"""
	
	d = urllib2.urlopen(blockexplorer('addressbalance') + '/' + str(PARAMETER))
	return float(d.read())


def addresstohash(PARAMETER):
	"""Returns the public key hash encoded in an address.
	   [PARAMETER] is required and should be a DRK address.
	"""
	
	d = urllib2.urlopen(blockexplorer('addresstohash') + '/' + str(PARAMETER))
	return d.read()


def checkaddress(PARAMETER):
	"""Checks if specified address is valid and returns
	   _pubkeyhash_version_byte.
	   [PARAMETER] is required and can be any crypto address.
	"""

	d = urllib2.urlopen(blockexplorer('checkaddress') + '/' + str(PARAMETER))
	return d.read()


def decode_address(PARAMETER):
	 """Returns the version prefix and hash encoded in an address.
	    [PARAMETER] is required and can be any crypto address.
	 """

	 d = urllib2.urlopen(blockexplorer('decode_address') + '/' + str(PARAMETER))
	 return d.read()


def getreceivedbyaddress(PARAMETER):
	"""Returns amount of DRK received by an address.
	   [PARAMETER] is required and should be a DRK address.
	"""

	d = urllib2.urlopen(blockexplorer('getreceivedbyaddress') + '/' + str(PARAMETER))
	return d.read()


def getsentbyaddress(PARAMETER):
	"""Returns amount of DRK sent by an address.
	   [PARAMETER] is required and should be a DRK address.
	"""

	d = urllib2.urlopen(blockexplorer('getsentbyaddress') + '/' + str(PARAMETER))
	return d.read()


def hashpubkey(PARAMETER):
	"""Returns the 160-bit hash of PUBKEY.
	   [PARAMETER] is required and should be a PUBKEY.
	"""

	d = urllib2.urlopen(blockexplorer('hashpubkey') + '/' + str(PARAMETER))
	return d.read()


def hashtoaddress(PARAMETER):
	"""Converts a 160-bit hash to an address.
	   [PARAMETER] is required and should be an address hash.
	"""

	d = urllib2.urlopen(blockexplorer('hashtoaddress') + '/' + str(PARAMETER))
	return d.read()


def translate_address(PARAMETER):
	"""Translates address for use in DRK chain.
	   [PARAMETER] is required and can be any crypto address.
	"""

	d = urllib2.urlopen(blockexplorer('translate_address') + '/' + str(PARAMETER))
	return d.read()
	

def generate_address():
	"""Returns a valid darkcoin address and it's
	   matching private key.
	   On OSX run this in i386 mode.
	"""

	return get_addr(gen_eckey(compressed=True,version=111),version=111)


def to_btc():
	"""Returns array with trading pair object."""

	c = urllib2.Request(exchange('drk_btc'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())


def to_ltc():
	"""Returns array with trading pair object."""

	c = urllib2.Request(exchange('drk_ltc'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())


def to_doge():
	"""Returns array with trading pair object."""

	c = urllib2.Request(exchange('drk_doge'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())
	

def to_usd():
	"""Returns array with trading pair object."""

	c = urllib2.Request(exchange('drk_usd'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())
