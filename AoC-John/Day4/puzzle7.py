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
        winning_board = None
        won = False
        nums_drawn = []
        while not won:
            draw = nums.pop(0)
            nums_drawn.append(draw)
            for board in boards:
                mark_board(draw, board)
                if check_win(board):
                    won = True
                    winning_board = board
                    break
    print(f"Numbers drawn: {nums_drawn}")
    print(f"Last num: {draw}")
    print("Winning board:")
    for row in winning_board:
        print(row)
    board_score = 0
    for row in winning_board:
        for num, marked in row:
            if not marked:
                board_score += num
    print(f"Board score: {board_score}")
    print(f"Final score: {board_score * draw}")


if __name__ == "__main__":
    main()
