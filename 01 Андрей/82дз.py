import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 400
y = 300
mr = False
ml = False
ms = False
mw = False
while True:
    clock.tick(120)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[200,200,0],[x,y],30)
    if mr == True:
        x = x+1
    if ml == True:
        x = x-1
    if ms == True:
        y = y+1
    if mw == True:
        y = y-1
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                mw = True
            if i.key == pygame.K_s:
                ms = True
            if i.key == pygame.K_a:
                ml = True
            if i.key == pygame.K_d:
                mr = True
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                mw = False
            if i.key == pygame.K_s:
                ms = False
            if i.key == pygame.K_a:
                ml = False
            if i.key == pygame.K_d:
                mr = False
    pygame.display.update()