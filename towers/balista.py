import random

import pygame
from player.player import PlayerBullet

clock = pygame.time.Clock()


class Balista:
    def __init__(self, x, y, enemy_list, bullets, display_scroll):
        self.x = x - 16 + display_scroll[0]
        self.y = y - 16 + display_scroll[1]
        self.enemies = enemy_list
        self.enemy = random.choice(self.enemies)
        self.bullets = bullets
        self.display_scroll = display_scroll
        self.rect = pygame.Rect(self.x - self.display_scroll[0], self.y - self.display_scroll[1], 32, 32)

    def main(self, display):
        if self.enemy.health <= 0:

            self.enemy = random.choice(self.enemies)
        self.rect = pygame.Rect(self.x - self.display_scroll[0], self.y - self.display_scroll[1], 32, 32)
        pygame.draw.rect(display, (0, 255, 255), self.rect)

    def shoot(self):
        self.bullets.append(
            PlayerBullet(self.x + 16 - self.display_scroll[0], self.y + 16 - self.display_scroll[1],
                         self.enemy.x + 15 - self.display_scroll[0], self.enemy.y + 15 - self.display_scroll[1], 0,
                         self.display_scroll))
