from Auth import Auth
import json
import requests


def prettify(s):
    return json.dumps(s, indent=4, sort_keys=True)


# create API auth using your keys
with open("private_api.json", "r") as f:
    keys = json.load(f)

public = (keys['public'])
secret = (keys['secret'])
version = 2

# print(public, secret)
api_url = 'https://api.coinbase.com/v2/'

auth = Auth(public, secret, version)
# Get accounts data

r = requests.get(api_url + 'accounts', auth=auth)
# print json formatted accounts info
print(prettify(r.json()))
