# coding:utf-8
#
import pytest
import random


def add(x, y):
    return x+y


@pytest.mark.parametrize("x, y, z", [(2, 3, 5), (112, 3, 5)])
def test_add1(x, y, z):
    assert add(x, y) == z


@pytest.mark.parametrize("x", [(13), (15)])
def test_add2(x):
    assert add(x, 1) == random.randint(10, 20)
