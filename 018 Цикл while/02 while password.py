# А эта программа будет заставлять вводить пользователя числа, пока он не введет ноль.
a = int(input('введите 0'))
while a !=0:
    print('Повторите ввод')
    a = int(input())

# Программа для ввода пароля.

p = input("Введите пароль: ")
password = "qwerty"
count = 1
while p != password and count < 3:
    count += 1
    p = input("повторите ввод :")
    if count == 3:
        if p == password:
            continue
        print("Использованы все попытки.")
        break
else:
    print("Вы ввели правильный пароль. Использовано попыток", count)