# coding:utf-8

import unittest
import htmltestrunner
import test_basicfunc

if __name__ == '__main__':
    report_title = '功能测试报告'
    report_desc = '测试用例报告'
    report_file = 'report.html'
    test_suite = unittest.TestSuite()
    test_cases = unittest.TestLoader().loadTestsFromModule(test_basicfunc)
    test_suite.addTests(test_cases)

    with open(report_file, 'wb') as f:
        runner = htmltestrunner.HTMLTestRunner(stream=f, title=report_title, description=report_desc)
        runner.run(test_suite)



