import turtle

turtle.speed(2)
def move(a,b):
     turtle.forward(a)
     turtle.left(90)
     turtle.forward(b)
     turtle.left(90)


def retangle(a,b,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        move(a,b)
    turtle.end_fill()



retangle(180,30,'silver')
turtle.goto(0,30)
retangle(180,30,'blue')
turtle.goto(0,60)
retangle(180,30,'red')




