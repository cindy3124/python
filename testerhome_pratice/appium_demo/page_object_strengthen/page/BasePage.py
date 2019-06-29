# coding:utf-8
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from testerhome_pratice.appium_demo.page_object_strengthen.driver.AndroidClient import AndroidClient


class BasePage(object):

    def __init__(self):
        # 可以自定义配置需要的driver
        # 如果，要测试WEB,则直接把这里的driver改下即可
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        # todo:处理各类弹框
        return self.driver.find_element(*kv)

    def findByText(self, text):
        return self.find((By.XPATH, "//*[@text='%s']" % text))

