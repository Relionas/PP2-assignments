import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (213, 50, 80)
GREEN = (0, 255, 0)

# Screen Dimensions
WIDTH = 600
HEIGHT = 400

# Game Settings
SNAKE_BLOCK = 20
INITIAL_SPEED = 10

# Initialize Display
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake - Serzhan Edition')

clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("verdana", 25)

def display_ui(score, level):
    """Displays score and level in the top-left corner."""
    score_text = score_font.render("Score: " + str(score), True, WHITE)
    level_text = score_font.render("Level: " + str(level), True, WHITE)
    dis.blit(score_text, [10, 10])
    dis.blit(level_text, [10, 40])

def draw_snake(snake_block, snake_list):
    """Draws each segment of the snake."""
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def generate_food_pos(snake_list):
    """Generates food position and ensures it doesn't spawn on the snake body."""
    while True:
        foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
        foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
        if [foodx, foody] not in snake_list:
            return foodx, foody

def gameLoop():
    game_over = False
    game_close = False

    # Snake starting position
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Movement variables
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    
    score = 0
    level = 1
    current_speed = INITIAL_SPEED

    # Initial food spawn
    foodx, foody = generate_food_pos(snake_List)

    while not game_over:

        while game_close == True:
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # FIX: Control updated to WASD keys
                # Also prevents moving in opposite direction
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

        # WALL COLLISION: Game Over if snake hits the boundaries
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        
        # Draw food
        pygame.draw.rect(dis, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        
        # Update snake body logic
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # SELF COLLISION: Check if snake hit itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        display_ui(score, level)

        pygame.display.update()

        # EATING FOOD: Increase score and check for level up
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food_pos(snake_List)
            Length_of_snake += 1
            score += 1
            
            # Level Progression: Every 3 foods, level and speed increase
            if score % 3 == 0:
                level += 1
                current_speed += 2 

        clock.tick(current_speed)

    pygame.quit()
    quit()

gameLoop()