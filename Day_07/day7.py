from aoc_utils import timed

def main():
    with open('day7_input.txt') as f:
        input = [int(x) for x in f.readline().split(',')]
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return min(sum(abs(x - option) for x in input) for option in set(input))

def part2(input):
    return min(sum(sum_to(abs(x - option)) for x in input) for option in set(input))

def sum_to(n):
    return (n+1)*n // 2

if __name__ == '__main__':
    main()