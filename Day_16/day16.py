from functools import reduce
from operator import mul
from aoc_utils import timed

def main():
    with open('day16_input.txt') as f:
        input = f.readline()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    global version_total
    version_total = 0
    parse_packet(Code(input))
    return version_total

def part2(input):
    return parse_packet(Code(input))

class Code:
    def __init__(self, hexcode, index=0):
        self.code = ''.join(f'{int(x, 16):04b}' for x in hexcode)
        self.index = index

    def parse_bits(self, n):
        val = int(self.code[self.index: self.index + n], 2)
        self.index += n
        return val

def parse_packet(code):
    global version_total
    version = code.parse_bits(3)
    version_total += version
    id = code.parse_bits(3)
    if id == 4:  # Literal
        num = 0
        while code.parse_bits(1):
            num = (num << 4) + code.parse_bits(4)
        num = (num << 4) + code.parse_bits(4)
        return num
    else:  # Operator
        arguments = []
        if code.parse_bits(1):  # Sub Packets
            sub_packet_count = code.parse_bits(11)
            for _ in range(sub_packet_count):
                arg = parse_packet(code)
                arguments.append(arg)
        else:  # Length
            length = code.parse_bits(15)
            end_index = code.index + length
            while code.index < end_index:
                arg = parse_packet(code)
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
