import random

m =3
n =3

a= [[random.randint(1,3)  for i in range(m)] for j in range(n)]

for i in a:
    print(i)

print()

d =[a[i][2] for i in range(n)]
c =[a[0][i] for i in range(m) if a[0][i] ==3] # Покажет все 3



print(d,'3 столбец по вертикали')
print(c,'1 столбец по горизонтали')


