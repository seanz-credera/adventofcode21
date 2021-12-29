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

    def get_max_height(self):
        return max(self.locations, key=itemgetter(1))[1]

    # Check if any probe locations go through target area
    def mark_target(self):
        for location in self.locations:
            x, y = location[0], location[1]
            if (x1 <= x and x <= x2) and (y1 <= y and y <= y2):
                probe.on_target = True


filename = "day17.txt"
debug = "AoC-John/Day17/" + filename

NUM_STEPS = 100

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    target_area = file_content[0].split()[2:]

    x = target_area[0][2:-1].split("..")
    x1, x2 = int(x[0]), int(x[1])
    y = target_area[1][2:].split("..")
    y1, y2 = int(y[0]), int(y[1])

    probes = []
    # Add probes with range of starting velocities
    for vxi in range(0, 1000):
        for vyi in range(0, 1000):
            probes.append(Probe(vxi, vyi))

    # Take probes through NUM_STEPS steps
    for step in range(NUM_STEPS):
        for probe in probes:
            probe.step()

    for probe in probes:
        probe.mark_target()

    for probe in probes:
        print(probe.on_target)
    # Keep track of max heights for each probe that goes through target
    max_height = 0
    for probe in probes:
        if probe.on_target:
            height = probe.get_max_height()
            if height > max_height:
                max_height = height

    print(f"Max height obtained: {max_height}")
