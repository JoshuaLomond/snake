import pygame

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Game settings
FPS = 15
SNAKE_SPEED = 10 # Pixels per frame (which is 1 grid block per frame if logic is grid-based)
