from random import randint

# for i in range(5):
#     a = randint(1, 10)
#     b = randint(ord('A'), ord('z'))
#     c = randint(ord('#'), ord('*'))
#     print(a, chr(b), chr(c), end='', sep='')
# zzz = int(input())
count =0
while True:

    count +=1
    n = int(input('Задайте количество символов'))

    for i in range(n):
         a = randint(1, 10)
         b = randint(ord('A'), ord('z'))
         c = randint(ord('#'), ord('*'))
         print(a, chr(b), chr(c), end='', sep='')
    if count ==5:
        break