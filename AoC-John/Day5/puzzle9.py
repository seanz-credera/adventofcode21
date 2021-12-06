from typing import List


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"{self.p1} -> {self.p2}"

    def is_vertical(self):
        return self.p1.x == self.p2.x

    def is_horizontal(self):
        return self.p1.y == self.p2.y


class Grid:
    def __init__(self, lines: List[Line]) -> None:
        self.lines = lines
        self.max_size = self.find_max_size()
        self.grid = [
            [0 for i in range(self.max_size + 1)] for j in range(self.max_size + 1)
        ]

    def __str__(self) -> str:
        grid_str = ""
        for line in self.grid:
            for num in line:
                grid_str += str(num)
            grid_str += "\n"
        return grid_str

    def find_max_size(self):
        max_size = 0
        for line in self.lines:
            if line.p1.x > max_size:
                max_size = line.p1.x
            if line.p1.y > max_size:
                max_size = line.p1.y
            if line.p2.x > max_size:
                max_size = line.p2.x
            if line.p2.y > max_size:
                max_size = line.p2.y
        return max_size

    def fill_grid(self):
        for line in self.lines:
            p1x, p1y = line.p1.x, line.p1.y
            p2x, p2y = line.p2.x, line.p2.y
            if line.is_vertical():
                # Start with p2, go to p1
                if p1y > p2y:
                    for y in range(p2y, p1y + 1):
                        self.grid[p1x][y] += 1
                else:
                    for y in range(p1y, p2y + 1):
                        self.grid[p1x][y] += 1
            elif line.is_horizontal():
                # Start with p2, go to p1
                if p1x > p2x:
                    for x in range(p2x, p1x + 1):
                        self.grid[x][p1y] += 1
                else:
                    for x in range(p1x, p2x + 1):
                        self.grid[x][p1y] += 1

    def count_overlap(self):
        num_overlap = 0
        for row in self.grid:
            for val in row:
                if val > 1:
                    num_overlap += 1
        return num_overlap


def read_points(line):
    split_line = line.split()
    p1 = split_line[0]
    p1 = p1.split(",")
    p1x, p1y = int(p1[0]), int(p1[1])

    p2 = split_line[2]
    p2 = p2.split(",")
    p2x, p2y = int(p2[0]), int(p2[1])
    return Point(p1x, p1y), Point(p2x, p2y)


def main():
    with open("day5.txt") as file:
        file_content = file.readlines()
        file_content = [line.strip() for line in file_content]
        lines = []
        for line in file_content:
            p1, p2 = read_points(line)
            lines.append(Line(p1, p2))

        grid = Grid(lines)
        grid.fill_grid()

        print(f"Number of overlaps: {grid.count_overlap()}")


if __name__ == "__main__":
    main()
