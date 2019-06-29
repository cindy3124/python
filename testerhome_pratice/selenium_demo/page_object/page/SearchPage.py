from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    def follow(self, keyword):
        self.driver.find_element_by_xpath('//*[text()="%s"]/../../../..//*[@class="iconfont"]' % keyword).click()
        return self
