name,family,age=input().split()
print(f"Уважаемый {name} {family}! Поздравляем Вас с {age}-летием!")


a,b,c=map(int,input().split())
print(f"Габариты: {a} x {b} x {c}")


# put your python code here
a,b=map(int,input().split())
c=min(a,b)
d=max(a,b)
print(f"{c} {d}")


a = input()
b = input()
print()
c = int(input())
print()
d = int(input())
print(f"г. {a}, ул. {b}, д. {c}, кв. {d}")


import math
a=float(input())
b=int(input())
c=math.ceil(b//a)
print(f"Вы можете получить {c}$ за {b} рублей по курсу {a}")