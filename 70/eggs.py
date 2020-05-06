from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:

    def __init__(self, limit):
        self.egg_it = (choice(COLORS) for _ in range(limit))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.egg_it)