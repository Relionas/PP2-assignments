import pygame
import math  # Needed for equilateral triangle calculations

def main():
    pygame.init()

    # Window settings
    WIDTH, HEIGHT = 800, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint - Dias Edition")

    clock = pygame.time.Clock()

    # Basic colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    # Color palette
    PALETTE = [
        (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 128)
    ]

    color = BLACK  # Current drawing color
    drawing_mode = 'pen'  # Default tool
    line_width = 5  # Thickness

    # Canvas (drawing area)
    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)

    # Variables for drawing
    start_pos = None
    last_pos = None
    is_drawing = False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # -------- TOOL SELECTION --------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: drawing_mode = 'rect'
                if event.key == pygame.K_c: drawing_mode = 'circle'
                if event.key == pygame.K_p: drawing_mode = 'pen'
                if event.key == pygame.K_e: drawing_mode = 'eraser'
                if event.key == pygame.K_s: drawing_mode = 'square'
                if event.key == pygame.K_t: drawing_mode = 'right_triangle'
                if event.key == pygame.K_y: drawing_mode = 'equilateral_triangle'
                if event.key == pygame.K_h: drawing_mode = 'rhombus'

            # -------- MOUSE DOWN --------
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check palette click
                if mouse_pos[1] > 610:
                    for i, c in enumerate(PALETTE):
                        rect = pygame.Rect(10 + i * 45, 620, 40, 40)
                        if rect.collidepoint(mouse_pos):
                            color = c
                else:
                    is_drawing = True
                    start_pos = mouse_pos
                    last_pos = mouse_pos

            # -------- MOUSE UP --------
            if event.type == pygame.MOUSEBUTTONUP:
                if is_drawing:

                    x1, y1 = start_pos
                    x2, y2 = mouse_pos
                    w = x2 - x1
                    h = y2 - y1

                    # ----- RECTANGLE -----
                    if drawing_mode == 'rect':
                        pygame.draw.rect(canvas, color, (x1, y1, w, h), 2)

                    # ----- SQUARE -----
                    elif drawing_mode == 'square':
                        side = min(abs(w), abs(h))  # equal sides
                        pygame.draw.rect(canvas, color, (x1, y1, side, side), 2)

                    # ----- CIRCLE -----
                    elif drawing_mode == 'circle':
                        r = int(((w)**2 + (h)**2)**0.5)
                        pygame.draw.circle(canvas, color, start_pos, r, 2)

                    # ----- RIGHT TRIANGLE -----
                    elif drawing_mode == 'right_triangle':
                        points = [
                            (x1, y1),
                            (x2, y1),
                            (x1, y2)
                        ]
                        pygame.draw.polygon(canvas, color, points, 2)

                    # ----- EQUILATERAL TRIANGLE -----
                    elif drawing_mode == 'equilateral_triangle':
                        side = abs(w)
                        height = (math.sqrt(3) / 2) * side

                        points = [
                            (x1, y1),
                            (x1 + side, y1),
                            (x1 + side / 2, y1 - height)
                        ]
                        pygame.draw.polygon(canvas, color, points, 2)

                    # ----- RHOMBUS -----
                    elif drawing_mode == 'rhombus':
                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2

                        points = [
                            (cx, y1),  # top
                            (x2, cy),  # right
                            (cx, y2),  # bottom
                            (x1, cy)   # left
                        ]
                        pygame.draw.polygon(canvas, color, points, 2)

                    is_drawing = False
                    start_pos = None
                    last_pos = None

            # -------- DRAWING WITH MOUSE MOVE --------
            if event.type == pygame.MOUSEMOTION and is_drawing:
                if drawing_mode == 'pen':
                    pygame.draw.line(canvas, color, last_pos, mouse_pos, line_width)
                    pygame.draw.circle(canvas, color, mouse_pos, line_width // 2)
                    last_pos = mouse_pos

                elif drawing_mode == 'eraser':
                    pygame.draw.line(canvas, WHITE, last_pos, mouse_pos, line_width * 4)
                    pygame.draw.circle(canvas, WHITE, mouse_pos, (line_width * 4) // 2)
                    last_pos = mouse_pos

        # -------- RENDER --------
        screen.fill(GRAY)
        screen.blit(canvas, (0, 0))

        # Draw palette
        for i, c in enumerate(PALETTE):
            pygame.draw.rect(screen, c, (10 + i * 45, 620, 40, 40))
            if color == c:
                pygame.draw.rect(screen, WHITE, (10 + i * 45, 620, 40, 40), 3)

        # -------- PREVIEW SHAPES --------
        if is_drawing and start_pos and mouse_pos[1] <= 600:
            x1, y1 = start_pos
            x2, y2 = mouse_pos
            w = x2 - x1
            h = y2 - y1

            if drawing_mode == 'rect':
                pygame.draw.rect(screen, color, (x1, y1, w, h), 2)

            elif drawing_mode == 'square':
                side = min(abs(w), abs(h))
                pygame.draw.rect(screen, color, (x1, y1, side, side), 2)

            elif drawing_mode == 'circle':
                r = int((w**2 + h**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, r, 2)

            elif drawing_mode == 'right_triangle':
                pygame.draw.polygon(screen, color, [(x1, y1), (x2, y1), (x1, y2)], 2)

            elif drawing_mode == 'equilateral_triangle':
                side = abs(w)
                height = (math.sqrt(3) / 2) * side
                pygame.draw.polygon(screen, color,
                                    [(x1, y1), (x1 + side, y1), (x1 + side / 2, y1 - height)], 2)

            elif drawing_mode == 'rhombus':
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                pygame.draw.polygon(screen, color,
                                    [(cx, y1), (x2, cy), (cx, y2), (x1, cy)], 2)

        # -------- UI TEXT --------
        font = pygame.font.SysFont("Verdana", 14)
        screen.blit(font.render(f"Tool: {drawing_mode.upper()}", True, BLACK), (400, 620))
        screen.blit(font.render(
            "P: Pen | R: Rect | C: Circle | E: Eraser | S: Square | T: Right Tri | Y: Eq Tri | H: Rhombus",
            True, BLACK), (200, 650))

        pygame.display.flip()
        clock.tick(120)

    pygame.quit()


if __name__ == '__main__':
    main()
