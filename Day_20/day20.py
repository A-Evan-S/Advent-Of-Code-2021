from collections import defaultdict
from itertools import product
from aoc_utils import timed

def main():
    input = []
    with open('day20_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def process_input(input):
    enhancement = [x == '#' for x in input[0]]
    image = input[2:]
    image_pixels = defaultdict(lambda: False)
    for r, c in product(range(len(image)), range(len(image[0]))):
        image_pixels[r, c] = image[r][c] == '#'
    return enhancement, image_pixels

def part1(input):
    enhancement, image_pixels = process_input(input)
    image_pixels = enhance(image_pixels, enhancement, True)
    image_pixels = enhance(image_pixels, enhancement, False)
    return sum(image_pixels.values())

def part2(input):
    enhancement, image_pixels = process_input(input)
    for i in range(50):
        image_pixels = enhance(image_pixels, enhancement, i%2 == 0)
    return sum(image_pixels.values())

def enhance(image_pixels, enhancement, count_off=False):
    rows = [r for r, c in image_pixels.keys()]
    cols = [c for r, c in image_pixels.keys()]
    new_image_pixels = defaultdict(lambda : count_off)
    for r in range(min(rows)-1, max(rows)+2):
        for c in range(min(cols)-1, max(cols)+2):
            n = 0
            for dr, dc in product(range(-1, 2), repeat=2):
                n = (n << 1) + image_pixels[r+dr, c+dc]
            if count_off != enhancement[n]:
                new_image_pixels[(r, c)] = not count_off
    return new_image_pixels


if __name__ == '__main__':
    main()