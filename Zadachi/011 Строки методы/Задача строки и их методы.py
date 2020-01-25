# Сколько слов в строке
w = 'Hello World Фига себе'
print(len(w.split()))  # метод split формирует в отдельную строку

w = 'Hello World Фига себе'
w = w.split()  # метод split формирует в отдельную строку
print(w)
print(len(w))

# Изменить строку @
d = 'Bilbo.Baggins@bagend.hobbiton.shire.me'
print(d)
d = d[::-1].replace('@', '')  # Убираем  @ медотом replace и сразу переворачиваем
print(d)

# Вывести знак * через букву
p = 'Python'
# print(p.split())
print('*'.join(p))

# Вывести с регистром 1 букву
p = 'ApPle'
print(p)
# вывести с заглавной
print(p.capitalize())
p = 'konjac'
print(p.capitalize())

# Изменить строку
a = input().lower() # С маленькой буквы
print(a)
a = a.replace('a', '')
a = a.replace('o', '')
a = a.replace('u', '')
a = a.replace('e', '')
a = a.replace('i', '')
a = a.replace('', '.')
print(a[0:-1])


#Дана строка, в которой буква h встречается минимум два раза.
#Удалите из этой строки первое и последнее вхождение буквы h,
#а также все символы, находящиеся между ними.
s ='In the hole in the ground there lived a hobbit'
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)


#Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
#Если она встречается два и более раз, выведите индекс её первого и последнего появления.
#Если буква f в данной строке не встречается, ничего не выводите.

s =input()
if s.count('f')==1:
    print(s.find('f'))
elif s.count(('f')) >=2:
    print(s.find('f'),s.rfind('f'))

# Поменять местами
s ='hello world !'
s1 = s[:s.find(' ')]
s2 =s[s.find(' ')+1:]
print(s2+' '+s1)

#Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
#Если буква f в данной строке встречается только один раз,
#выведите число -1, а если не встречается ни разу, выведите число -2.
s = 'coffe'
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))

# Сколько слов в этой строке
s ='hello world'
print(s.count(' ')+1)

