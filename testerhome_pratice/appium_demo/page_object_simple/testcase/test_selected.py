# coding:utf-8

import pytest

from testerhome_pratice.appium_demo.page_object_simple.page.MainPage import MainPage


class TestSelected(object):
    def test_price(self):
        main = MainPage()
        assert main.goto_selected().get_price_by_name("招商银行")==28.83

    def test_add_stock(self):
        pass

    def test_szcz(self):
        # 点击雪球行情，获得“深证成指”的指数，判断是否大于8000点
        main = MainPage()
