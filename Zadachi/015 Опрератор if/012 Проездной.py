# В единственной строке через пробел записано четыре целые числа n, m, a, b
# (1 ≤ n, m, a, b ≤ 1000) — количество проездов,
# запланированное Аней, количество проездов, которое покрывает абонемент, цена одного проезда и цена одного абонемента.

# n 6 - количество проездов Запланировала Аня
# m 2 - количество проездов, которое покрывает абонемент
# a 1 - цена одного проезда
# b 2 - цена одного абонемента.
# Выведите целое число — минимальную сумму в рублях, которую Ане придется потратить.
n,m,a,b = map(int,input().split())

n1 = n * a       # цена по поездкам
n2 = b * n // m  # Цена по абонементу
# print(min(n1,n2)) если ввести 7 поездок то мин сумм будет 7

if n1<=n2:
    print(n1) # за деньги
else:
    print(n2) # по абонементу дешевле
print(n1,n2)

