
def kvadrat(x):
    return x**2

a =kvadrat(5)
print(a)

b =[2,4,6,8] # К списку b применили фкнкцию квадрат

c =list(map(kvadrat,b))
print(c)


f =['hello', 'dog','roma']

c = list(map(len,f))
print(c,'длинна каждой строки')
print(sum(c),'Сумма всех букв')


# Введем наш список и применим квадрат
a =map(int,input().split())
b =list(map(kvadrat,a))
print(b)