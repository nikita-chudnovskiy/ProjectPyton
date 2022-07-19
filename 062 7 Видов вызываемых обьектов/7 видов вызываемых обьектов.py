# Вызываемый обьект Это такой обьект к которому можно применить оператор вызова ()
# Проверить явл ли обьект вызываемым можно при помощи одноименной функции callable

a = -2
s = 'sddad'
# print(a()) целые числа не явл вызываемыми
# print(s()) строки тоже не явл вызываемыми

# 1 Встроенные функции

print(abs(a))
print(len(s))

# 2 свои встроенные методы

a = [2, 1, 3, ]

a.sort()
print(a)


# 3 Самописные функции

def f():
    print('Heloo world')


f()

d = lambda: 'hi'
d()  # lyambda возвращает значение функции в отличии от функции f
print(d())
print(callable(f))
print(callable(d))


# 4 Классы

class Cat:
    pass


bob = Cat()
print(bob)
print(callable(Cat))
print(callable(bob))

# 5 Экземпляры класса если есть метод ___cal


class Cat:
    def __call__(self, *args, **kwargs):
        print('may')


bob = Cat()
print(bob)
print(callable(Cat))
print(callable(bob))
bob()


# 6 Методы класса


class Cat:
    def __call__(self, *args, **kwargs):
        print('may')

    def say_hallo(self):
        print('hallo')

bob = Cat()
print(bob)
print(callable(Cat))
print(callable(bob))
bob()
print(callable(bob.say_hallo))


# 7 Функции Генераторы

def ff():
    n =0
    while True:
        yield n
        n+=1
print(callable(ff))