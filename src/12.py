from common import lines

from collections import deque


NEIGHBOURS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


heights = [
    [ord(c) for c in line]
    for line in lines
]


def search(start, end):
    remaining = deque()
    remaining.append((0, start, ord('a'), ()))

    seen = set()

    while remaining:
        depth, (y, x), previous, history = remaining.popleft()

        if (y, x) == end:
            return depth

        if (y, x) in seen:
            continue

        seen.add((y, x))

        for dy, dx in NEIGHBOURS:
            ny, nx = y + dy, x + dx

            if len(heights) <= ny or ny < 0 or len(heights[0]) <= nx or nx < 0:
                continue

            new = heights[ny][nx]

            if new > previous + 1:
                continue

            remaining.append((depth + 1, (ny, nx), new, history + ((y, x),)))

    # oops, we couldn't actually get to the end!
    return float('inf')


starting_position = start_y, start_x = next((y, x) for y, row in enumerate(heights) for x, height in enumerate(row) if height == ord('S'))
ending_position = end_y, end_x = next((y, x) for y, row in enumerate(heights) for x, height in enumerate(row) if height == ord('E'))

heights[start_y][start_x] = ord('a')
heights[end_y][end_x] = ord('z')

print('Part 1:', search(start=starting_position, end=ending_position))

smallest = min(search(start=(y, x), end=ending_position) for y, row in enumerate(heights) for x, height in enumerate(row) if height == ord('a'))
print('Part 2:', smallest)
