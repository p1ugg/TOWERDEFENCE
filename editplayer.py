import pygame
import os
import sys
from constants import *
from level import *
from player import Player
import math


class EditPlayer(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.mouse_pos = pygame.mouse.get_pos()

        self.cursor_image = pygame.image.load('data/cursor.png')

        self.m_x = pygame.mouse.get_pos()[0] - 8
        self.m_y = pygame.mouse.get_pos()[1] - 8


        #self.image = pygame.image.load('data/cursor.png')
        # cursor = pygame.sprite.Sprite()
        # cursor.image = self.image
        # cursor.rect = cursor.image.get_rect()
        # visible_sprites.add(cursor)
        # print(self.rect)
        #
        # self.visible_sprites = visible_sprites
        # print(pos)

    def input(self):
        keys = pygame.key.get_pressed()
        pass

    def move(self, speed):
        pass

    def collision(self, direction):
        pass

    def update(self):
        pass
        pygame.display.update()
        # self.input()
        # self.move(self.speed)
