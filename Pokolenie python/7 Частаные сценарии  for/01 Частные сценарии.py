# Подсчет количества
# Вычисление суммы и произведения
# Обмен значений переменных
# Сигнальные метки
# Определение максимума и минимума
# Расширенные операторы присваивания (+=, -=, //= и т.д.)
from subprocess import check_output

#
# counter = 0
# for i in range(1, 11):
#     n = int(input())
#     if n > 10:
#         counter += 1
# print(counter)  # Больше 10

# counter1 = 0
# counter2 = 0
# for i in range(1, 11):
#     n = int(input())
#     if n > 10:
#         counter1 += 1
#     elif n == 0:
#         counter2 += 1
# print(counter1)  # Больше 10
# print(counter2)  # = 0

# counter = 0
# for i in range(1, 100):
#     if i**2 % 10 == 4:
#         print(i, i**2)
#         counter = counter + 1
# print(counter)


total = 0
for i in range(1, 5 + 1):
    total += i
print(total)

total = 0
for i in range(1, 5 + 1):
    num = int(input())
    total += num
print(total)
