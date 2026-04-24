import pygame

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint - Smooth Edition")
    
    clock = pygame.time.Clock()
    
    # Colors and Settings
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    
    PALETTE = [
        (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), 
        (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 128)
    ]
    
    color = BLACK
    drawing_mode = 'pen'
    line_width = 5 # Thickness of the line
    
    canvas = pygame.Surface((800, 600))
    canvas.fill(WHITE)
    
    start_pos = None # For shapes (rect/circle)
    last_pos = None  # For smooth drawing (pen/eraser)
    is_drawing = False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Tools Selection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: drawing_mode = 'rect'
                if event.key == pygame.K_c: drawing_mode = 'circle'
                if event.key == pygame.K_p: drawing_mode = 'pen'
                if event.key == pygame.K_e: drawing_mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[1] > 610: # Palette click
                    for i, c in enumerate(PALETTE):
                        rect = pygame.Rect(10 + i * 45, 620, 40, 40)
                        if rect.collidepoint(mouse_pos):
                            color = c
                else:
                    is_drawing = True
                    start_pos = mouse_pos
                    last_pos = mouse_pos # Start point for the line

            if event.type == pygame.MOUSEBUTTONUP:
                if is_drawing:
                    # Final shape drawing on canvas
                    if drawing_mode == 'rect':
                        w = mouse_pos[0] - start_pos[0]
                        h = mouse_pos[1] - start_pos[1]
                        pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], w, h), 2)
                    
                    elif drawing_mode == 'circle':
                        r = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
                        pygame.draw.circle(canvas, color, start_pos, r, 2)
                    
                    is_drawing = False
                    start_pos = None
                    last_pos = None

            if event.type == pygame.MOUSEMOTION and is_drawing:
                if drawing_mode == 'pen':
                    # DRAWING SMOOTH LINES: Connect last_pos to current mouse_pos
                    pygame.draw.line(canvas, color, last_pos, mouse_pos, line_width)
                    # Also draw circles at joints to make lines perfectly rounded
                    pygame.draw.circle(canvas, color, mouse_pos, line_width // 2)
                    last_pos = mouse_pos # Update last position
                
                elif drawing_mode == 'eraser':
                    pygame.draw.line(canvas, WHITE, last_pos, mouse_pos, line_width * 4)
                    pygame.draw.circle(canvas, WHITE, mouse_pos, (line_width * 4) // 2)
                    last_pos = mouse_pos

        # Render Interface
        screen.fill(GRAY)
        screen.blit(canvas, (0, 0))
        
        # Draw Palette
        for i, c in enumerate(PALETTE):
            pygame.draw.rect(screen, c, (10 + i * 45, 620, 40, 40))
            if color == c:
                pygame.draw.rect(screen, WHITE, (10 + i * 45, 620, 40, 40), 3)

        # Draw Preview (Phantom shapes while dragging)
        if is_drawing and start_pos and mouse_pos[1] <= 600:
            if drawing_mode == 'rect':
                w = mouse_pos[0] - start_pos[0]
                h = mouse_pos[1] - start_pos[1]
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], w, h), 2)
            elif drawing_mode == 'circle':
                r = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, r, 2)

        # Text Hints
        font = pygame.font.SysFont("Verdana", 14)
        screen.blit(font.render(f"Tool: {drawing_mode.upper()}", True, BLACK), (400, 620))
        screen.blit(font.render("P: Pen | R: Rect | C: Circle | E: Eraser", True, BLACK), (400, 650))

        pygame.display.flip()
        clock.tick(120) # Increased tick for better responsiveness

    pygame.quit()

if __name__ == '__main__':
    main()