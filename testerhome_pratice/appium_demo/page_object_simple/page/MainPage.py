# coding:utf-8

from testerhome_pratice.appium_demo.page_object_simple.driver.AndroidClient import AndroidClient
from testerhome_pratice.appium_demo.page_object_simple.page.QuotesPage import QuotesPage
from testerhome_pratice.appium_demo.page_object_simple.page.SelectedPage import SelectedPage


class MainPage(object):

    # 调用appium启动app
    def __init__(self):
        AndroidClient.restart_app()

    def goto_selected(self):
        # 调用全局的driver对象，使用webdriver api操作
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']").click()
        return SelectedPage()

    def goto_quotes(self):
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']").click()
        return QuotesPage()
