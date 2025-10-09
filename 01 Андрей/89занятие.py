import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 400
y = 300
timer = 60
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    timer = timer-1
    if timer == 0:
        x = random.randint(0,800)
        y = random.randint(0,600)
        timer = 30
    pygame.draw.circle(screen,[255,0,0],[x,y],30)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()