# coding:utf-8
# 作业：基金开户 蛋卷已有账户登录 密码登陆 输入错误的用户名和密码，点击安全登陆

from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import pytest
import allure
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("测试蛋卷基金登陆功能")
class TestWebview(object):
    @classmethod
    def setup_class(cls):
        cls.driver = cls.install_app()
        # 确认进入‘雪球’首页
        # cls.wait_element(cls.driver, MobileBy.XPATH, "//*[@text='雪球']")
        cls.driver.find_element_by_xpath("//*[@text='雪球']")
        # 进入‘交易’页面
        time.sleep(2)
        cls.driver.find_element_by_xpath("//*[@text='交易']").click()
        # 进入‘蛋卷基金’页面
        cls.driver.find_element_by_accessibility_id('基金开户').click()

    def setup_method(self):
        # 进入登录页面
        self.driver.find_element_by_accessibility_id('已有蛋卷基金账户登录').click()


    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {
            'platformName': 'android',
            'deviceName': 'stella',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'autoGrantPermissions': 'true'
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    def teardown_method(self):
        # 返回到'蛋卷基金'界面
        self.driver.back()
        self.driver.back()

    @classmethod
    def teardown_class(cls):
        # 退出app
        cls.driver.quit()

    @allure.story('测试蛋卷基金密码登录功能')
    @allure.title('此用例测试蛋卷基金密码登录功能')
    @allure.description('测试蛋卷基金密码登录失败并返回到 蛋卷基金 页面，若执行失败则截图')
    @pytest.mark.parametrize('usr, pwd', [('111', '222'), ('222', '333'), ('333', '444')])
    def test_login(self, usr, pwd):
        try:
            # 选择密码登录
            with allure.step('选择密码登录'):
                self.driver.find_element_by_accessibility_id('使用密码登录').click()
            # 输入手机号和密码
            with allure.step('输入手机号和密码'):
                self.driver.find_element_by_id('telno').send_keys(usr)
                self.driver.find_element_by_id('pass').send_keys(pwd)
            # 点击安全登录
            with allure.step('点击安全登录'):
                self.driver.find_element_by_accessibility_id('安全登录').click()
            # 获取错误信息，并校验
            with allure.step('获取错误信息，并校验'):
                msg = self.driver.find_element_by_id('message').get_attribute('name')
                assert '你输入的手机号码或者密码有误' in msg
        except Exception as e:
            # 报错则截图
            with allure.step('报错截图'):
                save_path = os.getcwd() + "/" + usr + "_error_tmp.png"
                self.driver.get_screenshot_as_file(save_path)
                f = open(save_path, 'rb').read()
                allure.attach(f, 'error_screenshot', attachment_type=AttachmentType.PNG)
                assert False
    '''
    @staticmethod
    def wait_element(driver, element_by, element, time=15):
        """
        等待元素出现
        :param driver: driver名称
        :param element_by: 元素定位方式
        :param element: 元素关键字
        :param time: 等待时间，默认10
        :return:
        """
        WebDriverWait(driver, time). \
                until(EC.presence_of_element_located((element_by, element)), '未找到元素')
'''


