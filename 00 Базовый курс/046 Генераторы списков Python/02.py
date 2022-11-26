# Все генераьторы списков строятся по следующему шаблону
# [ выражение for val in Коллекция if условие]

a = [ i for i in range(10) if i%2==0 and i%3 ==0]
print(a)

# Преобразование к целому числу

a = input().split()
print(a)

a =[int(i) for i in a ]
print(a)

n =5
m =5


a = [[0]*m for i in range(n)]
print(a)

for i in a:
    print(i)