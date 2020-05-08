from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f'{self.name} => {self.value*THUMBS_UP}'

    @classmethod
    def average(cls):
        values = [val.value for val in cls.__members__.values()]
        return sum(values) / len(cls)