# parol1 = 'qwerty123'
# parol2 = 'asdfg456'
# s = 3
# for i in range(3):
#     print('Введите пароль:')
#     parol = input()
#     s = s-1
#     if parol1 == parol or parol2 == parol:
#         print('Вы вошли в систему как:',parol1 or parol2)
#         break
#     if parol1 != parol or parol2 != parol:
#         print('Неверный пароль, попробуй еще раз, осталось попыток:',s)
# if parol1 != parol and parol2 != parol:
#     print('У вас закончились попытки')

key = 0
number = 0
position = number
for i in range(5):
    b = input()
    number = number+1
    if b == 'key':
        position = number
print(position)   

