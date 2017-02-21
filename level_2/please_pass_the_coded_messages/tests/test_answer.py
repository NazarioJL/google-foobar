from nose.tools import eq_

from ..solution import answer

def test_answer():
    test_data = [
        ([3, 1, 4, 1], 4311),
        ([3, 1, 4, 1, 5, 9], 94311),
        ([0], 0),
        ([], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 987654321)
    ]

    for _ in test_data:
        actual = answer(_[0])
        expected = _[1]
        yield eq_, expected, actual
