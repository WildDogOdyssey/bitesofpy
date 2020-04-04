from operator import add, sub, mul, truediv


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """

    ops_dict = dict(zip('+ - * /'.split(), [add, sub, mul, truediv]))

    a, ops, b = calculation.split()

    try:
        func = ops_dict[ops]
        return func(int(a), int(b))
    except (KeyError, ZeroDivisionError):
        raise ValueError

# print(simple_calculator('2 + 3'))