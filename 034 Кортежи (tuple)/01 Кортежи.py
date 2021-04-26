# Кортеж -представляет собой неизменяемую последовательность
# Обычно используется для хранения разнотипных объектов

# Похож на список одна важная особенность Кортеж является не изменяемым объектом в отличии от списка !!!

# 'abc'     строки
# [1,2,3,]  Список
# {'key':1} Словарь
# (1,2,3,)  Кортеж

# 1 Способ
a =(1,2,3)
print(a,type(a))

# 2 Способ не явный
a =1,2,3

# 3 Способ
a = 1, # !!! Важно запятая, если ее убрать то будет целое число int


# СОЗДАНИЕ КОРТЕЖА
b =tuple(range(5)) # передаем итерабельную последовательность
print(b,type(b))

c =tuple([1,2,3])
print(c,type(c))
c =tuple((1,2,3))
print(c,type(c))
c =()
d =tuple()