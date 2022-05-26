def fact(n):
    pr = 1
    c = []

    for i in range(1, n + 1):
        pr = pr * i
        c.append(pr)
    return c


print(fact(10))


# Ниже код Выполнится в десятки раз быстрее и не будет хранить объекты в памяти !!!

def factN(n):
    pr = 1

    for i in range(1, n + 1):
        pr = pr * i
        yield pr


for i in factN(10):
    print(i, end=' ')
