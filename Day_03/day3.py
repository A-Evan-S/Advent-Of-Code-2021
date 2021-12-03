from aoc_utils import timed

def main():
    input = []
    with open('day3_input.txt') as f:
        for line in f:
            input.append(int(line[::-1], 2))
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    gamma, epsilon = 0, 0
    for i in range(12):
        common = sum(x & 1 << i != 0 for x in input) > len(input) / 2
        gamma = 2 * gamma + common
        epsilon = 2 * epsilon + (not common)
    return gamma * epsilon

def part2(input):
    return get_rating(input, True) * get_rating(input, False)

def get_rating(input, get_common):
    result = 0
    for i in range(12):
        result *= 2
        common = 2 * sum(x % 2 for x in input) >= len(input)
        result += common ^ (not get_common and len(input) > 1)
        input = [x // 2 for x in input if (x % 2 == common) == get_common or len(input) == 1]
    return result

if __name__ == '__main__':
    main()
