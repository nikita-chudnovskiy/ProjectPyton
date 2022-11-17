import random

name = ['Вася','Петя','Андрей']
d = ['гулял','играл','плакал','бесился']

z = [name,d]

l =[random.choice(i)  for i in z]
print(l)
