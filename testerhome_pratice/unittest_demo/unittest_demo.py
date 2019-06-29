# coding:utf-8

import unittest


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始执行类初始...')
        TestDemo.foo2 = list(range(10, 20))
        print(str(TestDemo.foo2), '\n')

    def setUp(self):
        print('开始执行方法初始...')
        self.foo1 = list(range(10))
        print(str(self.foo1))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(self.foo1.pop(), 9)
        self.assertEqual(TestDemo.foo2.pop(), 19)

    def test_2st(self):
        print('test_2st')
        self.assertEqual(self.foo1.pop(), 9)
        self.assertEqual(TestDemo.foo2.pop(), 18)

    def tearDown(self):
        print('执行方法结束...')

    @classmethod
    def tearDownClass(cls):
        print('执行类结束...')


if __name__ == '__main__':
    unittest.main()
