import pygame

cursor_image = pygame.image.load('data/cursor.png')


class Cursor:
    def __init__(self, x, y):
        self.x = x - 8
        self.y = y - 8
        print(self.x, self.y)

    def main(self, display):
        display.blit(pygame.transform.scale(cursor_image, (16, 16)), (self.x, self.y))
