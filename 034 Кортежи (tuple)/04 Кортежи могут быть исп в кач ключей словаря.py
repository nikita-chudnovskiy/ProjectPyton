# Кортежи могут быть исп в кач ключей ключей словаря

a = (1, 2, 3)
b = {}
b[a] = 100

c = [1, 2, 3]
# b[c]='hi'   ключами словаря могут быть только не изменяемые объекты
print(b)
print()
# ЕСЛИ МЫ ХОТИМ ИЗМЕНИТЬ ЭЛЕМЕНТЫ В НУТРИ КОРТЕЖА ТО ПЕРЕВОДИМ В СПИСОК И ОБРАТНО

a = tuple((1, 2, 3,))
a =list(a)
print(a)
a.append(100)
a.reverse()
print(a)
a=tuple(a)

print(a)

for i in a:
    print(i)

print()

for i in range(len(a)):
    print(a[i])

