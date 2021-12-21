from functools import reduce
from itertools import permutations
from aoc_utils import timed

def main():
    input = []
    with open('day18_input.txt') as f:
        for line in f:
            input.append(eval(line))
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

class Fish:
    def __init__(self, parent, left, right, is_left_child):
        self.parent = parent
        self.left = left
        self.right = right
        self.is_left_child = is_left_child

    def __repr__(self):
        return f'[{self.left}, {self.right}]'

    def explode(self, depth=1):
        if depth > 4:
            self.parent.send_explosion(depth - 1, self.is_left_child)
            return True
        if isinstance(self.left, Fish):
            if self.left.explode(depth + 1):
                return True
        if isinstance(self.right, Fish):
            if self.right.explode(depth + 1):
                return True

    def split(self):
        if isinstance(self.left, int):
            if self.left > 9:
                self.left = Fish(self, self.left // 2, (self.left + 1) // 2, True)
                return True
        elif self.left.split():
            return True
        if isinstance(self.right, int):
            if self.right > 9:
                self.right = Fish(self, self.right // 2, (self.right + 1) // 2, False)
                return True
        elif self.right.split():
            return True


    def send_explosion(self, depth, from_left):
        if from_left:
            going_left, going_right = self.left.left, self.left.right
            self.left = 0
            if isinstance(self.right, int):
                self.parent.send_value_going_left_up(going_left, depth - 1, self.is_left_child)
                self.right += going_right
            else:
                self.right.send_value_going_left_down(going_right, depth+1)
                self.parent.send_value_going_left_up(going_left, depth - 1, self.is_left_child)
        else:
            going_left, going_right = self.right.left, self.right.right
            self.right = 0
            if isinstance(self.left, int):
                self.parent.send_value_going_right_up(going_right, depth - 1, self.is_left_child)
                self.left += going_left
            else:
                self.left.send_value_going_right_down(going_left, depth+1)
                self.parent.send_value_going_right_up(going_right, depth - 1, self.is_left_child)

    def send_value_going_right_up(self, value, depth, from_left):
        if from_left:
            if isinstance(self.right, int):
                self.right += value
            else:
                self.right.send_value_going_left_down(value, depth + 1)
        else:
            if self.parent:
                self.parent.send_value_going_right_up(value, depth - 1, self.is_left_child)

    def send_value_going_left_up(self, value, depth, from_left):
        if from_left:
            if self.parent:
                self.parent.send_value_going_left_up(value, depth - 1, self.is_left_child)
        else:
            if isinstance(self.left, int):
                self.left += value
            else:
                self.left.send_value_going_right_down(value, depth + 1)

    def send_value_going_right_down(self, value, depth):
        if isinstance(self.right, int):
            self.right += value
        else:
            self.right.send_value_going_right_down(value, depth+1)

    def send_value_going_left_down(self, value, depth):
        if isinstance(self.left, int):
            self.left += value
        else:
            self.left.send_value_going_left_down(value, depth+1)


def make_fish(input, parent=None, is_left_child=False):
    if isinstance(input, int):
        return input
    fish = Fish(parent, None, None, is_left_child)
    fish.left = make_fish(input[0], fish, True)
    fish.right = make_fish(input[1], fish, False)
    return fish

def part1(input):
    return magnitude(reduce(add, map(make_fish, input)))

def part2(input):
    return max(magnitude(add(make_fish(a), make_fish(b))) for a, b in permutations(input, 2))

def magnitude(fish):
    return fish if isinstance(fish, int) else 3*magnitude(fish.left) + 2*magnitude(fish.right)

def add(a, b):
    result = Fish(None, a, b, False)
    a.parent = result
    a.is_left_child = True
    b.parent = result
    b.is_left_child = False
    while True:
        while result.explode():
            continue
        if not result.split():
            break
    return result

if __name__ == '__main__':
    main()
