import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 50
y = 100
w = False
s = False
a = False
d = False
while True:
    clock.tick(120)
    screen.fill([255,255,255])
    pygame.draw.circle(screen,[255,0,0],[x,y],15)
    pygame.draw.rect(screen, [0, 0, 255], [300, 200, 35, 35])
    if w == True:
        y = y-1
    if s == True:
        y = y+1
    if a == True:
        x = x-1
    if d == True:
        x = x+1
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                w = True
            if i.key == pygame.K_s:
                s = True
            if i.key == pygame.K_a:
                a = True
            if i.key == pygame.K_d:
                d = True
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                w = False
            if i.key == pygame.K_s:
                s = False
            if i.key == pygame.K_a:
                a = False
            if i.key == pygame.K_d:
                d = False
    pygame.display.update()