import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, RED


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
        )

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
