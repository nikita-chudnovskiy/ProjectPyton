# между значениями переменных должен стоять один пробел)

# Вывести через пробел и на след строке
a,b,c =7,-4,3
print(a,b,c, sep =" ")
print(a,b,c, sep ="\n")

# Вывести на 1 строрске
print('Hello',end=" ")
print('Андрей')

# ввод данных
s1, s2 = map(str.strip, input().split())
print(f"Word 1: {s1} | Word 2: {s2}")

# Возведение в степень первого во второе
a,b=map(int,input().split())
print(a**b)


"""
В магазине продается X синих ручек, Y зеленых, черных в два раза больше, 
чем синих, а красных в четыре раза больше зеленых.
Напишите программу, в которой вводятся целые значения X, Y в 
одну строку через пробел с помощью команды:
"""
x,y = map(int,input().split())
print((x+x*2)+(y+y*4))

# Sample Output:
# 3.142
import math
a=math.pi

print(round(math.pi,3))

a=float(input())
print(f"Вы ввели число {a}")