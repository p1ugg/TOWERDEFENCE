import pygame
import random


class Slime:
    def __init__(self, x, y, base, display_scroll):
        self.x = x
        self.y = y
        self.display_scroll = display_scroll
        self.base_x = base.x
        self.base_y = base.y
        self.animation_images = [pygame.image.load('enemy/slime0.png'),
                                 pygame.image.load('enemy/slime1.png'),
                                 pygame.image.load('enemy/slime2.png'),
                                 pygame.image.load('enemy/slime3.png')]
        self.angry_animation_images = [pygame.image.load('enemy/slime_angry0.png'),
                                       pygame.image.load('enemy/slime_angry1.png'),
                                       pygame.image.load('enemy/slime_angry2.png'),
                                       pygame.image.load('enemy/slime_angry3.png')]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150)

        self.rect = pygame.rect.Rect(self.x, self.y, 24, 30)
        self.health = 5

    def main(self, display, bullet_list):
        self.rect = pygame.rect.Rect((self.x - self.display_scroll[0], self.y - self.display_scroll[1]), (24, 30))

        if self.animation_count + 1 >= 32:
            self.animation_count = 0

        if self.health >= 3:
            display.blit(pygame.transform.scale(self.animation_images[self.animation_count // 8], (24, 30)),
                         (self.x - self.display_scroll[0], self.y - self.display_scroll[1]))
            self.animation_count += 1

            if self.reset_offset <= 0:
                self.offset_x = random.randrange(-150, 150)
                self.offset_y = random.randrange(-150, 150)
                self.reset_offset = random.randrange(120, 150)
            else:
                self.reset_offset -= 10

            if self.base_x + self.offset_x - self.display_scroll[0] > self.x - self.display_scroll[0]:
                self.x += 1
            elif self.base_x + self.offset_x - self.display_scroll[0] < self.x - self.display_scroll[0]:
                self.x -= 1

            if self.base_y + self.offset_y - self.display_scroll[1] > self.y - self.display_scroll[1]:
                self.y += 1
            elif self.base_y + self.offset_y - self.display_scroll[1] < self.y - self.display_scroll[1]:
                self.y -= 1
        else:
            display.blit(pygame.transform.scale(self.angry_animation_images[self.animation_count // 8], (24, 30)),
                         (self.x - self.display_scroll[0], self.y - self.display_scroll[1]))
            self.animation_count += 1

            if self.reset_offset <= 0:
                self.offset_x = random.randrange(-50, 50)
                self.offset_y = random.randrange(-50, 50)
                self.reset_offset = random.randrange(120, 150)
            else:
                self.reset_offset -= 100

            if self.base_x + self.offset_x  - self.display_scroll[0] > self.x - self.display_scroll[0]:
                self.x += 2
            elif self.base_x + self.offset_x - self.display_scroll[0] < self.x - self.display_scroll[0]:
                self.x -= 2

            if self.base_y + self.offset_y - self.display_scroll[1] > self.y - self.display_scroll[1]:
                self.y += 2
            elif self.base_y + self.offset_y - self.display_scroll[1] < self.y - self.display_scroll[1]:
                self.y -= 2

        collide_with = self.rect.collidelist([i.rect for i in bullet_list])
        if collide_with != -1:
            bullet_list.pop(collide_with)
            self.health -= 1
