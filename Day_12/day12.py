from collections import defaultdict, Counter
from aoc_utils import timed

def main():
    input = []
    with open('day12_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    edges = prep_map(input)
    return solve(edges, 'start', [])

def part2(input):
    edges = prep_map(input)
    return solve(edges, 'start', [], True)

def prep_map(input):
    edges = defaultdict(list)
    for line in input:
        a, b = line.split('-')
        edges[a].append(b)
        edges[b].append(a)
    return edges

def solve(edges, curr, prev, allow_doubles=False):
    if curr.islower():
        prev = prev + [curr]
    if curr == 'end':
        return 1
    total = 0
    for neighbor in edges[curr]:
        if neighbor not in prev or allow_doubles and neighbor != 'start' and len(prev) == len(set(prev)):
            total += solve(edges, neighbor, prev, allow_doubles)
    return total

if __name__ == '__main__':
    main()
