import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 400
y = 300
b = 50
w = False
s = False
color = [255, 0, 0]
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,color,[x,y],b)
    events = pygame.event.get()
    if w == True:
        b = b+1
    if s == True:
        b = b-1
    for i in events:
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                w = False
            if i.key == pygame.K_s:
                s = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                w = True
            if i.key == pygame.K_s:
                s = True
            if i.key == pygame.K_SPACE:
                    if color == [255, 0, 0]:
                        color = [0, 0, 255]
                    else:
                        color = [255, 0, 0]
        if i.type == pygame.QUIT:
            exit()
        pygame.display.update()