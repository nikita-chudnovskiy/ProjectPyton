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


print(1, 2, 3, sep=',') # разделитель запятой
print(4, 5, sep='???', end=', ') # end не переводит на следующую строку 6
print(6, sep='123')  # Нужно как минимум 2 значения

rub = 10
kop = 99
print('У меня есть %s рублей %s копеек' % (rub, kop))
print('У меня есть {} рублей'.format(rub))

rub,kop = map(int,input().split())
print('Нам дали {} рублей {} копеек'.format(rub,kop))
