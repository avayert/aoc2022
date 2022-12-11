from common import raw

import collections
import copy
import dataclasses
import heapq
import math
import re


pattern = re.compile(
    'Monkey \d:\s+'
    'Starting items: ([\d, ]+)\s+'
    'Operation: new = (.*)\s+'
    'Test: divisible by (\d+)\s+'
    'If true: throw to monkey (\d)\s+'
    'If false: throw to monkey (\d)'
)

@dataclasses.dataclass
class Monkey:
    items: list[int]
    operation: str
    divisor: int
    truthy: int
    falsey: int
    inspections: int = 0

monkey_templates = raw.split('\n' * 2)

monkeys = []
for template in monkey_templates:
    items, operation, divisor, truthy, falsey = pattern.match(template).groups()

    items = collections.deque(int(n) for n in items.split(','))
    divisor, truthy, falsey = int(divisor), int(truthy), int(falsey)

    monkeys.append(Monkey(items, operation, divisor, truthy, falsey))

upper_bound = math.prod([monkey.divisor for monkey in monkeys])

smuggled = copy.deepcopy(monkeys)


def tick(manage_worry):
    global monkeys

    for monkey in monkeys:
        monkey.inspections += len(monkey.items)

        while monkey.items:
            # tee hee
            old = monkey.items.popleft()
            new = eval(monkey.operation)

            if manage_worry:
                new //= 3

            new %= upper_bound

            index = monkey.truthy if new % monkey.divisor == 0 else monkey.falsey

            monkeys[index].items.append(new)


for round in range(20):
    tick(manage_worry=True)

a, b = heapq.nlargest(2, monkeys, key=lambda monkey: monkey.inspections)
print('Part 1:', a.inspections * b.inspections)

monkeys = smuggled
for round in range(10_000):
    tick(manage_worry=False)

a, b = heapq.nlargest(2, monkeys, key=lambda monkey: monkey.inspections)
print('Part 2:', a.inspections * b.inspections)
