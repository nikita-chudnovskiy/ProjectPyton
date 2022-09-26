
# C:\\Python 3.10\\lib\\pprint.py'>,
# когда устанавливаете python то вместе с интепритатором ставится огромное количество этих модулей 3.10
# Стандартная библиотека модулей

import pprint # Стандартная библиотека модулей  https://docs.python.org/3.10/library/index.html
import calendar

#import math

import math as m # Дали псевдоним

from math import factorial,pi,e  # Указываем напрямую
from math import * # !!!! Используем все имена !!!!

def say():
    print('hello')
    age=30
    return age # В пространсво имен не попадут локальные переменные age

me_str ='beautiful'
my_nums =2
my_nums2 =3

pprint.pprint(locals())

c=calendar.TextCalendar()
print(c.formatyear(2022))
#pprint.pprint(dir(math))
pprint.pprint(dir(m))

# навести мышку зажать ctrl и провалится в него посмотреть что это переменная или клас или функция
# pprint.pprint(math.e) # переменная
# pprint.pprint(math.pi) # переменная
# pprint.pprint(math.factorial(5)) # функция

#pprint.pprint(m.e) # переменная
#pprint.pprint(m.pi) # переменная
#pprint.pprint(m.factorial(5)) # функция

pprint.pprint(e) # переменная
pprint.pprint(pi) # переменная
pprint.pprint(factorial(5)) # функция