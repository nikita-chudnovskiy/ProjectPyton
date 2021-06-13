a,b =map(int,input('введите числа ').split())


def printMax(a,b):
    if a>b:
        print(a)
    elif a==b:
        print('=')
    else:
        print(b,'max')

printMax(a,b)


