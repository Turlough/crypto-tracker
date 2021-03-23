from ApiRequest import ApiRequest
import json


def prettify(s):
    return json.dumps(s, indent=4, sort_keys=True)


def get_currencies():
    api = ApiRequest(keyfile='../security/api_keys.json')
    obj = api.get_object('accounts')
    print(obj)
    currencies = list(filter(lambda data: data.balance.currency == "MANA", obj.data))
    print(currencies[0].name)


def get_accounts():
    api = ApiRequest(keyfile='../security/api_keys.json')
    j = api.get_json('accounts')
    print(prettify(j.json()))


get_currencies()
# get_accounts()
