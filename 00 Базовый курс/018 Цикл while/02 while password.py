# А эта программа будет заставлять вводить пользователя числа, пока он не введет ноль.
# a = input('введите пароль  qwerty')
# while a !='qwerty':
#     print('Повторите ввод')
#     a = input()
# print('Вы угадали')


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
    print("правильный пароль. Использовано попыток", count)