import pickle
y = []
s = []
g = []
while True:
    l = input('> ')
    if l == 'добавить':
        j = input('Введите название товара: ')
        y.append(j)
        x = int(input('введите количество товара: '))
        s.append(x)
        h = int(input('цена за единицу: '))
        g.append(h)
        print('товар - ',j,x,'шт по',h,'руб','добавлен')
    if l == 'показать':
        for i in zip(y,s,g):
            print(i[0],'-',i[1],'штук по цене',i[2],'всего',i[1]*i[2])
    if l == 'итого':
        all = 0
        for f in zip(y,s,g):
            all += f[1]*f[2]
        print(all)
    if l == 'сохранить':
        file = open('товары','wb')
        pickle.dump([y,s,g],file)
        file.close()
    if l == 'загрузить':
        file = open('товары','rb')
        y,s,g = pickle.load(file)
        file.close()
    if l == 'выйти':
        break