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
screen = pygame.display.set_mode((1280, 720), 0, 32)

font = pygame.font.SysFont('arial', 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False

    while True:

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
        screen.blit(f1, (50, 100))
        screen.blit(f2, (50, 200))
        screen.blit(f3, (50, 300))
        pygame.display.update()
        mainClock.tick(60)


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
