def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    max_row_len = rows*2-1
    tree = [('*'*_num_stars(row+1)).center(max_row_len, ' ') for row in range(rows)]
    return '\n'.join(tree)

def _num_stars(row_num):
    return row_num*2-1