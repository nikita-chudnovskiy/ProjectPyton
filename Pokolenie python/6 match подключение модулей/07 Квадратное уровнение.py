from math import *

a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    print('Нет корней')
