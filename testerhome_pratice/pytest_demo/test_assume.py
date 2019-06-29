# coding:utf-8

import pytest


def test1():
    pytest.assume(1 == 1)
    pytest.assume(2 == 3)
    pytest.assume(3 == 3)
