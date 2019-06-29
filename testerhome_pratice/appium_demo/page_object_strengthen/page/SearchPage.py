from selenium.webdriver.common.by import By
from testerhome_pratice.appium_demo.page_object_strengthen.page.BasePage import BasePage


class SearchPage(BasePage):
    _edit_locator = (By.CLASS_NAME, "android.widget.EditText")

    def search(self, key):
        self.find(self._edit_locator).send_keys(key)
        # 没跳到其他页面就只要返回自己就可以
        return self

    def addToSelected(self, key):
        # todo: 股票添加关注
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'follow_btn')]")
        self.find(follow_button).click()
        # 还在当前页面，返回自己，为了链式调用，可以链式调用自身
        # 其他方法调用本类时，在调用本方法后还能继续调用本类中其他方法
        return self

    def removeFromSelected(self, key):
        # todo: 股票取消关注
        followed_button = (By.XPATH,
                           "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                           "//*[contains(@resource-id, 'followed_btn')]")
        self.find(followed_button).click()
        # 还在当前页面，返回自己，为了链式调用，可以链式调用自身
        # 其他方法调用本类时，在调用本方法后还能继续调用本类中其他方法
        return self

    def isInSelected(self, key):
        # todo: 判断是否选择过
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'follow')]")
        # 获取'resourceId'属性
        id = self.find(follow_button).get_attribute('resourceId')
        return "ed" in id

    def searchByUser(self, key):
        # todo: 作业2 点击用户关注
        self.findByText('用户').click()
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'user_name') and "
                                   "contains(@text,'%s')]/../..//*"
                                   "[contains(@resource-id,'follow') and contains(@text,'关注')]" % key)
        print(follow_button)
        self.find(follow_button).click()

    def isFollowed(self, key):
        # todo: 作业2 判断是否关注成功
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'user_name') and "
                                   "contains(@text,'%s')]/../..//*"
                                   "[contains(@resource-id,'follow') and contains(@text,'关注')]" % key)
        print(follow_button)
        id = self.find(follow_button).get_attribute('resourceId')
        print(id)
        return 'ed' in id

    def cancel(self):
        self.findByText("取消").click()



