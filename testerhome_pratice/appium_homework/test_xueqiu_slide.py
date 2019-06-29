# coding:utf-8
# 作业二：进入雪球首页，进入基金的新闻页（不是第一个基金按钮），
#        对他以及它右侧的每个新闻栏目，执行上滑5次，进入下个栏目用从右边到左边滑动
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestSlide(object):
    @classmethod
    def setup_class(cls):
        '''
        初始类，只执行一次
        '''
        print('初始类，只执行一次')
        cls.install_app()

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
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)
        return driver

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
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)
        return driver

    def setup_method(self):
        '''
        初始进入雪球首页，等待'雪球'按钮出现
        '''
        print('重启app')
        self.driver = self.restart_app()
        print('进入雪球首页')
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'tabs')]//*[@text='雪球']")
        time.sleep(5)

    def teardown_method(self):
        '''
        退出app
        '''
        print('执行完成，退出app')
        self.driver.quit()

    def test_slide(self):
        '''
        测试用例：点击基金及其之后菜单，并分别滑动5次
        '''
        # 点击基金菜单
        found_button = self.driver.find_element_by_xpath("//*[contains(@resource-id,'filter_line')]//*[@text='基金']")
        found_button.click()
        # 基金滑动5次
        self.slide_element([0.8, 0.8, 0.8, 0.4], 5)
        # 点击基金后的所有菜单，并滑动
        title_list = self.get_title_list('基金')
        self.click_and_slide_list_element(title_list)
        # 滑动到最右边菜单
        self.slide_element([0.85, 0.14, 0.16, 0.14], 1)
        # 点击后面所有菜单，并滑动
        name = title_list[-1]
        title_list = self.get_title_list(name)
        self.click_and_slide_list_element(title_list)


    def get_title_list(self, name) -> list:
        '''
        作用：获取当前页面中，指定文本后面的菜单
        入参：文本
        出参：入参文本后面的菜单列表
        '''
        # 获取基金同级菜单列表
        element_list = self.driver.find_elements_by_xpath("//*[contains(@resource-id,'public_timeline_fixed_filter')]//*[@resource-id='com.xueqiu.android:id/filter_name']")
        num = len(element_list)
        # 获取菜单列表的菜单名称
        all_list = []
        for element in element_list:
            all_list.append(element.get_attribute("text"))
        print('获取当前显示页面所有菜单名称：', all_list)
        # 获取name后面的菜单名称列表
        for element_text in all_list:
            if element_text == name:
                # 获取name序号
                found_num = all_list.index(element_text)
                break
            else:
                print('不处理的菜单名称是：' + str(element_text))
                continue
        # 返回所需菜单列表
        return all_list[found_num+1:num]

    def click_and_slide_list_element(self, element_list):
        '''
        作用：点击文本列表中元素，并滑动
        入参：文本列表
        出参：无
        '''
        for element_text in element_list:
            print('点击的菜单名称是：'+element_text)
            element = self.driver.find_element_by_xpath("//*[contains(@resource-id,'filter_line')]//*[@text='"+element_text+"']")
            element.click()
            time.sleep(1)
            self.slide_element([0.8, 0.8, 0.8, 0.4], 5)

    def slide_element(self, proportion_list, num):
        '''
         作用：循环执行滑动num次
         入参：proportion 比例列表, num 运行次数
         出参：无
         '''
        rect = self.driver.get_window_rect()
        rect_h = rect['height']
        rect_w = rect['width']
        action = TouchAction(self.driver)
        print('进行滑动操作')
        for i in range(num):
            action.press(x=rect_w * proportion_list[0], y=rect_h * proportion_list[1]).move_to(x=rect_w * proportion_list[2], y=rect_h * proportion_list[3]).release().perform()
            time.sleep(1)

