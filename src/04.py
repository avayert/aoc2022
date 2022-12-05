from common import lines
from itertools import islice
import re


lines = [
    tuple(int(digit) for digit in re.findall('\d+', line))
    for line in lines
]

print('Part 1:', sum((a <= x and b >= y) or (x <= a and y >= b) for (a, b, x, y) in lines))
print('Part 2:', sum(a <= y and x <= b for (a, b, x, y) in lines))
