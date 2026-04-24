import pygame
import time
import random

pygame.init()

# -------- COLORS --------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (213, 50, 80)
GREEN = (0, 255, 0)

# -------- SCREEN --------
WIDTH = 600
HEIGHT = 400

# -------- GAME SETTINGS --------
SNAKE_BLOCK = 20
INITIAL_SPEED = 10

# -------- FOOD SETTINGS (NEW) --------
FOOD_LIFETIME = 5000  # milliseconds (5 seconds)

# -------- DISPLAY --------
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake - Dias Edition')

clock = pygame.time.Clock()

# -------- FONT --------
score_font = pygame.font.SysFont("verdana", 25)

def display_ui(score, level):
    """Draw score and level"""
    score_text = score_font.render("Score: " + str(score), True, WHITE)
    level_text = score_font.render("Level: " + str(level), True, WHITE)
    dis.blit(score_text, [10, 10])
    dis.blit(level_text, [10, 40])

def draw_snake(snake_block, snake_list):
    """Draw snake body"""
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

# -------- NEW: FOOD CLASS --------
class Food:
    def __init__(self, snake_list):
        self.spawn(snake_list)

    def spawn(self, snake_list):
        """Generate food with random weight and position"""

        while True:
            self.x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            self.y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

            if [self.x, self.y] not in snake_list:
                break

        # -------- RANDOM WEIGHT --------
        self.weight = random.choice([1, 2, 3])

        # Size depends on weight
        self.size = SNAKE_BLOCK + (self.weight * 5)

        # Start timer
        self.spawn_time = pygame.time.get_ticks()

    def draw(self):
        """Draw food"""
        pygame.draw.rect(dis, RED, [self.x, self.y, self.size, self.size])

    def is_expired(self):
        """Check if food lifetime is over"""
        return pygame.time.get_ticks() - self.spawn_time > FOOD_LIFETIME


def gameLoop():
    game_over = False
    game_close = False

    # -------- INITIAL POSITION --------
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    score = 0
    level = 1
    current_speed = INITIAL_SPEED

    # -------- CREATE FOOD --------
    food = Food(snake_List)

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            msg = score_font.render("Game Over! Q-Quit or C-Again", True, RED)
            dis.blit(msg, [WIDTH / 5, HEIGHT / 2.5])
            display_ui(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # -------- INPUT --------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                # WASD movement (no reverse)
                if event.key == pygame.K_a and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # -------- WALL COLLISION --------
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Move snake
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)

        # -------- FOOD TIMER (NEW) --------
        if food.is_expired():
            food.spawn(snake_List)

        # Draw food
        food.draw()

        # -------- SNAKE LOGIC --------
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        display_ui(score, level)

        pygame.display.update()

        # -------- EATING FOOD --------
        if x1 == food.x and y1 == food.y:
            # Add weight instead of +1
            score += food.weight

            Length_of_snake += 1

            # Respawn food
            food.spawn(snake_List)

            # Level system
            if score % 3 == 0:
                level += 1
                current_speed += 2

        clock.tick(current_speed)

    pygame.quit()
    quit()


gameLoop()
