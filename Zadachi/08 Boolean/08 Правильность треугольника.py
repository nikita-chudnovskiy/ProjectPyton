# Треугольник правильный?
# Задача под вопросом проверить
x,y,z = map(int,input('Введите 3 числа делятся ли они на 7 и 4 ').split())
print(x % 7 == 0 or y % 7 == 0 and 7 % 4 == 0)