import pygame
import os
from settings import (
    BLACK,
    FPS,
    GRID_SIZE,
    PLAY_AREA_X,
    PLAY_AREA_Y,
    PLAY_AREA_WIDTH,
    PLAY_AREA_HEIGHT,
    GRID_COLOR,
    WHITE,
)
from snake import Snake
from food import Food
from ui import draw_score, draw_start_screen, draw_game_over_screen


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.high_score = self.load_high_score()
        self.running = True

    def load_high_score(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def update(self):
        if not self.snake.move():
            return False  # Game Over (Self collision)

        # Check wall collision
        head = self.snake.positions[0]
        if (
            head[0] < PLAY_AREA_X
            or head[0] >= PLAY_AREA_X + PLAY_AREA_WIDTH
            or head[1] < PLAY_AREA_Y
            or head[1] >= PLAY_AREA_Y + PLAY_AREA_HEIGHT
        ):
            return False  # Game Over (Wall collision)

        # Check food collision
        if self.snake.positions[0] == self.food.position:
            self.snake.length += 1
            self.snake.score += 10
            self.food.randomize_position()
            # Ensure food doesn't spawn on snake
            while self.food.position in self.snake.positions:
                self.food.randomize_position()

        if self.snake.score > self.high_score:
            self.high_score = self.snake.score

        return True

    def draw(self):
        self.surface.fill(BLACK)

        # Draw Grid
        for x in range(0, PLAY_AREA_WIDTH, GRID_SIZE):
            pygame.draw.line(
                self.surface,
                GRID_COLOR,
                (PLAY_AREA_X + x, PLAY_AREA_Y),
                (PLAY_AREA_X + x, PLAY_AREA_Y + PLAY_AREA_HEIGHT),
            )
        for y in range(0, PLAY_AREA_HEIGHT, GRID_SIZE):
            pygame.draw.line(
                self.surface,
                GRID_COLOR,
                (PLAY_AREA_X, PLAY_AREA_Y + y),
                (PLAY_AREA_X + PLAY_AREA_WIDTH, PLAY_AREA_Y + y),
            )

        # Draw Border
        pygame.draw.rect(
            self.surface,
            WHITE,
            (
                PLAY_AREA_X - 2,
                PLAY_AREA_Y - 2,
                PLAY_AREA_WIDTH + 4,
                PLAY_AREA_HEIGHT + 4,
            ),
            2,
        )

        self.snake.draw(self.surface)
        self.food.draw(self.surface)
        draw_score(self.surface, self.snake.score, self.high_score)
        pygame.display.flip()

    def run(self):
        draw_start_screen(self.surface)

        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.snake.handle_event(event)

            if not self.update():
                self.save_high_score()
                draw_game_over_screen(self.surface, self.snake.score, self.high_score)
                self.snake.reset()
                self.food.randomize_position()
                draw_start_screen(self.surface)
            else:
                self.draw()

        pygame.quit()
