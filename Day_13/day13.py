import re
from aoc_utils import timed

def main():
    input = []
    with open('day13_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    dots, folds = prep_paper(input)
    dots = apply_fold(folds[0], dots)
    return len(dots)

def part2(input):
    dots, folds = prep_paper(input)
    for fold in folds:
        dots = apply_fold(fold, dots)
    # display(dots)
    return "LGHEGUEJ"

def prep_paper(input):
    dots = set()
    folds = []
    dots_mode = True
    for line in input:
        if len(line) == 0:
            dots_mode = False
            continue
        if dots_mode:
            x, y = map(int, line.split(','))
            dots.add((x, y))
        else:
            m = re.match(r'fold along ([xy])=(\d+)', line)
            direction = m.group(1)
            val = int(m.group(2))
            folds.append((direction, val))
    return dots, folds

def apply_fold(fold, dots):
    new_dots = set()
    for dot in dots:
        if fold[0] == 'x':
            if dot[0] != fold[1]:
                new_dots.add((min(dot[0], 2 * fold[1] - dot[0]), dot[1]))
        else:
            if dot[1] != fold[1]:
                new_dots.add((dot[0], min(dot[1], 2 * fold[1] - dot[1])))
    return new_dots

def display(dots):
    rows = max(dot[1] for dot in dots) + 1
    cols = max(dot[0] for dot in dots) + 1
    paper = [['  ' for _ in range(cols)] for _ in range(rows)]
    for dot in dots:
        paper[dot[1]][dot[0]] = '██'
    for row in paper:
        print(''.join(row))

if __name__ == '__main__':
    main()
