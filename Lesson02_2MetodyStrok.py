# Методы строк
s = 'Hello World'
print(s.upper(),' Все большие')
print(s.lower(),' Все маленькие')
print(s,' вывели значение')
s = s.upper() # присвоили строке другое значение
print(s,' изменили значение - строку')

# Поиск в строке
print(s.count('O',5,6),' раз встретилась буква O') # Что ищем в строке, откуда и до куда
print(s.rfind('D'),'ПОИСК С права на лево')
print(s.find('Z'))
print(s.index('O'))

# Замена
print(s.replace('O','???')) # Что будем менять на что будем менять
print(s.replace('L','')) # Заменили на пустую строку
print(s.replace(' ','')) # Убрали пробел
print(s.replace('L','',3)) # Убрали Все буквы L

# Метод проверяет из чего состоит строка
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
