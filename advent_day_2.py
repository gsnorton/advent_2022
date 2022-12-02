
#
# advent_day_2.py
#
# usage: advent_day_2.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput

# -----------------------------------------------------------------------------

def _main():
    score = 0
    score_2 = 0

    for line in fileinput.input():
        opponent, mine = line.split()

        score += ord(mine) - ord('X') + 1

        if opponent == 'A' and mine == 'X':
            score += 3
        elif opponent == 'B' and mine == 'Y':
            score += 3
        elif opponent == 'C' and mine == 'Z':
            score += 3
        elif opponent == 'A' and mine == 'Z':
            score += 0
        elif opponent == 'B' and mine == 'X':
            score += 0
        elif opponent == 'C' and mine == 'Y':
            score += 0
        elif opponent == 'A' and mine == 'Y':
            score += 6
        elif opponent == 'B' and mine == 'Z':
            score += 6
        elif opponent == 'C' and mine == 'X':
            score += 6

        outcome = mine

        if opponent == 'A' and outcome == 'X':
            score_2 += 0 + 3
        elif opponent == 'B' and outcome == 'Y':
            score_2 += 3 + 2
        elif opponent == 'C' and outcome == 'Z':
            score_2 += 6 + 1
        elif opponent == 'A' and outcome == 'Z':
            score_2 += 6 + 2
        elif opponent == 'B' and outcome == 'X':
            score_2 += 0 + 1
        elif opponent == 'C' and outcome == 'Y':
            score_2 += 3 + 3
        elif opponent == 'A' and outcome == 'Y':
            score_2 += 3 + 1
        elif opponent == 'B' and outcome == 'Z':
            score_2 += 6 + 3
        elif opponent == 'C' and outcome == 'X':
            score_2 += 0 + 2

    print score
    print score_2

if __name__ == '__main__':
    _main()
