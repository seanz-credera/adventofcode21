filename = "day4.txt"

# Each num is part of tuple with bool to mark if number has been called
def read_board(text):
    board = [list(map(int, text.pop(0).split())) for i in range(5)]

    return [[[num, False] for num in row] for row in board]


# Mark 'board' where 'draw' appears
def mark_board(draw, board):
    for row in range(5):
        for col in range(5):
            if board[row][col][0] == draw:
                board[row][col][1] = True


def check_rows(board):
    for row in board:
        marked_count = 0
        for num, marked in row:
            if marked:
                marked_count += 1
        if marked_count == 5:
            return True
    return False


def check_cols(board):
    for col in range(5):
        marked_count = 0
        for row in range(5):
            if board[row][col][1]:
                marked_count += 1
        if marked_count == 5:
            return True
    return False


# Check if input board contains bingo
def check_win(board):
    return check_rows(board) or check_cols(board)


# Read the drawn numbers and boards
def process_input(text):
    # Clean text
    while "\n" in text:
        text.remove("\n")
    text = [line.strip() for line in text]

    # Extract numbers drawn
    nums = text.pop(0)
    nums = list(map(int, nums.split(",")))

    # Extract boards
    boards = []
    while len(text) > 0:
        boards.append(read_board(text))
    return nums, boards


def main():
    with open(filename) as file:
        lines = file.readlines()
        nums, boards = process_input(lines)

        nums_drawn = []
        last_board_won = False
        last_board = None
        iter_boards = [board for board in boards]
        while not last_board_won:
            draw = nums.pop(0)
            nums_drawn.append(draw)
            next_iter_boards = [board for board in iter_boards]
            for board in iter_boards:
                mark_board(draw, board)
                if check_win(board):
                    next_iter_boards.remove(board)
                    if len(next_iter_boards) == 0:
                        last_board = board
                        last_board_won = True
                        break

            iter_boards = [board for board in next_iter_boards]

    print(f"Numbers drawn: {nums_drawn}")
    print(f"Last num: {draw}")
    print("Last Winning board:")
    for row in last_board:
        print(row)
    board_score = 0
    for row in last_board:
        for num, marked in row:
            if not marked:
                board_score += num
    print(f"Board score: {board_score}")
    print(f"Final score: {board_score * draw}")


if __name__ == "__main__":
    main()
