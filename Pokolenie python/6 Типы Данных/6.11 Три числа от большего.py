# Так как у нас всего три числа, то можно найти наибольшее и наименьшее числа с помощью
# функций max(a, b, c) и min(a, b, c), а среднее число -- это разность
# суммы начальных чисел и найденных двух значений: a + b + c - max(a, b, c) - min(a, b, c).


a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a,b,c))
