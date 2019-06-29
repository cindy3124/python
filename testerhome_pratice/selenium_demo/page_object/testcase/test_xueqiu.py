from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from page_object.page.MainPage import MainPage


class TestXueqiu(object):
    def setup(self):
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com")
        self.main = MainPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.main.search("alibaba").follow("1688")
        # todo: add assertion

