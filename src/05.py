from common import lines
import copy
import itertools
import re


lines = iter(lines)
boxes = itertools.takewhile(''.__ne__, lines)

# first, disregard all inconsequential characters
columns = [level[1::4] for level in boxes]
# then compose from column to row representation
columns = zip(*columns)
# finally, collect the strings into stacks
# reversal is done so we can pop and push from the end, thus having not to do a linear shift of the characters each time
columns = [[c for c in reversed(column) if c.isupper()] for column in columns]

# store a separate copy for each part
part1, part2 = copy.deepcopy(columns), copy.deepcopy(columns)


for line in lines:
    n, source, destination = re.findall('\d+', line)

    n = int(n)
    source, destination = int(source) - 1, int(destination) - 1

    for i in range(n):
        part1[destination] += [part1[source].pop()]

    part2[destination] += part2[source][-n:]
    del part2[source][-n:]

print('Part 1:', ''.join(top for *bottom, top in part1))
print('Part 2:', ''.join(top for *bottom, top in part2))
