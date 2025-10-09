import pygame
from pygame.cursors import sizer_x_strings
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
a = False
d = False
while True:
    clock.tick(120)
    screen.fill([0,0,0])
    if a == True:
        pygame.draw.rect(screen,[0,0,255],[100,200,200,200])
    if a == False:
        pygame.draw.rect(screen,[255,0,0], [100,200,200,200])
    if d == True:
        pygame.draw.rect(screen,[0,0,255],[500,200,200,200])
    if d == False:
        pygame.draw.rect(screen,[255,0,0],[500,200,200,200])
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