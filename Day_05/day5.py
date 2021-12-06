from aoc_utils import timed
import re

def main():
    input = []
    with open('day5_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return solve(input)

def part2(input):
    return solve(input, True)

def solve(input, count_diagonals=False):
    seen, seen_twice = set(), set()
    for line in input:
        x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
        if x1 == x2 or y1 == y2 or count_diagonals:
            xd = (x2-x1) // (abs(x2-x1) or 1)
            yd = (y2-y1) // (abs(y2-y1) or 1)
            for i in range(max(abs(y2-y1), abs(x2 - x1)) + 1):
                point = x1 + i * xd, y1 + i * yd
                if point in seen:
                    seen_twice.add(point)
                seen.add(point)
    return len(seen_twice)

if __name__ == '__main__':
    main()
