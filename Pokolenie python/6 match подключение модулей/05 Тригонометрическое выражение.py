from math import sin, cos, tan, radians
# x = float(input()) * pi / 180 # В синус косинус танг нужно исп уже в радианах
x = radians(float(input()))
a = (sin(x)) + (cos(x)) + pow(tan(x),2)
print(a)
