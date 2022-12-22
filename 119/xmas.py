def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    branch = ""
    for r in range(1, rows + 1):
        branch += " " * (rows - r) + "*" * 2 * (r -1) + "*" + "\n" 

    return branch[:-1]
        

if __name__ == "__main__":
    print(generate_xmas_tree(11))
