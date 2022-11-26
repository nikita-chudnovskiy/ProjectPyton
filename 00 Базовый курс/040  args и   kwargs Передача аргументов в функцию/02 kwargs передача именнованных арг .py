
def f(*a):
    print(a,type(a))

f(1,2,3) #



def f(*args): # Сумма   При пом * можем передать неопределенное количество не именнованных аргументов
    s =0
    for i in args:
        s+=i
    return s
print(f(1,2,3)) # Все явл кортеж


def f(**kwargs):
    print(kwargs,type(kwargs)) # Все явл всловарем

f(a=2,b=3,c =4)

def f(*args,**kwargs):
    print(args,kwargs)
f(1,2,3, a=5,b=3)