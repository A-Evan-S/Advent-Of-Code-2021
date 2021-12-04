from aoc_utils import timed

def main():
    input = []
    with open('day4_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def parse_input(input):
    numbers_called = [int(x) for x in input[0].split(',')]
    boards, board = [], []
    for line in input[2:]:
        if line:
            board.append([int(x) for x in line.split()])
        else:
            boards.append(board)
            board = []
    boards.append(board)
    return numbers_called, boards

def part1(input):
    numbers_called, boards = parse_input(input)
    prev_called = set()
    for num in numbers_called:
        prev_called.add(num)
        for board in boards:
            if is_winner(board, prev_called):
                return score(board, prev_called, num)

def part2(input):
    numbers_called, boards = parse_input(input)
    prev_called = set()
    for num in numbers_called:
        prev_called.add(num)
        for board in boards:
            if is_winner(board, prev_called):
                if len(boards) == 1:
                    return score(board, prev_called, num)
                boards.remove(board)

def is_winner(board, prev_called):
    win_options = board[:]
    for c in range(5):
        win_options.append([row[c] for row in board])
    return any(all(x in prev_called for x in win) for win in win_options)

def score(board, prev_called, num):
    points = 0
    for row in board:
        points += sum(val for val in row if val not in prev_called)
    return points * num

if __name__ == '__main__':
    main()
