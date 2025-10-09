import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 400
y = 300
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[255,0,0],[x,y],25)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    for i in events:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                x = random.randint(25, 775)
                y = random.randint(25, 575)
    pygame.display.update()