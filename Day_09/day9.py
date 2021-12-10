from aoc_utils import timed

def main():
    input = []
    with open('day9_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return "Incomplete"

def part2(input):
    return "Incomplete"

if __name__ == '__main__':
    main()
