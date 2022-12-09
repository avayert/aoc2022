from common import lines

import math


MAX_DISTANCE = math.sqrt(2)
DIRECTIONS = dict(R=1+0j, L=-1+0j, U=0-1j, D=0+1j)


instructions = [
    (DIRECTIONS[direction], int(distance))
    for line in lines
    for direction, distance in [line.split()]
]


def clamp(start, mid, end):
    return max(min(mid, end), start)


def clamp_direction(direction):
    # there _has_ to be a better way to do this right?
    return complex(
        clamp(-1, direction.real, 1),
        clamp(-1, direction.imag, 1),
    )


head = tail = 0+0j

found = {tail}

for direction, distance in instructions:
    for _ in range(distance):
        head += direction

        difference = head - tail
        if abs(difference) <= MAX_DISTANCE:
            continue

        tail += clamp_direction(difference)

        found.add(tail)

print('Part 1:', len(found))


# big old bruh moment
segments = [0+0j] * 10

found = set()

for direction, distance in instructions:
    for _ in range(distance):
        segments[0] += direction

        for index, (previous, next) in enumerate(zip(segments, segments[1:]), start=1):
            difference = previous - next
            if abs(difference) <= MAX_DISTANCE:
                continue

            segments[index] += clamp_direction(difference)

        found.add(segments[-1])

print('Part 2:', len(found))
