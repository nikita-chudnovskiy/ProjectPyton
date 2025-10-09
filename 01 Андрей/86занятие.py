# import pygame
# pygame.init()
# screen = (pygame.display.set_mode([800,600]))
# clock = pygame.time.Clock()
# while True:
#     clock.tick(60)
#     mx = pygame.mouse.get_pos()[0]
#     my = pygame.mouse.get_pos()[1]
#     pygame.draw.circle(screen,[200,0,0],[mx,my],10)
#     events = pygame.event.get()
#     for i in events:
#         if i.type == pygame.KEYDOWN:
#             if i.key == pygame.K_SPACE:
#                 screen.fill([0,0,0])
#         if i.type == pygame.QUIT:
#             exit()
#     pygame.display.update()

import pygame
pygame.init()
screen = (pygame.display.set_mode([800,600]))
clock = pygame.time.Clock()
x = 400
y = 300
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]
    if mx > x:
        x = x+5
    if mx < x:
        x = x-5
    if my > y:
        y = y+5
    if my < y:
        y = y-5
    pygame.draw.circle(screen,[200,0,0],[x,y],10)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()