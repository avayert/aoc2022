from common import raw
from collections import deque
import itertools


def sliding_window(iterable, *, n):
    it = iter(iterable)

    window = deque(maxlen=n)
    window.extend(itertools.islice(it, n))
    yield tuple(window)

    for elem in it:
        window.append(elem)
        yield tuple(window)


def find_distinct(n):
    return next(
        index
        for index, view in enumerate(sliding_window(raw, n=n), start=n)
        if len(set(view)) == n
    )


print('Part 1:', find_distinct(n=4))
print('Part 1:', find_distinct(n=14))
