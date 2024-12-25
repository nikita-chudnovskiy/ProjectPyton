from math import pow, sqrt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

distance = sqrt(pow(x1 - x2, 2) + (pow(y1 - y2, 2)))
print(distance)
