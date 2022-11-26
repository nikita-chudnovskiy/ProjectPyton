# Определение Декорратора Это функуия которая принимает на вход другую функцию и возвращает функию

# Расширим возможности функуии say за счет вызова нашей вунку decorator

# Декораторы нужны чтобы в нашей функции добавилось новое поведение или новый функционал

def decorator(func):

    def inner(*args,**kwargs):  # Аргументы функции могут менятся при изм мы получим ошибку по этому *, **
        print('star decorator')
        func(*args,**kwargs)
        print('stop decorator')
    return inner


def say(name,surname,age):
    print('Првиет мир',name,surname,age) # наша функция отработает с 2 или 3 аргументами

def buy(age):
    print('buy hello',age)

# для изменения мы должны не какую по имени say сохранить результат вызова
#d =decorator(say)
say=decorator(say)

say('Vasya','Васильевич',30)
print('Она теперь содержит дополнительное поведение Которое мы назначили в нашем декораторе')
buy = decorator(buy)
buy(30)







