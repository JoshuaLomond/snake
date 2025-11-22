import pygame

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Game settings
FPS = 15
SNAKE_SPEED = 10  # Pixels per frame

# Border settings
BORDER_WIDTH = 40
PLAY_AREA_X = BORDER_WIDTH
PLAY_AREA_Y = BORDER_WIDTH + 40  # Extra space at top for score
PLAY_AREA_WIDTH = SCREEN_WIDTH - (2 * BORDER_WIDTH)
PLAY_AREA_HEIGHT = SCREEN_HEIGHT - BORDER_WIDTH - PLAY_AREA_Y

# Grid settings
GRID_SIZE = 20  # Increased grid size for better visibility
GRID_WIDTH = PLAY_AREA_WIDTH // GRID_SIZE
GRID_HEIGHT = PLAY_AREA_HEIGHT // GRID_SIZE
GRID_COLOR = (40, 40, 40)
