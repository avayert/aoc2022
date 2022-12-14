from common import lines

import itertools


occupied = set()

points = [
    [tuple(map(int, points.split(','))) for points in line.split('->')]
    for line in lines
]

for group in points:
    for (x1, y1), (x2, y2) in zip(group, group[1:]):
        # lol no minmax
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        horizontal = range(x1, x2 + 1)
        vertical = range(y1, y2 + 1)
        for x, y in itertools.product(horizontal, vertical):
            occupied.add(complex(x, y))

bottom = max(coordinate.imag for coordinate in occupied)

with_floor = occupied.copy()


CANDIDATE_POSITIONS = (0 + 1j, -1 + 1j, 1 + 1j)

def simulate():
    for n_sand in itertools.count(start=0):
        sand = 500 + 0j

        while True:
            if sand.imag > bottom:
                return n_sand

            # haha yes!
            for candidate_position in CANDIDATE_POSITIONS:
                if sand + candidate_position not in occupied:
                    sand += candidate_position
                    break
            else:
                occupied.add(sand)
                break


print('Part 1:', simulate())

bottom += 1

# I'm lazy
def simulate():
    for n_sand in itertools.count(start=0):
        sand = 500 + 0j

        if sand in with_floor:
            return n_sand

        while True:
            if sand.imag == bottom:
                break

            for candidate_position in CANDIDATE_POSITIONS:
                if sand + candidate_position not in with_floor:
                    sand += candidate_position
                    break
            else:
                break

        with_floor.add(sand)

print('Part 2:', simulate())
