import pprint
class Person():
    name='Ivan'
    age = 30
    print(f'{name} {age}')
print(Person.__dict__) # Посмотреть все атрибуты


# Значение атрибута указывать строкой ( третий параметр поможет избежать error !)
print(getattr(Person,'age')) # если нет атрибута можно написать что нам возвращать
print(getattr(Person,'x',100)) # если нет атрибута можно написать что нам возвращать
print(getattr(Person,'name',200)) # Вернет имя тк атрибут есть !!!

a=Person()
print(a)