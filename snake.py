import pygame
from settings import (
    GRID_SIZE,
    GREEN,
    WHITE,
    PLAY_AREA_X,
    PLAY_AREA_Y,
    PLAY_AREA_WIDTH,
    PLAY_AREA_HEIGHT,
)


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [
            (
                (PLAY_AREA_X + PLAY_AREA_WIDTH // 2),
                (PLAY_AREA_Y + PLAY_AREA_HEIGHT // 2),
            )
        ]
        self.direction = (0, 0)
        self.color = GREEN
        self.score = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if (
                event.key == pygame.K_UP or event.key == pygame.K_w
            ) and self.direction != (0, 1):
                self.direction = (0, -1)
            elif (
                event.key == pygame.K_DOWN or event.key == pygame.K_s
            ) and self.direction != (0, -1):
                self.direction = (0, 1)
            elif (
                event.key == pygame.K_LEFT or event.key == pygame.K_a
            ) and self.direction != (1, 0):
                self.direction = (-1, 0)
            elif (
                event.key == pygame.K_RIGHT or event.key == pygame.K_d
            ) and self.direction != (-1, 0):
                self.direction = (1, 0)

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE))), (cur[1] + (y * GRID_SIZE)))

        # Check if snake hits the wall (for game over logic later, but here we just update position)
        # Actually, collision detection should probably be handled in the Game class or here.
        # Let's just update the position here.

        if self.length > 1 and new in self.positions[2:]:
            return False  # Self collision

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def reset(self):
        self.length = 1
        self.positions = [
            (
                (PLAY_AREA_X + PLAY_AREA_WIDTH // 2),
                (PLAY_AREA_Y + PLAY_AREA_HEIGHT // 2),
            )
        ]
        self.direction = (0, 0)
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect(p[0], p[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, WHITE, rect, 1)  # Border
