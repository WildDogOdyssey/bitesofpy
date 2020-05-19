from math import log, floor


def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    try:
        pwr = floor(log(number, base))
    except ValueError:
        pwr = 0

    q = number // (base ** pwr)
    r = number % (base ** pwr)

    if pwr == 0:
        return number
    else:
        return q*(10**pwr) + dec_to_base(r, base)

# print(dec_to_base(5, 6))
# print(dec_to_base(10, 2))