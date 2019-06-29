# coding:utf-8
from selenium.webdriver.common.by import By

from testerhome_pratice.appium_demo.page_object_strengthen.page.ProfilePage import ProfilePage
from testerhome_pratice.appium_demo.page_object_strengthen.driver.AndroidClient import AndroidClient
from testerhome_pratice.appium_demo.page_object_strengthen.page.BasePage import BasePage
from testerhome_pratice.appium_demo.page_object_strengthen.page.QuotesPage import QuotesPage
from testerhome_pratice.appium_demo.page_object_strengthen.page.SearchPage import SearchPage
from testerhome_pratice.appium_demo.page_object_strengthen.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    _profile_button = (By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")

    def goto_selected(self):
        # 调用全局的driver对象，使用webdriver api操作
        # zx = (By.XPATH, "//*[@text='自选']")
        self.findByText("自选").click()
        # self.driver.find_element_by_xpath("//*[@text='自选']")
        # self.driver.find_element_by_xpath("//*[@text='自选']").click()
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:
        # search_button = (By.ID, "home_search")
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        # self.find(MainPage._profile_button).click()
        # return ProfilePage()
        self.loadSteps("../data/MainPage.yaml", "gotoProfile")
        return ProfilePage()

    def goto_quotes(self):
        self.driver.find_element_by_xpath("//*[@text='行情']")
        self.driver.find_element_by_xpath("//*[@text='行情']").click()
        return QuotesPage()


