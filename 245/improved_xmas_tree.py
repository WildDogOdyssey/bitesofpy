STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    max_row = rows*2-1
    star = [STAR.center(max_row)]
    leaves = [(count*LEAF).center(max_row) for count in range(1, max_row + 2, 2)]
    trunks = [((round(max_row/2)+1)*TRUNK).center(max_row) for row in range(2)]
    return '\n'.join(star + leaves + trunks)

# print(generate_improved_xmas_tree())