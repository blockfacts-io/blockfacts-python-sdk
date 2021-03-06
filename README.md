![alt text](https://blockfacts.io/img/logo/bf-logo@2x.png "BlockFacts official logo")
# BlockFacts Python SDK
Official BlockFacts Python SDK including Rest and WebSocket API support.

[![PyPI version](https://badge.fury.io/py/blockfacts-sdk.svg)](https://badge.fury.io/py/blockfacts-sdk)

## Features

- REST API client with a function wrapper for easy API access
- WebSocket API client for real-time data gathering

**Note**: In order to read more and get richer details regarding our REST and WebSocket APIs, please refer to our official docs: https://docs.blockfacts.io.

* [Installation](#installation)
* [Quick start](#quick-start)
* [Using Rest API Client](#using-rest-api-client)
* [Asset endpoints](#asset-endpoints)
* [BlockFacts endpoints](#blockfacts-endpoints)
* [Exchange endpoints](#exchange-endpoints)
* [Using WebSocket API Client](#using-websocket-api-client)

## Installation
```bash
$ pip install blockfacts-sdk
```

## Quick start
To start using our SDK just import the package and pass the `API-KEY` and `API-SECRET` in the constructor.

```python
from blockfacts import RestClient 
from blockfacts import WebsocketClient 

key = 'your-api-key'
secret = 'your-api-secret'

restClient = RestClient(key, secret)
websocketClient = WebsocketClient(key, secret)
```

## Using Rest API Client
In the examples below, you can see which method is mapped to call it's predefined endpoint. You can also read more about authorization and how to obtain an API Key here: https://docs.blockfacts.io/?python#authorization

## Asset endpoints

### List all assets
Get all assets that we support.
- [`listAllAssets()`](https://docs.blockfacts.io/?python#list-all-assets)

```python
jsonResponse = restClient.assets.listAllAssets()
```

### Get specific asset
Get specific asset by ticker ID.
- [`getSpecificAsset(tickerId)`](https://docs.blockfacts.io/?python#specific-asset)

```python
jsonResponse = restClient.assets.getSpecificAsset("BTC")
```

## BlockFacts endpoints

### Exchanges in normalization
List exchanges that go into the normalization for specific asset-denominator pair.
- [`getExchangesInNormalization(pairs)`](https://docs.blockfacts.io/?python#exchanges-in-normalization)

```python
jsonResponse = restClient.blockfacts.getExchangesInNormalization(["BTC-USD", "ETH-USD"])

# OR

jsonResponse = restClient.blockfacts.getExchangesInNormalization("BTC-USD, ETH-USD")
```

### Current data
Get current normalization data for specific asset-denominator pair.
- [`getCurrentData(assets, denominators)`](https://docs.blockfacts.io/?python#current-data)

```python
jsonResponse = restClient.blockfacts.getCurrentData(["BTC", "ETH"], ["USD", "EUR"])

# OR

jsonResponse = restClient.blockfacts.getCurrentData("BTC, ETH", "USD, EUR")
```

### Snapshot data
Get last 600 BlockFacts normalized prices for provided asset-denominator pairs.
- [`getSnapshotData(assets, denominators)`](https://docs.blockfacts.io/?python#data-snapshot)

```python
jsonResponse = restClient.blockfacts.getSnapshotData(["BTC", "ETH"], ["USD", "EUR"])

# OR

jsonResponse = restClient.blockfacts.getSnapshotData("BTC, ETH", "USD, EUR")
```

### OHLCV Snapshot data
Gets the snapshot of Blockfacts OHLCV data for provided asset-denominator pairs and intervals.
- [`getOHLCVSnapshotData(assets, denominators, intervals)`](https://docs.blockfacts.io/?python#data-snapshot-ohlcv-blockfacts)

```python
jsonResponse = restClient.blockfacts.getOHLCVSnapshotData(["BTC", "ETH"], ["USD", "EUR"], ["30s", "1m", "1h"])

# OR

jsonResponse = restClient.blockfacts.getOHLCVSnapshotData("BTC, ETH", "USD, EUR", "30s, 1m, 1h")
```
**Note:** You can find all supported intervals on our official documentation here: https://docs.blockfacts.io/?python#data-snapshot-ohlcv-blockfacts

### Historical data
Get historical normalization data by asset-denominator, date, time and interval.
- [`getHistoricalData(asset, denominator, date, time, interval, page)`](https://docs.blockfacts.io/?python#historical-data)

```python
jsonResponse = restClient.blockfacts.getHistoricalData("BTC", "USD", "2.9.2019", "14:00:00", 20)

# OR with page parameter (optional)

jsonResponse = restClient.blockfacts.getHistoricalData("BTC", "USD", "2.9.2019", "14:00:00", 20, 3)
```

### OHLCV Historical data
Get historical OHLCV data by asset-denominator, date, time and interval.
- [`getHistoricalOHLCVData(asset, denominator, interval, dateStart, timeStart, dateEnd, timeEnd, page)`](https://docs.blockfacts.io/?python#ohlcv-historical-data)

```python
jsonResponse = restClient.blockfacts.getHistoricalOHLCVData("BTC", "USD", "1d", "5.8.2020", "14:00:00", "10.8.2020", "14:00:00")

# OR with page parameter (optional)

jsonResponse = restClient.blockfacts.getHistoricalOHLCVData("BTC", "USD", "1d", "5.8.2020", "14:00:00", "10.8.2020", "14:00:00", 2)
```

### Specific historical data
Get historical normalized price by specific point in time.
- [`getSpecificHistoricalData(asset, denominator, date, time)`](https://docs.blockfacts.io/?python#specific-historical-data)

```python
jsonResponse = restClient.blockfacts.getSpecificHistoricalData("BTC", "USD", "2.9.2019", "14:00:00")
```

### Normalization pairs
Get all running normalization pairs. Resulting in which asset-denominator pairs are currently being normalized inside our internal system.
- [`getNormalizationPairs()`](https://docs.blockfacts.io/?python#normalization-pairs)

```python
jsonResponse = restClient.blockfacts.getNormalizationPairs()
```

### Period movers
Get the moving percentage, and difference in price over a certain time period.
- [`getPeriodMovers(denominator, date, interval, sort)`](https://docs.blockfacts.io/?python#period-movers)

```python
jsonResponse = restClient.blockfacts.getPeriodMovers("USD", "11.8.2020", "sevenDay", -1)
```

## Exchange endpoints

### List all exchanges
List all exchanges that we support.
- [`listAllExchanges()`](https://docs.blockfacts.io/?python#all-exchanges)

```python
jsonResponse = restClient.exchanges.listAllExchanges()
```

### Specific exchange data
Get information about a specific exchange by its name. Returns information such as which assets are supported, asset ticker info, etc.
- [`getSpecificExchangeData(exchange)`](https://docs.blockfacts.io/?python#specific-exchange-data)

```python
jsonResponse = restClient.exchanges.getSpecificExchangeData("KRAKEN")
```

### Current trade data
Get current trade data for specific asset-denominator pair, from specific exchange(s).
- [`getCurrentTradeData(assets, denominators, exchanges)`](https://docs.blockfacts.io/?python#current-trade-data)

```python
jsonResponse = restClient.exchanges.getCurrentTradeData(["BTC", "ETH"], ["USD", "GBP"], ["KRAKEN", "COINBASE"])

# OR

jsonResponse = restClient.exchanges.getCurrentTradeData("BTC, ETH", "USD, GBP", "KRAKEN, COINBASE")
```

### Pair info
Get the Blockfacts pair representation of the provided exchange pair.
- [`getPairInfo(exchange, pair)`](https://docs.blockfacts.io/?python#pair-info)

```python
jsonResponse = restClient.exchanges.getPairInfo("BITSTAMP", "BTCUSD")
```

### Snapshot trade data
Get 600 latest trades that happened on the requested exchange(s) and pairs.
- [`getSnapshotTradeData(assets, denominators, exchanges)`](https://docs.blockfacts.io/?python#snapshot-trade-data)

```python
jsonResponse = restClient.exchanges.getSnapshotTradeData(["BTC", "ETH"], ["USD", "GBP"], ["KRAKEN", "COINBASE"])

# OR

jsonResponse = restClient.exchanges.getSnapshotTradeData("BTC, ETH", "USD, GBP", "KRAKEN, COINBASE")
```

### Snapshot OHLCV data
 Gets the snapshot of provided exchange(s) OHLCV data for provided asset-denominator pairs and intervals.
- [`getOHLCVSnapshotData(assets, denominators, exchanges, intervals)`](https://docs.blockfacts.io/?python#data-snapshot-ohlcv-exchange)

```python
jsonResponse = restClient.exchanges.getOHLCVSnapshotData(["BTC", "ETH"], ["USD", "GBP"], ["KRAKEN", "COINBASE"], ["30s", "1m", "1h"])

# OR

jsonResponse = restClient.exchanges.getOHLCVSnapshotData("BTC, ETH", "USD, GBP", "KRAKEN, COINBASE", "30s, 1m, 1h")
```

**Note:** You can find all supported intervals on our official documentation here: https://docs.blockfacts.io/?python#data-snapshot-ohlcv-exchange

### Historical trade data
Get exchange historical price by asset-denominator, exchange, date, time and interval.
- [`getHistoricalTradeData(asset, denominator, exchanges, date, time, interval, page)`](https://docs.blockfacts.io/?python#historical-trade-data)

```python
jsonResponse = restClient.exchanges.getHistoricalTradeData("BTC", "USD", ["KRAKEN", "COINBASE"], "2.9.2019", "14:00:00", 20)

# OR with page parameter (optional)

jsonResponse = restClient.exchanges.getHistoricalTradeData("BTC", "USD", "KRAKEN, COINBASE", "2.9.2019", "14:00:00", 20, 3)
```

### OHLCV Historical data
Get historical OHLCV data by asset-denominator, exchange, date, time and interval.
- [`getHistoricalOHLCVData(asset, denominator, exchanges, interval, dateStart, timeStart, dateEnd, timeEnd, page)`](https://docs.blockfacts.io/?python#ohlcv-historical-data-2)

```python
jsonResponse = restClient.exchanges.getHistoricalOHLCVData("BTC", "USD", ["KRAKEN", "COINBASE"], "1d", "5.8.2020", "14:00:00", "10.8.2020", "14:00:00")

# OR with page parameter (optional)

jsonResponse = restClient.exchanges.getHistoricalOHLCVData("BTC", "USD", "KRAKEN, COINBASE", "1d", "5.8.2020", "14:00:00", "10.8.2020", "14:00:00", 1)
```

### Specific trade data
Get historical exchange trades in specific second.
- [`getSpecificTradeData(asset, denominator, exchanges, date, time)`](https://docs.blockfacts.io/?python#specific-trade-data)

```python
jsonResponse = restClient.exchanges.getSpecificTradeData("BTC", "USD", ["KRAKEN", "COINBASE"], "2.9.2019", "14:00:00")

# OR

jsonResponse = restClient.exchanges.getSpecificTradeData("BTC", "USD", "KRAKEN, COINBASE", "2.9.2019", "14:00:00")
```

### Total trade volume
Get the total traded volume on all exchanges by asset-denominator and interval.
- [`getTotalTradeVolume(asset, denominator, interval)`](https://docs.blockfacts.io/?python#total-trade-volume)

```python
jsonResponse = restClient.exchanges.getTotalTradeVolume("BTC", "USD", "1d")
```

### Period movers
Get the moving percentage, and difference in price over a certain time period.
- [`getPeriodMovers(exchange, denominator, date, interval, sort)`](https://docs.blockfacts.io/?python#period-movers-2)

```python
jsonResponse = restClient.exchanges.getPeriodMovers("KRAKEN", "USD", "11.8.2020", "sevenDay", -1)
```

## Using WebSocket API Client
Our WebSocket feed provides real-time market data streams from multiple exchanges at once and the BlockFacts normalized price stream for each second. The WebSocket feed uses a bidirectional protocol, and all messages sent and received via websockets are encoded in a `JSON` format.

### Getting started and connecting
To get started simply create a new instance of the WebsocketClient class, and create handler functions for websocket events. You can then call the `connect()` function and open a connection with the BlockFacts websocket server.

```python
from blockfacts import WebsocketClient
import json

key = 'your-api-key'
secret = 'your-api-secret'

def on_open():
    print("BlockFacts websocket server connection open")

def on_message(message):
    data = json.loads(message)
    print(data)    
    # Handle websocket server messages

def on_close():
    print("BlockFacts websocket server connection closed")

def on_error(err):
    print(err)

websocketClient = WebsocketClient(key, secret)
websocketClient.onOpen = on_open
websocketClient.onMessage = on_message
websocketClient.onClose = on_close
websocketClient.onError = on_error
websocketClient.connect()
```

### Subscribing
In order to subscribe to specific channels or asset-pairs you must send out a `subscribe` type message. The subscribe message must be sent out after the connection with the websocket has been established. You can call the `subscribe()` function right after the `connect()` function, or in the `on_open()` event handler and pass it a list of channels: 

```python
websocketClient.connect()
websocketClient.subscribe([
    {
        "name":"BLOCKFACTS",
        "pairs": [
            "BTC-USD"
        ]
    },
    {
        "name":"HEARTBEAT"
    }
])

# OR

def on_open():
    print("BlockFacts websocket server connection open")
    websocketClient.subscribe([
      {
        "name":"BLOCKFACTS",
        "pairs": [
            "BTC-USD"
        ]
      },
      {
        "name":"HEARTBEAT"
      }
    ])
```

The `subscribe` type message supports two more optional parameters which are `id` and `snapshot`. You can pass those parameters after the listed channels dictionary in the `subscribe()` function. 

```python
websocketClient.subscribe([
    {
        "name":"BLOCKFACTS",
        "pairs": [
            "BTC-USD"
        ]
    },
    {
        "name":"HEARTBEAT"
    }
], "some-id", True)
```

To read more about the `snapshot` type message, please refer to our official documentation: https://docs.blockfacts.io/?python#snapshot

### Unsubscribing
If you wish to unsubscribe from certain channels or pairs, you can do so by sending the `unsubscribe` type message.

```python
websocketClient.unsubscribe([
    {
      "name":"BLOCKFACTS",
      "pairs": [
          "BTC-USD",
          "ETH-USD"
      ]
    },
    {
      "name":"HEARTBEAT"
    },
    {
      "name":"KRAKEN"
    }
], 12345)
```

The `unsubscribe` type message supports one more optional parameter which is `id`. You can pass this parameter after the listed channels dictionary in the `unsubscribe()` function. 

### Ping
Clients can send `ping` type messages to determine if the server is online.

```python
websocketClient.ping()
```

The `ping` type message supports one optional parameter which is `id`. You can pass this parameter in the `ping()` function. 

### Pong
Clients must respond to `ping` type messages sent from the server with a `pong` type message.

```python
def on_message(message):
    data = json.loads(message)

    if (data["type"] == "ping"):
      websocketClient.pong()
```

The `on_message()` event handler can also be used to handle all message types from the websocket, for example:

```python
def on_msg(message):
    data = json.loads(message)

    if data["type"] == 'subscribed':
      # Subscribed type message  

    if data["type"] == 'snapshot':
      # Snapshot type message  

    if data["type"] == 'unsubscribed':
      # Unsubscribed type message    

    if data["type"] == 'exchangeTrade':
      # ExchangeTrade type message    

    if data["type"] == 'blockfactsPrice':
      # BlockfactsPrice type message    

    if data["type"] == 'ping':
      # Ping type message     
      websocketClient.pong()   

    if data["type"] == 'pong':
      # Pong type message       

    if data["type"] == 'status':
      # Status type message       

    if data["type"] == 'heartbeat':
      # Heartbeat type message        

    if data["type"] == 'error':
      # Error type message   
```

### Disconnect
Clients can disconnect from the BlockFacts websocket by calling the `disconnect()` function. The disconnect function will work only if the connection has already been established.

```python
websocketClient.disconnect()
```

In order to have a better understanding of our server responses, please refer to: https://docs.blockfacts.io/?python#server-messages