import pygame
from pygame.cursors import sizer_x_strings

pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
ly = 100
bx = 400
by = 300
sx = 1
sy = 1
s = False
w = False
while True:
    clock.tick(120)
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[255,255,255],[25,ly,20,100])
    if w == True:
        ly = ly-3
    if s == True:
        ly = ly+3
    if ly <0:
        ly = 0
    if ly >500:
        ly = 500
    pygame.draw.circle(screen,[255,255,255],[bx,by],15)
    bx = bx+sx
    by = by+sy
    if by < 15:
        sy = -1*sy
    if by > 585:
        sy = -1*sy
    if bx > 785:
        sx = -1*sx
    if bx < 15:
        sx = -1*sx
    lbx = pygame.Rect(25,ly,20,100)
    bbx = pygame.Rect(bx-15,by-15,30,30)
    if lbx.colliderect(bbx):
        sx = -1*sx
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
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