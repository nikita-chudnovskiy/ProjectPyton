# 13.01.2020

a = input()                                        # str Ввести строку Строку

a,b,c= map(int,input().split())                    #  ввести 3 числа

print(sum(map(int, input('Сумма всех').split())))  # вывести сумму



# Проверяем есть ли в веденной строке имя Nikita
name = (input('Проверка имени '))
if 'Nikita' in name:
    print('Success!')
else:
    print('No')



