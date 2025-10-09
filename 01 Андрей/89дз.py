import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
v = 400
h = 300
s = False
w = False
a = False
d = False
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[0,0,255],[v,h],40)
    events = pygame.event.get()
    if w == True:
        h = h-6
    if s == True:
        h = h+6
    if a == True:
        v = v-6
    if d == True:
        v = v+6
    if v < 40:
        v = 40
    if v > 760:
        v = 760
    if h < 40:
        h = 40
    if h > 560:
        h = 560
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