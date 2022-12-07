from common import lines

import collections

# I wanted to use pathlib with grea joy, but it doesn't actually seem like it'd help much, since we'd need to call
# `stat` to actually get file sizes and it doesn't seem like that can be virtualized. Shame!

cumulative_sizes = collections.Counter()

cwd = []
for line in lines:
    match line.split():
        case ['$', 'cd', '..']:
            cwd.pop()
        case ['$', 'cd', directory]:
            cwd.append(directory)
        case [size, filename] if size.isdecimal():
            # sub-directory names aren't unique so use a tuple of ('/', 'a', 'b') as key
            for bound in range(0, len(cwd)):
                path = tuple(cwd[:bound + 1])
                cumulative_sizes[path] += int(size)

print('Part 1:', sum(size for size in cumulative_sizes.values() if size <= 100_000))

MAX_SIZE = 70_000_000 - 30_000_000
ROOT_SIZE = cumulative_sizes[('/',)]

print('Part 2:', min(size for size in cumulative_sizes.values() if ROOT_SIZE - size <= MAX_SIZE))
