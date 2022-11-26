
#Ввести слова и добавить

slova=input('Введите слова')          # a+  это ключ означает что можем добавлять
file =open(r'/00 Базовый курс/063  Работа с файлами в Python/1.txt', 'a+', encoding ='utf-8')
print(file.read())
#file.write(c.formatyear(god))
file.write(f'{slova}\n')
file.close()

