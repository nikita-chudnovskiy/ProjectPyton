
# ВСТРОЕННЫЕ МАТЕМАТИЧЕСКИЕ ФУНКЦИИ ПО РАБОТЕ С ЦЕЛЫМИ ЧИСЛАМИ

print(abs(-7))          # отбрасывает знак
print(abs(-5*2))        # вначале выполнится действие потом отбросится знак
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))
print(pow(2,3))         # принимает 2 значения и возводит первое в степень второго
print(round(3.4))       # Округление по ум до целого числа
print(round(3.5))
print(round(3.456,2))   # если хотим округлить по сотые то указываем 2
print(round(3.456,1))   # по десятые , 1 число после ,
print(round(456,-1))    # Округление к 10
print(round(456,-2))    # Округление к 100


# Округление # match.floor(), math.ceil(), math.ceil()

# Если нажать math.  то выведится весь список функций (sqrt, cos, и т д cil)

# Если остальные функции не нужны из модуля то можно написать так
# from math import  sqrt и тогда будет только sqrt

import math   # from math import sqrt
a =5.65
print('Округление')
print(round(a)) # округление как в большую так и в меньшую 5.65 будет 6 (4.5 -будет 5)
print(math.floor(a)) # Округление в меньшую
print(math.ceil(a)) # Округление в большую сторону
print(math.pi) #Точнность ограничивается вещественным числом в PYTHON
f =25
print(math.sqrt(f),'Корень')
print(math.factorial(f))


# Отрицательные числа  минус на - дает +

i = (-7 + 2) * (-4)
print(i)
# i = i/0; print(i) # division by zero  на 0 делить нельзя

i= 9.86500; print(i)    #9.865   # НУЛИ ОТБРАСЫВАЮТСЯ  Помним об ЭТОМ часто приводит к ошибкам
i = 6 * 7; print(i)     #42
i = 4 + 1.65; print(i)  #5.65

# ОПЕРАЦИИ НА МЕСТЕ
x = 2
x += 3;  print(x)       #  / - * / % Возможно с другими операциями
x *= 3;  print(x)
x **= 3; print(x)       # 15 в 3 степени

# Операции на месте могут применяться и к другим типам данных, например к строкам

x = 'spamm'
print(x)
x += 'egg'
print(x)
print(len(x)) # len() узнать длинну строки #
