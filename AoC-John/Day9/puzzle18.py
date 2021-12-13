def is_min(cave_map, row, col):
    curr_val = cave_map[row][col][0]
    surroundings = {"L": None, "R": None, "U": None, "D": None}
    try:
        surroundings["L"] = cave_map[row][col - 1]
    except:
        print("curr_val on left edge, no adjacent entry to the left.")
    try:
        surroundings["R"] = cave_map[row][col + 1]
    except:
        print("curr_val on right edge, no adjacent entry to the right.")
    try:
        surroundings["U"] = cave_map[row - 1][col]
    except:
        print("curr_val on upper edge, no adjacent entry upward.")
    try:
        surroundings["D"] = cave_map[row + 1][col]
    except:
        print("curr_val on lower edge, no adjacent entry downward.")

    for dir, val in surroundings.items():
        if val is not None and curr_val >= val:
            return False

    return True


# Get low points of cave_map as coordinate points
def get_low_points(cave_map):
    low_points = []
    for row in range(cave_map):
        for col in range(cave_map[0]):
            if cave_map[row][col][1]:
                low_points.append((row, col))


with open("day9.txt") as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    risk_level = 0
    cave_map = []
    for line in file_content:
        cave_map.append([[int(digit), False] for digit in line])

    for row in range(len(cave_map)):
        for col in range(len(cave_map[0])):
            if is_min(cave_map, row, col):
                cave_map[row][col][1] = True
    low_points = get_low_points(cave_map)
    print(f"Risk level: {risk_level}")
