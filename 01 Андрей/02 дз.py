print('Введите первое число:')
d = int(input())
print('Введите второе число:')
g = int(input())
print('Введите третье число:')
s = int(input())
f = d+g+s
print(f)

print('Введите массу в кг:')
a = int(input())
s = a*1000
print('Масса в граммах:', s)

print('Введите свой возраст:')
a = int(input())
if  a<34:
    print('Вы молодой:')
else:
    print('Вы немолодой:')

print('Введите номер месяца:')
a = int(input())
if a == 1:
    print('Январь')
if a == 2:
    print('Февраль')
if a == 3:
    print('Март')
if a == 4:
    print('Апрель')
if a >12 or a<1:
    print('Неверный номер')

print('Введите температуру воздуха')
a = int(input())
if a <10:
    print('Холодно')
if a >=10 and a <=20:
    print('Прохладно')
if a >=21 and a <=30:
    print('Тепло')
if a >=31:
     print('Жарко')