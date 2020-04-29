THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    def __mul__(self, score):
        if score == 0:
            raise ValueError
        thumb = THUMBS_UP if score > 0 else THUMBS_DOWN
        num = abs(score)
        return (thumb + f' ({num}x)') if num > 3 else thumb*num

    __rmul__ = __mul__

    # def __call__(self, score):
    #     # Raise ValueError if 0
    #     if score == 0:
    #         raise ValueError
    #     # Thumbs up or down based on sign
    #     thumb = THUMBS_UP if score > 0 else THUMBS_DOWN
    #     # Long form representation
    #     num = abs(score)
    #     rep = f' ({num}x)' if num > 3 else thumb*(num - 1)
    #
    #     return thumb + rep
    #
    # def __mul__(self, other):
    #     return self.__call__(other)
    #
    # __rmul__ = __mul__
