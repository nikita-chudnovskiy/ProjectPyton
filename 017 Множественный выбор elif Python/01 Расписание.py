# Множественнй Выбор если условие не верно то пропускает и идет к следующему

n1 = [
    ['Математика', 'Русский', 'Чтение', 'Изо', 'Физкультура'],
    ['Русский', 'Математика', 'Английский', 'Окр Мир', 'Шахматы'],
    ['Физкультура', 'Математика', 'Русский', 'Чтение', ],
    ['Английский', 'Русский', 'Математика', 'Чтение', 'Труд'],
    ['Математика', 'Чтение', 'Окр Мир', 'Музыка']
]
while True:
    n = int(input('Расписание выберите 1-5, 10 Выход'))
    print()
    if n == 1:

        print('Понедельник:')
        for i, value in enumerate(n1[0], 1):
            print(i, value)

    elif n == 2:
        print('Вторник:')
        for i, value in enumerate(n1[1], 1):
            print(i, value)
    elif n == 3:
        print('Среда:')
        for i, value in enumerate(n1[2], 1):
            print(i, value)

    elif n == 4:
        print('Четверг:')
        for i, value in enumerate(n1[3], 1):
            print(i, value)
    elif n == 5:
        print('Пятница:')
        for i, value in enumerate(n1[4], 1):
            print(i, value)
    elif n == 10:
        print('End')
        break
