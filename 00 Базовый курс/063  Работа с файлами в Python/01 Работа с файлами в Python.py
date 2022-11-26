# Работа с файлами

file = open('111.txt', encoding ='utf-8') # Указать кодировку
file2 =open(r'C:\1.txt',encoding ='utf-8') # r будет убирать все служебные символы
print(file.read())
#print(file2.read())

# Как корретка считывает последовательно уже не выведет
# если нужно откатится то file2.seek(0)
#file2.seek(0)
#print(file2.readline())
#print(file2.readline())

for i in file2:
    print(i,end='')

file2.seek(0)
print()
print(file2.read())

file.seek(0)

# Прохождение по одному символу в нашем файле
for row in file:
    for letter in row:
        print(letter)



file3 =open(r'Стих.txt', encoding ='utf-8') # r будет убирать все служебные символы
for row in file3:
    print(row)