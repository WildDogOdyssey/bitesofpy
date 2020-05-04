from dataclasses import dataclass

@dataclass()
class Bite(object):
    number: int
    title: str
    level: str = 'Beginner'

    def __post_init__(self):
        self.title = self.title.capitalize()

    def __lt__(self, other):
        return True if self.number < other.number else False

# b1 = Bite(number=1, title="sum of numbers")
# b2 = Bite(number=2, title="a second bite", level="Intermediate")
# b3 = Bite(number=3, title="a hard bite", level="Advanced")
# bites = [b1, b2, b3]
#
# print(bites)
# print(sorted(bites, reverse=True))

