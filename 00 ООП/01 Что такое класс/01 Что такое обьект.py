# Что такое обьект в программировании

# Обьект это -контейнер состоящий из:
# 1 данных и состояния  будем называть атрибуты
# 2 поведение  -методы обьекта

# Обьекты (данные и поведение)
# Классы
# Экземпляры классов

# Класс  по сути шаблон при помощи которого мы будем создавать обьекты


class Point:

    color = "red"
    circle=2

Point.color='black'

print(Point.color,Point.circle)
print(Point.__dict__)
print(Point.__doc__)

a =Point()
b =Point()
print(a.color,b.color)
a.color='green' # в экземплярах класса поменял значение атрибутa

print(print(a.color,b.color))
print(a.__dict__) # в экземплярах класса поменял значение атрибутa

# ДОБАВИТЬ ДИНАМИЧЕСКИ АТРИБУТ
#Point.type_pt ='disc'
#print(Point.__dict__)
setattr(Point,'type_pt','disc')
print(Point.__dict__)
print(getattr(Point,'a',False)) # ВАЖНО будет возвр если указ атрибут не обнаружен
print(getattr(Point,'type_pt')) # ВАЖНО будет возвр если указ атрибут не обнаружен
