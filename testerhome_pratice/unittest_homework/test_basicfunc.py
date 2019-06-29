# coding:utf-8

import unittest
import basicfunc
import ddt


@ddt.ddt
class TestCacul(unittest.TestCase):

    @ddt.data([basicfunc.caculate_num(10, '+', 20), 30],
              [basicfunc.caculate_num(20, '-', 10), 10],
              [basicfunc.caculate_num(10, '*', 20), 200],
              [basicfunc.caculate_num(20, '/', 10), 2])
    @ddt.unpack
    def test_cacu_normal(self, caculate, expect):
        self.assertEqual(caculate, expect)

    @unittest.skip('除0的选择跳过')
    def test_cacu_unnormal(self):
        result = basicfunc.caculate_num(20, '/', 0)
        self.assertEqual(result, '除数不能为0')


@ddt.ddt
class TestConvert(unittest.TestCase):

    @ddt.data([basicfunc.convert_string('abcde', 'upper'), 'ABCDE'],
              [basicfunc.convert_string('XYZ', 'lower'), 'xyz'],
              [basicfunc.convert_string('eere', 'abcd'), 'type只允许为upper或lower'])
    @ddt.unpack
    def test_convert_normal(self, caculate, expect):
        self.assertEqual(caculate, expect)


class TestRandom(unittest.TestCase):
    def test_name_in(self):
        self.assertIn('wyf', basicfunc.random_string(50))


if __name__ == '__main__':
    unittest.main()


