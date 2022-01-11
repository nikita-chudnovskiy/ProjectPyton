#  *args и ** kwargs Передача аргументов в функцию

*a,b,c =[1,'hello',3,4,5,6,7,8,]
print(a,b,c)

*a,b,c =[2,3]
print(a,b,c)


s =[4,10]
print(list(range(1,5)))
print(list(range(*s)))


def f(a,b,c,d):
    print(a,b,c,d)

a = ('hello',True,78,[3,4,5])
f(1,2,3,4)
f(*a)
