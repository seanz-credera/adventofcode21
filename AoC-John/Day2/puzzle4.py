filename = "puzzle3.txt"
with open(filename) as file:
    directions = file.readlines()
    directions = [line.strip() for line in directions]
    horz = 0
    depth = 0
    aim = 0
    for line in directions:
        separate = line.split()
        direction = separate[0]
        magnitude = int(separate[1])
        if direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
        else:  # forward
            horz += magnitude
            depth += magnitude * aim
    print(f"Depth: {depth}")
    print(f"Distance: {horz}")
    print(f"Product: {depth * horz}")
