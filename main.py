import os
import random

import pygame
import sys
from pygame.locals import *

mainClock = pygame.time.Clock()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
AQUA = (127, 255, 212)
PURPLE = (75, 0, 130)
YELLOW = (255, 255, 0)
pygame.init()
pygame.display.set_caption('game base')
width = 1280
height = 720
screen = pygame.display.set_mode((1280, 720), 0, 32)

font = pygame.font.SysFont('arial', 20)

screen_rect = (0, 0, width, height)
all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, GRAVITY=0):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()

def create_particles(position):
    # количество создаваемых частиц
    particle_count = 2
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))



def drawCursor(x, y):
    create_particles((x, y))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False

    while True:
        screen = pygame.display.set_mode((1280, 720), 0, 32)
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        f1 = font.render('TOWER DEFENSE', True, WHITE)
        f2 = font.render('INFO', True, WHITE)
        f3 = font.render('EXIT', True, WHITE)
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                info()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, PURPLE, button_1)
        pygame.draw.rect(screen, PURPLE, button_2)
        pygame.draw.rect(screen, PURPLE, button_3)
        screen.blit(f1, (50, 100))
        screen.blit(f2, (50, 200))
        screen.blit(f3, (50, 300))
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pos = pygame.mouse.get_pos()
        drawCursor(pos[0], pos[1])
        all_sprites.draw(screen)

        pygame.display.update()
        all_sprites.update()
        pygame.display.flip()
        screen.fill((0, 0, 0))



        mainClock.tick(30)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('TOWER DEFENSE', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def info():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('INFO', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
