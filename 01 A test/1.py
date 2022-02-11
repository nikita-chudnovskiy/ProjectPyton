def calendarb():
    k=('январь','февраль','март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')


    mesyac = int(input('Выберите месяц'))

    for i in range(len(k)):

        if i+1 == mesyac:
            print(k[i])
            for i in range(1,8):
                if i <8:
                    print(i,end=' ',)
            print()
            for i in range(8, 15):
                if i < 15:
                    print(i, end=' ', )
            print()
            for i in range(15, 22):
                if i < 22:
                    print(i, end=' ', )
            print()
            for i in range(22, 29):
                if i < 29:
                    print(i, end=' ', )
            print()
            for i in range(29, 32):
                if i < 32:
                    print(i, end=' ', )



calendarb()
