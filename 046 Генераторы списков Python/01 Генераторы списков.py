import random
# Все генераьторы списков строятся по следующему шаблону
# [ выражение for val in Коллекция]
a = [0 for i in range(7)]
print(a)
a = [i for i in range(1,15)]
print(a)

a = [i**2 for i in range(1,15)]
print(a)

a = [i %4 for i in range(1,15)]
print(a)


a = [i for i in 'hello']
print(a)

a = [i*5 for i in 'hello']
print(a)


a = [random.randint(-10,10) for i in range(10)]
print(a)


# Можем также генератором обходить элементы другого списка

b =[abs(i)+1 for i in a] # Можем убрать минусы и увеличить на 1 
print(b)