from code.JsonObj import JsonObj
from tests.TestBase import TestBase
import json
from hamcrest import *

from code.ApiRequest import ApiRequest


class TestApiRequest(TestBase):
    api = ApiRequest(keyfile='../security/api_keys.json')
    currency = 'MANA'  # edit as appropriate

    def test_request(self):
        response = self.api.get_json('accounts')
        assert_that(response.status_code, is_(200))

    def test_convert_json(self):
        j = self.api.get_json('accounts')
        o = JsonObj(j.content)
        assert_that(len(o.data), is_not(0))

    def test_obj(self):
        o = self.api.get_object('accounts')
        assert_that(len(o.data), is_not(0))
        print(json.dumps(o.data[0]))
        assert_that(o.data[0]["currency"]["code"], is_(self.currency))
