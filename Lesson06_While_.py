for x  in range(1,100,1): # start stop шаг
    if x <5 :
        print(x, 'Дошли до 5') # доходим до 5 продолжаем
        continue
    print(x)
    if x >= 10: # доходим до 8 выходим
        break