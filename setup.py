#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'darkcoin',
    version = '0.1',
    url = 'https://github.com/c0ding/darkcoin-api',
    download_url = 'https://github.com/c0ding/darkcoin-api/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['darkcoin'],
    description = 'Python API for the Darkcoin cryptocurrency.',
    long_description = file('README.md','r').read(),
    keywords = ['DRK', 'Darkcoin', 'HBN', 'Hobonickels', 'LTC', 'Litecoin', 'BTC', 'Bitcoin', 'DOGE', 'Dogecoin', 'WDC', 'Worldcoin', 'cryptocurrency', 'API'],
)
