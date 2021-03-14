import json
import requests
from Auth import Auth


class ApiRequest:

    version = 2
    base_url = 'https://api.coinbase.com/v2/'

    def __init__(self, keyfile):
        # create API auth using your keys
        with open(keyfile, "r") as f:
            keys = json.load(f)

        self.public = (keys['public'])
        self.secret = (keys['secret'])

    def request(self, endpoint):

        auth = Auth(self.public, self.secret, self.version)
        return requests.get(self.base_url + endpoint, auth=auth)

