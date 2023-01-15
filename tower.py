import pygame

towers = []

class Tower:
    def __init__(self, x, y, size, damage, speed, price):
        self.image = pygame.image.load('data/tower.jpg').convert_alpha()
        self.x = x
        self.y = y
        self.size = size
        self.damage = damage
        self.speed = speed
        self.price = price

    def tower_select(self):
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pressed_x = mouse_pressed[0]
        mouse_pressed_y = mouse_pressed[1]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            towers.append(Tower)


