
# Функция это многократное используемые фрагменты программы

# Определение Функции всегда пишем вверху файла

def sayHello():
    print('hi')
    print('all')
    print('World')

def square(x): # Сколько параметров передали столько и вводим в данном случае 1
    print('Квадрат числа',x,'=',x**2)

def multiplay(a,b):
    print('Результат умножения',a*b)


def even(a):
    if a % 2 == 0:
        print(a,'четное')
    else:
        print(a,'Не четное')



if 5 >1:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

#Главная программа
square(5)
square(10)

# В цикле for каждое число от 1 до 3 возводится в квадарат путем вызова square(i) со значением i - перебором
for i in range(1,10):
    square(i)

for i in range(20,30):
    even(i)

primer()


