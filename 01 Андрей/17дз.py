# s = False
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     if a > 100:
#         s = True
# if s == True:
#     print('Yes')
# if s == False:
#     print('No')

s = 3
karta1 ='kkgf256'
karta2 = 'qwerty228'
print('Добро пожаловать в нашу систему онлайн управления картами. Введите номер карты (1 или 2)')
while True:
    a = int(input())
    if a > 2 or a < 1:
        print('Неверный номер карты. Попробуйте еще раз. Введите номер карты (1 или 2)')
    if a == 1 or a == 2:
        while True:
            print('Введите пароль:')
            parol = input()
            if parol != karta1 and parol != karta2:
                print('Неверный пароль. Введите пароль:')
                s = s - 1
                if s == 0:
                    print('Карта заблокирована')
                    break
            if parol == karta1 or parol == karta2:
                print('Добро пожаловать')
                exit(0)