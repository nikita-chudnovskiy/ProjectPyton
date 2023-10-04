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

Point.color='black'

print(Point.color)
print(Point.circle)
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


print()
# ДОБАВИТЬ ДИНАМИЧЕСКИ АТРИБУТ
#Point.type_pt ='disc'
#print(Point.__dict__)
setattr(Point,'type_pt','disc')

print("sdadasdasdadasdasdas")

print(Point.__dict__)
print(getattr(Point,'a',False)) # ВАЖНО будет возвр если указ атрибут не обнаружен
print(getattr(Point,'type_pt')) # ВАЖНО будет возвр значение если его нет то выдаст ошибку тк проверки нет на False
Point.ttt='123'
print(Point.ttt)
print(Point.__dict__)
del Point.ttt
print(Point.__dict__)
print(hasattr(Point,'color')) # Проверяет на наличие атрибута
print('SSSSSSSSSSSSSS')

a.x =1
a.y =5
b.x =2
print(a.x, a.y)
print(a.__doc__)
print(a)
