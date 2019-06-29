import pytest

value1 = 0


@pytest.mark.run(order=2)
def test_compare1():
    assert 5 < value1


@pytest.mark.run(order=1)
def test_compare2():
    global value1
    value1 = 10
    assert value1 == 10
