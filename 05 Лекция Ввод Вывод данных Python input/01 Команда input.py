# 13.01.2020
# Найти Периметр
print('Найти Периметр')
a = input('введите число')        # str Ввести строку Строку
b = int(input('введите число'))   # int  Целое Число ВАжно !
c = float(input('введите число')) # float Вещественное число
perimetr=(int(a) + b + int(c)) # Преобразование типов к int
print(perimetr)

# 2 Вариант
a,b,c= map(int,input('3 числа').split())
perimetr = a+b+c
print(perimetr)

print(sum(map(int, input('Сумма всех введенных чисел ').split())))



# Проверяем есть ли в веденной строке имя Nikita
name = (input('Проверка имени '))
if 'Nikita' in name:
    print('Success!')
else:
    print('No')



