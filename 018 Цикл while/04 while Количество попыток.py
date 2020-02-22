# Программа для ввода пароля.

p = input("Введите пароль: ")
password = "qwerty"
count = 1
while p != password and count < 3:
    count += 1
    print("Неправильный пароль.")
    p = input("Введите пароль: ")
    if count == 3:
        if p == password:
            continue
        print("Использованы все попытки.")
        break
else:
    print("Вы ввели правильный пароль.")
    print("Использовано попыток", count)


