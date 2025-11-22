import pygame
from settings import WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT


def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_start_screen(surface):
    surface.fill(BLACK)
    draw_text(surface, "SNAKE GAME", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(surface, "Arrows to move", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(
        surface, "Press any key to play", 18, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 / 4
    )
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False


def draw_game_over_screen(surface, score, high_score):
    surface.fill(BLACK)
    draw_text(surface, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(
        surface, "Score: " + str(score), 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    )
    draw_text(
        surface,
        "High Score: " + str(high_score),
        22,
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2 + 30,
    )
    draw_text(
        surface,
        "Press any key to play again",
        18,
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT * 3 / 4,
    )
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False


def draw_score(surface, score, high_score):
    draw_text(surface, "Score: " + str(score), 24, SCREEN_WIDTH // 2, 20)
    draw_text(surface, "High Score: " + str(high_score), 18, SCREEN_WIDTH // 2, 45)
