from collections import OrderedDict

"""TODO: two elements affect RN character, decimal place and repeats of four:
1) each decimal place has own char, 2) each char cannot repeat more than 3 times (< 4).
Hence, each decimal place has two chars with the last sourced from the next decimal place.
"""

RN = {
    1000: (None, None, 'M'),
    100: ('M', 'D', 'C'),
    10: ('C', 'L', 'X'),
    1: ('X', 'V', 'I')
}

def romanize(decimal_number: int) -> str:
    """Takes a decimal number int and converts its Roman Numeral str"""

    if not isinstance(decimal_number, int):
        raise ValueError
    if (decimal_number <= 0 or decimal_number >= 4000):
        raise ValueError

    dn_str = str(decimal_number)
    dn_len = len(dn_str)
    dn_by_digit = [int(n) for n in dn_str]

    dn_place = list(zip(dn_by_digit,
                        [10**(dn_len - 1 - i) for i in range(dn_len)]))

    res = [_convert(n, place) for n, place in dn_place]
    return ''.join(res)

def _convert(n: int, place: int) -> str:
    """Helper function to turn one number with its decimal place information
    to the corresponding roman numeral in that decimal place.
    """

    rn = RN[place]
    if n < 4:
        return rn[2] * n
    elif n == 4:
        return rn[2] + rn[1]
    elif n == 5:
        return rn[1]
    elif n == 9:
        return rn[2] + rn[0]
    else:
        return rn[1] + rn[2] * (n - 5)


# print(romanize(3999))

# for i in range(10):
#     print(_convert(i, 1000))

# print(_convert(3, 1000))