# Что такое обьект в программировании

# Обьект это -контейнер состоящий из:
# 1 данных и состояния  будем называть атрибуты
# 2 поведение  -методы обьекта

# Обьекты (данные и поведение)
# Классы
# Экземпляры классов

# Класс  по сути шаблон при помощи которого мы будем создавать обьекты


class Point:
    "Класс для предоставления Координат"
    color = "red"
    circle=2

Point.color='black' # Изменили значение атрибута

print(Point.color) # Вывели значение атрибутов
print(Point.circle)
print()
print(Point.__doc__) # Содержит строку с описанием класса
print()
print(Point.__dict__) #Просмотреть атрибуты класса

print()
a =Point()
b =Point()
print(a)
print(a.color,b.color)
a.color='green' # в экземплярах класса поменял значение атрибутa

print(a.color)
print(b.color)
print(a.__dict__) # в экземплярах класса поменял значение атрибутa


print("# ДОБАВИТЬ ДИНАМИЧЕСКИ АТРИБУТ")
# ДОБАВИТЬ ДИНАМИЧЕСКИ АТРИБУТ
#Point.type_pt ='disc'

setattr(Point,'type_pt','disc') # Добавить атрибут со значением
print(Point.__dict__)
print(getattr(Point,'a',False)) # ВАЖНО будет возвр если указ атрибут не обнаружен
print(getattr(Point,'type_pt')) # ВАЖНО будет возвр значение если его нет то выдаст ошибку тк проверки нет на False
print(hasattr(Point, 'type_pt'))  # Проверяет на наличие атрибута
delattr(Point, 'type_pt')  # Удаляет атрибут
print('Удалили атрибут type_pt')
print(Point.__dict__)


print()
Point.ttt='123'
print(Point.__dict__)
del Point.ttt

print()

a.x =1
a.y =5
b.x =2
print(a.x, a.y)
print(a.__doc__)
print(a)
