import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()
pygame.mixer.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5
SCORE = 0
COIN_COUNT = 0

# NEW: coins needed to increase difficulty
COINS_FOR_SPEEDUP = 5  

# Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font_large = pygame.font.SysFont("Verdana", 60)
game_over = font_large.render("Game Over", True, BLACK)

# Window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer - Dias Edition")

# Background
bg_raw = pygame.image.load("images/AnimatedStreet.jpeg")
background_img = pygame.transform.scale(bg_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

# -------- SOUND --------
try:
    pygame.mixer.music.load("sound/background.mp3")
    pygame.mixer.music.play(-1)
except:
    print("No background music")

crash_sound = None
try:
    crash_sound = pygame.mixer.Sound("sound/crash.wav")
except:
    print("No crash sound")

# -------- ENEMY CLASS --------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw = pygame.image.load("images/Enemy.png")
        self.image = pygame.transform.scale(pygame.transform.rotate(raw, 90), (35, 70))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Spawn enemy at random X position
        self.rect.center = (random.randint(60, SCREEN_WIDTH - 60), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # If enemy leaves screen → increase score
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_position()

# -------- COIN CLASS (UPDATED) --------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load base coin image
        self.base_image = pygame.image.load("images/coin.png")

        self.weight = 1  # coin value (1, 2, 3)
        self.image = None
        self.rect = None

        self.randomize()  # generate first coin

    def randomize(self):
        """
        Assign random weight and size
        """
        self.weight = random.choice([1, 2, 3])

        # Different size based on weight
        size = 20 + self.weight * 10  # 30, 40, 50

        self.image = pygame.transform.scale(self.base_image, (size, size))
        self.rect = self.image.get_rect()

    def spawn(self, obstacles):
        """
        Spawn coin at random position (no collision with enemies)
        """
        self.randomize()

        while True:
            self.rect.center = (random.randint(60, SCREEN_WIDTH - 60), 0)
            if not pygame.sprite.spritecollideany(self, obstacles):
                break

    def move(self, obstacles):
        """
        Move coin downward
        """
        self.rect.move_ip(0, SPEED)

        # Respawn if out of screen
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn(obstacles)

# -------- PLAYER --------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw = pygame.image.load("images/Player.png")
        self.image = pygame.transform.scale(pygame.transform.rotate(raw, -90), (35, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        # Move left
        if self.rect.left > 45:
            if keys[K_a]:
                self.rect.move_ip(-5, 0)

        # Move right
        if self.rect.right < SCREEN_WIDTH - 45:
            if keys[K_d]:
                self.rect.move_ip(5, 0)

# -------- CREATE OBJECTS --------
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Groups
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# Initial coin spawn
C1.spawn(enemies)

# -------- MAIN LOOP --------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background_img, (0, 0))

    # UI text
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COIN_COUNT}", True, BLACK)

    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # Draw all objects
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Movement
    P1.move()
    E1.move()
    C1.move(enemies)

    # -------- COIN COLLISION --------
    if pygame.sprite.spritecollideany(P1, coins):
        # Add coin weight instead of +1
        COIN_COUNT += C1.weight

        # Respawn coin
        C1.spawn(enemies)

        # -------- SPEED INCREASE LOGIC --------
        if COIN_COUNT % COINS_FOR_SPEEDUP == 0:
            SPEED += 1  # increase difficulty

    # -------- ENEMY COLLISION --------
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        if crash_sound:
            crash_sound.play()

        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
