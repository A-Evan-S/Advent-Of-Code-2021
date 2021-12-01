from aoc_utils import timed

def main():
    input = []
    with open('day1_input.txt') as f:
        for line in f:
            input.append(int(line))
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return sum(a > b for a, b in zip(input[1:], input))

def part2(input):
    return sum(a > b for a, b in zip(input[3:], input))

if __name__ == '__main__':
    main()