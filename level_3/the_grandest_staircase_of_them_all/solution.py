def answer(n):
    # there will be only *one* sequence with count 1
    result = make_stairs_count(n) - 1
    return result


def make_stairs(total_remaining):
    """Returns a list of all sequences of increasing values that add up to total_remaining"""
    all_lists = []

    def make_stairs_rec(prev_step_size, left, l):
        if left == 0:
            all_lists.append(l)
            return
        if left < 0:
            return

        for new_step_size in xrange(prev_step_size + 1, left + 1):
            new_left = left - new_step_size
            make_stairs_rec(new_step_size, new_left, l + [new_step_size])

        return

    make_stairs_rec(0, total_remaining, [])

    return all_lists


def make_stairs_count(total_remaining):
    """Returns the count of all sequences of increasing values that add up to total_remaining

    Since the problem only requires the count, this method will not keep track of the
    actual sequence.

    """
    def make_stairs_count_rec(prev_step_size, remaining):
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0

        result = 0

        for new_step_size in xrange(prev_step_size + 1, remaining + 1):
            new_remaining = remaining - new_step_size
            result += make_stairs_count_rec(new_step_size, new_remaining)
            # TODO: further pruning, and consider dynamic memory approach

        return result

    all_count = make_stairs_count_rec(0, total_remaining)

    return all_count
