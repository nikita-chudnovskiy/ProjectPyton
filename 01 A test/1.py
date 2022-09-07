def main_func():
    y = 'yellow'
    def reyn():
        g ='green'
        nonlocal y
        y='eqe'
        print(g,y)
    reyn()
main_func()