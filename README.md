<h1><img src="https://raw.github.com/c0ding/darkcoin-api/master/doc/darkcoin.png" height=55 alt="darkcoin" title="darkcoin"> darkcoin-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/darkcoin.svg)](https://pypi.python.org/pypi/darkcoin/)   [![Downloads](http://img.shields.io/pypi/dm/darkcoin.svg)](https://pypi.python.org/pypi/darkcoin/)

darkcoin is an APACHE licensed library written in Python designed to provide a simple to use API for the Darkcoin cryptocurrency.

## More about Darkcoin:

Darkcoin was engineered to be a digital version of cash. Transactions are pooled together in the blockchain, making them anonymous from the wallet.

You can send Darkcoin to family or friends, or pay for goods or services, anywhere in the world. The network is decentralized and free from middlemen. It's an anonymous payment system in your control. Darkcoin is a decentralized currency, meaning there are no banks to take a cut of your money.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install darkcoin

## API Documentation:

This API can currently retrieve the following stats from [explorer.darkcoin.io](http://explorer.darkcoin.io/) and [CryptoCoin](http://www.cryptocoincharts.info):

### Network:

  - Difficulty:

```
>>> import darkcoin
>>> darkcoin.get_difficulty()
1286234.254
```

  - Hashrate:

```
>>> darkcoin.hashrate()
14825354215
```

  - Block count:

```
>>> darkcoin.block_count()
73355.0
```

  - Total coins:

```
>>> darkcoin.total_coins()
4318521.0
```

### Addresses:

  - Address balance:
    [PARAMETER] is required and should be a DRK address.

```
>>> darkcoin.addressbalance(PARAMETER)
50.0
```

  - Address to hash:
    [PARAMETER] is required and should be a DRK address.

```
>>> darkcoin.addresstohash(PARAMETER)
D73E63C04A6CBAD8D5DC94FDBEF5175D2364E32F
```

  - Check address:
    [PARAMETER] is required and can be any crypto address.

```
>>> darkcoin.checkaddress(PARAMETER)
6F
```

  - Get received by address:
    [PARAMETER] is required and should be a DRK address.

```
>>> darkcoin.getreceivedbyaddress(PARAMETER)
50.0
```

  - Get sent by address:
    [PARAMETER] is required and should be a DRK address.

```
>>> darkcoin.getsentbyaddress(PARAMETER)
0
```

  - PUBKEY hash:
    [PARAMETER] is required and should be a PUBKEY.

```
>>> darkcoin.hashpubkey(PARAMETER)
3687D874F0CC6D498290F3D789EEA20BDDD25020
```

  - Hash to address:
    [PARAMETER] is required and should be an address hash.

```
>>> darkcoin.hashtoaddress(PARAMETER)
n194KCwPQJjti53z9gN6wh9wUChfVePEab
```

  - Translate address:
    [PARAMETER] is required and can be any crypto address.

```
>>> darkcoin.translate_address(PARAMETER)
n194KCwPQJjti53z9gN6wh9wUChfVePEab
```

  - Address/private key generation :

```
>>> darkcoin.generate_address()
{
    "address": "mvtAbz75TgSuKe888vh76CczXD4pd8aqw3", 
    "private_key": "cUba5Mx5iFye5TstsocsGX4YRncrTgzm1fQSRnWtcVqxVUVef2id" 
}
```

### Exchanges:

  - BTC:

```
>>> darkcoin.to_btc()
{
    "latest_trade": "2014-05-23 12:26:35", 
    "volume_btc": "11432.46", 
    "price": "0.02620001", 
    "price_before_24h": "0.01938800", 
    "volume_first": "496722.792057532", 
    "best_market": "mintpal", 
    "volume_second": "11432.4638341046", 
    "id": "drk/btc"
}
```

  - LTC:

```
>>> darkcoin.to_ltc()
{
    "latest_trade": "2014-05-23 11:58:36", 
    "volume_btc": "4.54", 
    "price": "1.49999000", 
    "price_before_24h": "0.00000000", 
    "volume_first": "173.949761137366", 
    "best_market": "mintpal", 
    "volume_second": "206.622965976596", 
    "id": "drk/ltc"
}
```

  - DOGE:

```
>>> darkcoin.to_doge()
{
    "latest_trade": "2014-05-09 19:36:06", 
    "volume_btc": "0.00", 
    "price": "250.00000001", 
    "price_before_24h": "250.00000001", 
    "volume_first": "0", 
    "best_market": "allcrypt", 
    "volume_second": "0", 
    "id": "drk/doge"
}
```

  - USD:

```
>>> darkcoin.to_usd()
{
    "latest_trade": "2014-05-22 12:03:45", 
    "volume_btc": "0.00", 
    "price": "9.90000000", 
    "price_before_24h": "9.90000000", 
    "volume_first": "0.0355698296152695", 
    "best_market": "exmoney", 
    "volume_second": "0.373674205737188", 
    "id": "drk/usd"
}
```


## License:

```
  Apache v2.0 License
  Copyright 2014 Martin Simon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## Useful links:

* [Darkcoin website](http://www.darkcoin.io/)
* [Darkcoin Blockexplorer](http://explorer.darkcoin.io/)

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
DRK : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
