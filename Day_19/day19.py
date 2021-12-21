from itertools import *
from aoc_utils import timed

def main():
    with open('day19_input.txt') as f:
        input = ''.join(f.readlines()).split('\n\n')
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

directions = [(0, 1, 2, 1, 1, 1),
              (0, 2, 1, 1, 1, -1),
              (0, 1, 2, 1, -1, -1),
              (0, 2, 1, 1, -1, 1),
              (0, 1, 2, -1, 1, -1),
              (0, 2, 1, -1, 1, 1),
              (0, 1, 2, -1, -1, 1),
              (0, 2, 1, -1, -1, -1),
              (1, 0, 2, 1, 1, -1),
              (1, 2, 0, 1, -1, -1),
              (1, 0, 2, 1, -1, 1),
              (1, 2, 0, 1, 1, 1),
              (1, 0, 2, -1, 1, 1),
              (1, 2, 0, -1, 1, -1),
              (1, 0, 2, -1, -1, -1),
              (1, 2, 0, -1, -1, 1),
              (2, 1, 0, 1, 1, -1),
              (2, 0, 1, 1, -1, -1),
              (2, 1, 0, 1, -1, 1),
              (2, 0, 1, 1, 1, 1),
              (2, 1, 0, -1, 1, 1),
              (2, 0, 1, -1, 1, -1),
              (2, 1, 0, -1, -1, -1),
              (2, 0, 1, -1, -1, 1)]

def make_scanner(scanner_str):
    data = scanner_str.split('\n')
    return {tuple(int(x) for x in line.split(',')) for line in data[1:]}

def try_match(a, b):
    for b_beacon, a_beacon in product(b, a):
        d = a_beacon[0] - b_beacon[0], a_beacon[1] - b_beacon[1], a_beacon[2] - b_beacon[2]
        shifted_a = {(beacon[0] - d[0], beacon[1] - d[1], beacon[2] - d[2]) for beacon in a}
        matching_beacons = 0
        for beacon in shifted_a:
            matching_beacons += beacon in b
            if matching_beacons == 12:
                return d, b.union(shifted_a)
    return None, None

def attempt_match(a, b):
    for x, y, z, sx, sy, sz in directions:
        reoriented_a = set()
        for beacon in a:
            reoriented_a.add((beacon[x]*sx, beacon[y]*sy, beacon[z]*sz))
        delta, result = try_match(reoriented_a, b)
        if result:
            return delta, (x, y, z, sx, sy, sz), result
    return None, None, None

def solve(input):
    global results
    scanners = [([[i, [0, 0, 0]]], make_scanner(input[i])) for i in range(len(input))]
    while len(scanners) > 1:
        for i, j in combinations(range(len(scanners)), 2):
            nb, b = scanners[j]
            na, a = scanners[i]
            delta, direction, result = attempt_match(a, b)
            if result:
                scanners.pop(j)
                scanners.pop(i)
                for s in na:
                    x, y, z, sx, sy, sz = direction
                    s[1] = [s[1][x] * sx, s[1][y] * sy, s[1][z] * sz]
                    s[1][0] += delta[0]
                    s[1][1] += delta[1]
                    s[1][2] += delta[2]
                scanners.append((na + nb, result))
                break
    results = scanners[0]

def part1(input):
    solve(input)
    return len(results[1])

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def part2(input):
    return max(distance(a[1], b[1]) for a, b in combinations(results[0], 2))

if __name__ == '__main__':
    main()
