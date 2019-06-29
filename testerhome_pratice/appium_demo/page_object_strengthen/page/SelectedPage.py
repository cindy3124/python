from selenium.webdriver.common.by import By

from testerhome_pratice.appium_demo.page_object_strengthen.driver.AndroidClient import AndroidClient
from testerhome_pratice.appium_demo.page_object_strengthen.page.BasePage import BasePage


class SelectedPage(BasePage):
    def add_default(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self

    def get_price_by_name(self, name) -> float:
        pricelocator = (By.XPATH, "//*[contains(@resource-id, 'stockName') and "
             "@text='"+name+"']/../../..//*[contains(@resource-id, 'currentPrice')]")
        price = self.find(pricelocator).text
        # self.driver.find_element_by_xpath("//*[@text='全部']")
        # self.driver.find_element_by_xpath("//*[@text='全部']").click()
        # price = self.driver.find_element_by_xpath\
        #     ("//*[contains(@resource-id, 'stockName') and "
        #      "@text='"+name+"']/../../..//*[contains(@resource-id, 'currentPrice')]").text
        return float(price)
