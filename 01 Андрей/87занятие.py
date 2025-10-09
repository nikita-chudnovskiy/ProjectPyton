import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 400
y = 300
w = False
a = False
s = False
d = False
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[255,255,255],[x,y],20)
    if d == True:
        x = x+2
    if a == True:
        x = x-2
    if s == True:
        y = y+2
    if w == True:
        y = y-2
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                w = True
            if i.key == pygame.K_a:
                a = True
            if i.key == pygame.K_s:
                s = True
            if i.key == pygame.K_d:
                d = True
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                w = False
            if i.key == pygame.K_a:
                a = False
            if i.key == pygame.K_s:
                s = False
            if i.key == pygame.K_d:
                d = False
    pygame.display.update()
