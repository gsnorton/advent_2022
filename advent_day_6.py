
#
# advent_day_6.py
#
# usage: advent_day_6.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput
import collections

# -----------------------------------------------------------------------------

def _main():

    # Part One

    # _q = collections.deque(maxlen=4)

    # Part Two

    _q = collections.deque(maxlen=14)

    for line in fileinput.input():
        _i = 1

        for _c in line:
            _q.append(_c)

            # Part One

            # if len(set(_q)) == 4:
            #     break

            # Part Two

            if len(set(_q)) == 14:
                break

            _i += 1

    print _i

if __name__ == '__main__':
    _main()
