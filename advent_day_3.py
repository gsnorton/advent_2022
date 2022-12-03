
#
# advent_day_3.py
#
# usage: advent_day_3.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput

from collections import Counter, deque

# -----------------------------------------------------------------------------

def _priority(_c):
    if ord(_c) >= ord('a'):
        return ord(_c) - ord('a') + 1
    return ord(_c) - ord('A') + 27

def _main():
    _sum = 0
    line_count = 0

    _sum_2 = 0

    _q = deque(maxlen=3)

    for line in fileinput.input():
        _line = line.strip()
        half1 = Counter(_line[:len(_line)/2])
        half2 = Counter(_line[len(_line)/2:])

        common = half1 & half2

        _sum += _priority(list(common.elements())[0])

        line_count += 1

        _q.append(Counter(_line))

        if (line_count % 3) == 0:
            common = _q[0] & _q[1] & _q[2]
            _sum_2 += _priority(list(common.elements())[0])

    print _sum
    print _sum_2

if __name__ == '__main__':
    _main()
