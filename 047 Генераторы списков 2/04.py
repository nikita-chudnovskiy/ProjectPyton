import random

m =3
n =5

a= [[random.randint(1,8)  for i in range(m)] for j in range(n)]

for i in a:
    print(i)

print()

d =[a[i][2] for i in range(n)]
c =[a[0][i] for i in range(m)]



print(d,'3 столбец по вертикали')
print(c,'1 столбец по горизонтали')


