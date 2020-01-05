# СТРОКИ

print("Hello \"World\" ")                       # Экранирование     \"        " World "
print('Hello\n"World"')                         # Перевод строки    \n
print('Hello\t World')                          # Табудляция        \t
i='My name i\'s '
print(i+ '(!)')                                 # Добавили переменной  i значение (!)  My name i's Andrey !

# ПРОСТЫЕ ФУНКЦИИ ВВОДА

a ='hello'
b ="world"
c ='''hel
lo Перенос Строки'''
print(c)
r =input('Введите Строку или символ ') # input выводит ВСЁ  строкой !!!! Не нужно приводить к type str
print('Привет'+'Мир'+' '+'Конкатенация ')
print(a+b,'Конкатенация')
print(a +' '+ b)
print('Длинна строки')
b = input()
print(len(b)) # длинна строки len
b ='233456'
print('4' in b,'Да 4 присутствует',sep=',') # ПРоверить in ессть ли 4 в переменной b # разделитель и не перенос строки

a = 'abc'
r = 'r'
print(ord(r),a > r,'abc > r')# покозать номер символа

# ИНДЕКСЫ

d = 'hello world'
print(d)
print(d*2) # Задублировать символ, Строки можно умножать на цыфры
print(len(d),d[0],d[-1], 'Длинна, Нулевой индекс и последний')

# СРЕЗЫ

print(d[0:5]) # от начала до 5
print(d[0:])  # от начала до последнего
print(d[:4])  # до 4

print(d[1]) # второй индекс
print(d[:]) # Полностью всю строку
print(d[::2]) # Если хотим через один шаг равен 2
print(d[1::2])
print(d[::-1]) #  НАОБОРОТ
print(d[2:8:3]) # Начало Конец и шаг 3  (hello world l пробел и до 7 потому что 8 не берем шаг 3
n = 'nikita chudnovskiy'
print(n[::-1])
print('{}, {:_^35}'.format(n, d))           # Объеденили методом format
n = 'Andrey'
print(n[0:])
print(n[-1])
print(len(n))
print(n[0:6])
n = n[0:0]+'E'+n[1:]
print(n)





