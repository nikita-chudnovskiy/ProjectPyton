parol = 'qwerty123'
s = 3
for i in range(3):
    parol1 = input()
    if parol1 == parol:
        if s == 3:
            print('Вход в систему осуществлён',s)
        else:
            print('Подтвердите пароль:')
            parol2 = input()
            if parol == parol2:
                print('Вход в систему осуществлен')
            else:
                print('Аккаунт заблокирован.')
        break
    if parol1 != parol:
        print('Не верный пароль у вас осталось',s)
        s = s-1
if parol != parol1:
    print('Поытки исчерпаны.Аккаунт заблокирован.')