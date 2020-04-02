STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """

    rubric = list(range(1, width, 2)) + list(range(width, 0, -2))
    for i in rubric:
        yield (i*STAR).center(width)

# print(list(gen_rhombus(5)))