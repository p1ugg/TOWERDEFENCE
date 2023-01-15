import pygame
from Board import Board, BLACK

if __name__ == '__main__':
    pygame.init()
    size = width, height = 750, 750
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    is_rad = True
    board = Board(30, 30, size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and is_rad:
                if event.button == 1:
                    board.get_click(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_rad = not is_rad
        if not is_rad:
            board.next_gen()
        board.render(screen)
        clock.tick(10)
        pygame.display.flip()
        screen.fill(BLACK)
    pygame.quit()
