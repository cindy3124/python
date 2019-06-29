from testerhome_pratice.appium_demo.page_object_strengthen.page.BasePage import BasePage
from testerhome_pratice.appium_demo.page_object_strengthen.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        # self.findByText("点击登录").click()
        self.loadSteps('../ProfilePage.yaml', 'gotoLogin')
        return LoginPage()

