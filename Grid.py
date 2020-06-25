class Grid:
    neighbours = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    def __init__(self, width, height):
        self.grid = [[False for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return "{}".format(self.grid)

    def __getitem__(self, i):
        return self.grid[i]

    def __len__(self):
        return len(self.grid)

    def update(self):
        for x, y in self.cell_changing_state():
            self.grid[y][x] = not self.grid[y][x]

    def cell_changing_state(self):
        changing_cell = set()
        for j in range(len(self.grid)):
            for i in range(len(self.grid[0])):
                count = self.compute_neighbours(i, j)
                if (not self.grid[j][i] and count == 3) or (
                    self.grid[j][i] and (count < 2 or count > 3)
                ):
                    changing_cell.add((i, j))
        return changing_cell

    def compute_neighbours(self, i, j):
        count = 0
        for x, y in Grid.neighbours:
            next_i = i + x
            next_j = j + y
            if (
                (0 <= next_i < len(self.grid[0]))
                and (0 <= next_j < len(self.grid))
                and self.grid[next_j][next_i]
            ):
                count += 1
        return count

    def clear(self):
        for j in range(len(self.grid)):
            for i in range(len(self.grid[0])):
                self.grid[j][i] = False
