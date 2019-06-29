# coding:utf-8
import pytest


@pytest.fixture(scope='class', autouse=True)
@pytest.mark.run(order=1)
def open_browser():
    print('\n打开浏览器...')


@pytest.fixture()
@pytest.mark.run(order=2)
def test_login(request):
    user = request.param['user']
    pwd = request.param['pwd']
    print('登录中...')
    if user == 'a1' and pwd == '123456':
        print('登录页面成功...')
        assert True
        return '登录页面成功...'
    else:
        print('用户名或密码错误，请重新检查...')
        assert False

