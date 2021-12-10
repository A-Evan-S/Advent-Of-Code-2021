from itertools import product
from aoc_utils import timed

def main():
    input = []
    with open('day9_input.txt') as f:
        for line in f:
            input.append(line.strip())
    arr = [[int(x) for x in line] for line in input]
    print("Part 1:", timed(part1, arr))
    print("Part 2:", timed(part2, arr))

def part1(arr):
    total = 0
    for r, c in product(range(len(arr)), range(len(arr[0]))):
        neighbors = get_neighbors(arr, r, c)
        if all(arr[r][c] < arr[neighbor[0]][neighbor[1]] for neighbor in neighbors):
            total += 1 + arr[r][c]
    return total

def part2(arr):
    basin_sizes, visited = [], set()
    for pos in product(range(len(arr)), range(len(arr[0]))):
        if pos not in visited:
            basin_size, q = 0, [pos]
            while q:
                curr = q.pop(0)
                if curr not in visited and arr[curr[0]][curr[1]] != 9:
                    basin_size += 1
                    visited.add(curr)
                    q.extend(get_neighbors(arr, *curr))
            basin_sizes.append(basin_size)
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

def get_neighbors(arr, r, c):
    neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    return [neighbor for neighbor in neighbors if is_valid(arr, *neighbor)]

def is_valid(arr, r, c):
    return 0 <= r < len(arr) and 0 <= c < len(arr[r])

if __name__ == '__main__':
    main()
