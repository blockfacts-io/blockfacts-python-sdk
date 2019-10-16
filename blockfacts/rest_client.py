from .api_endpoints import AssetEndpoints
from .api_endpoints import BlockfactsEndpoints
from .api_endpoints import ExchangeEndpoints

class RestClient(object):
    def __init__(self, key = "api-key-not-specified", secret = "api-secret-not-specified"):
        self.assets = AssetEndpoints(key, secret)
        self.blockfacts = BlockfactsEndpoints(key, secret)
        self.exchanges = ExchangeEndpoints(key, secret)

    """
    Sets the API Key.
    @param {string} apiKey 
    """
    def setKey(self, apiKey):
        self.assets.key = apiKey
        self.blockfacts.key = apiKey
        self.exchanges.key = apiKey

    """
    Sets the API Secret.
    @param {string} apiSecret 
    """
    def setSecret(self, apiSecret):
        self.assets.secret = apiSecret
        self.blockfacts.secret = apiSecret
        self.exchanges.secret = apiSecret