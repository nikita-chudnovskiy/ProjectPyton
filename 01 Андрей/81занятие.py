# g = []
# for i in range(3):
#     a = int(input())
#     g.append(a)
# print(min(g),max(g))

import pygame
pygame.init()
scrin = pygame.display.set_mode([800,600])
color = [0,0,255]
timer = 200
while True:
    scrin.fill(color)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    timer = timer-1
    if timer == 0:
        timer = 1500
        if color == [0,0,255]:
            color = [255,0,0]
        else:
            color = [0,0,255]
    pygame.display.update()
