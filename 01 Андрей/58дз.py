def chislovoi(w):
    for i in w:
        if i not in '1234567890':
            return(False)
    return(True)

while True:
    print('Введите номер телефона:')
    a = input()
    if len(a) == 12 and a[0:3] == '+79' and chislovoi(a[3:]) == True:
        print('Номер:',a, '-> Корректный')
    else:
        print('Номер',a,'-> Некорректный')
