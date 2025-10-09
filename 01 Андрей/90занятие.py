import pygame
import math
import random
w = False
s = False
x = 20
y = 50
v = 15
vx = 0
vy = 0
gravity = 0.1
angle = 0
pygame.init()
screen = pygame.display.set_mode([1500,900])
clock = pygame.time.Clock()
pushka = pygame.image.load('C:/Project/01 Андрей/images/пушка.png')
pushka = pygame.transform.scale(pushka,[840//2,336//2])
while True:
    clock.tick(60)
    screen.fill([255,255,255])
    pygame.draw.rect(screen,[66,18,8],[0,800,1500,100])
    pygame.draw.rect(screen, [0,255,0], [0, 775, 1500, 25])
    newpushka = pygame.transform.rotate(pushka,angle)
    screen.blit(newpushka,[-150+210-newpushka.get_width()//2,627+84-newpushka.get_height()//2])
    pygame.draw.circle(screen, [255, 0, 0], [x, y], 20)
    x = x+vx
    vy = vy+gravity
    y = y+vy
    events = pygame.event.get()
    if w == True:
        angle = angle+1
    if s == True:
        angle = angle-1
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                x = -150+210-newpushka.get_width()//2
                y = 627+84-newpushka.get_height()//2
                vx = v*math.cos(angle*math.pi/180)
                vy = -v*math.sin(angle*math.pi/180)
            if i.key == pygame.K_w:
                w = True
            if i.key == pygame.K_s:
                s = True
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                w = False
            if i.key == pygame.K_s:
                s = False
    pygame.display.update()