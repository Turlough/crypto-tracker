from unittest import TestCase
from hamcrest import *
import sys
sys.path.insert(1, '../code')
sys.path.insert(1, '../security')
from code.ApiRequest import ApiRequest


class TestApiRequest(TestCase):

    api = ApiRequest(keyfile='../security/api_keys.json')

    def test_request(self):
        response = self.api.request('accounts')
        assert_that(response.status_code, is_(200))
