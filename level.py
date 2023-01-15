import pygame
from constants import *
from wall import Wall
from player import Player
from debug import debug


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Создание группы спрайтов
        self.visible_sprites = HitBoxCameraGroup()
        self.interactive_sprites = pygame.sprite.Group()

        # Создание спрайтов
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * WALLSIZE
                y = row_index * WALLSIZE
                if col == 'x':
                    Wall((x, y),[self.visible_sprites, self.interactive_sprites])
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.interactive_sprites)

    def run(self):
        self.visible_sprites.c_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class HitBoxCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2 # Половина ширины монитора 1920 // 2
        self.half_height = self.display_surface.get_size()[1] // 2 # Половина высоты монитора 1080 // 2
        self.visible_area = pygame.math.Vector2()

    def c_draw(self, player):

        # Камера следует за серединой x, y персонажа

        self.visible_area.x = player.rect.centerx - self.half_width
        self.visible_area.y = player.rect.centery - self.half_height
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            visible_area_pos = sprite.rect.topleft - self.visible_area
            self.display_surface.blit(sprite.image, visible_area_pos)