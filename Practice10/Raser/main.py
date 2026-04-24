import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_COUNT = 0 

# Setting up Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font_large = pygame.font.SysFont("Verdana", 60)
game_over = font_large.render("Game Over", True, BLACK)

# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer - Serzhan Edition")

# Load and scale background road
bg_raw = pygame.image.load("images/AnimatedStreet.jpeg")
background_img = pygame.transform.scale(bg_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

# --- SOUND SETUP ---
try:
    pygame.mixer.music.load("sound/background.mp3") 
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Warning: background.mp3 not found")

crash_sound = None
try:
    crash_sound = pygame.mixer.Sound('sound/crash.wav')
    crash_sound.set_volume(1.0)
except pygame.error:
    print("Warning: crash.wav not found")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        raw_image = pygame.image.load("images/Enemy.png")
        rotated_image = pygame.transform.rotate(raw_image, 90)
        self.image = pygame.transform.scale(rotated_image, (35, 70))
        self.rect = self.image.get_rect()
        # Spawn within road limits
        self.rect.center = (random.randint(60, SCREEN_WIDTH-60), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(60, SCREEN_WIDTH - 60), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_coin = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(raw_coin, (30, 30))
        self.rect = self.image.get_rect()

    def spawn(self, obstacle_group):
        while True:
            # Spawn within road limits
            self.rect.center = (random.randint(60, SCREEN_WIDTH - 60), 0)
            if not pygame.sprite.spritecollideany(self, obstacle_group):
                break 

    def move(self, obstacle_group):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.spawn(obstacle_group)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        raw_image = pygame.image.load("images/Player.png")
        rotated_image = pygame.transform.rotate(raw_image, -90)
        self.image = pygame.transform.scale(rotated_image, (35, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # FIX: Added road boundaries (45px from each side to stay off grass)
        if self.rect.left > 45:
              if pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 45:        
              if pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)

# Create objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite grouping
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

C1.spawn(enemies)

# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background_img, (0,0))
    
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coin_text = font_small.render("Coins: " + str(COIN_COUNT), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 110, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    P1.move()
    E1.move()
    C1.move(enemies) 

    if pygame.sprite.spritecollideany(P1, coins):
        COIN_COUNT += 1
        C1.spawn(enemies)

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()
          if crash_sound:
              crash_sound.play()
          
          time.sleep(0.5)
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30, 250))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)