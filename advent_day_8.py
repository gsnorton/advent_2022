
#
# advent_day_8.py
#
# usage: advent_day_8.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput
import heapq
import collections

# -----------------------------------------------------------------------------

def look_at_line(line, ignore_col=None):
    visible = 0
    cols = []

    for _i, tree in enumerate(line):

        try:
            heapq.heappush(_q, tree)

            if _q[0] == tree:
                heapq.heappop(_q)
            elif tree in _q:
                if not ignore_col or _i not in ignore_col:
                    visible += 1
                    cols.append(_i)

            while _q[0] < tree:
                heapq.heappop(_q)

        except NameError:
            _q = [tree] # Create the queue

    return visible, cols

def process_line(line):

    # Look from left

    left_visible, cols = look_at_line(line[:-1])

    # Look from right

    line_rev = "".join(reversed(line))

    try:
        right_visible, cols_r = look_at_line(line_rev[:-1],
                                             [(len(line) - 1 - cols[-1])])

    except IndexError:
        right_visible, cols_r = look_at_line(line_rev[:-1])

    for col in cols_r:
        cols.append(len(line) - 1 - col)

    return left_visible + right_visible, sorted(cols)

def process_col(col):
    print col

def _main():

    for _line in fileinput.input():

        line = _line.strip()

        if fileinput.isfirstline():
            line_index = 0

            cols_look_up = [collections.deque(tree) for tree in line]
            ignore_line_col = []
            dim = len(line)

            visible = 4*(dim - 1)

        elif not line_index == (dim - 2):
            line_index += 1

            for _i, tree in enumerate(line):
                cols_look_up[_i].appendleft(tree)

            line_visible, cols = process_line(line)
            visible += line_visible

            ignore_line_col.extend([(line_index, col) for col in cols])

            print line_index, line, line_visible, cols

        else:
            for _i, tree in enumerate(line[1:-1]):

                # XXXX Is there a cleaner way to build col?
                col = [tree]
                for _t in cols_look_up[_i+1]:
                    col.append(_t)

                line_visible, rows = process_line(col)

                print _i+1, "".join(col), line_visible, rows

                # XXXX Could this be cleaner?
                for _r in rows:
                    if not (len(col) - 1 - _r, _i+1) in ignore_line_col:
                        visible += 1

            print visible

if __name__ == '__main__':
    _main()
