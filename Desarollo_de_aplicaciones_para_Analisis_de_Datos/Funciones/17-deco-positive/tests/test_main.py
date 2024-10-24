import os
from functools import reduce
from operator import add

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ((2, 5, -9), None),
    ((10, 5), 15),
    ((2, 8, 4, 9, -1), None),
    ((9, 4, 12, 3), 28),
    ((5.25, 8), 13.25),
    ((1.2, 3.4), 4.6),
    ((-7.2, 6.1), None),
]


@pytest.mark.dependency()
def test_func_exists():
    assert getattr(
        main, 'assert_positive', None
    ), 'La función principal debe llamarse assert_positive'


@pytest.mark.parametrize('values, expected', testdata)
@pytest.mark.dependency(depends=['test_func_exists'])
def test_expected(values, expected):
    def check(*args):
        return reduce(add, args)

    assert main.assert_positive(check)(*values) == expected
