# Вложенные циклы

for i in range(3): # Выполнить Цикл 3 раза
    for j in range(5):
        print('*',end=' ') # По 5 звездочек
    print()



for j in range(1,10):
    for i in range(1,11):
        print(i,' * ', j , '=', i * j,'  ', end = ' ')
    print()