from aoc_utils import timed
from itertools import permutations
import re

def main():
    input = []
    with open('day8_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    total = 0
    for line in input:
        output_values = re.findall('[abcdefg]+', line.split('|')[1])
        total += sum(len(val) in (2, 3, 4, 7) for val in output_values)
    return total

def part2(input):
    return sum(map(solve_single, input))

display = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
digits = set(display.keys())

def solve_single(line):
    numbers = re.findall('[abcdefg]+', line)
    wire_map = find_map(numbers)
    output_values = re.findall('[abcdefg]+', line.split('|')[1])
    result = 0
    for output_value in output_values:
        result *= 10
        result += display[''.join(sorted(output_value.translate(wire_map)))]
    return result

def find_map(numbers):
    for p in permutations('abcdefg'):
        wire_map = str.maketrans(''.join(p), 'abcdefg')
        if all(''.join(sorted(number.translate(wire_map))) in digits for number in numbers):
            return wire_map

if __name__ == '__main__':
    main()
