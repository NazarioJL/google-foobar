from solution import answer

from nose.tools import eq_

def test_answer():
    no_solution = [-1, -1]
    eq_([2, 3], answer([4, 3, 10, 2, 8], 12))
    eq_(no_solution, answer([1, 2, 3, 4], 15))
    eq_(no_solution, answer([1, 1, 40], 30))
    eq_([2, 2], answer([1, 1, 30], 30))
