from Auth import Auth
import json
import requests


def test_timestamp():
    url = 'https://api.coinbase.com/v2/time'
    r = requests.get(url)
    print(r.json())


# create API auth using your keys
with open("private_api.json", "r") as f:
    keys = json.load(f)

public = (keys['public'])
secret = (keys['secret'])
# print(public, secret)
api_url = 'https://api.coinbase.com/v2/'

auth = Auth(public, secret)
# Get accounts data
test_timestamp()
r = requests.get(api_url + 'accounts', auth=auth)
# print json formatted accounts info
print(r.content)
