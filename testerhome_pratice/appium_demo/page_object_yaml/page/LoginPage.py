from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testerhome_pratice.appium_demo.page_object_strengthen.page.BasePage import BasePage



class LoginPage(BasePage):
    _close_locator = (By.ID, "iv_close")
    _other_locator = (By.ID, "tv_login_by_phone_or_others")
    _register_phone_number_locator = (By.ID, "register_phone_number")
    _register_code_locator = (By.ID, "register_code")
    _login_button_locator = (By.ID, "button_next")
    _tv_login_with_account_locator = (By.ID, "tv_login_with_account")
    _login_account_locator = (By.ID, "login_account")
    _login_password_locator = (By.ID, "login_password")
    _close2_locator = (By.ID, "iv_action_back")
    _error_msg = (By.ID, "md_content")
    _back_locator = (By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")

    def loginByWX(self):
        return self

    def loginByMAG(self, phone, code):
        return self

    def loginByPwd(self, account, pwd):
        # 点击 "手机及其他登录"
        # self.find(self._other_locator).click()
        # # 点击 "邮箱手机号密码登录"
        # self.find(self._tv_login_with_account_locator).click()
        # # 输入 手机号
        # self.find(self._login_account_locator).send_keys(account)
        # # 输入 密码
        # self.find(self._login_password_locator).send_keys(pwd)
        # # 点击 登录
        # self.find(self._login_button_locator).click()

        # load from yaml
        self.loadSteps("../data/LoginPage.yaml", "loginByPasswd", var1=account, var2=pwd)
        return self

    def loginSuccessByPwd(self, account, pwd):
        from testerhome_pratice.appium_demo.page_object_strengthen.page.MainPage import MainPage
        return MainPage()

    def back(self):
        # todo:点击关闭，退回 选择登录方式 页面
        # 显示等待2秒，等待元素出现
        # self.find(self._back_locator).click()
        self.loadSteps("../data/LoginPage.yaml", "back")
        # WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(self._close_locator))
        from testerhome_pratice.appium_demo.page_object_strengthen.page.ProfilePage import ProfilePage
        return ProfilePage()

    def getErrorMsg(self):
        # todo:获取报错内容
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg
