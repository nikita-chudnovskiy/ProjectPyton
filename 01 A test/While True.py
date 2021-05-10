running =True
while running:
    a = int(input())
    if a ==10:
        print('Вы угадали')
        running= False
    else:
        print('Попробуй еще')
else:
    print('Завершено')


while True:
    a = int(input())
    if a ==10:
        print('Вы угадали')
        break
    else:
        print('Попробуй еще')
else:
    print('Завершено')
