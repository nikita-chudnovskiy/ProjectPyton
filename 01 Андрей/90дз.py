import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
bx = 400
by = 300
sx = 1
sy = 1
while True:
    clock.tick(120)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[255,0,0],[bx,by],30)
    bx = bx+sx
    by = by+sy
    if by < 30:
        sy = -1*sy
    if by > 570:
        sy = -1*sy
    if bx > 770:
        sx = -1*sx
    if bx < 30:
        sx = -1*sx
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()