a = [1, 2, 3]                       # Метод append  добовляет в конец списка
print(a)
a.append(100)
print(a,'Добавили посл значение списка')

a.pop()                             # удаляет последний   # pop(0)  удаляет в конце или указанный индекс тут нулевом
print(a,'Удалили посл значчение')

b=a[:]
print(b,'Скопировали обьекат a')    # copy() a[:]  Метод копирует обьект

print(b.count(1))                   # count(3)  сколько раз встреч значение

                                    # clear() делает список пустым
                                    # index(3) ищет индекс числа с лева на право
                                    # insert(0,100) добавить в 0 индекс 100
                                    # remove(3) удаляет первое найденное значение тут тройку
                                    # sort() сортирует впо увеличению
b.reverse()                         # revers() перевернули
print(b)
                                    # a.sort(reverse=True) перевернули и отсортировали по убыванию
                                    # Проверка 45 in a
