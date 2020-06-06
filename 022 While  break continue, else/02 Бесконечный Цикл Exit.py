count =0
while True:
    a =input('Введите строку ')
    count+=1
    if a =='exit':     # Бесконечно вводим строку пока не введем exit и выйдем из цикла
        break
    print('Длинна строки',len(a),'Вы ввели ',a)
print('Попытка',count)



