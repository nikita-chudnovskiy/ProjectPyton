# remove 5

a = [1,5,5,]*3
while 5 in a:    #  Проверка есть ли 5 в списке и пока она есть цикл будет выполнятся (мы удаляем все пятерки)
    a.remove(5)  #  как только в списке удалятся все 5 то он прекратится
    print(a)# выводим каждый раз демонстрируем
print(a)