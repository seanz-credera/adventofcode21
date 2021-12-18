class Probe:
    def __init__(self, vxi, vyi) -> None:
        self.x = 0
        self.y = 0
        self.v = [vxi, vyi]
        self.locations = [(0, 0)]

    # Take a step for the probe
    def step(self) -> None:
        # Change position according to velocity
        self.x += self.v[0]
        self.y += self.v[1]

        # Adjust velocity for drag and gravity
        if self.v[0] < 0:
            self.v[0] += 1
        elif self.v[0] > 0:
            self.v[0] -= 1

        self.v[1] -= 1

        # Keep track of location for this step
        self.locations.append((self.x, self.y))


class Grid:
    def __init__(self, probe: Probe, x1: int, x2: int, y1: int, y2: int) -> None:
        self.probe = probe
        self.target_range = (x1, x2, y1, y2)

    # Check if any probe locations go through target area
    def is_on_target(self):
        for location in self.probe.locations:
            x, y = location[0], location[1]
            if (x1 <= x and x <= x2) and (y1 <= y and y <= y2):
                return True
        return False


filename = "day17.txt"
debug = "AoC-John/Day17/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    target_area = file_content[0].split()[2:]

    x = target_area[0][2:-1].split("..")
    x1, x2 = int(x[0]), int(x[1])
    y = target_area[1][2:].split("..")
    y1, y2 = int(y[0]), int(y[1])

    vxi, vyi = 0, 0
    probe = Probe(vxi, vyi)

    grid = Grid(probe, x1, x2, y1, y2)
    print("done")
