import pickle
b = []
while True:
    f = input('> ')
    if f == 'новая задача':
        h = input('описание задачи: ')
        b.append(h)
        print('Задача добавлена')
    if f == 'выполнено':
        print('Задача ',b[0],'выполнена')
        # b = b[1:]
        # b.remove(b[0])
        b.pop(0)
    if f == 'вывести':
        n = 1
        for i in b:
            print(n,i)
            n = n+1
    if f == 'выйти':
        break
    if f == 'сохранить':
        file = open('tasks','wb')
        pickle.dump(b,file)
        file.close()
    if f == 'восстановить':
        file = open('tasks','rb')
        b = pickle.load(file)
        file.close()