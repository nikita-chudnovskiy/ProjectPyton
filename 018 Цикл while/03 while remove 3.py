# remove 3

a = [1,2,3,]*3
print(a)
while 3 in a:    #  Проверка есть ли 3 в списке и пока она есть цикл будет выполнятся (мы удаляем все пятерки)
    a.remove(3)  #  как только в списке удалятся все 3 то он прекратится
    #print(a)# выводим каждый раз демонстрируем
print(a)