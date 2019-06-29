# coding:utf-8

import htmltestrunner
import unittest
import unittest_demo
import unittest_module


report_title = '测试报告'
desc = '测试用例执行报告'
report_file = 'UnittestReport.html'
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(unittest_demo.TestDemo))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(unittest_module.TestDemo1))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(unittest_module.TestDemo2))

with open(report_file, 'wb') as r:
    runner = htmltestrunner.HTMLTestRunner(stream=r, title=report_title, description=desc)
    runner.run(test_suite)
