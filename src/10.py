from common import lines


total = cycles = 0
register = 1

image = ''

# we can remove duplicate logic by inserting non-addx instructions
# into the data and pretending addx takes one cycle after all.
lines = [
    instruction
    for line in lines
    for instruction in ['noop'] + [line] * (line != 'noop')  # xd
]


for instruction in lines:
    # reading comprehension devil strikes again
    pixel = cycles % 40
    if pixel == 0:
        image += '\n'
    image += '#' if register - 1 <= pixel <= register + 1 else '.'

    cycles += 1

    if (cycles + 20) % 40 == 0:
        total += register * cycles

    _, sep, n = instruction.partition(' ')
    if sep:
        register += int(n)


print('Part 1:', total)
print('Part 2:', image, sep='\n')
