import os
import random
import pygame
import sys
from pygame.locals import *
from constants import *

pygame.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('TOWER DEFENSE')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rect = (0, 0, width, height)
all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('arial', 20)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Particle(pygame.sprite.Sprite):  # класс для создания звездочек в меню игры
    fire = [load_image("star.png")]
    for scale in (0.4, 0.6, 0.8, 1, 1.2):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, GRAVITY=0.01):
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
    # выводим звездочки на экран
    create_particles((x, y))


def draw_text(text, font, color, surface, x, y):
    # отрисовка текста
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    # МЕНЮ ИГРЫ
    click = False
    pygame.mouse.set_visible(False)
    while True:
        screen1 = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen1.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        # получаем позицию мыши для того, чтобы проверять на какую кнопку нажали

        text_button1 = font.render('TOWER DEFENSE', True, WHITE)
        text_button2 = font.render('INFO', True, WHITE)
        text_button3 = font.render('EXIT', True, WHITE)
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
        # проверка нажатия на кнопку

        pygame.draw.rect(screen, PURPLE, button_1)
        pygame.draw.rect(screen, PURPLE, button_2)
        pygame.draw.rect(screen, PURPLE, button_3)
        screen.blit(text_button1, (50, 100))
        screen.blit(text_button2, (50, 200))
        screen.blit(text_button3, (50, 300))
        # отрисовка кнопочек
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
        # берем позицию мыши, чтобы отрисовывать звездочки
        drawCursor(pos[0], pos[1])
        all_sprites.draw(screen)

        pygame.display.update()
        all_sprites.update()
        pygame.display.flip()
        screen1.fill((0, 0, 0))

        mainClock.tick(FPS)


def game():
    # ИГРА
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
        mainClock.tick(FPS)


def info():
    # ИНФА О ПРОГЕ
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('INFO', font, (255, 255, 255), screen, 20, 20)
        draw_text('Игра в жанре Tower Defense с элементами РПГ', font, WHITE, screen, 20, 80)
        draw_text('Главные механики игры:', font, WHITE, screen, 20, 100)
        draw_text('Возведение и улучшение различных башен.', font, WHITE, screen, 20, 140)
        draw_text('Сбор ресурсов для разного рода улучшений.', font, WHITE, screen, 20, 160)
        draw_text('Несколько персонажей с уникальной:', font, WHITE, screen, 20, 180)
        draw_text('Спец-ультимативной способностью', font, WHITE, screen, 40, 200)
        draw_text('Пассивной способностью', font, WHITE, screen, 40, 220)
        draw_text('Атакой', font, WHITE, screen, 40, 240)
        draw_text('Сундуки с полезными предметами.', font, WHITE, screen, 20, 280)
        draw_text('Расходники:', font, WHITE, screen, 20, 300)
        draw_text('ПИВО - восстановление здоровья', font, WHITE, screen, 40, 320)
        draw_text('КУМЫС - ускорение передвижения', font, WHITE, screen, 40, 340)
        draw_text('ТАРХУН - щит, блокирующий несколько попаданий по персонажу', font, WHITE, screen, 40, 360)
        draw_text('КЕФИР - неуязвимость на несколько секунд', font, WHITE, screen, 40, 380)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(FPS)


main_menu()
