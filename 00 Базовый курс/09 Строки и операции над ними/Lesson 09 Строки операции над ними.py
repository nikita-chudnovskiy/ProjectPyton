# СТРОКИ

#print("Hello \"World\" ")                       # Экранирование     \"        " World "
#print('Hello\n"World"')                         # Перевод строки    \n
#print('Hello\t World')                          # Табудляция        \t
#i='My name i\'s '
#print(i+ '(!)')                                 # Добавили переменной  i значение (!)  My name i's Andrey !

# ПРОСТЫЕ ФУНКЦИИ ВВОДА

a ='hello'
b ="world"
c ='''hel
lo Перенос 3 Строки'''
print(c)
r =input('Введите Строку или символ ') # input выводит ВСЁ  строкой !!!! Не нужно приводить к type str

# КОНКАТЕНАЦИЯ
print('Привет'+'Мир'+' '+'Конкатенация ')
print(a+b,'Конкатенация')
print(a +' '+ b)

# Введите строку len покозать сколько в ней символов
s = input('Введите строку qwerty')
print('Вы ввели',len(s),'символов') # длинна строки len

# Найти в строке есть ли 4
b =input('Введите 1234')
print('4' in b,' Да 4 присутствует',sep=',' ) # ПРоверить in ессть ли 4 в переменной b # разделитель

# В Python Важен регистр букв Сравнение символов в строке
s1 = 'AAA'
s2 = 'aaa'
s3 = 3
print(s1==s2,'Строки !=')
# Сложение строки
print(s1+str(s3))
# Так как r дальше то и ее значение будет больше( На самом деле сравнивается числовое значение ord('a')
# ЛЮБАЯ СТРОКА ИЗ ЗАГЛАВНЫХ БУКВ БУДЕТ МЕНЬШЕ маленьких букв
a = 'abc'
r = 'r'
print(ord('a'),a > r,'abc > r')# покозать номер символа
a = 'abc'
b = 'abcd'
print(a>b) # false там 4 символа и она будет больше

print('Привет '*4)

# Строки поддерживают unicod кодировку (utf8)
print('привет'.encode())

#hello python
s1,s2=map(str,input().split())
print((s1+" ")*2+(s2+" ")*3)

# Переменная a = 2, переменная b = -5
a,b =map(int,input().split())
print("Переменная a ="+" "+str(a)+","+" переменная b ="+" "+str(b))

#hello Balakirev
s=input()
print("Строка: "+s+". "+"Длина:"+"",len(s))

#hello python
s1,s2=map(str,input().split())
print(s1 in s2, s1==s2, s1>s2,s1<s2)

# Коды: a = 97, z = 122
a,z = input().split()
print("Коды: "+a+" = "+str(ord(a))+", "+z+" = "+str(ord(z)))


