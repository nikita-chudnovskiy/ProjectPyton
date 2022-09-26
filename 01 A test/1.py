def decor(func):
    def inner(*args,**kwargs):
        print('start')
        func(*args,**kwargs)
        print('finish')
    return inner


@decor
def say(name,surname,age):
    print('Првиет мир',name,surname,age) # наша функция отработает с 2 или 3 аргументами

say('Vasya','Ivanov',30)