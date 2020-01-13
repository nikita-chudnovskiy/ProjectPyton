# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
#math.sqrt(X) - квадратный корень из X.
# C в квадрате = a квадрате +b квадрате
# Входные 3 и 4   Ввыходные 5.0
import math
a,b = map(int,input().split())
c = pow(a,2)+pow(b,2)
#c = c **0.5
c = math.sqrt(c)
print(c)

# Катеты ищем a
b,c = map(int,input().split())
a =c**2-b**2
print(math.sqrt(a)) # Корень из a

# Катеты ищем b
b,c = map(int,input().split())
b =c**2-c**2
print(math.sqrt(b)) # Корень из b