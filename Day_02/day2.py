from aoc_utils import timed

def main():
    input = []
    with open('day2_input.txt') as f:
        for line in f:
            input.append(line)
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    x, y = 0, 0
    for line in input:
        dir, amt = line.split(' ')
        if dir == 'forward':
            x += int(amt)
        if dir == 'up':
            y -= int(amt)
        if dir == 'down':
            y += int(amt)
    return x * y

def part2(input):
    x, y, aim = 0, 0, 0
    for line in input:
        dir, amt = line.split(' ')
        if dir == 'forward':
            x += int(amt)
            y += aim * int(amt)
        if dir == 'up':
            aim -= int(amt)
        if dir == 'down':
            aim += int(amt)
    return x * y

if __name__ == '__main__':
    main()