p = input("Введите пароль: ")
password = "qwerty"
count = 1
while p != password and count < 3:
    count += 1
    p = input("повторите ввод :")
    if count==3:
        print('Использованы все попытки' ,count)
        break
else:
    print('Вы ввели правильный пароль, количество попыток',count)



