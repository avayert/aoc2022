from common import raw

import functools


sections = [
    tuple(map(eval, section.splitlines()))
    for section in raw.split('\n' * 2)
]


def compare(left, right):
    match left, right:
        case list(), list():
            # this is some top tier bullshit right here
            for a, b in zip(left, right):
                ret = compare(a, b)
                if ret:
                    return ret
            return compare(len(left), len(right))
        case list(), int():
            return compare(left, [right])
        case int(), list():
            return compare([left], right)
        case int(), int():
            # this is also some good bullshit
            return (right < left) - (left < right)


in_order = sum(index for index, (left, right) in enumerate(sections, start=1) if compare(left, right) == -1)
print('Part 1:', in_order)

items = [item for section in sections for item in section]
items.extend(([[2]], [[6]]))
items.sort(key=functools.cmp_to_key(compare))
a, b = items.index([[2]]), items.index([[6]])
print('Part 2:', (a + 1) * (b + 1))
