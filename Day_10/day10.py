from aoc_utils import timed
from functools import reduce

def main():
    input = []
    with open('day10_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

def part1(input):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(scores.get(invalid_character(line), 0) for line in input)

def part2(input):
    scores = [score_single(line) for line in input if invalid_character(line) is None]
    scores.sort()
    return scores[len(scores) // 2]

def invalid_character(line):
    stack = []
    for c in line:
        if c in pairs.keys():
            stack.append(pairs[c])
        elif stack.pop() != c:
            return c

def score_single(line):
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    stack = []
    for c in line:
        if c in pairs.keys():
            stack.append(pairs[c])
        elif stack[-1] == c:
            stack.pop()
    return reduce(lambda total, c: 5*total + points[c], stack[::-1], 0)

if __name__ == '__main__':
    main()
