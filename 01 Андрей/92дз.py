import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 150
y = 100
b = 60
v = 80
w = False
s = False
a = False
d = False
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[255,0,0],[x,y],20)
    pygame.draw.circle(screen, [0, 0, 255],[b,v],20)
    if b < x:
        b = b+2
    if b > x:
        b = b-2
    if v < y:
        v = v+2
    if v > y:
        v = v-2
    if w == True:
        y = y-4
    if s == True:
        y = y+4
    if a == True:
        x = x-4
    if d == True:
        x = x+4
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