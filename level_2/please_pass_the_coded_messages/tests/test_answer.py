from ..solution import answer

from nose.tools import eq_

def test_answer():
    eq_(4311, answer([3, 1, 4, 1]))
    eq_(94311, answer([3, 1, 4, 1, 5, 9]))
    eq_(0, answer([0]))
    eq_(0, answer([]))
    eq_(987654321, answer([1, 2, 3, 4, 5, 6, 7, 8, 9]))
