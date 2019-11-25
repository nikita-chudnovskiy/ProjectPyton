import turtle
#Команда	Значение
#forward(X)	Пройти вперёд X пикселей
#backward(X)	Пройти назад X пикселей
#left(X)	Повернуться налево на X градусов
#right(X)	Повернуться направо на X градусов
#penup()	Не оставлять след при движении
#pendown()	Оставлять след при движении
#shape(X)	Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
#stamp()	Нарисовать копию черепахи в текущем месте
#color()	Установить цвет
#begin_fill()	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
#end_fill()	Вызвать после окончания рисования фигуры
#width()	Установить толщину линии
#goto(x, y)	Переместить черепашку в точку (x, y)
turtle.shape('turtle')
i = 0
while i <= 3:
    i+=1
    turtle.forward(80)
    turtle.left(90)


turtle.penup()

turtle.goto(50, 10)
turtle.pendown()

turtle.begin_fill()
turtle.color('red')
turtle.shape('turtle')
turtle.left(90)
turtle.forward(10)

i = 0
while i <= 35:
    i+=1
    turtle.left(10)
    turtle.forward(10)



turtle.penup()

turtle.goto(6, 6)
turtle.pendown()
turtle.shape('turtle')




