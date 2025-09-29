"""
Simple Snake game using Pygame
Save as: snake_game.py
Requires: pygame (install with `pip install pygame`)
"""

import pygame
import random
import sys
import os

# --- Config ---
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20  # size of grid cell (snake + food)
assert WINDOW_WIDTH % CELL_SIZE == 0 and WINDOW_HEIGHT % CELL_SIZE == 0
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

FPS = 10  # base speed (increase for harder game)
SNAKE_INITIAL_LENGTH = 4

# Colors (R,G,B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
RED = (200, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 120, 255)
YELLOW = (230, 230, 50)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# --- Helper functions ---
def random_food_position(snake):
    """Return a random position (x,y) within the grid that is not occupied by the snake."""
    available = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in snake
    ]
    if not available:
        # No space left: return None to signal victory (snake fills grid)
        return None
    return random.choice(available)


def draw_cell(surface, position, color):
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)


def draw_grid(surface):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (0, y), (WINDOW_WIDTH, y))


# --- Game classes / state ---
class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.large_font = pygame.font.SysFont("Arial", 48, bold=True)

        # High score file in the same directory as the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.high_score_file = os.path.join(script_dir, "highscore.txt")
        self.high_score = self.load_high_score()

        # Start screen flag
        self.show_start_screen = True

        # Initialize game state
        self.reset()

    def draw_start_screen(self):
        self.screen.fill(BLACK)
    
        title_surf = self.large_font.render("SNAKE", True, GREEN)
        title_rect = title_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
        self.screen.blit(title_surf, title_rect)
    
        prompt_surf = self.font.render("Press ENTER to play", True, WHITE)
        prompt_rect = prompt_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
        self.screen.blit(prompt_surf, prompt_rect)
    
        high_score_surf = self.font.render(f"High score: {self.high_score}", True, YELLOW)
        high_score_rect = high_score_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40))
        self.screen.blit(high_score_surf, high_score_rect)
    
        pygame.display.flip()

    def load_high_score(self):
        """Load the high score from file if available, else return 0."""
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, "r") as f:
                    return int(f.read().strip())
            except (ValueError, FileNotFoundError):
                return 0
        return 0
    
    def save_high_score(self):
        """Save the current high score to file."""
        with open(self.high_score_file, "w") as f:
            f.write(str(self.high_score))

    def reset(self):
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        # Snake is a list of positions, head is first element
        self.snake = [(start_x - i, start_y) for i in range(SNAKE_INITIAL_LENGTH)]
        self.direction = RIGHT
        self.next_direction = RIGHT  # buffer next direction to prevent instant reversal
        self.score = 0
        self.speed = FPS
        self.food = random_food_position(self.snake)
        self.game_over = False
        self.paused = False

    def handle_key(self, key):
        # Map keys to directions; ignore reversal
        if key in (pygame.K_UP, pygame.K_w):
            new_dir = UP
        elif key in (pygame.K_DOWN, pygame.K_s):
            new_dir = DOWN
        elif key in (pygame.K_LEFT, pygame.K_a):
            new_dir = LEFT
        elif key in (pygame.K_RIGHT, pygame.K_d):
            new_dir = RIGHT
        else:
            return

        # Prevent reversing (e.g., moving left when currently moving right)
        if (new_dir[0] * -1, new_dir[1] * -1) == self.direction:
            return
        self.next_direction = new_dir

    def update(self):
        if self.game_over or self.paused:
            return

        # Apply the buffered direction
        self.direction = self.next_direction

        # Compute new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Collision with walls?
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            self.game_over = True
            # Check and save high score
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            return

        # Collision with self?
        if new_head in self.snake:
            self.game_over = True
            # Check and save high score
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            return

        # Move snake
        self.snake.insert(0, new_head)

        # Check food collision
        if self.food is not None and new_head == self.food:
            self.score += 1
            # Optionally speed up a bit every few points:
            if self.score % 5 == 0:
                self.speed += 1
            self.food = random_food_position(self.snake)
            # If food is None, snake filled the board — player wins (treat as game over)
            if self.food is None:
                self.game_over = True
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
        else:
            # Remove tail segment (normal movement)
            self.snake.pop()

    def draw_hud(self):
        # Draw score
        score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (10, 10))
        # Draw instructions
        instr = "Arrows / WASD: Move   P: Pause   R: Restart   Q / ESC: Quit"
        instr_surf = self.font.render(instr, True, WHITE)
        self.screen.blit(instr_surf, (10, WINDOW_HEIGHT - 26))

    def render(self):
        # Background
        self.screen.fill(BLACK)

        # Grid (optional)
        draw_grid(self.screen)

        # Draw food
        if self.food is not None:
            draw_cell(self.screen, self.food, RED)

        # Draw snake: head a different color
        for i, segment in enumerate(self.snake):
            color = BLUE if i == 0 else GREEN
            draw_cell(self.screen, segment, color)

        # Draw HUD
        self.draw_hud()

        # If paused
        if self.paused:
            pause_surf = self.large_font.render("PAUSED", True, YELLOW)
            rect = pause_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(pause_surf, rect)

        # If game over
        if self.game_over:
            over_surf = self.large_font.render("GAME OVER", True, YELLOW)
            rect = over_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
            self.screen.blit(over_surf, rect)

            score_surf = self.font.render(f"Final score: {self.score}", True, WHITE)
            rect2 = score_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 10))
            self.screen.blit(score_surf, rect2)

            high_score_surf = self.font.render(f"High score: {self.high_score}", True, WHITE)
            rect3 = high_score_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            self.screen.blit(high_score_surf, rect3)

            hint_surf = self.font.render("Press R to restart or Q/ESC to quit", True, WHITE)
            rect4 = hint_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            self.screen.blit(hint_surf, rect4)

        pygame.display.flip()

    def run(self):
        while True:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_q, pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()

                    if self.show_start_screen:
                        if event.key == pygame.K_RETURN:
                            self.show_start_screen = False
                            self.reset()
                    else:
                        if event.key == pygame.K_r:
                            self.reset()
                        if event.key == pygame.K_p:
                            self.paused = not self.paused
                        # If game over, allow pressing R to restart
                        if not self.game_over:
                            self.handle_key(event.key)
        
            if self.show_start_screen:
                self.draw_start_screen()
            else:
                # Update game logic
                self.update()
                # Draw everything
                self.render()
                # Tick
                self.clock.tick(self.speed)


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
