from unittest import TestCase
from hamcrest import *
import json

import sys

sys.path.insert(1, '../code')


from code.ApiRequest import ApiRequest


class TestAuth(TestCase):
    api = ApiRequest(keyfile='../security/api_keys.json')

    def prettify(s):
        return json.dumps(s, indent=4, sort_keys=True)

    def test_get_accounts(self):

        response = self.api.request('accounts')
        assert_that(response.status_code, is_(200))
