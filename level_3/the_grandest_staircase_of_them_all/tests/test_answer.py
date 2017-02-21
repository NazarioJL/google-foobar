from nose.tools import eq_

from ..solution import answer

def test_answer():
    # define expected input / output values
    test_data = {
        0 : 0, 1 : 0, 2 : 0, 3 : 1, 4 : 1, 5 : 2,
        6 : 3, 7 : 4, 8 : 5, 9 : 7, 10 : 9, 11 : 11
    }

    for key, expected in test_data.items():
        yield eq_, expected, answer(key)
