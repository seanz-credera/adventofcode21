from typing import List, Tuple
from operator import itemgetter


class Probe:
    x: int
    y: int
    v: List[int]
    locations: List[Tuple[int, int]]
    on_target: bool

    def __init__(self, vxi, vyi) -> None:
        self.x = 0
        self.y = 0
        self.v = [vxi, vyi]
        self.locations = [(0, 0)]
        self.on_target = False

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

    def max_height(self):
        return max(self.locations, key=itemgetter(1))[1]


class Grid:
    probes: List[Probe]
    target_range: Tuple[int, int, int, int]

    def __init__(self, x1, x2, y1, y2) -> None:
        self.probes = []
        self.target_range = (x1, x2, y1, y2)

    def add_probe(self, probe: Probe) -> None:
        self.probes.append(probe)

    # Check if any probe locations go through target area
    def is_on_target(self):
        for probe in self.probes:
            for location in probe.locations:
                x, y = location[0], location[1]
                if (x1 <= x and x <= x2) and (y1 <= y and y <= y2):
                    probe.on_target = True


filename = "day17.txt"
debug = "AoC-John/Day17/" + filename

NUM_STEPS = 25

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    target_area = file_content[0].split()[2:]

    x = target_area[0][2:-1].split("..")
    x1, x2 = int(x[0]), int(x[1])
    y = target_area[1][2:].split("..")
    y1, y2 = int(y[0]), int(y[1])

    grid = Grid(x1, x2, y1, y2)
    # Add probes with range of starting velocities
    for vxi in range(0, 100):
        for vyi in range(0, 100):
            grid.add_probe(Probe(vxi, vyi))

    # Take probes through NUM_STEPS steps
    for step in range(NUM_STEPS):
        for probe in grid.probes:
            probe.step()

    # Mark the probes that are on target
    grid.is_on_target()

    # Keep track of max heights for each probe that goes through target
    max_heights = []
    for probe in grid.probes:
        if probe.on_target:
            max_heights.append(probe.max_height())

    print(f"Max height obtained: {max(max_heights)}")
