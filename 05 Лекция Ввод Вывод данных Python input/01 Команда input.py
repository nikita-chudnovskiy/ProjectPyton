# 13.01.2020
#!/usr/bin/env python3  для Linux чтоб файл автоматически запускался
# -*- coding: utf-8 -*-   # Кодировка

a = input('введите симвлы: ')  # str Ввести строку Строку

a, b, c = map(int, input('Ввести 3 числа через пробел ').split())  # ввести 3 числа

print(sum(map(int, input('Введите 3 числа через пробел Сумма всех: ').split())))  # вывести сумму

# Проверяем есть ли в веденной строке имя Nikita
name = (input('Проверка имени '))
if 'Nikita' in name:
    print('Success!')
else:
    print('No')
