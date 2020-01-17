# A. Выражение (1,2,3) (2,10,3) Найти максимальное из разных комбинаций числа менять нельзя
a, b, c = map(int, input().split())
x1 = a + b + c
x2 = a + b * c
x3 = a * b + c
x4 = (a + b) * c
x5 = a * (b + c)
x6 = a * b * c
print(max(x1, x2, x3, x4, x5, x6))