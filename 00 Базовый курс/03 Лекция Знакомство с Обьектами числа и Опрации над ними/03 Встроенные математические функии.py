# ВСТРОЕННЫЕ МАТЕМАТИЧЕСКИЕ ФУНКЦИИ ПО РАБОТЕ С ЦЕЛЫМИ ЧИСЛАМИ
import math
from math import sqrt
print(abs(-7))  # отбрасывает знак
print(abs(-5 * 2))  # вначале выполнится действие потом отбросится знак
print(min(1, 2, 3, 4, 5))
print(max(1, 2, 3, 4, 5))
print(pow(2, 3))  # принимает 2 значения и возводит первое в степень второго
print(round(3.4))  # Округление по ум до целого числа
print(round(3.5))
print(round(3.456, 2))  # если хотим округлить по сотые то указываем 2
print(round(3.456, 1))  # по десятые , 1 число после ,
print(round(456, -1))  # Округление к 10
print(round(456, -2))  # Округление к 100

# Округление #  math.ceil(),match.floor(), в большую и в меньшую



print(math.pi)  # Точнность ограничивается вещественным числом в PYTHON
f = 25
print(sqrt(f), 'Корень')
print(math.factorial(f))


# ОПЕРАЦИИ НА МЕСТЕ
x = 2
x += 3;
print(x)  # / - * / % Возможно с другими операциями
x *= 3;
print(x)
x **= 3;
print(x)  # 15 в 3 степени

# Операции на месте могут применяться и к другим типам данных, например к строкам

x = 'spamm'
print(x)
x += 'egg'
print(x)
print(len(x))  # len() узнать длинну строки #
