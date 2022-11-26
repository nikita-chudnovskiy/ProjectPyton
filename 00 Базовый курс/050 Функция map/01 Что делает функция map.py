# Функуия map применяется ко всем итерируемым обьектам в списке

# map (func , iterables) ---> map object
a =[-2,-3,-4,5]
b = map(abs,a)

# map object
print(b)    # map object

b = list(map(abs,a))
print(b)

print('Циклом for')
a =[-2,-3,-4,5]
for i in a:
    i =abs(i)
    print(i,end=" ")
print()
print('Генератором')
# Генератор
a =[-2,-3,-4,5]
c =[abs(i) for i in a]
print(c)

# список превратили в строку
print('-'.join([str(i) for i in c]))