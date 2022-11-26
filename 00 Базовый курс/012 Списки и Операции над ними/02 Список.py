# Объект в списке ищется по индексу

# показать первый элемнт списка - это будет под индексом 0
my_list =[1,2,3,'hello']
print(my_list[0])

# добавиить в конец списка
my_list.append(4)
print(my_list)

# вставить в 5 индекс 99
my_list.insert(5,99) #
print(my_list)

# Удалить под пятым индексом
del my_list[5]
print(my_list)

# Удалить первый встреч элемент под цифрой 2
my_list.remove(2)
print(my_list)


# Списки можно складывать
my_list2 = [1,2,3]
my_list2=my_list2+[4,5,6]
print(my_list2)


# Можно умножать
my_list2=my_list2*2
print(my_list2)

# В список можно вставлять переменную
car = 'Тойота'
my_list3 =['audi',car]
print(my_list3)

# Создать список списков найдем средний элемнт найди меня его индексы будут [1][1]
matrix = [[1,2,3],[4,'найди меня',6],[7,8,9]]
print(matrix[1][1])


a =[1,2,3]
print(1 in a)