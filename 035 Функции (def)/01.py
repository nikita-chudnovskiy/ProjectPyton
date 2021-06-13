a,b =input('введите числа ')


def printMax(a,b):
    if a>b:
        print(a)
    elif a==b:
        print('=')
    else:
        print(b,'max')


printMax(a,b)
