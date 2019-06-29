# coding:utf-8
from testerhome_pratice.appium_demo.page_object_strengthen.page.App import App


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def test_price(self):
        assert self.mainPage.goto_selected().gotoHS().get_price_by_name("招商银行") == 28.83


