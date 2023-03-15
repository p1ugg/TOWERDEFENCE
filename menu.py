import sys

import pygame.image
from pygame.locals import *
from data.settings import *
from data.cursor import Cursor

pygame.init()
pygame.mouse.set_visible(False)

pygame.mixer.music.load('sounds/manabreak.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
pygame.display.set_caption('TOWER DEFENSE')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

font = pygame.font.Font('data/hardpixel.otf', 20)


def draw_text(text, font, color, surface, x, y):
    # отрисовка текста
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    # МЕНЮ ИГРЫ

    vol = 0.1
    sound_off_icon = pygame.transform.scale(pygame.image.load('data/iconmute.png'), (24, 24))
    sound_up_icon = pygame.image.load('data/sound+.png')
    sound_down_icon = pygame.image.load('data/sound-.png')

    while True:
        screen1 = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen1.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()

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
        # получаем позицию мыши для того, чтобы проверять на какую кнопку нажали

        text_button1 = font.render('TOWER DEFENSE', True, WHITE)
        text_button2 = font.render('INFO', True, WHITE)
        text_button3 = font.render('EXIT', True, WHITE)
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        sound_off = pygame.Rect(10, 10, 24, 24)
        sound_up = pygame.Rect(34, 10, 24, 24)
        sound_down = pygame.Rect(58, 10, 24, 24)

        pygame.draw.rect(screen, PURPLE, button_1)
        pygame.draw.rect(screen, PURPLE, button_2)
        pygame.draw.rect(screen, PURPLE, button_3)
        pygame.draw.rect(screen, PURPLE, sound_off)
        pygame.draw.rect(screen, PURPLE, sound_up)
        pygame.draw.rect(screen, PURPLE, sound_down)
        screen.blit(text_button1, (50, 100))
        screen.blit(text_button2, (50, 200))
        screen.blit(text_button3, (50, 300))
        screen.blit(sound_down_icon, (10, 10))
        screen.blit(sound_up_icon, (34, 10))
        screen.blit(sound_off_icon, (58, 10))

        if button_1.collidepoint((mx, my)):
            if click:
                click = False
                import game
        if button_2.collidepoint((mx, my)):
            if click:
                info()
                click = False
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        if sound_off.collidepoint((mx, my)):
            if click:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
        if sound_up.collidepoint((mx, my)):
            if click:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
        if sound_down.collidepoint((mx, my)):
            if click:
                if pygame.mixer.music.get_volume() == 0:
                    pygame.mixer.music.set_volume(vol)
                else:
                    pygame.mixer.music.set_volume(0)
        # проверка нажатия на кнопку

        cursor = Cursor(mx, my)
        cursor.main(screen)

        pygame.display.update()
        pygame.display.flip()

        clock.tick(FPS)


def info():
    # ИНФА О ПРОГЕ
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('мы хищные грибы узбекистана', font, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(FPS)


main_menu()
