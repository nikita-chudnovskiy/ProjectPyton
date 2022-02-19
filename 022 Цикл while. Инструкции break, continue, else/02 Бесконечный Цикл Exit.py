while True:
    a =input('Введите строку ')
    if a =='exit':     # Бесконечно вводим строку пока не введем exit и выйдем из цикла
        break
    print('Длинна строки',len(a))


while True:
     a = int(input())
     if a ==5:
        break
     if a<6:
        continue
     print(a)




while True:
    a= input()
    if len(a)<=5:
        print('мало')
        continue
    break