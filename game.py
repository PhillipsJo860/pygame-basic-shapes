# Pygame game template

import pygame, sys, config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_rect(screen, rect, color, thickness):
            pygame.draw.rect(screen, color, rect, thickness)
# Write this function above your main( ) function
def draw_circle(screen, center, radius, color, thickness):
    """Draws a circle on the Pygame window."""
    pygame.draw.circle(screen, color, center, radius, thickness)


        

# Call the function that draws the circle from your main() function


# Write function above your main( ) function
def draw_line(surface, color, start_pos, end_pos, thickness):
    pygame.draw.line(surface, color, start_pos, end_pos, thickness)

    


def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.COLOR_WHITE)

        # Rectangle
        myrect1 = [100, 100, 200, 150]
        thickness1 = 8
        draw_rect(screen, myrect1, config.COLOR_DARKOLIVEGREEN, thickness1)

        # Circle
        circle_center = (300, 400)  
        circle_radius = 50           
        circle_color = config.COLOR_GREEN   
        circle_thickness = 0
        draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)

        # Line
        draw_line(screen, config.COLOR_DARKBLUE, [100, 100], [700, 500], 5)  
        draw_line(screen, config.COLOR_CRIMSON, [75, 250], [500, 300], 2)
        

        pygame.display.flip()
        clock.tick(config.FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
