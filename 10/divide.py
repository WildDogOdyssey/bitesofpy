def positive_divide(numerator, denominator):
    try:
        r = numerator / denominator
    except ZeroDivisionError:
        r = 0
    if r < 0:
        raise ValueError
    else:
        return r