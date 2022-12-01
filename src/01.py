from common import raw
import heapq


sections = raw.split('\n' * 2)

food_carried = [sum(map(int, section.split())) for section in sections]

print('Part 1:', max(food_carried))
print('Part 2:', sum(heapq.nlargest(iterable=food_carried, n=3)))
