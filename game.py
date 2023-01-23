import random
import sys
from data.settings import *
from enemy.enemy import *
from data.cursor import Cursor
from player.player import *
from towers.balista import *
from towers.base import *

pygame.init()
pygame.mouse.set_visible(False)

font = pygame.font.Font('data/hardpixel.otf', 36)

display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

display_scroll = [0, 0]

player = Player(WIDTH // 2, HEIGHT // 2, 32, 32, display_scroll)

towers = []

enemies = []

base = Base(WIDTH // 2, HEIGHT // 2, enemies, display_scroll)

enemies = [Slime(random.randrange(-50, 200), random.randrange(-50, 200), base, display_scroll)]

base = Base(WIDTH // 2, HEIGHT // 2, enemies, display_scroll)

bullets = []

time_delay1 = 700
towers_shoot = pygame.USEREVENT + 1
pygame.time.set_timer(towers_shoot, time_delay1)

time_delay2 = 900
player_shoot = pygame.USEREVENT + 1
pygame.time.set_timer(player_shoot, time_delay2)

time_delay3 = 300
tower_place = pygame.USEREVENT + 1
pygame.time.set_timer(player_shoot, time_delay3)

player_shootable = False
tower_placeable = False

kills = 0
money = 20

while True:
    display.fill((0, 200, 100))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    mouse_keys = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    cursor = Cursor(mouse_x, mouse_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == towers_shoot:
            for tower in towers:
                tower.shoot()
        if event.type == player_shoot:
            player_shootable = True
        if event.type == tower_place:
            tower_placeable = True

    if mouse_keys[0] is True:
        if player_shootable:
            player_shootable = False
            bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y, 0.05, display_scroll))

    if mouse_keys[2] is True:
        if tower_placeable:
            if money >= 15:
                money -= 15
                tower_placeable = False
                towers.append(Balista(mouse_x, mouse_y, enemies, bullets, display_scroll))
    if keys[pygame.K_ESCAPE]:
        import menu

    if keys[pygame.K_a]:
        display_scroll[0] -= 5
        for bullet in bullets:
            bullet.x += 5

        player.is_idle = False
        player.moving_left = True
        player.moving_right = False

    if keys[pygame.K_d]:
        display_scroll[0] += 5
        for bullet in bullets:
            bullet.x -= 5

        player.is_idle = False
        player.moving_left = False
        player.moving_right = True

    if keys[pygame.K_w]:
        display_scroll[1] -= 5
        for bullet in bullets:
            bullet.y += 5

        player.is_idle = False

    if keys[pygame.K_s]:
        display_scroll[1] += 5
        for bullet in bullets:
            bullet.y -= 5

        player.is_idle = False

    if len(enemies) <= kills:
        enemies.append(
            Slime(random.randrange(-50, 200), random.randrange(-50, 200), base, display_scroll))

    for tower in towers:
        tower.main(display)

    if len(bullets) > 300:
        bullets.pop(0)

    base.main(display)

    for enemy in enemies:
        enemy.main(display, bullets)
        if enemy.health <= 0:
            enemies.pop(enemies.index(enemy))
            kills += 1
            money += random.randrange(1, 3)

    for bullet in bullets:
        bullet.main(display)

    player.main(display)

    cursor.main(display)

    kill_count = font.render(f'Убийства: {str(kills)}', True, RED)
    display.blit(kill_count, (25, 25))

    money_count = font.render(f'Монеты: {str(money)}', True, (255, 255, 0))
    display.blit(money_count, (25, 75))

    clock.tick(60)
    pygame.display.update()
