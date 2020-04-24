def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""

    # res = ''
    # for color in rgb:
    #     if color not in range(0, 256):
    #         raise ValueError
    #     res += '{0:02X}'.format(color)
    # return f'#{res}'

    if not all(color in range(0, 256) for color in rgb):
        raise ValueError
    return '#' + ''.join('{0:02X}'.format(color) for color in rgb)

print(rgb_to_hex((255, 0, 255)))