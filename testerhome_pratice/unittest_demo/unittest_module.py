import unittest


def setUpModule():
    print("模块初始化...")
    global foo
    foo = list(range(10))


class TestDemo1(unittest.TestCase):
    def test_1st(self):
        print('test_1st')
        self.assertEqual(foo.pop(), 9)


class TestDemo2(unittest.TestCase):
    def test_1st(self):
        print('test_1st')
        self.assertEqual(foo.pop(), 8)


def tearDownModule():
    print("模块结束...")


if __name__ == '__main__':
    unittest.main()
