def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    conv = {'cm': 2.54, 'in': 1/2.54}

    try:
        rate = conv[fmt.lower()]
    except KeyError:
        raise ValueError

    return round(value * rate, 4)

