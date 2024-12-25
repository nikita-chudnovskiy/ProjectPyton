from math import sqrt

a, b = float(input()), float(input())

print((a + b) / 2)  # Среднеарифметическое
print(sqrt(a * b))  # среднее геометрическое чисел
print(((a * b) * 2) / (a + b))  # среднее гармоническое чисел
print(sqrt((pow(a, 2) + pow(b, 2)) / 2)) # Среднеквадратичное
