
#
# advent_day_8.py
#
# usage: advent_day_8.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput
import heapq

# -----------------------------------------------------------------------------

def look_at_line(line, ignore_col=None):
    visible = 0
    cols = []

    print ignore_col,

    for _i, tree in enumerate(line):

        try:
            heapq.heappush(_q, tree)

            if _q[0] == tree:
                heapq.heappop(_q)
            elif tree in _q:
                if not ignore_col or _i in ignore_col:
                    visible += 1
                    cols.append(_i)
            while _q[0] < tree:
                heapq.heappop(_q)

        except NameError:
            _q = [tree] # Create the queue

    print visible, cols

    return visible, cols

def process_line(line):

    print line

    # Look from left

    left_visible, cols_l = look_at_line(line[:-1])

    # Look from right

    line_rev = "".join(reversed(line))

    try:
        right_visible, cols_r = look_at_line(line_rev[:-1],
                                             [(len(line) - 1 - cols_l[-1])])

    except IndexError:
        right_visible, cols_r = look_at_line(line_rev[:-1])

    # XXXX

    return left_visible + right_visible

def _main():

    for _line in fileinput.input():

        line = _line.strip()

        if fileinput.isfirstline():
            line_index = 0

            cols_up = [list(tree) for tree in line]
            dim = len(line)

            visible = 4*(dim - 1)

        elif not line_index == (dim - 2):
            line_index += 1

            line_visible = process_line(line)
            visible += line_visible

            # XXXX

        else:
            pass # XXXX

    print visible

if __name__ == '__main__':
    _main()
