from ApiRequest import ApiRequest
import json


def prettify(s):
    return json.dumps(s, indent=4, sort_keys=True)


api = ApiRequest(keyfile='./security/api_keys.json')
j = api.request('accounts')
print(prettify(j.json()))