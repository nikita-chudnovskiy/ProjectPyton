
# Генератор списка
a =[i**2 for i in range(1,6)]
print(a)

# Выражения генератор               !!! Генератор представляет итератор элем которого можно обойти только 1 раз !!!
c =(i**2 for i in range(1,6))       #### Итератор обьект который поддерж функцию next


print(sum(c)) # генераторы можно Обойти только 1 раз Элементы генератора не хранятся в памяти все вместеa
print(sum(c))
for i in c:
    print(i)


print(c)


print(list(c))
