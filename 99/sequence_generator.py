import string
from itertools import cycle

def sequence_generator():
    seq = zip(list(range(1, 27)), string.ascii_uppercase)
    flat = [val for subtuple in seq for val in subtuple]
    
    return cycle(flat)

# print(sequence_generator())
# print(next(sequence_generator()))