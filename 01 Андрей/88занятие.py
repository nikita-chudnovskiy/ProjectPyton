import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 150
y = 400
sy = 0
p = 700
onground = True
while True:
    clock.tick(60)
    screen.fill([255,255,255])
    sy = sy+1
    y = y+sy
    if y > 400:
        onground = True
        y = 400
        sy = 0
    if y < 400:
        onground = False
    pygame.draw.circle(screen,[64,64,64],[x,y],30)
    pygame.draw.rect(screen,[0,0,0],[0,430,1000,20])
    pygame.draw.rect(screen, [0, 0, 0], [p, 300, 50, 130])
    p = p-6
    if p < - 50:
        p = 800
    if p < 250 and onground == True:
        sy = -20

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE and onground == True:
                sy = -20

    pygame.display.update()