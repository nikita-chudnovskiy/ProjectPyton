
print('Введите пароль')



count = 5
while True:
    a = input()

    count -=1
    if a =='10':
        print(f'Ввели пароль {a} количество символов {len(a)} ')
        print('Вы угадали')

        break
    elif a!=10:
        print('Попробуй еще')
        print('Попыток осталось',count)
    if count<=0:
        break

else:
    print('Завершено')

