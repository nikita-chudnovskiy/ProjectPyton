q = 200
while True:
    w = input('> ')
    if w == 'append':
        g = int(input('Введите сумму: '))
        q = q+g
        print('Текущий баланс:',q)
    if w == 'use':
        l = int(input('Введите сумму: '))
        q = q-l
        print('Текущий баланс:',q)
    if w == 'print':
        print('Баланс:',q)
    if w == 'exit':
        break