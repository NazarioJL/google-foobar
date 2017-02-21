from nose.tools import eq_

from ..solution import answer

def test_answer():
    no_solution = [-1, -1]
    test_data = [
        (([4, 3, 10, 2, 8], 12), [2, 3]),
        (([1, 2, 3, 4], 15), no_solution),
        (([1, 1, 40], 30), no_solution),
        (([1, 1, 30], 30), [2, 2])]

    for _ in test_data:
        actual = answer(*_[0])
        expected = _[1]
        yield eq_, expected, actual
