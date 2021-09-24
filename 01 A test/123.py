import math

c,d = map(int, input('Ввести 2 числа через пробел ').split())  # ввести 2 числа

def kvadrat_Chisla(a,b):
    print('Квадрат числа',math.sqrt(a),' ',math.sqrt(b))


kvadrat_Chisla(c,d)