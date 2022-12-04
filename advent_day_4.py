
#
# advent_day_4.py
#
# usage: advent_day_4.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput

from collections import Counter

# -----------------------------------------------------------------------------

# H/T: https://stackoverflow.com/questions/2250633/
#          python-find-a-list-within-members-of-another-listin-order

def is_sublist(_a, _b):
    if not _a:
        return True
    if not _b:
        return False
    return _b[:len(_a)] == _a or is_sublist(_a, _b[1:])

def _main():
    contained_count = 0
    overlap_count = 0

    for line in fileinput.input():
        _range1 = line.strip().split(',')[0]
        range1 = range(int(_range1.split('-')[0]),
                       int(_range1.split('-')[1]) + 1)

        _range2 = line.strip().split(',')[1]
        range2 = range(int(_range2.split('-')[0]),
                       int(_range2.split('-')[1]) + 1)

        if is_sublist(range1, range2) or is_sublist(range2, range1):
            contained_count += 1

        if list(Counter(range1) & Counter(range2)):
            overlap_count += 1

    print contained_count
    print overlap_count

if __name__ == '__main__':
    _main()
