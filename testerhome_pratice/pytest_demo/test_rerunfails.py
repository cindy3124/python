# coding:utf-8
# 失败用例重跑调用命令：pytest --reruns 3 test_rerunfails.py

import random


def test_compare():
    assert 5 == random.randint(4, 20)


