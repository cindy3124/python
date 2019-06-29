# coding:utf-8
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):

    driver:WebDriver
    @classmethod
    def install_app(cls) -> WebDriver:
        '''
        启动app(只第一次用)
        '''
        caps = {
            'platformName': 'android',
            'deviceName': 'stella',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'autoGrantPermissions': 'true'
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        '''
        重启app
        '''
        caps = {
            'platformName': 'android',
            'deviceName': 'stella',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': 'true'
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

