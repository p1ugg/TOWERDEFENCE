import random

import pygame
import math
from data.settings import *

player_idle_images = [pygame.image.load('player/idle0.png'),
                      pygame.image.load('player/idle1.png'),
                      pygame.image.load('player/idle2.png')]

player_walk_images = [pygame.image.load('player/walk0.png'),
                      pygame.image.load('player/walk1.png'),
                      pygame.image.load('player/walk2.png'),
                      pygame.image.load('player/walk3.png')]

player_weapon = pygame.image.load('weapon/gun0.png')
player_bullet = pygame.image.load('weapon/bullet0.png')


class Player:
    def __init__(self, x, y, width, height, display_scroll):
        self.x = x - display_scroll[0]
        self.y = y - display_scroll[1]
        self.display_scroll = display_scroll
        self.width = width
        self.height = height
        self.idle_animation_count = 0
        self.walk_animation_count = 0
        self.is_idle = True
        self.moving_right = True
        self.moving_left = False

        self.rect = pygame.rect.Rect(self.x, self.y, 64, 64)

    def main(self, display):
        if self.idle_animation_count + 1 >= 24:
            self.idle_animation_count = 0
        if self.walk_animation_count + 1 >= 32:
            self.walk_animation_count = 0

        self.idle_animation_count += 1
        self.walk_animation_count += 1

        if self.is_idle:
            if self.moving_right:
                display.blit(pygame.transform.scale(player_idle_images[self.idle_animation_count // 8], (22, 34)),
                             (self.x, self.y))
            elif self.moving_left:
                display.blit(pygame.transform.flip(pygame.transform.scale(
                    player_idle_images[self.idle_animation_count // 8], (22, 34)), True, False), (self.x, self.y))
        else:
            if self.moving_right:
                display.blit(pygame.transform.scale(player_walk_images[self.walk_animation_count // 8], (22, 34)),
                             (self.x, self.y))
            elif self.moving_left:
                display.blit(pygame.transform.flip(pygame.transform.scale(
                    player_walk_images[self.walk_animation_count // 8], (22, 34)), True, False), (self.x, self.y))

        self.handle_weapons(display)

        self.is_idle = True

    def handle_weapons(self, display):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x -= 8
        mouse_y -= 8

        rel_x, rel_y = mouse_x - WIDTH//2, mouse_y - HEIGHT//2
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        if mouse_x >= WIDTH / 2:
            self.moving_left = False
            self.moving_right = True
            player_weapon_copy = pygame.transform.rotate(pygame.transform.scale(player_weapon, (32, 32)), angle)

            display.blit(player_weapon_copy, (self.x + 22 - int(player_weapon_copy.get_width() / 2),
                                              (self.y + 25 - int(player_weapon_copy.get_height() / 2))))
        elif mouse_x <= WIDTH / 2:
            self.moving_left = True
            self.moving_right = False
            player_weapon_copy = pygame.transform.rotate(pygame.transform.flip(
                pygame.transform.scale(player_weapon, (32, 32)), False, True), angle)

            display.blit(player_weapon_copy, (self.x - int(player_weapon_copy.get_width() / 2),
                                              (self.y + 25 - int(player_weapon_copy.get_height() / 2))))


class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y, spread, display_scroll):
        self.x = x
        self.display_scroll = display_scroll
        self.y =y
        self.mouse_x = mouse_x - 8
        self.mouse_y = mouse_y - 8
        self.speed = 15
        self.angle = math.atan2(self.y - self.mouse_y, self.x - self.mouse_x) + \
            random.uniform(-spread, spread)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.rect = pygame.Rect(self.x, self.y, 16, 16)

    def main(self, display):
        self.x -= self.x_vel
        self.y -= self.y_vel

        display.blit(pygame.transform.scale(player_bullet, (16, 16)), (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, 8, 8)
