print(1, 2, 3, sep=',') # sep разделитель разделяет запятой
print(4, 5, sep='???', end=',') # sep разделяет ??? end (не  переводит на следующую строку 6)
print(6, sep='123')  # Нужно как минимум 2 значения

rub = 10
kop = 99
print('У меня есть %s рублей %s копеек' % (rub, kop))
print('У меня есть {} рублей'.format(rub))

rub,kop = map(int,input().split())
print('Нам дали {} рублей {} копеек'.format(rub,kop))