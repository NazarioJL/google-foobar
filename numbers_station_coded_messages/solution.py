def answer(l, t):
    list_size = len(l)
    # create default result of subsequence not found
    result = [-1, -1]

    # first and last pointers
    first = 0
    last = 0

    # this variable holds the sublist sum bound by first / last indexes
    running_sum = l[first]

    while True:
        if running_sum < t:
            if last == list_size - 1:
                # all numbers are positive, no need to keep substracting
                # shorter list -> smaller number
                break
            # increase the subsequence to the right
            last += 1
            if last == list_size:
                break
            running_sum += l[last]
        elif running_sum > t:
            # decrease the subsequence from the left
            if first == last:
                last += 1
                if last == list_size:
                    break
                running_sum += l[last]
            running_sum -= l[first]
            first += 1
        else:
            result = [first, last]
            break

    return result
