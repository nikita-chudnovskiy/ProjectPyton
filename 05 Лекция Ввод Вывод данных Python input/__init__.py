name = (input())
if 'Nikita' in name:
    print('Success!')
else:
    print('No')


a = input('введите число')  # str
b = int(input('введите число'))  # int
c = float(input('введите число'))  # float

print(int(a) + b + int(c))

a, b = map(int, input('Введите 2 числа ').split())
print(a + b)

print(1, 2, 3, sep=',')
print(4, 5, sep='???', end=', ') # end не переводит на следующую строку 6
print(6, sep='123')  # Нужно как минимум 2 значения

rub = 10
kop = 99
print('У меня есть %s рублей %s копеек' % (rub, kop))
print('У меня есть {} рублей'.format(rub))

rub,kop = map(int,input().split())
print('Нам дали {} рублей {} копеек'.format(rub,kop))
