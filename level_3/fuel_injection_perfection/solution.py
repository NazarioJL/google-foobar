import math

 # Define operation constants
DIVIDE = '/'
INCREMENT = '+'
DECREMENT = '-'

def answer(n):
    # the incoming value is a string, python handles big integers pretty well
    fuel = int(n)
    return sum(1 for item in refine_fuel(fuel))

def pretty_print_operations(initial_fuel, ops):
    result = '({}) => [{}] {}'.format(initial_fuel, len(ops), str(initial_fuel))
    for op in ops:
        result += '->({}) {}'.format(op[0], op[1])
    print result

def refine_fuel(fuel_qty):
    """
    Calculates the minimum sequence of operations required to refine the input fuel.

    Generates the smallest sequence of operations applied to the input value to reduce it to 1.
    The allowed operations are:
        - INCREMENT: Increment the value by 1 ('+')
        - DECREMENT: Decrement the value by 1 ('-')
        - DIVIDE: Divide the value by 2, can only be applied to even numbers. ('/')

    Args:
        fuel_qty (int): The amount of fuel that needs to be refined.

    Yields:
        (tuple): tuple containing:
            operation (str): one of (DIVIDE, INCREMENT, DECREMENT)
            state (int): the intermediate value of remaining fuel after the operation is applied

    """

    if fuel_qty == 0:
        raise StopIteration

    while fuel_qty > 1:
        if fuel_qty % 2 == 0:
            # number is even always, always half
            fuel_qty /= 2
            yield (DIVIDE, fuel_qty)
        else:
            # number is odd
            # special casing 3 since 2 and 4 are both powers of 2
            if fuel_qty == 3:
                fuel_qty -= 1
                yield (DECREMENT, fuel_qty)
                continue

            # calculate the next power of 2
            log_2 = int(math.log(fuel_qty, 2))
            bigger_pow2 = 2 ** (log_2 + 1)

            bigger = fuel_qty + 1
            smaller = fuel_qty - 1

            # TODO: Seems like this can be simplified
            # We only want to increment if the half of smaller is odd and the half of bigger is even
            # or if bigger is a pure power of 2
            if ((smaller / 2) % 2 != 0) and ((bigger / 2) % 2 == 0) or bigger == bigger_pow2:
                fuel_qty = bigger
                yield (INCREMENT, fuel_qty)
            else:
                fuel_qty = smaller
                yield (DECREMENT, fuel_qty)
    return
