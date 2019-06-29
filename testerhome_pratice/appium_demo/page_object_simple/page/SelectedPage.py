from testerhome_pratice.appium_demo.page_object_simple.driver.AndroidClient import AndroidClient


class SelectedPage(object):
    def add_default(self):
        return self

    def get_price_by_name(self, name) -> float:
        # todo:
        AndroidClient.driver.find_element_by_xpath("//*[@text='全部']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='全部']").click()
        price = AndroidClient.driver.find_element_by_xpath\
            ("//*[contains(@resource-id, 'stockName') and "
             "@text='"+name+"']/../../..//*[contains(@resource-id, 'currentPrice')]").text
        return float(price)
