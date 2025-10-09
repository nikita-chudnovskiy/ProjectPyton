import pickle
t = []
while True:
    b = input('> ')
    if b == 'добавить':
        j = int(input('Введите номер задачи: '))
        if j not in t:
            t.append(j)
        else:
            print('Задача',j,'уже отмечена как решённая')
    if b == 'показать диапазон':
        f = int(input('Введите первое число: '))
        v = int(input('Введите второе число: '))
        for i in range(f,v+1):
            if i in t:
                print(i)
    if b == 'добавить диапазон':
        r = int(input('Введите первое число: '))
        l = int(input('Введите второе число: '))
        for i in range(r,l+1):
            if i not in t:
                t.append(i)
    if b == 'показать':
        for n in t:
            print(n)
    if b == 'удалить':
        k = int(input('введите номер задачи который нужно удалить: '))
        if k in t:
            t.remove(k)
        else:
            print('такой задачи нет.')
    if b == 'сохранить':
        file = open('zadachi','wb')
        pickle.dump(t,file)
        file.close()
    if b == 'загрузить':
        file = open('zadachi','rb')
        t = pickle.load(file)
        file.close()
    if b == 'выйти':
        break