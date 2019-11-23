def add(x:int, y:"int>0")->int :  # (x:"int>0", y:"int>0")->int : : Если нам явно надо указать типы введения и условия
     """складывает x +y """
     return x + y
print(add(2,3))
print(add('2','3'))

print(add(str(1),add('2','3')))

def p3(x):
    print('Андрей')
    print('Вася')
    print(3+4)

x = p3('Hello')
print(type(x))
