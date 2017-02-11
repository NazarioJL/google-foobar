from itertools import combinations
from functools import reduce

def answer(l):
    # sort list and reverse
    sorted_l = sorted(l)
    sorted_l.reverse()

    list_size = len(sorted_l)

    if list_size == 0:
        return 0

    # try to find combinations with higher number of elements first that satisfy criteria
    # a number that is divisible by 3 will have the sum of its digits also divisible by 3
    for combo_size in xrange(list_size, 0, -1):
        # lazily generate combinations in lexicographic order
        result = next((x for x in combinations(sorted_l, combo_size) if sum(x) % 3 == 0), None)
        if result:
            # convert list to number i.e. [1,2,3] -> 123 and exit early with result
            return reduce((lambda acc, curr: acc * 10 + curr), result, 0)
    # we found no combination suitable, we return 0
    return 0
