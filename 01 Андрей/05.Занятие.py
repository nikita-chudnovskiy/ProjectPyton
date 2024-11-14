print('Введите ваш выбор')
a = input()
print('Введите ваш выбор')
b = input()
if a == 'бумага':
    if b == 'камень':
        print('win:', 1)
    if b == 'ножницы':
        print('win', 2)
    if b == 'бумага':
        print('Ничья')
if a =='ножницы':
    if b =='камень':
        print('win', 2)
if a =='ножницы':
    if b =='бумага':
        print('win', 1)
if a == 'ножницы':
    if b == 'ножницы':
        print('Ничья')
if a == 'камень':
    if b == 'ножницы':
        print('win', 1)
if a =='камень':
    if b =='бумага':
        print('win', 2)
if a =='камень':
    if b =='камень':
        print('Ничья')