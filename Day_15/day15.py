from aoc_utils import timed
from heapq import heappop, heappush

def main():
    input = []
    with open('day15_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    return solve(input, False)

def part2(input):
    return solve(input, True)

def solve(input, is_part_2):
    cavern = [[int(x) for x in row] for row in input]
    h = [(0, (0, 0))]
    seen = set()
    goal = len(cavern) + 4 * len(cavern) * is_part_2 - 1, len(cavern[0]) + 4 * len(cavern[0]) * is_part_2 - 1
    while h:
        cost, pos = heappop(h)
        if pos == goal:
            return cost
        if pos not in seen:
            seen.add(pos)
            for neighbor in get_neighbors(cavern, *pos, is_part_2):
                heappush(h, (cost + risk(cavern, *neighbor), neighbor))

def get_neighbors(cavern, r, c, is_part_2):
    neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    rows = 5*len(cavern) if is_part_2 else len(cavern)
    cols = 5*len(cavern[0]) if is_part_2 else len(cavern[0])
    return [(row, col) for row, col in neighbors if 0 <= row < rows and 0 <= col < cols]

def risk(cavern, r, c):
    rows = len(cavern)
    cols = len(cavern[0])
    cost = cavern[r % rows][c % cols] + (r//rows) + (c//cols)
    return (cost-1) % 9 + 1

if __name__ == '__main__':
    main()
