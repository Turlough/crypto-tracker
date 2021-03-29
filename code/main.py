from ApiRequest import ApiRequest
import json


# for now, these are simply tests
def prettify(s):
    return json.dumps(s, indent=4, sort_keys=True)


def get_currencies():
    obj = api.get_object('accounts')
    print(obj)
    currencies = list(filter(lambda data: data.balance.currency == "MANA", obj.data))
    print(currencies[0].name)


def get_accounts():
    j = api.get_json('accounts')
    print(prettify(j.json()))


def get_rates():
    j = api.get_exchange_rates()
    print(prettify(j.json()))


def get_bitcoin_price():
    j = api.get_price('BTC')
    print(prettify(j.json()))


def test_buy(amount, coin):
    price = float(api.get_price(coin).json()['data']['amount'])
    value = api.test_buy(amount, coin, price)
    print(f'Spent {amount} euro on {coin} and received {value} {coin}')


if __name__ == '__main__':
    api = ApiRequest(keyfile='../security/api_keys.json')
    # get_currencies()
    # get_accounts()
    # get_rates()
    # get_bitcoin_price()
    test_buy(50, 'BTC')
