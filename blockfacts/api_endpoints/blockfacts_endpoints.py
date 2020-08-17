import requests

class BlockfactsEndpoints(object):
    def __init__(self, key = "api-key-not-specified", secret = "api-secret-not-specified"):
        self.key = key
        self.secret = secret
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.key,
            'X-API-SECRET': self.secret
        }

    """
    Lists all exchanges that go into the normalization for specific asset-denominator pair.
    @param {list/string} pairs Pair list or comma-separated string
    You can pass a list of asset-denominator string pairs, or pass just one string with comma separated pairs.
    Reference: https://docs.blockfacts.io/?python#exchanges-in-normalization
    """   
    def getExchangesInNormalization(self, pairs):
        pairsString = ""

        if type(pairs) != list and type(pairs) != str:
            raise Exception("Parameter 'pairs' must be of 'str' or 'list' type")

        if isinstance(pairs, list):
            pairsString = ','.join([str(x) for x in pairs])
        else:
            pairsString = pairs

        pairsString = pairsString.replace(" ", "")

        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/normalization/whitelist/' + pairsString, headers=self.headers)
        return response.json() 

    """
    Gets current normalization data for specific asset-denominator pair.
    @param {list/string} assets Asset list or comma-separated string.
    @param {list/string} denominators Denominator list or comma-separated string.
    Reference: https://docs.blockfacts.io/?python#current-data
    """   
    def getCurrentData(self, assets, denominators):
        assetsString = ""
        denominatorsString = ""

        if type(assets) != list and type(assets) != str:
            raise Exception("Parameter 'assets' must be of 'str' or 'list' type")

        if type(denominators) != list and type(denominators) != str:
            raise Exception("Parameter 'denominators' must be of 'str' or 'list' type")

        if isinstance(assets, list):
            assetsString = ','.join([str(x) for x in assets])
        else:
            assetsString = assets

        if isinstance(denominators, list):
            denominatorsString = ','.join([str(x) for x in denominators])
        else:
            denominatorsString = denominators

        assetsString = assetsString.replace(" ", "")
        denominatorsString = denominatorsString.replace(" ", "")

        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/price?asset=' + assetsString + "&denominator=" + denominatorsString, headers=self.headers)
        return response.json()

    """
    Gets last 600 BlockFacts normalized prices for provided asset-denominator pairs.
    @param {list/string} assets Asset list or comma-separated string.
    @param {list/string} denominators Denominator list or comma-separated string.
    Reference: https://docs.blockfacts.io/?python#data-snapshot
    """   
    def getSnapshotData(self, assets, denominators):
        assetsString = ""
        denominatorsString = ""

        if type(assets) != list and type(assets) != str:
            raise Exception("Parameter 'assets' must be of 'str' or 'list' type")

        if type(denominators) != list and type(denominators) != str:
            raise Exception("Parameter 'denominators' must be of 'str' or 'list' type")

        if isinstance(assets, list):
            assetsString = ','.join([str(x) for x in assets])
        else:
            assetsString = assets

        if isinstance(denominators, list):
            denominatorsString = ','.join([str(x) for x in denominators])
        else:
            denominatorsString = denominators

        assetsString = assetsString.replace(" ", "")
        denominatorsString = denominatorsString.replace(" ", "")

        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/price/snapshot?asset=' + assetsString + "&denominator=" + denominatorsString, headers=self.headers)
        return response.json()

    """
    Gets the snapshot of Blockfacts OHLCV data for provided asset-denominator pairs and intervals.
    @param {list/string} assets Asset list or comma-separated string.
    @param {list/string} denominators Denominator list or comma-separated string.
    @param {list/string} intervals Interval list or comma-separated string.
    Reference: https://docs.blockfacts.io/?python#data-snapshot-ohlcv-blockfacts
    """   
    def getOHLCVSnapshotData(self, assets, denominators, intervals):
        assetsString = ""
        denominatorsString = ""
        intervalsString = ""

        if type(assets) != list and type(assets) != str:
            raise Exception("Parameter 'assets' must be of 'str' or 'list' type")

        if type(denominators) != list and type(denominators) != str:
            raise Exception("Parameter 'denominators' must be of 'str' or 'list' type")

        if type(intervals) != list and type(intervals) != str:
            raise Exception("Parameter 'intervals' must be of 'str' or 'list' type")

        if isinstance(assets, list):
            assetsString = ','.join([str(x) for x in assets])
        else:
            assetsString = assets

        if isinstance(denominators, list):
            denominatorsString = ','.join([str(x) for x in denominators])
        else:
            denominatorsString = denominators

        if isinstance(intervals, list):
            intervalsString = ','.join([str(x) for x in intervals])
        else:
            intervalsString = intervals

        assetsString = assetsString.replace(" ", "")
        denominatorsString = denominatorsString.replace(" ", "")
        intervalsString = intervalsString.replace(" ", "")

        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/price/ohlcv-snapshot?asset=' + assetsString + "&denominator=" + denominatorsString + "&interval=" + intervalsString, headers=self.headers)
        return response.json()

    """
    Gets historical normalization data by asset-denominator, date, time and interval.
    @param {string} asset 
    @param {string} denominator 
    @param {string} date 
    @param {string} time 
    @param {int} interval 
    @param {int} page 
    Reference: https://docs.blockfacts.io/?python#historical-data
    """
    def getHistoricalData(self, asset, denominator, date, time, interval, page=None):
        if page is None:
            page = 1

        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/price/historical?asset=' + str(asset) + "&denominator=" + str(denominator) + "&date=" + str(date) + "&time=" + str(time) + "&interval=" + str(interval) + "&page=" + str(page), headers=self.headers)
        return response.json()

    """
    Gets historical OHLCV data by asset-denominator, date, time and interval.
    @param {string} asset 
    @param {string} denominator 
    @param {string} interval 
    @param {string} dateStart
    @param {string} timeStart 
    @param {string} dateEnd
    @param {string} timeEnd 
    @param {int} page 
    Reference: https://docs.blockfacts.io/?python#ohlcv-historical-data
    """
    def getHistoricalOHLCVData(self, asset, denominator, interval, dateStart, timeStart, dateEnd, timeEnd, page=None):
        if page is None:
            page = 1

        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/ohlcv?asset=' + str(asset) + "&denominator=" + str(denominator) + "&interval=" + str(interval) + "&dateStart=" + str(dateStart) + "&timeStart=" + str(timeStart) + "&dateEnd=" + str(dateEnd) + "&timeEnd=" + str(timeEnd) + "&page=" + str(page), headers=self.headers)
        return response.json()

    """
    Get historical normalized price by specific point in time.
    @param {string} asset 
    @param {string} denominator 
    @param {string} date 
    @param {string} time 
    Reference: https://docs.blockfacts.io/?python#specific-historical-data
    """
    def getSpecificHistoricalData(self, asset, denominator, date, time):
        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/price/specific?asset=' + str(asset) + "&denominator=" + str(denominator) + "&date=" + str(date) + "&time=" + str(time), headers=self.headers)
        return response.json()
  
    """
    Gets all running normalization pairs. Resulting in which asset-denominator pairs are currently being normalized inside our internal system.
    Reference: https://docs.blockfacts.io/?python#normalization-pairs
    """
    def getNormalizationPairs(self):
        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/normalization/trades', headers=self.headers)
        return response.json()

    """
    Gets the moving percentage, and difference in price over a certain time period.
    @param {string} denominator 
    @param {string} date 
    @param {string} interval 
    @param {string} sort 
    Reference: https://docs.blockfacts.io/?python#period-movers
    """
    def getPeriodMovers(self, denominator, date, interval, sort):
        response = requests.get('https://api.blockfacts.io/api/v1/blockfacts/period-movers?denominator=' + str(denominator) + "&date=" + str(date) + "&interval=" + str(interval) + "&sort=" + str(sort), headers=self.headers)
        return response.json()