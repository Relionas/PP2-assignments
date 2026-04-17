import pygame
import sys
from ball import Ball

def main():
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    WHITE = (255, 255, 255)
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()
    
    ball = Ball(WIDTH, HEIGHT)

    while True:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move("UP")
                elif event.key == pygame.K_DOWN:
                    ball.move("DOWN")
                elif event.key == pygame.K_LEFT:
                    ball.move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    ball.move("RIGHT")

        # 2. Drawing
        screen.fill(WHITE)
        ball.draw(screen)
        
        # 3. Refresh Screen
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()