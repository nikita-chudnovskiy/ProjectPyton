# parol = 'qwerty123'
# a = 3
# for i in range(3):
#     print('Введите пароль')
#     parol1 = input()
#     a = a-1
#     if parol == parol1:
#         print('Доступ разрешен')
#         break
#     if parol != parol1:
#         print('Неверный пароль, попробуй еще раз, у тебя осталось попыток:',a)
# if parol != parol1:
#     print('У тебя закончились попытки')

key = 0
number = 0
for i in range(5):
    a = input()
    number = number+1
    if a == 'key':
        print(number)
        break