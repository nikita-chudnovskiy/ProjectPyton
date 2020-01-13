# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
#math.sqrt(X) - квадратный корень из X.
# C в квадрате = a квадрате +b квадрате
import math
a,b = map(int,input().split())
c = pow(a,2)+pow(b,2)
#c = c **0.5
c = math.sqrt(c)
print(c)
