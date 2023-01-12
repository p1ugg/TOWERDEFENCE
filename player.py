import pygame
from constants import *
from level import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, interactive_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('data/saulgoodman.jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.interactive_sprites = interactive_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.interactive_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Если идём направо
                        self.hitbox.right = sprite.hitbox.left # Правая сторона персонажа = Левая сторона препятствия
                    if self.direction.x < 0: # Если идём направо
                        self.hitbox.left = sprite.hitbox.right # Левая сторона персонажа = Правая сторона препятствия

        if direction == 'vertical':
            for sprite in self.interactive_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Если идём вниз
                        self.hitbox.bottom = sprite.hitbox.top # Нижняя сторона персонажа = Верхняя сторона препятствия
                    if self.direction.y < 0: # Если идём вверх
                        self.hitbox.top = sprite.hitbox.bottom # Верхняя сторона персонажа = Нижняя сторона препятствия

    def update(self):
        self.input()
        self.move(self.speed)
