# conding:utf-8

import logging
import pytest
import time
import allure


@allure.feature('测试登录功能')
class TestLogin:
    @allure.story('测试登陆成功场景')
    @allure.severity('blocker')
    @allure.testcase("http://www.baidu.com")
    @allure.issue("http://www.baidu.com")
    def test_2474608(self):
        '''
        【用例描述】用例1测试登录成功的场景
        '''
        with allure.step("通过电话密码的方式登录雪球"):
            logging.info('输入电话、密码')
            time.sleep(2)

        with allure.step("点击用户图标，验证登录是否成功"):
            logging.info('点击用户图标')
            time.sleep(2)

        with allure.step("验证登录是否成功"):
            logging.debug('获取登录名字')
            user_name_text = 'stella'
        assert user_name_text == 'stella'

    @allure.story('测试登录失败场景')
    @allure.testcase("http://www.baidu.com")
    @allure.issue("http://www.baidu.com")
    @allure.severity('normal')
    def test_2474609(self):
        '''
        【用例描述】用例2测试登录失败的场景
        '''
        with allure.step("通过电话密码的方式登录雪球"):
            logging.info('输入电话、密码')
            time.sleep(2)

        with allure.step("点击用户图标，验证登录是否成功"):
            logging.info('点击用户图标')
            time.sleep(2)

        with allure.step("验证登录是否成功"):
            logging.debug('获取登录名字')
            user_name_text = ''
        assert user_name_text == ''

    @pytest.mark.parametrize('username',['tom','jim'])
    @pytest.mark.parametrize('password', ['tom123', 'jim123'])
    def test_login_with_two(self, username, password):
        logging.info('param1:'+str(username), 'param2:'+str(password))





