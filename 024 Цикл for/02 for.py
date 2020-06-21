from random import randint

n = int(input())  # вводим сколько чисел
s =0
for i in range(n):
    a =randint(1,100)       # случайных чисел randit от и до
    print(a,end=' ')
    s+=a              # сумма случайных чисел
print()
print(s)


for i in range(5): # при умножении строки на число строка повторяется  определенное количество раз
    print('*' * i)


for i in range(1,11): # первые 10 степеней двойки
    print(2**i)

s =0
n=int(input())
for i in range(n):
    a =int(input())
    s+=a
    print('current',s)
print('total summa',s)
print('srednee arifm =',s/n)