from itertools import product
from aoc_utils import timed

def main():
    input = []
    with open('test_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    arr = [[int(x) for x in row] for row in input]
    return sum(step(arr) for _ in range(100))

def part2(input):
    arr = [[int(x) for x in row] for row in input]
    step_count = 1
    while step(arr) != 100:
        step_count += 1
    return step_count

def step(arr):
    flash_count, any_flashed = 0, True
    for r, c in product(range(10), repeat=2):
        arr[r][c] += 1
    while any_flashed:
        neighbors = []
        any_flashed = False
        for r, c in product(range(10), repeat=2):
            if arr[r][c] >= 10:
                any_flashed = True
                arr[r][c] = 0
                flash_count += 1
                neighbors.extend(product(range(r - 1, r + 2), range(c - 1, c + 2)))
        for r, c in neighbors:
            if valid(arr, r, c) and arr[r][c]:
                arr[r][c] += 1
    return flash_count

def valid(arr, r, c):
    return 0 <= r < len(arr) and 0 <= c < len(arr[r])

if __name__ == '__main__':
    main()
