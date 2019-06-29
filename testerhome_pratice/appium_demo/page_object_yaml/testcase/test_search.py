# coding:utf-8
import pytest

from testerhome_pratice.appium_demo.page_object_strengthen.page.MainPage import MainPage
from testerhome_pratice.appium_demo.page_object_strengthen.page.App import App


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.mainPage: MainPage = self.mainPage
        self.searchPage = self.mainPage.gotoSearch()

    def teardown_method(self):
        self.searchPage.cancel()

    def test_is_selected_stock(self):
        # todo:关注"alibaba"股票，并判断是否关注成功
        # 搜索栏搜索"alibaba"
        search_Page = self.searchPage.search("alibaba")
        # 添加关注
        self.searchPage.addToSelected('BABA')
        # 验证关注成功
        assert search_Page.isInSelected("BABA") == True
        assert search_Page.isInSelected("1688") == False

    @pytest.mark.parametrize("key, code", [
        ("招商银行", "SH600036"),
        ("平安银行", "SZ000001"),
        ("pingan", "SH601318")
    ])
    def test_is_selected_stock_hs(self, key, code):
        # todo: 判断 沪深的股票 关注成功
        searchPage = self.searchPage.search(key)
        assert searchPage.isInSelected(code) == False

    def test_add_stock_hs(self):
        # todo: 添加沪深的"招商银行"股票
        key = "pingan"
        code = "SH601318"
        searchPage = self.searchPage.search(key)
        if searchPage.isInSelected(code)==True:
            # todo:判断已经关注过，则重新关注
            searchPage.removeFromSelected(code)
        searchPage.addToSelected(code)
        assert searchPage.isInSelected(code) == True

    def test_is_follow_user(self):
        # todo:作业2：用户搜索seveniruby，并关注，并判断是否关注成功
        search_page = self.mainPage.gotoSearch().search("seveniruby")
        search_page.searchByUser('seveniruby')
        assert search_page.isFollowed('seveniruby') == True

    def test_szcz(self):
        # todo:作业1：点击雪球行情，获得“深证成指”的指数，判断是否大于8000点
        pass



