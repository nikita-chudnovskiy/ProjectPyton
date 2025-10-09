import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
x = 400
y = 300
while True:
    clock.tick(60)
    screen.fill([0,0,0])
    pygame.draw.circle(screen,[200,200,0],[x,y],20)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            x = mpos[0]
            y = mpos[1]
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()
