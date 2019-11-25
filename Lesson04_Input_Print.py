"""a = input() #str
b = int(input())# int
c = float(input()) # float
"""
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
p = a+b+c
print(p)

a,b = map(int,input().split())
print(a+b)

name = 'Андрей'
age = 2
print('Исполнилось %s %s'%(name,age))

print(1,2, sep=',', end=',')
print(3)

