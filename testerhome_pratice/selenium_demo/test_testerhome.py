from selenium import webdriver


class TestTesterHome(object):
    def setup(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com/")

    def test_mtsc2019(self):
        # 部分文本匹配
        self.driver.find_element_by_partial_link_text("MTSC2019").click()
        # 点击"目录"：法一：使用xpath匹配1
        self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        # 点击"目录"：法一：使用xpath匹配2 用文本内容定位
        # 备注：text在appium是属性 使用@text，在selenium是文本内容 使用text()
        self.driver.find_element_by_xpath('//*[text()[contains(.,"目录")]]').click()
        # 点击"目录"：法二：使用css定位1 空格点 表示父子关系
        self.driver.find_element_by_css_selector('.toc-container .btn').click()
        # 点击"目录"：法二：使用css定位2 []内可以增加目标属性
        self.driver.find_element_by_css_selector('.btn.btn-default[data-toggle=dropdown]').click()
        # 部分文本匹配
        self.driver.find_element_by_partial_link_text("金数据投票表单").click()
        self.driver.find_element_by_partial_link_text("http://2019.test-china.org/").click()
