from copy import deepcopy


DOWN = "v"
RIGHT = ">"
EMPTY = "."


def move_right(sea_cukes, old_sea_cukes, i, j):
    row_len = len(sea_cukes[0])
    # Check next element to right to see if we have room to move right. Use % to wrap around
    if old_sea_cukes[i][(j + 1) % row_len] == EMPTY:
        sea_cukes[i][(j + 1) % row_len] = RIGHT
        sea_cukes[i][j] = EMPTY
        return True, sea_cukes
    else:
        return False, sea_cukes


def move_down(sea_cukes, old_sea_cukes, i, j):
    col_len = len(sea_cukes)
    # Check next element down to see if we have room to move down. Use % to wrap around
    if old_sea_cukes[(i + 1) % col_len][j] == EMPTY:
        sea_cukes[(i + 1) % col_len][j] = DOWN
        sea_cukes[i][j] = EMPTY
        return True, sea_cukes
    else:
        return False, sea_cukes


filename = "day25.txt"
debug = "AoC-John/Day25/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    sea_cukes = []
    for line in file_content:
        sea_cukes.append(list(line))

    steps_taken = 0
    cukes_moving = True

    while cukes_moving:
        old_sea_cukes = deepcopy(sea_cukes)
        cukes_moving = False
        moved = False
        steps_taken += 1
        # if steps_taken == 58:
        #     print("I'm here")
        # Rightward moving pass
        for i, row in enumerate(old_sea_cukes):
            for j, cuke in enumerate(row):
                if cuke == RIGHT:
                    moved, sea_cukes = move_right(sea_cukes, old_sea_cukes, i, j)
                if moved:
                    cukes_moving = True

        # Have to recopy to account for movement after right pass
        old_sea_cukes = deepcopy(sea_cukes)
        # Downward moving pass
        for i, row in enumerate(old_sea_cukes):
            for j, cuke in enumerate(row):
                if cuke == DOWN:
                    moved, sea_cukes = move_down(sea_cukes, old_sea_cukes, i, j)
                if moved:
                    cukes_moving = True
        # print(f"After {steps_taken} steps taken: ")
        # for row in sea_cukes:
        #     print("".join(row))

    print(f"Number of steps taken to stop: {steps_taken}")
