d ={
    1: 'One',
    2: 'two',
    3: 'three',
    4:'four'

}

print(d)
# d.clear()  очистить словарь
print(d)

print(d.get(1)) # Выведет значение
print(d.get(5)) # если ключа нет то вернет None
print(d.get(5,'No such key')) # Важно могу изменить поведение если ключа нет, передать параметр какой хотим  (No such key)

# Создается ключ 6, а если хотим добавить значение то пишем [ Только тогда , когда еще нет ключа]
d.setdefault(6)
d.setdefault(7,'seven')
d.setdefault(2,'seven')
print(d)

# Метод pop вернет значение но удалит элемент
print()
print(d)
print(d.pop(1))
print(d)

# Удалит рандомное значение - неупорядоченное
print(d.popitem())
print(d.popitem())

# Получить все ключи словаря
print(d.keys())

# Вернуть все значения словаря
print(d.values())
for i in d:
    print(d[i])

print(d.values())
for values in d.values(): # Вывести в цикле for
    print(values)

# d.items  возращает коллекцию где содержатся все пары ключ - значение
print(d.items())

for para in d.items():  # Вывести в цикле for
    print(para)

# Можно передать и ключ и значение Важно Сразу 2 параметра !!!!
for key,value in d.items():  # Вывести в цикле for
    print(key,value)
