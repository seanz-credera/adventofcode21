NUM_STEPS = 100


class mylist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)


def add_one(octopuses):
    for row in range(len(octopuses)):
        for col in range(len(octopuses[0])):
            octopuses[row][col] += 1


def flash(octopuses, row, col):
    try:
        if octopuses[row - 1][col - 1] != 0:
            octopuses[row - 1][col - 1] += 1
    except:
        pass

    try:
        if octopuses[row - 1][col] != 0:
            octopuses[row - 1][col] += 1
    except:
        pass

    try:
        if octopuses[row - 1][col + 1] != 0:
            octopuses[row - 1][col + 1] += 1
    except:
        pass

    try:
        if octopuses[row][col - 1] != 0:
            octopuses[row][col - 1] += 1
    except:
        pass

    try:
        if octopuses[row][col + 1] != 0:
            octopuses[row][col + 1] += 1
    except:
        pass

    try:
        if octopuses[row + 1][col - 1] != 0:
            octopuses[row + 1][col - 1] += 1
    except:
        pass

    try:
        if octopuses[row + 1][col] != 0:
            octopuses[row + 1][col] += 1
    except:
        pass

    try:
        if octopuses[row + 1][col + 1] != 0:
            octopuses[row + 1][col + 1] += 1
    except:
        pass


def find_flashes(octopuses):
    num_flashes = 0
    while max(mylist(i for row in octopuses for i in row)) > 9:
        for row in range(len(octopuses)):
            for col in range(len(octopuses[0])):
                if octopuses[row][col] > 9:
                    flash(octopuses, row, col)
                    octopuses[row][col] = 0
                    num_flashes += 1
    return num_flashes


def complete_step(octopuses):
    add_one(octopuses)
    return find_flashes(octopuses)


relative_path = "day11.txt"
absolute_path = "AoC-John/Day11/day11.txt"

with open(relative_path) as file:
    file_content = mylist(file.readlines())
    file_content = mylist(line.strip() for line in file_content)
    print("Initial Board:")
    for line in file_content:
        print(line)
    octopuses = mylist()
    for line in file_content:
        octopuses.append(mylist(int(num) for num in line))

    num_flashes = 0
    for i in range(NUM_STEPS):
        num_flashes += complete_step(octopuses)
        print(f"\nBoard after {i + 1} steps:\n")
        board = ["".join(map(str, row)) for row in octopuses]
        for line in board:
            print(line)
    print(f"Number of flashes: {num_flashes}")
