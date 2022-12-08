from common import lines

import itertools


lines = [[int(digit) for digit in line] for line in lines]
mask = [[False] * len(line) for line in lines]


def rotated(grid):
    transposed = [list(row) for row in zip(*grid)]
    transposed.reverse()
    return transposed


# our strategy is to simply look for visible trees going left-to-right,
# then transposing the entire grid to repeat it four times. Marking a tree
# as visible is idempodent so we can't get duplicates.
for i in range(4):
    for index, line in enumerate(lines):
        largest_found = -1

        for offset, digit in enumerate(line):
            if digit > largest_found:
                mask[index][offset] = True
                largest_found = digit

            # 9 is the highest that a tree can be so we can terminate early
            if digit == 9:
                break

    lines = rotated(lines)
    mask = rotated(mask)

print('Part 1:', sum(map(sum, mask)))


# This is just a brute force approach. Preprocessing would be more ugly, I think.
OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def scenic_score(row, column):
    total = 1
    height = lines[column][row]

    for dy, dx in OFFSETS:
        # we always count the distance, so we start from 1
        for i in itertools.count(start=1):
            y = column + dy * i
            x = row + dx * i

            # negative indexing is a thing so I opt to bounds check explicitly
            if y == -1 or x == -1 or y == len(lines) or x == len(lines[0]):
                i -= 1
                break

            # if the tree at that point is as tall or taller, we cannot see further.
            if lines[y][x] >= height:
                break

        total *= i

    return total

score = max(
    scenic_score(column, row)
    for column, line in enumerate(lines)
    for row, _ in enumerate(line)
)
print('Part 2:', score)
