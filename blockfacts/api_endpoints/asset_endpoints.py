import requests

class AssetEndpoints(object):
    def __init__(self, key = "api-key-not-specified", secret = "api-secret-not-specified"):
        self.key = key
        self.secret = secret
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.key,
            'X-API-SECRET': self.secret
        }

    """
    Lists all assets that we support.
    Reference: https://docs.blockfacts.io/?python#list-all-assets
    """
    def listAllAssets(self):
        response = requests.get('https://api.blockfacts.io/api/v1/assets', headers=self.headers)
        return response.json()
  
    """
    Gets specific asset by ticker ID.
    @param {string} tickerId
    Reference: https://docs.blockfacts.io/?python#specific-asset
    """
    def getSpecificAsset(self, tickerId): 
        response = requests.get('https://api.blockfacts.io/api/v1/assets/' + str(tickerId), headers=self.headers)
        return response.json()
    