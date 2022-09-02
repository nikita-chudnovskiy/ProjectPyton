
g ='gray' # Глобальная переменная

def colors():
    y ='yellov' #находится внутри локальной области функции colors()
    def print_red():
        nonlocal y
        r='red'
        g ='green' # *** Приоритет в поиске видимости передается локальным областям !!! выведется green

        print(r,y,g) # Можем исп y тк она глобальная для print_red
        y = 'was change'

    def print_blue():
        b='blue'
        print(b,y,g)
    print_red()
    print_blue()
colors()


a3='A5'
def audi(param ='a3'):

    def print_adi_a3():
        a3 ='a3'
        print(a3)


    def print_audi_a4():
        a4='a4'
        print(a4)

    if param == 'a3':
        print_adi_a3()
    elif param == 'a4':
        print_audi_a4()
    else:
        print('i do know this auto')
audi('a4')