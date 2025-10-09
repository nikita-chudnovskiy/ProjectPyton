import os
menu = '''список доступных операций:
          1. количество символов
          2. количество слов
          3. количество конкретной буквы
          4. самое длинное слово
          5. копировать файл
          6. выйти
'''
while True:
    v = input('Введите название файла: ')
    if os.path.exists(v) and os.path.isfile(v):
        print(menu)
        n = int(input('Введите номер операции: '))
        if n == 6:
            print('Завершение')
            break
        if n == 1:
            file = open(v,encoding='utf-8')
            b = file.read()
            file.close()
            print('Количество символов:',len(b))
        if n == 2:
            file = open(v, encoding='utf-8')
            b = file.read()
            file.close()
            print('Количество слов',len(b.split()))
        if n == 3:
            file = open(v, encoding='utf-8')
            b = file.read()
            file.close()
            k = input('Введите букву: ')
            h = 0
            for i in b:
                if i == k:
                    h = h+1
            print('Буква встречается',h,'раз')
        if n == 5:
            file = open(v, encoding='utf-8')
            b = file.read()
            file.close()
            u = input('название файла в которую скопировать: ')
            file2 = open(u,'w',encoding='utf-8')
            file2.write(b)
            file2.close()
            print('Файл успешно скопирован')
    else:
        print('Такого файла не существует')