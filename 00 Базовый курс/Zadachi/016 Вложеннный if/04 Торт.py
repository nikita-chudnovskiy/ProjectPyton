# Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.
a = int(input())
if a%2==0:
    print(int(a/2))
else:
    print(a)


a = int(input())
a = a//2
if a%2 == 0:
    print('Yes',float(a))
else:
    print('No',float(a))