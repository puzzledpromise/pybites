import re
from collections import namedtuple
import sys

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

LRTB = namedtuple("LRTB", "left right top bottom")

small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

intermediate_grid = """
43 - 44 - 45 - 46 - 47 - 48 - 49
 |
42   21 - 22 - 23 - 24 - 25 - 26
 |    |                        |
41   20    7 -  8 -  9 - 10   27
 |    |    |              |    |
40   19    6    1 -  2   11   28
 |    |    |         |    |    |
39   18    5 -  4 -  3   12   29
 |    |                   |    |
38   17 - 16 - 15 - 14 - 13   30
 |                             |
37 - 36 - 35 - 34 - 33 - 32 - 31
"""

def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    analysis = analyze_grid(grid)
    min_num = min(analysis.keys())
    max_num = max(analysis.keys()) 
   
    res = analysis[min_num]
    mov = get_movement(res, min_num+1)

    buf = ""
    for i in range(min_num, max_num+1):
        print(buf + str(i),end="")
        res = analysis[i]
        mov_next = get_movement(res, i+1)
        if mov != mov_next:
            print(" " + mov_next)
            buf = ""
        else:
            buf = " " 
        mov = mov_next




def get_movement(lrtb, look_for):

    if look_for == lrtb.top:
        return UP
    elif look_for == lrtb.bottom:
        return DOWN
    elif look_for == lrtb.left:
        return LEFT
    else:
        return RIGHT

        

def get_lines(grid):
    lines = grid.split("\n")
    lines = lines[1:] # Drop the first line (empty)
    lines.pop() # Drop the last line (empty)
    return lines

def get_entry_at(lines, row, col):
    """Get the entry (number, |, -) at the given row and col index."""
    line = lines[row]
   
    lrtb = [None, None, None, None]
    s,e,digit = get_digit_at(lines, row, col)

    if row > 1:
        if e < len(lines[row-1]) and lines[row-1][e] =="|":
            lrtb[2] = get_digit_at(lines, row-2,e)[2]
    if row + 2 < len(lines):
        if e < len(lines[row+1]) and lines[row+1][e]== "|":
            lrtb[3]= get_digit_at(lines, row+2,e)[2]
    if s >= 5:
        if len(str(digit))<2:
            offset = 1
        else:
            offset = 0
        if lines[row][s-2-offset]=="-":
            lrtb[0] = get_digit_at(lines, row, s-4-offset)[2]
    if e + 4 < len(lines[row]):
        if lines[row][e+2] == "-":
            lrtb[1] = get_digit_at(lines, row, e+5)[2]
    return digit, LRTB(*lrtb) 

def get_digit_at(lines, row, col):
    line = lines[row]
    entry = line[col]
    if entry.isdigit():
        s = col
        while(True):
            if s > 0 and line[s-1].isdigit():
                s-=1
            else:
                break

        # at this point we should be on the first digit of the number
        e = s
        entry = ""
        while(True):
            entry = entry + line[e]
            if e + 1 < len(line) and line[e+1].isdigit():
                e+=1
            else:
                break
        return s, e, int(entry)

def analyze_grid(grid):
    lines = get_lines(grid)
    result = dict()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (lines[row][col]).isdigit():
                dig = get_digit_at(lines, row, col)[2]
            
                if dig not in result:
                    result[dig] = get_entry_at(lines, row, col)[1]

    return result





if __name__ == "__main__":
    print_sequence_route(intermediate_grid)
    
      
