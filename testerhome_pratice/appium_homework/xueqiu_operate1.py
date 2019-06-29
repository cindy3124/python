# coding:utf-8

'''
作业：打开雪球，添加自选股，输入alibaba，添加到自选股
'''

from appium import webdriver


caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "stella"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

# 使用appium keyboard
caps["resetKeyboard"] = "true"
caps["unicodeKeyboard"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 隐式等待（机子比较卡，等待时间长了点）
driver.implicitly_wait(20)

# 步骤1、等待进入雪球首页（找个首页元素）
el0 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[1]/android.widget.TextView")
# 步骤2、点击‘+’
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
el1.click()
# 步骤3、点击‘加自选股’
el2 = driver.find_element_by_id("com.xueqiu.android:id/item_add_stock")
el2.click()
# 步骤4、输入‘alibaba’
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.click()
el3.send_keys("alibaba")
# 步骤5、点击‘加入自选股’
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
el4.click()
# el5 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative")
# el5.click()

driver.quit()