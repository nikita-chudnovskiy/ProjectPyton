# a = input('Введите строку: ')
# for i in a:
#     if i in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
#         print(i,end='')

# b1 = 0
# b2 = 0
# b3 = 0
# b4 = 0
# b5 = 0
# b6 = 0
# for i in range(10):
#     from random import randint
#     a = randint(1,6)
#     if a == 1:
#         b1 = b1+1
#     if a == 2:
#         b2 = b2+1
#     if a == 3:
#         b3 = b3+1
#     if a == 4:
#         b4 = b4+1
#     if a == 5:
#         b5 = b5+1
#     if a == 6:
#         b6 = b6+1
# print(b1,b2,b3,b4,b5,b6)

a = ['яблоко','банан','апельсин','груша','виноград','киви']
from random import randint
b = randint(0,5)
word = a[b]
kol_vo_bukv = len(word)
g = []
for i in range(len(word)):
    g.append('-')
while True:
    print('Текущее слово: ',*g)
    d = input('Введите букву: ')
    if d not in word:
        print('Такой буквы нет.')
    if d in word:
        f = 0
        for i in word:
            if i == d:
                g[f] = d
            f = f+1