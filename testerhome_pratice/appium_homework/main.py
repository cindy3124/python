# coding:utf-8

import os
import subprocess
import pytest


if __name__ == '__main__':

    report_path = os.getcwd()+'/testreport'
    html_report_path = report_path+'/html'
    print('执行pytest main')
    pytest.main(['-s', 'test_xueqiu_webview.py', '--alluredir', report_path])
    command = 'allure generate --clean %s -o %s' % (report_path, html_report_path)
    print('执行生成allure html报告')
    subprocess.call(command, shell=True)