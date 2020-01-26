money = int(input())
bilet = 90
if money > bilet:
    print('Ураaaa')
    print('Я иду в кино')
print('Я иду домой')

# Вывести самое большое
a = int(input())
b = int(input())
c = a            # если a > b то с = a условие не выполнилось

if b > a:        # tckb b > a то условие выполнилось и с = b
    c = b
print(c)

# Что бы в а окозалось большее из них
a = int(input())
b = int(input())
if b>a:
    a,b = b,a # сохраняет значение b в переменную a. А значение а в переменную b
print(a,b)