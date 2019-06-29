# coding:utf-8
import pytest
import allure
import os
import time
from PIL import ImageGrab
from allure_commons.types import AttachmentType

user_list = [{'user': 'a1', 'pwd': 'abc'},
             {'user': 'c1', 'pwd': '123456'},
             {'user': 'a1', 'pwd': '123456'}]

add_staff = [{'name': 'stella', 'sex': 'female', 'age': 20},
             {'name': 'tony', 'sex': 'male', 'age': 35},
             {'name': 'cindy', 'sex': 'female', 'age': 25}]


@allure.feature('测试登录模块')
@pytest.mark.parametrize("test_login", user_list, indirect=True)
class TestLogin:
    def test_login_case(self, test_login):
        a = test_login
        print("登录用例执行信息为：%s" % a)


@allure.feature('测试人员新增查询模块')
@pytest.mark.parametrize("test_login", [{'user': 'a1', 'pwd': '123456'}], indirect=True)
class TestAddSearch:
    @allure.story('测试查询员工信息用例')
    @allure.title('验证查询员工信息正确')
    def test_search_staff(self, test_login):
        print('查询员工...')

    @allure.story('测试新建员工信息用例')
    @allure.title('验证新建员工成功')
    @pytest.mark.parametrize('staff_info', add_staff)
    def test_add_staff(self, test_login, staff_info):
        print('开始新建员工...')
        time.sleep(1)
        print('员工姓名：%s' % staff_info['name'])
        print('员工性别：%s' % staff_info['sex'])
        print('员工年龄：%s' % staff_info['age'])


@allure.feature('测试人员修改删除模块')
class TestModiDel:
    @allure.story('测试修改员工信息用例')
    @allure.title('验证修改员工成功')
    def test_modify_staff(self):
        with allure.step('选择用户信息'):
            print('点击一条用户信息...')
        with allure.step('点击修改用户按钮'):
            print('点击修改按钮...')
        with allure.step('验证修改成功'):
            print('验证修改成功...')

    @allure.story('测试删除员工信息用例')
    @allure.title('验证删除员工信息并产生截图')
    @allure.description('此用例验证删除员工信息是否成功')
    def test_delete_staff(self):
        print('删除员工...')
        allure.attach('http://www.baidu.com', 'test_attach_url')
        pic = ImageGrab.grab()
        save_path = os.getcwd() + "/tmp.png"
        pic.save(save_path)
        f = open(save_path, 'rb').read()
        allure.attach(f, 'img_screenshot', attachment_type=AttachmentType.PNG)


if __name__ == '__main__':
    pytest.main(['-s -v', 'test_staff'])