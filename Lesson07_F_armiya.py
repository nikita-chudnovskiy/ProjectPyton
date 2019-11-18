print('Введите сколько Вам лет ')
running = True
while running:
    age = int(input())
    if age >= 18 and age <= 27:
        print('Ты в армии Сынок ')
        running = False
    elif age < 18:
        print('Мал еще')

    else:
        print('Иди за военником ')
else:
    print('Служу Росии ')