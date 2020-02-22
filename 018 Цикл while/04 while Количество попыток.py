# Программа для ввода пароля.

p = input("Введите пароль: ")
password = "qwerty"
count = 1
while p != password and count < 3:
    count += 1
    p = input("Введите пароль: ")
    if count == 3:
        if p == password:
            continue
        print("Использованы все попытки.")
        break
else:
    p1 = 1
    p2 = 2
    if count == p1:
        print("Вы ввели правильный пароль. Использовано",count,'попытка')
    else:
        print("Вы ввели правильный пароль. Использовано", count,'попытки')



