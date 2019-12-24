# Методы строк
s = 'Hello World'
print(s.upper(),' Все большие')
print(s.lower(),' Все маленькие')
s = s.upper() # присвоили строке другое значение
print(s,' изменили значение - строку')
s = s.lower()

# Поиск в строке
print(s.count('o',1,9),' Сколько раз встретилась буква О c 5 по 6  ') # Что ищем в строке, откуда и до куда
print(s.find('l')) # Ищем Индекс Буквы d
print(s.rfind('e')) # Ищем индекс с права на лево
print(s.index(''))

# Замена replace
print(s.replace('h','???')) # Что будем менять на что будем менять
print(s.replace('h','')) # Заменили на пустую строку
print(s.replace(' ','')) # Убрали пробел
print(s.replace('l','',3)) # Убрали Все буквы l

# Метод проверяет из чего состоит строка ( Буквы isalpha)
print(s.isalpha()) # Целиком из букв ? есть пробел по этому false
s = '123'
print(s.isdigit()) # Проверяет из цифр ли строка
print(s.rjust(10,'0')) # меняем значение с лева на право
print(s.ljust(10,'-')) # c права на лево

d = 'ivanov ivan ivanovich'
print(d.split())
print(len(d.split()))
print(d.split('n'))
w = '234, 234, 234'.split(',')
print(w)
print('='.join(w))
print('.'.join(d).split())

a ='Hello   '
b = '   12'
print(a.rstrip())
print(b.lstrip())
print(a.strip())

a = input().replace('e','a').upper()
print(a)
