import json
import requests
from CoinbaseAuth import CoinbaseAuth


class ApiRequest:
    """
    Wrapper to authenticate request.
    Specify keyfile in constructor.
    Specify REST endpoint (excluding base url) in request
    """

    version = '2021-02-22'
    base_url = 'https://api.coinbase.com/v2/'

    def __init__(self, keyfile):
        # create API auth using your keys
        with open(keyfile, "r") as f:
            keys = json.load(f)

        self.public = (keys['public'])
        self.secret = (keys['secret'])

    def request(self, endpoint):

        auth = CoinbaseAuth(self.public, self.secret, self.version)
        return requests.get(self.base_url + endpoint, auth=auth)

