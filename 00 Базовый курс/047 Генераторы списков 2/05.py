import random

name = ['Вася','Петя','Андрей']
d = ['гулял','играл','плакал','бесился']

z = [name,d]
print(z)

l =[random.choice(i)  for i in z]
print(l)



b = [random.randint(1,10)  for i in range(5) ]
print(b)
print(random.sample(b,3))
