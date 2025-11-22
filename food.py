import pygame
import random
from settings import (
    GRID_SIZE,
    RED,
    PLAY_AREA_X,
    PLAY_AREA_Y,
    PLAY_AREA_WIDTH,
    PLAY_AREA_HEIGHT,
)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            PLAY_AREA_X
            + random.randint(0, (PLAY_AREA_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            PLAY_AREA_Y
            + random.randint(0, (PLAY_AREA_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
        )

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
