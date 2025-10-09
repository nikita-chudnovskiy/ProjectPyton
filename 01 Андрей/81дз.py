import pygame
import time
pygame.init()
ekran = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    pygame.draw.circle(ekran,[255,255,255],[30,30],30)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
    pygame.display.update()