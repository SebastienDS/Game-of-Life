import time, pygame
import Grid

pygame.init()

COLOR = [(0, 0, 0), (255, 255, 255)]


class Game:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = Grid.Grid(width // cell_size, height // cell_size)
        self.updating = False
        self.last_update = 0
        self.mouse_pressed = False
        self.time_for_update = 0.2

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def draw(self):
        for j in range(len(self.grid.grid)):
            for i in range(len(self.grid.grid[0])):
                state = self.grid.grid[j][i]
                pygame.draw.rect(
                    self.screen,
                    COLOR[state],
                    (
                        i * self.cell_size,
                        j * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def update(self):
        if self.updating and time.time() - self.last_update > self.time_for_update:
            self.grid.update()
            self.last_update = time.time()
        if self.mouse_pressed:
            pos = pygame.mouse.get_pos()
            self.grid.grid[pos[1] // self.cell_size][pos[0] // self.cell_size] = True

    def mainloop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    elif event.key == pygame.K_SPACE:
                        self.updating = not self.updating
                    elif event.key == pygame.K_RIGHT:
                        self.time_for_update -= 0.05
                    elif event.key == pygame.K_LEFT:
                        self.time_for_update += 0.05
                    elif event.key == pygame.K_c:
                        self.grid.clear()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pressed = False

            self.screen.fill(COLOR[0])
            self.draw()
            self.update()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game(850, 850, 15)
    game.mainloop()
