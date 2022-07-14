from random import randint

for i in range(5):
    a = randint(1, 10)
    b = randint(ord('A'), ord('z'))
    c = randint(ord('#'), ord('*'))
    print(a, chr(b), chr(c), end='', sep='')
zzz = int(input())

while True:
    print('  Нажмите от 1 до 9 Если Вам нужно выйти нажмите 10 ')
    n = 5
    zzz = int(input())
    if zzz < 10:

        for i in range(n):
            a = randint(1, 10)
            b = randint(ord('A'), ord('z'))
            c = randint(ord('#'), ord('*'))
            print(a, chr(b), chr(c), end='', sep='')
    elif zzz == 10:
        break
