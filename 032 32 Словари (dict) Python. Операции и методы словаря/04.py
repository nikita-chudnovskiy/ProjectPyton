# Удаляем ключ

d ={
    1: 'One',
    2: 'two',
    3: 'three'

}
del d[1]
print(d)

print(len(d))

print(2 in d, 5 in d, 7 not in d) # ПРоверить есть ли ключи в словаре   2 есть 5 нет , нет ли 7 да 7 нет


d ={
    1: 'One',
    2: 'two',
    3: 'three',
    4:'four'

}

# если 5 есть вывести если нет то создастся
if 5 in d:
    print(d[5])
else:
    d[5] ='five'
print(d)

# print()
# print()
# print()
# print()

for key in d:
    print(key,d[key])