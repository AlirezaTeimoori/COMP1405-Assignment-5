import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

rect_x = 100
rect_y = 500
running = True

while running:
    ev = pygame.event.poll()
    print(ev.type)
    if ev.type == pygame.QUIT:
        running = False

    screen.fill([105,114,206])
    pygame.draw.rect(screen,[10,10,35],[rect_x, rect_y, 100,100])
    rect_x += 0.1

    pygame.display.flip()