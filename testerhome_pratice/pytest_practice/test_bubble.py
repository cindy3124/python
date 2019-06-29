# conding=utf-8

import pytest
import pytest_bubble


@pytest.mark.parametrize('list1 ,y', [([3, 1, 7, 4, 0, 8, 6], [0, 1, 3, 4, 6, 7, 8]),
                                      ([9, 7, 5, 3, 1, 5], [1, 3, 5, 5, 7, 9])])
def test_bubble(list1, y):
    result = pytest_bubble.bubble_sort(list1)
    pytest.assume(result == y)
