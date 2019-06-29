from selenium import webdriver
import json

from selenium.webdriver import DesiredCapabilities


class TestXueqiu(object):
    def setup(self):
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # options.binary_location = "chrome path"
        # self.driver = webdriver.Chrome(options=options)
        # 调用远程环境执行
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com")

    def test_search(self):
        # 搜索框输入"alibaba"
        self.driver.find_element_by_xpath('//*[@placeholder="搜索"]').send_keys('alibaba')
        # 点击"搜索"
        self.driver.find_element_by_css_selector('.icon.iconfont').click()
        # 点击 01688的加
        self.driver.find_element_by_xpath('//*[text()="01688"]/../../../..//*[@class="iconfont"]').click()
        # 输入手机号和密码
        self.driver.find_element_by_xpath('//*[@placeholder="请输入手机号或者邮箱"]').send_keys('15000000000')
        self.driver.find_element_by_xpath('//*[@placeholder="请输入登录密码"]').send_keys('123')
        # 点击登录
        self.driver.find_element_by_css_selector('.modal__login__btn').click()

    def test_basic(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def test_execute_script(self):
        # 获取当前页面
        raw = self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)
        print(json.dumps(json.loads(raw), indent=4))

    def test_execute(self):
        # 新增的API可以用此方法来调用
        self.driver.execute("getxxx", params={"x": 1, "y": 2})

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        print(self.driver.get_cookies())
        # 新增一个cookie值
        self.driver.add_cookie({"name": "a", "value": "b"})
        # 覆盖原来的cookie值
        self.driver.add_cookie({"name": "name", "value": "name demo"})
        print(self.driver.get_cookies())

