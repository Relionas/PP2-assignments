import pygame
import sys
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spotify Style Music Player")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 22)
BIG_FONT = pygame.font.SysFont("arial", 32)

# Colors (Spotify-like dark theme)
BG = (18, 18, 18)
PANEL = (24, 24, 24)
GREEN = (30, 215, 96)
WHITE = (230, 230, 230)
GRAY = (120, 120, 120)

player = MusicPlayer("music")


def draw_ui():
    screen.fill(BG)

    # LEFT PANEL (playlist)
    pygame.draw.rect(screen, PANEL, (0, 0, 250, HEIGHT))

    title = FONT.render("PLAYLIST", True, GREEN)
    screen.blit(title, (20, 20))

    for i, track in enumerate(player.playlist):
        name = track.split("\\")[-1]

        color = GREEN if i == player.index else WHITE
        txt = FONT.render(name, True, color)
        screen.blit(txt, (20, 60 + i * 30))

    # CENTER TRACK INFO
    current = BIG_FONT.render(player.get_current_track(), True, WHITE)
    screen.blit(current, (300, 200))

    status = FONT.render(
        "Playing" if player.is_playing else "Paused",
        True,
        GRAY
    )
    screen.blit(status, (300, 250))

    # PROGRESS BAR
    pygame.draw.rect(screen, GRAY, (300, 400, 500, 6))

    pos = player.get_pos()
    pygame.draw.rect(screen, GREEN, (300, 400, min(pos * 5, 500), 6))

    # CONTROLS INFO
    controls = [
        "P - Play/Pause",
        "S - Stop",
        "N - Next",
        "B - Back",
        "Q - Quit"
    ]

    for i, c in enumerate(controls):
        txt = FONT.render(c, True, GRAY)
        screen.blit(txt, (300, 450 + i * 25))


def handle_keys(event):
    if event.key == pygame.K_p:
        player.play()

    elif event.key == pygame.K_s:
        player.stop()

    elif event.key == pygame.K_n:
        player.next()

    elif event.key == pygame.K_b:
        player.previous()

    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()


# MAIN LOOP
running = True
while running:
    clock.tick(30)+

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            handle_keys(event)

    draw_ui()
    pygame.display.update()

pygame.quit()