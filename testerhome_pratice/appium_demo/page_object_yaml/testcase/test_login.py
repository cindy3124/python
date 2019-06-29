from testerhome_pratice.appium_demo.page_object_strengthen.page.App import App
import pytest


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().gotoProfile()

    def setup_method(self):
        self.loginPage = self.profilePage.gotoLogin()

    def teardown_method(self):
        self.loginPage.back()

    @pytest.mark.parametrize("user, pwd, msg", [
        ("156005347600", "11111111", "手机号码"),
        ("15600534760", "11111111", "密码错误")
    ])
    def test_login_password(self, user, pwd, msg):
        self.loginPage.loginByPwd(user, pwd)
        assert msg in self.loginPage.getErrorMsg()




