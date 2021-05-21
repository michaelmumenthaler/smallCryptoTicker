# Small Crypto Ticker

![demo][]

[demo]: https://github.com/michaelmumenthaler/smallCryptoTicker/blob/master/Assets/demo.gif


A small ticker which shows the current prices for the cryptos you're interested in. \
No clutter and a non disruptive interface. Ideal to just leave it running while you search for a nice residence on the moon.

## Installation
A virtual environment is recommended. \
Run ``` pip install -r requirements.txt ``` \
Then use the following command to start it: ``` python smallTicker.py ```


## Features

You can just add symbols in the symbols.json file while it is running and after a few seconds the newly added symbol will be awailable in the ticker.

## How to use it

While the ticker is running you can quit it by pressing "Q" on your keyboard, to switch to the next symbol press the "F" key. \ 
Note that the ticker must be in focus for the keys to work (click on it first).

## Will it steal my cryptos?

The Small Crypto Ticker uses the binance public API. You do not have to enter your API token or any other credentials for it to work.
