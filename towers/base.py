import pygame
from data.settings import *
pygame.init()

print(pygame.font.get_fonts())
# font = pygame.font.Font(None, 24)
font = pygame.font.Font('data/hardpixel.otf', 36)
class Base:
    def __init__(self, x, y, enemy_list, display_scroll):
        self.display_scroll = display_scroll
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.enemies = enemy_list
        self.rect = pygame.Rect(self.x - self.display_scroll[0], self.y - self.display_scroll[1], 64, 64)

        self.health = 20

    def main(self, display):
        self.rect = pygame.Rect(self.x - self.display_scroll[0], self.y - self.display_scroll[1], 64, 64)
        pygame.draw.rect(display, (0, 255, 255), self.rect)

        health_count = font.render(str(self.health), True, (0, 0, 0))
        display.blit(health_count, (self.x - self.display_scroll[0], self.y - self.display_scroll[1]))

        collide_with = self.rect.collidelist([i.rect for i in self.enemies])
        if collide_with != -1:
            self.enemies.pop(collide_with)
            self.health -= 1

