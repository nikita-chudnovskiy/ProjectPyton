import pickle
k = []
while True:
    c = input('> ')
    if c == 'добавить':
        b = input('film: ')
        k.append(b)
        print('Фильм',b,'добавлен')
    if c == 'показать':
        for i in k:
            print('-',i)
    if c == 'удалить':
        f = input('film: ')
        if f in k:
            k.remove(f)
            print('фильм',f,'удалён')
    if c == 'сохранить':
        file = open('films','wb')
        pickle.dump(k,file)
        file.close()
    if c == 'загрузить':
        file = open('films','rb')
        k = pickle.load(file)
        file.close()
    if c == 'выйти':
        break