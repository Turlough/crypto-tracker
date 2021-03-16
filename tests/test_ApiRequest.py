from code.JsonObj import JsonObj
from tests.TestBase import TestBase
from hamcrest import *

from code.ApiRequest import ApiRequest


class TestApiRequest(TestBase):
    api = ApiRequest(keyfile='../security/api_keys.json')

    def test_request(self):
        response = self.api.get_json('accounts')
        assert_that(response.status_code, is_(200))

    def test_get_object(self):
        j = self.api.get_json('accounts')
        o = JsonObj(j.content)
        assert_that(len(o.data), is_not(0))
