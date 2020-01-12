# ТИПЫ В PYTHON
print(type(1))                          # int
print(type(2.0))                        # float
name = 'Andrey'; print(type(name))      # str
status = True; print(type(status))      # boolS
print(max(1,2,3,4,5,abs(-56)))          # применяется abs потом max

# Округление # match.floor(), math.ceil(), math.ceil()
import math
a =5.65
print('Округление')
print(round(a)) # округление как в большую так и в меньшую 5.65 будет 6 (4.5 -будет 5)
print(math.floor(a)) # Округление в меньшую
print(math.ceil(a)) # Округление в большую сторону
print(math.pi) #Точнность ограничивается вещественным числом в PYTHON

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
print(len(x)) # len() узнать длинну строки