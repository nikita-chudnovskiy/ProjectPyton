import datetime
import pickle
m = []
while True:
    l = input('> ')
    if l == 'добавить':
        j = input('Введите текст заметки: ')
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        m.append(time+" "+j)
        print('заметка',j,'добавлена')
    if l == 'показать':
        for n in m:
            print(n)
    if l == 'удалить последнюю':
        m.remove(m[-1])
    if l == 'сохранить':
        file = open('zametki','wb')
        pickle.dump(m,file)
        file.close()
    if l == 'загрузить':
        file = open('zametki','rb')
        m = pickle.load(file)
        file.close()
    if l == 'выйти':
        break