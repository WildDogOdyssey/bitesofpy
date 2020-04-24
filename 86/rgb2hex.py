def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    res = ''
    for color in rgb:
        if color not in range(0, 256):
            raise ValueError
        hx = str(hex(color)).replace('0x', '').upper()
        res += hx if len(hx) == 2 else '0' + hx
    return f'#{res}'

print(rgb_to_hex((255, 0, 255)))