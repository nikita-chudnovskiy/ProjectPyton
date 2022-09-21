def decorator(func):

    def inner():
        print('star decorator')
        func()
        print('stop decorator')
    return inner


def say():
    print('Првиет мир')

def buy():
    print('buy hello')

# для изменения мы должны не какую по имени say сохранить результат вызова
#d =decorator(say)
say=decorator(say)
print(say)
say()
print('Она теперь содержит дополнительное поведение Которое мы назначили в нашем декораторе')
buy = decorator(buy)
buy()


# Расширим возможности функуии say за счет вызова нашей вунку decorator
# Определение Декорратора Это функуия которая принимает на вход другую функцию и возвращает функию
# Декораторы нужны чтобы в нашей функции добавилось новое поведение или новый функционал


