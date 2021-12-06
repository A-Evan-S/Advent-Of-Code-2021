from collections import defaultdict
from collections import Counter
from aoc_utils import timed

def main():
    with open('day6_input.txt') as f:
        input = f.readline()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return count_fish(input, 80)

def part2(input):
    return count_fish(input, 256)

def count_fish(input, n):
    fish = Counter(map(int, input.split(',')))
    for j in range(n):
        next_fish = defaultdict(int)
        next_fish[6] = fish[0]
        next_fish[8] = fish[0]
        for i in range(1, 9):
            next_fish[i-1] += fish[i]
        fish = next_fish
    return sum(fish.values())

if __name__ == '__main__':
    main()