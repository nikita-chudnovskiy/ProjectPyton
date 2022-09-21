def header(func):

    def inner(*args,**kwargs):  # Аргументы функции могут менятся при изм мы получим ошибку по этому *, **
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')
    return inner

def table(func):

    def inner(*args,**kwargs):  # Аргументы функции могут менятся при изм мы получим ошибку по этому *, **
        print('<table>')
        func(*args,**kwargs)
        print('<table>')
    return inner

# Навешивание декораторов !!!
@table
@header #say = header(say)

def say(name,surname,age):
    print('Првиет мир',name,surname,age) # наша функция отработает с 2 или 3 аргументами







say('Vasya','Ivanov',30)
