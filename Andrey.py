number = 33

while True:
    age = int(input('Введите  '))
    if age == number:
        print("Вы угадали")
        break
    elif  age < number:
        print('Чуть больше')
    else:
        print('Чуть меньше еще')


