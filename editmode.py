import pygame
from constants import *
from towerplace import TowerPlace
from wall import Wall
from debug import debug
from editplayer import EditPlayer
from player import Player
from cursor import Cursor


class Level2:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Создание группы спрайтов
        self.visible_sprites = HitBoxCameraGroup()
        self.interactive_sprites = pygame.sprite.Group()

        # Создание спрайтов
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(EDIT_WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * WALLSIZE
                y = row_index * WALLSIZE
                if col == 'x':
                    Wall((x, y), [self.visible_sprites, self.interactive_sprites])
                elif col == 'p':
                    self.editplayer = EditPlayer((x, y))
                elif col == 't':
                    TowerPlace((x, y), [self.visible_sprites, self.interactive_sprites])

    def run(self):
        self.visible_sprites.c_draw(self.editplayer)
        self.visible_sprites.update()


class HitBoxCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2  # Половина ширины монитора 1920 // 2
        self.half_height = self.display_surface.get_size()[1] // 2  # Половина высоты монитора 1080 // 2
        self.visible_area = pygame.math.Vector2()

    def c_draw(self, editplayer):
        # Камера следует за серединой x, y персонажа
        mouse_x, mouse_y = pygame.mouse.get_pos()
        cursor = Cursor(mouse_x, mouse_y)


        self.visible_area.x = pygame.mouse.get_pos()[0] - self.half_width
        self.visible_area.y = pygame.mouse.get_pos()[1] - self.half_height

        for sprite in self.sprites():
            # self.display_surface.blit(pygame.transform.scale(self.cursor_image, (16, 16)), (self.m_x, self.m_y))

            visible_area_pos = sprite.rect.topleft - self.visible_area

            self.display_surface.blit(sprite.image, visible_area_pos)
        cursor.main(self.display_surface)