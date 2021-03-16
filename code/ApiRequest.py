import json
import requests
from CoinbaseAuth import CoinbaseAuth
from code.JsonObj import JsonObj


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

    def get_json(self, endpoint):

        auth = CoinbaseAuth(self.public, self.secret, self.version)
        return requests.get(self.base_url + endpoint, auth=auth)

    def get_object(self, endpoint):
        return JsonObj(self.get_json(endpoint).content)
