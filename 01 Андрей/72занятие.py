import pickle
import os

if os.path.exists('balanse.txt'):
    f = open('balanse.txt','rb')
    d = pickle.load(f)
    f.close()
else:
    d = 100

while True:
    g = input()
    if g == 'баланс':
        print('Ваш баланс:',d)
    if g == 'снять':
        h = int(input('Введите сумму: '))
        d = d-h
        print('Осталось на балансе: ',d)
    if g == 'внести':
        w = int(input('Введите сумму: '))
        d = d+w
        print('Текущий баланс:',d)
    if g == 'стоп':
        f = open('balanse.txt','wb')
        pickle.dump(d,f)
        f.close()
        break