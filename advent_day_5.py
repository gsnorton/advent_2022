
#
# advent_day_5.py
#
# usage: advent_day_5.py input_file_1.txt [ input_file_2.txt ... ]
#

import fileinput
import re
import collections

# -----------------------------------------------------------------------------

_NUM_MATCH = re.compile('[0-9]+')

def _main():

    for line in fileinput.input():

        if fileinput.isfirstline():

            # Start drawing

            drawing_done = False
            drawing = [line]

        elif not line.strip():

            # Blank line indicates end of drawing

            drawing_done = True

        elif not drawing_done and not _NUM_MATCH.search(line):

            # Add a line of crates to the drawing

            drawing.append(line)

        elif not drawing_done:

            # Process the label line and build the stacks

            stacks = []

            for label in _NUM_MATCH.finditer(line):
                stacks.append(collections.deque())

                # Extract the crates for this stack from
                # from each level in the dawing

                stack_index = (int(label.group()[0]) - 1)*4

                for level in drawing:
                    crate = level[stack_index + 1]
                    if crate.split():
                        stacks[-1].append(crate)

        else:

            # Move the crates according to the instruction line

            instruction = list(_NUM_MATCH.finditer(line))

            move_count = int(instruction[0].group())
            src_stack_index = int(instruction[1].group()) - 1
            dest_stack_index = int(instruction[2].group()) - 1

            print move_count, src_stack_index, dest_stack_index,

            # Part One

            # for _ in xrange(move_count):
            #     stacks[dest_stack_index].appendleft(stacks[src_stack_index].popleft())

            # Part Two

            group = collections.deque()

            for _ in xrange(move_count):
                group.append(stacks[src_stack_index].popleft())
            while group:
                stacks[dest_stack_index].appendleft(group.pop())

            # Print the stacks

            for stack in stacks:
                try:
                    print stack[0],
                except:
                    print "-",

            print

if __name__ == '__main__':
    _main()
