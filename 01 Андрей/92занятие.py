from turtledemo.forest import randomfd

import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,900])
clock = pygame.time.Clock()
balls = []
def buildball():
    k = random.randint(15,25)
    c = random.randint(15,785)
    r = random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    color = [r,g,b]
    ball = [c,15,color,k]
    balls.append(ball)
def render():
    for i in balls:
        pygame.draw.circle(screen,i[2],[i[0],i[1]],i[3])
def update():
    for i in balls:
        i[1] = i[1]+1
while True:
    clock.tick(60)
    screen.fill([255,105,180])
    p = random.randint(1,20)
    if p == 1:
        buildball()
    render()
    update()
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()