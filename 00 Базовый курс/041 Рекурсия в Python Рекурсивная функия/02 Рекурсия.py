import math
def fact(x):
    if x ==1:
        return 1
    return fact(x-1)*x

print(fact(5))

print(math.factorial(3))


# Fibonacchi Класической рекурсией считается нахождение чисел Fibonacchi

# 0,1   сложение двух предыдущих    0,1,1,2,3,5,8,13,21,34

# f(7) чтобы найти седьмое число мы должны 6 число сложить с 5 числом f(6)+f(5)

# по формуле fibonacсhi см google или видео

def fib (n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))  # Количество вызовов очень сильно растет при вызове 70 числа будет очень долго работать , есть другие способы раб с фибоначи