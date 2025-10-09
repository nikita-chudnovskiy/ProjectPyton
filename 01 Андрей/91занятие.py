import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,900])
clock = pygame.time.Clock()
balls = []
timer = 30
while True:
    clock.tick(60)
    screen.fill([255,105,180])
    timer = timer-1
    if timer == 0:
        timer = 30
        #Создание мячиков:
        x = random.randint(10,790)
        y = 10
        red = random.randint(15,255)
        green = random.randint(15,255)
        blue = random.randint(15,255)
        color = [red,green,blue]
        r = random.randint(20,30)
        ball = [x,y,color,r]
        balls.append(ball)

    #Рисование:
    for i in balls:
        pygame.draw.circle(screen,i[2],i[0:2],i[3])

    #Движение:
    for i in balls:
        i[1]+=3
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            for l in balls:
                bx = pygame.Rect(l[0]-l[3],l[1]-l[3],2*l[3],2*l[3])
                if bx.collidepoint(mpos):
                    balls.remove(l)
    pygame.display.update()