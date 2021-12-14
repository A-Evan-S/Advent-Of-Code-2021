from collections import defaultdict, Counter
from aoc_utils import timed

def main():
    input = []
    with open('day14_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    poly = input[0]
    rules = get_rules(input[2:])
    for _ in range(10):
        poly = ''.join(poly[i] + rules[poly[i:i+2]] for i in range(len(poly) - 1)) + poly[-1]
    c = Counter(poly)
    return max(c.values()) - min(c.values())

def part2(input):
    poly = input[0]
    rules = get_rules_part_2(input[2:])

    c = Counter(poly[i:i+2] for i in range(len(poly) - 1))
    for _ in range(40):
        c_next = defaultdict(int)
        for pair in c:
            a, b = rules[pair]
            c_next[a] += c[pair]
            c_next[b] += c[pair]
        c = c_next

    letter_count = defaultdict(int)
    for pair in c:
        letter_count[pair[0]] += c[pair]
    letter_count[input[0][-1]] += 1

    return max(letter_count.values()) - min(letter_count.values())

def get_rules(input):
    rules = {}
    for line in input:
        a, b = line.split(' -> ')
        rules[a] = b
    return rules

def get_rules_part_2(input):
    rules = {}
    for line in input:
        a, b = line.split(' -> ')
        rules[a] = (a[0] + b, b + a[1])
    return rules

if __name__ == '__main__':
    main()
