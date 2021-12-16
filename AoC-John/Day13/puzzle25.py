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
    def __init__(self, points: List[Point]) -> None:
        self.points = points
        self.max_size_x, self.max_size_y = self._find_max_size()
        self.grid = [
            ["." for i in range(self.max_size_x + 1)]
            for j in range(self.max_size_y + 1)
        ]
        self._fill_grid()

    def __str__(self) -> str:
        grid_str = ""
        for line in self.grid:
            for point in line:
                grid_str += point
            grid_str += "\n"
        return grid_str

    def _find_max_size(self):
        max_size_x = 0
        max_size_y = 0
        for point in self.points:
            if point.x > max_size_x:
                max_size_x = point.x
            if point.y > max_size_y:
                max_size_y = point.y
        return max_size_x, max_size_y

    def _fill_grid(self):
        for point in self.points:
            x, y = point.x, point.y
            self.grid[y][x] = "#"

    def count(self):
        counts = 0
        for row in self.grid:
            for val in row:
                if val == "#":
                    counts += 1
        return counts

    def fold(self, fold: str) -> None:
        fold = fold.split()[-1].strip()
        fold = fold.split("=")
        axis, val = fold[0], int(fold[1])
        # Fold left
        if axis == "x":
            inverted_grid = []
            for row in range(len(self.grid)):
                row_piece = self.grid[row][val + 1 :]
                row_piece.reverse()
                inverted_grid.append(row_piece)
                self.grid[row] = self.grid[row][:val]
            size_dif = len(self.grid[0]) - len(inverted_grid[0])
            for row in range(len(inverted_grid)):
                for col in range(len(inverted_grid[0])):
                    if inverted_grid[row][col] == "#":
                        self.grid[row][size_dif + col] = "#"

        # Fold up
        elif axis == "y":
            # Slice out the part we are folding and reverse it to flip the orientation from fold
            inverted_grid = self.grid[val + 1 :]
            inverted_grid.reverse()
            self.grid = self.grid[:val]
            size_dif = len(self.grid) - len(inverted_grid)
            for row in range(len(inverted_grid)):
                for col in range(len(inverted_grid[0])):
                    if inverted_grid[row][col] == "#":
                        self.grid[size_dif + row][col] = "#"


filename = "day13.txt"
debug = "AoC-John/Day13/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content if len(line.strip()) > 0]
    points_input = [line for line in file_content if not line.startswith("fold")]
    folds = [line for line in file_content if line.startswith("fold")]

    points = []
    for point in points_input:
        split_line = point.split(",")
        x, y = int(split_line[0]), int(split_line[1])
        points.append(Point(x, y))

    grid = Grid(points)
    print(grid)

    grid.fold(folds[0])
    print(f"After {folds[0]}:")
    print(grid)

    print(f"Number of visible points: {grid.count()}")
