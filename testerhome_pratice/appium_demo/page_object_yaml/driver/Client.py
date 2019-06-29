# coding:utf-8
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml


class AndroidClient(object):

    driver:WebDriver
    platform = "android"
    @classmethod
    def install_app(cls) -> WebDriver:
        '''
        启动app(只第一次用)
        '''
        #
        # caps = {
        #     'platformName': 'android',
        #     'deviceName': 'stella',
        #     'appPackage': 'com.xueqiu.android',
        #     'appActivity': '.view.WelcomeActivityAlias',
        #     'autoGrantPermissions': 'true'
        # }
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(20)
        # return cls.driver
        return cls.initDriver("install_app")

    @classmethod
    def restart_app(cls) -> WebDriver:
        '''
        重启app
        '''
        # caps = {
        #     'platformName': 'android',
        #     'deviceName': 'stella',
        #     'appPackage': 'com.xueqiu.android',
        #     'appActivity': '.view.WelcomeActivityAlias',
        #     'noReset': True,
        #     'unicodeKeyboard': True,
        #     'resetKeyboard': True
        # }
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(20)
        # return cls.driver
        return cls.initDriver("restart_app")

    @classmethod
    def initDriver(cls, key):
        driver_data = yaml.load(open("../data/driver.yaml"))
        # 取服务器地址和隐性等待时间
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        # 获取是哪个平台的driver
        platform = str(driver_data['platform'])
        cls.platform = platform

        caps = driver_data[key]['caps'][platform]
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver



