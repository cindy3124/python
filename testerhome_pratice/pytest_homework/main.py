# coding:utf-8

import pytest
import subprocess
import os

if __name__ == '__main__':
    xml_report_path = os.getcwd()+'/report'
    html_report_path = xml_report_path+'/html'
    pytest.main(['-s', '-q', '--alluredir', xml_report_path])
    command = 'allure generate --clean %s -o %s' % (xml_report_path, html_report_path)
    subprocess.call(command, shell=True)
