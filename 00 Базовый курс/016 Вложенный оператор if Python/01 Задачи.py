
# Нужно вывести пункт меню, связанный с этим числом
m =int(input())
if m ==1:
    print('1. Введение в Python')
elif m ==2:
    print("2. Строки и списки")
elif m==3:
    print("3. Условные операторы")
elif m==4:
    print("4. Циклы")
elif m ==5:
    print("5. Словари, кортежи и множества")
elif m ==6:
    print("6. Выход")

# Вводятся три целых числа в одну строку через пробел.
# Необходимо определить наименьшее среди них и вывести его на экран.
# 8 11 -1
a,b,c =map(int,input().split())

if a<=b and a<=c:
    print(a)
elif b<=a and b<=c:
    print(b)
elif c<=a and c<=b:
    print(c)


# 1) легкий вес – до 60 кг (включительно);
# 2) первый полусредний вес – до 64 кг (включительно);
# 3) полусредний вес – до 69 кг (включительно);
# 4) остальные - более 69 кг.


kg = float(input())
if kg <= 60:
    print(1)
elif kg <= 64:
    print(2)
elif kg > 64 and kg <= 69:
    print(3)
elif kg > 69:
    print(4)

# Вторник
m =int(input())
if m ==1:
    print('понедельник')
elif m ==2:
    print("вторник")
elif m==3:
    print("среда")
elif m==4:
    print("четверг")
elif m ==5:
    print("пятница")
elif m ==6:
    print("суббота")
elif m ==7:
    print("воскресенье")


year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = int(input())
if 1 <= num <= 12:
    print(year[num - 1])
else:
    print('Введите число от 1 до 12')


