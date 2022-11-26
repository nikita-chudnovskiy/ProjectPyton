
def kvadrat(x):
    return x**2


print(kvadrat(5))
b =[2,4,6]
print(list(map(kvadrat,b)))


f =['hello', 'dog','roma']
c = list(map(len,f))
print(c,'длинна каждой стсроки')
print(sum(c),'Сумма всех букв')


# Введем наш список и применим квадрат
a =map(int,input().split())
b =list(map(kvadrat,a))
print(b)



