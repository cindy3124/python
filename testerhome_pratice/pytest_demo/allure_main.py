# coding:utf-8

import sys
import pytest
import os

if __name__ == '__main__':
    xml_report_path = '/scipt/python/testerhome_pratice/report/testreport'
    html_report_path = xml_report_path+'/html'
    test_dir = '/scipt/python/testerhome_pratice/pytest_practice'
    '''
    allure_list = '--allure-severities=normal'
    args = ['-s', '-q', '--alluredir', xml_report_path, allure_list]
    self_args = sys.argv[1:]
    pytest.main(args)
    '''
    cmd1 = 'find '+xml_report_path+' -name "*.txt"'
    os.system(cmd1)
    cmd2 = 'pytest --alluredir=%s  %s' % (xml_report_path, test_dir)
    os.system(cmd2)
    cmd3 = 'allure generate --clean %s -o %s' % (xml_report_path, html_report_path)
    os.system(cmd3)
