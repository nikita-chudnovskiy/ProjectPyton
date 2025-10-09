import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
a = False
d = False
x = 10
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    if a == True:
        x = x-5
    if d == True:
        x = x+5
    if x < 0:
        x = 0
    if x > 760  :
        x = 760
    pygame.draw.rect(screen,[255,255,255],[x,570,40,30])
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                a = True
            if i.key == pygame.K_d:
                d = True
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                a = False
            if i.key == pygame.K_d:
                d = False
    pygame.display.update()