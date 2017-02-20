from ..solution import answer

from nose.tools import eq_

def test_answer():
    # define expected input / output values
    test_data = [
        ("1", 0), ("8", 3), ("100", 8), ("507", 11), ("1024", 10), ("1025", 11),
        ("654645646465465465464654654654654654", 152)
    ]

    for _ in test_data:
        actual = answer(_[0])
        expected = _[1]
        eq_(expected, actual)
