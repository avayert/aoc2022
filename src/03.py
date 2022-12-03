from common import lines
from itertools import islice


OFFSET_UPPERCASE = ord('A') - 27  # Uppercase item types A through Z have priorities 27 through 52.
OFFSET_LOWERCASE = ord('a') - 1   # Lowercase item types a through z have priorities 1 through 26.


def priority(character):
    offset = OFFSET_LOWERCASE if character >= 'a' else OFFSET_UPPERCASE
    return ord(character) - offset


total = 0
for line in lines:
    pivot_point = len(line) // 2
    left, right = line[:pivot_point], line[pivot_point:]

    common_characters = set(left).intersection(right)
    total += sum(map(priority, common_characters))

print('Part 1:', total)


def chunks(iterable, *, n):
    it = iter(iterable)
    return iter(lambda: tuple(islice(it, n)), ())


total = 0
for first, *others in chunks(lines, n=3):
    common_characters = set(first).intersection(*others)
    total += sum(map(priority, common_characters))

print('Part 2:', total)
