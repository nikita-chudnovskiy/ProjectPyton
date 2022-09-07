def main_func(name):
    #name = value
    def inner_func():
        print('Hello my friend',name)
    return inner_func
a =main_func('Misha') # переменная а будет являтся теперь самой функцией
v =main_func('Fedya')
print(a)
a()
v()


# В этом примере мы исп значение которое поступает на вход функции но мы их никак не меняем
def one(value):  # Принимает значение 5 и каждый раз как вызываем будем прибавлять уже 5
    def twho(a):
        return value+a
    return twho
c =one(5)
b =one(6)
print(c(5))
print(b(6))


def counter():
    count = 0
    def inner():
        nonlocal count
        count+=1
        return count
    return inner
q =counter()
c =counter()
print(q())
print(q())
print(q())
print(q())
print(q())
print(c(),' С 1 тк другая переменная') # !!!!!!! с 1 тк другой переменной