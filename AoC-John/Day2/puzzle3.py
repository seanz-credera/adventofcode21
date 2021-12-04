filename = "puzzle3.txt"
with open(filename) as file:
    directions = file.readlines()
    directions = [line.strip() for line in directions]
    horz = 0
    depth = 0
    for line in directions:
        separated = line.split()
        direction = separated[0]
        magnitude = int(separated[1])
        if direction == "forward":
            horz += magnitude
        elif direction == "up":
            depth -= magnitude
        else:
            depth += magnitude

    print(f"Depth: {depth}")
    print(f"Distance: {horz}")
    print(f"Product: {depth * horz}")
