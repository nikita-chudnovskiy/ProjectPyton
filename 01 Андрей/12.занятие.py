summ = 0
for i in range(10):
    a = input()
    if a == 'print':
        print(summ)
    if a == 'add':
        print('How Much')
        f = int(input())
        summ = summ+f
        print(summ)
    if a == 'spend':
        print('How Much')
        g = int(input())
        if summ >g:
            summ = summ-g
            print(summ)
        else:
            print("You dont have enough money")