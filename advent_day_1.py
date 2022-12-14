
#
# advent_day_1.py
#
# usage: advent_day_1.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput

# -----------------------------------------------------------------------------

def _main():
    elf_list = []
    calories = 0

    for line in fileinput.input():
        try:
            calories += int(line)
        except ValueError:
            elf_list.append(calories)
            calories = 0

    print sorted(elf_list, reverse=True)[0]
    print sum(sorted(elf_list, reverse=True)[0:3])

if __name__ == '__main__':
    _main()
