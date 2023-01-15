import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Board:
    def __init__(self, width, height, size):
        self.screen_size = size
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = (self.screen_size[0] - self.left * 2) // self.width

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, GREEN, (self.cell_size * j + self.left,
                                                     self.cell_size * i + self.top,
                                                     self.cell_size,
                                                     self.cell_size))
                pygame.draw.rect(screen, WHITE, (self.cell_size * j + self.left,
                                                 self.cell_size * i + self.top,
                                                 self.cell_size,
                                                 self.cell_size), 1)

    def get_cell(self, mos_pos):
        x, y = mos_pos
        x_cell = (x - self.left) // self.cell_size
        y_cell = (y - self.top) // self.cell_size
        if 0 <= x_cell < self.width and 0 <= y_cell < self.height:
            return x_cell, y_cell

    def on_click(self, cell_coords):
        y, x = cell_coords
        self.board[x][y] = not self.board[x][y]

    def get_click(self, mouse_pos):
        coords = self.get_cell(mouse_pos)
        if coords:
            self.on_click(coords)

    def is_exist(self, pos):
        x, y = pos
        if 0 <= x < self.width and  0 <= y < self.height:
            return True
        return False

    def count_neighbors(self, pos):
        x, y = pos
        summ = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.is_exist((i, j)):
                    summ += self.board[i][j]
        summ -= self.board[x][y]
        return summ

    def next_gen(self):
        new_board = [[0] * self.width for i in range(self.height)]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                v = self.count_neighbors((i, j))
                if self.board[i][j] == 1:
                    if v == 2 or v == 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 0
                elif self.board[i][j] == 0:
                    if v == 3:
                        new_board[i][j] = 1

        self.board = new_board[:]

