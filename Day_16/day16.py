from functools import reduce
from operator import mul
from aoc_utils import timed

def main():
    with open('day16_input.txt') as f:
        input = ''.join(f'{int(x, 16):04b}' for x in f.readline())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(code):
    global version_total
    version_total = 0
    parse_packet(code, MutableInt())
    return version_total

def part2(code):
    return parse_packet(code, MutableInt())

class MutableInt:
    def __init__(self, val=0):
        self.val = val

def parse_bits(code, index, n):
    val = int(code[index.val: index.val + n], 2)
    index.val += n
    return val

def parse_packet(code, index):
    global version_total
    version = parse_bits(code, index, 3)
    version_total += version
    id = parse_bits(code, index, 3)
    if id == 4:  # Literal
        num = 0
        while parse_bits(code, index, 1):
            num = (num << 4) + parse_bits(code, index, 4)
        num = (num << 4) + parse_bits(code, index, 4)
        return num
    else:  # Operator
        arguments = []
        if parse_bits(code, index, 1):  # Sub Packets
            sub_packet_count = parse_bits(code, index, 11)
            for _ in range(sub_packet_count):
                arg = parse_packet(code, index)
                arguments.append(arg)
        else:  # Length
            length = parse_bits(code, index, 15)
            end_index = index.val + length
            while index.val < end_index:
                arg = parse_packet(code, index)
                arguments.append(arg)

        if id == 0:
            return sum(arguments)
        if id == 1:
            return reduce(mul, arguments)
        if id == 2:
            return min(arguments)
        if id == 3:
            return max(arguments)
        if id == 5:
            return int(arguments[0] > arguments[1])
        if id == 6:
            return int(arguments[0] < arguments[1])
        if id == 7:
            return int(arguments[0] == arguments[1])

if __name__ == '__main__':
    main()
