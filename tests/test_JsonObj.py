from TestBase import TestBase
from hamcrest import *
import json

from code.JsonObj import JsonObj


class TestJsonObj(TestBase):

    def test_flat_json(self):
        j = '{"cash": "dollar"}'
        o = JsonObj(j)

        assert_that(o.cash, is_('dollar'))

    def test_nested_object(self):
        j = '{"cash": {"dollars": "50"}}'
        o = JsonObj(j)

        assert_that(o.cash.dollars, is_('50'))

