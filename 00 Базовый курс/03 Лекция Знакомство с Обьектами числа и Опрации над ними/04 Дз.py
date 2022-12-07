import math
a = -7
print(abs(a))
print(round(5.3))
print(round(5.5))

d1,d2,d3 = map(int,input().split()) # разделяет ввод по пробелу

print(max(d1,d2,d3))
print(min(d1,d2,d3))

a = 3
b = 4

z =(a**2)+(b**2)
print(math.sqrt(z))


#  n дети m вожатые (40 ,5) сколько надо автобусов
n =40
m = 5
z= (n+m)/20
print(math.ceil(z))


# Ручки если подешевели на 10% сколько можно купить на 500 р если 1 стоила 20
x =20
y =500/100*10
total = (500+y)/x
print(math.floor(total))
