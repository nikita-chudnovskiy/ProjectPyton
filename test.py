p = input('Введите пароль')
password ='qwerty'
count = 1

while password !=p and count <3:
    count+=1
    print('попытка',count)
    p = input()
    if count == 3:
        if p == password:
            continue
        print("Использованы все попытки.")
        break
else:
    print('Верно, кол попыток',count)


