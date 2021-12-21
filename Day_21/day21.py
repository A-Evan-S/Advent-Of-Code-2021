from functools import cache
from aoc_utils import timed

def main():
    input = []
    with open('day21_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    positions = [int(line.split(': ')[1]) for line in input]
    scores, turn, turn_count, die = [0, 0], 0, 0, 1
    while max(scores) < 1000:
        for _ in range(3):
            turn_count += 1
            positions[turn] += die
            die = (die % 100) + 1
        positions[turn] = (positions[turn] - 1) % 10 + 1
        scores[turn] += positions[turn]
        turn = (turn + 1) % 2
    return turn_count * min(scores)


def part2(input):
    positions = tuple(int(line.split(': ')[1]) for line in input)
    return max(roll(positions, (0, 0), 0))

@cache
def roll(positions, scores, turn):
    if max(scores) >= 21:
        return [score // 21 for score in scores]
    else:
        results = [0, 0]
        roll_outcomes = [3]*1 + [4]*3 + [5]*6 + [6]*7 + [7]*6 + [8]*3 + [9]*1
        new_positions = ((positions[turn] + roll - 1) % 10 + 1 for roll in roll_outcomes)
        for position in new_positions:
            if turn == 1:
                result = roll((positions[0], position), (scores[0], scores[1]+position), 0)
            else:
                result = roll((position, positions[1]), (scores[0]+position, scores[1]), 1)
            results[0] += result[0]
            results[1] += result[1]
        return results

if __name__ == '__main__':
    main()