a = 2
b = 5
tmp = a
a = b
b = tmp  # Через переменную tmp поменяли местами

x = 2
y = 5

tmp1 = y  # Меняем местами через 2 переменные
tmp2 = x
x = tmp1
y = tmp2

# Каскадное

x = y = z = 0;
print(x, y, z)
# Множественное
a, b, c = 1, 2, 3;
print(a, b, c)

a = 2;
b = 5;
print(a, b)

a, b = b, a;
print(a, b)
