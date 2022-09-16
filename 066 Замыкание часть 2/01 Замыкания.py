#Среднее значение


def everage_numbers():
    a = []
    def inner(numbers):
        a.append(numbers)
        print(a)
        return print(sum(a)/len(a))
    return inner
z =everage_numbers()
z(10)
z(20)
z(30)
print('Второй пример')


def everage_numbers1():
    summa=0
    count=0
    def inner1(chislo):
        nonlocal summa
        nonlocal count
        summa = summa+ chislo
        count+=1
        return print(summa/count)
    return inner1
g =everage_numbers1()
g(10)
g(20)
g(30)

