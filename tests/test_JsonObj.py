from TestBase import TestBase
from hamcrest import *

from code.JsonObj import JsonObj


class TestJsonObj(TestBase):

    def test_flat_json(self):
        j = '{"cash": "dollar", "data": "Feed Me"}'
        o = JsonObj(j)

        assert_that(o.cash, is_('dollar'))
